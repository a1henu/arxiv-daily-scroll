import asyncio
import json, re, time, random, os
from typing import List, Dict, Any, Tuple
from openai import AsyncOpenAI
from tqdm import tqdm

SYSTEM_PROMPT = open("utils/prompts/system.txt", "r", encoding="utf-8").read()
USER_TEMPLATE = open("utils/prompts/user.txt", "r", encoding="utf-8").read()

def get_client(api_key: str = None):
    api_key = api_key or os.getenv("DEEPSEEK_API_KEY") 
    if not api_key:
        raise RuntimeError("Missing API key. Set DEEPSEEK_API_KEY or pass api_key.")
    client = AsyncOpenAI(
        api_key=api_key,
        base_url="https://api.deepseek.com"
    )
    return client

def get_prompt(user_prompt: str, meta: dict) -> str:
    title = (meta.get("title") or "No Title").strip()
    authors_list = meta.get("authors", [])
    if isinstance(authors_list, list):
        authors = ", ".join(a.strip() for a in authors_list) or "No Authors"
    else:
        authors = str(authors_list).strip() or "No Authors"
    summary = (meta.get("summary") or "No Summary").strip()
    prompt = (user_prompt
              .replace("{title}", title)
              .replace("{authors}", authors)
              .replace("{summary}", summary))
    return prompt

def _parse_json_safely(text: str) -> Dict[str, Any]:
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        m = re.search(r'(\{[\s\S]*\})', text)
        if m:
            try:
                return json.loads(m.group(1))
            except json.JSONDecodeError:
                return {"_parse_error": "failed to decode extracted JSON", "_raw": text}
        else:
            return {"_parse_error": "no json object found", "_raw": text}

async def _one_call(
    client: AsyncOpenAI,
    meta: Dict[str, Any],
    sem: asyncio.Semaphore,
    idx: int,
    max_retries: int = 4,
    temperature: float = 0.2,
    request_timeout: int = 120,
) -> Dict[str, Any]:
    prompt = get_prompt(USER_TEMPLATE, meta)
    backoff = 1.5
    for attempt in range(1, max_retries + 1):
        async with sem:
            try:
                resp = await client.chat.completions.create(
                    model="deepseek-chat",
                    messages=[
                        {"role": "system", "content": SYSTEM_PROMPT},
                        {"role": "user", "content": prompt},
                    ],
                    temperature=temperature,
                    response_format={"type": "json_object"},  # 强制 JSON
                    timeout=request_timeout,
                )
                text = resp.choices[0].message.content
                if not isinstance(text, str):
                    text = str(text)
                ai_summary = _parse_json_safely(text)
                merged = {**meta, **ai_summary, "_index": idx}
                return merged
            except Exception as e:
                if attempt == max_retries:
                    return {**meta, "_index": idx, "_model_error": f"{type(e).__name__}: {e}"}
                await asyncio.sleep(backoff + random.uniform(0, 0.7))
                backoff *= 1.8

async def update_ai_summary_async(
    client: AsyncOpenAI,
    metas: List[Dict[str, Any]],
    concurrency: int = 8,
    temperature: float = 0.2,
) -> List[Dict[str, Any]]:
    """
    并发调用 DeepSeek，显示 tqdm 进度。返回顺序与输入一致。
    """
    sem = asyncio.Semaphore(concurrency)
    tasks = [asyncio.create_task(_one_call(client, meta, sem, idx=i, temperature=temperature))
             for i, meta in enumerate(metas)]

    results = [None] * len(metas)
    ok = err = 0
    t0 = time.time()

    for fut in tqdm(asyncio.as_completed(tasks), total=len(tasks), desc="DeepSeek", unit="paper"):
        try:
            item = await fut
            i = item.get("_index", None)
            if i is not None and 0 <= i < len(results):
                results[i] = item
            else:
                # 保险：如果没带索引或异常，附加到末尾
                results.append(item)
            if "_model_error" in item or "_parse_error" in item:
                err += 1
            else:
                ok += 1
        except Exception as e:
            err += 1
        done = ok + err
        elapsed = time.time() - t0
        rps = done / max(1e-9, elapsed)
        # tqdm.write(f"[progress] ok={ok} err={err} rps={rps:.2f}")

    for i, v in enumerate(results):
        if v is None:
            results[i] = {**metas[i], "_index": i, "_model_error": "TaskMissing"}

    return results

if __name__ == '__main__':
    api_key = os.getenv("DEEPSEEK_API_KEY")
    client = get_client(api_key)

    in_path = '../data/2025-10-12/arxiv_2025-10-12.json'
    out_path = '../data/2025-10-12/ai_summary_2025-10-12.json'

    with open(in_path, 'r', encoding='utf-8') as f:
        papers = json.load(f).get("papers", [])

    results = asyncio.run(update_ai_summary_async(client, papers, concurrency=8, temperature=0.2))
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump({"papers": results}, f, ensure_ascii=False, indent=4)
    print(f"Done. Wrote: {out_path}")
