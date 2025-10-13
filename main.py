from utils.scrapy import load_tags, get_today_arxiv
from utils.analyser import get_client, update_ai_summary_async

import asyncio
import json
import os

if __name__ == '__main__':
    tags = load_tags('tags.json')
    result, label_date = get_today_arxiv(tags, max_results=1000)
    os.makedirs(f'data/{label_date}', exist_ok=True)
    with open(f'data/{label_date}/arxiv.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    metas = result.get("papers", [])
    
    api_key = os.getenv("DEEPSEEK_API_KEY")
    client = get_client(api_key)
    results = asyncio.run(update_ai_summary_async(client, metas, concurrency=8, temperature=0.2))
    with open(f'data/{label_date}/ai_summary.json', 'w', encoding='utf-8') as f:
        json.dump({"papers": results}, f, ensure_ascii=False, indent=4)
    print(f"Done. Wrote: data/{label_date}/arxiv.json and ai_summary.json")