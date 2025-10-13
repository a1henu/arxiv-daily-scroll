from typing import List, Tuple, Dict
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

import json
import arxiv

US_EASTERN = ZoneInfo("US/Eastern")

def load_tags(tags_file: str) -> List[str]:
    with open(tags_file, 'r', encoding='utf-8') as f:
        tags = json.load(f)
    return tags['tags']

def get_UTC_range() -> Tuple[str, str, str]:
    fmt = "%Y%m%d%H%M"
    
    now_utc = datetime.now(timezone.utc)
    now_et = now_utc.astimezone(US_EASTERN)
    today_et = now_et.date()
    t2000_et = datetime(today_et.year, today_et.month, today_et.day, 20, 0, 0, tzinfo=US_EASTERN)
    
    if now_et < t2000_et:
        end_et = t2000_et - timedelta(days=1, minutes=1)
    else:
        end_et = t2000_et
    if end_et.weekday() in (4, 5):  # Friday or Saturday
        end_et -= timedelta(days=end_et.weekday() - 3, minutes=1)  # Move to Thursday
    
    if end_et.weekday() == 6:
        start_et = end_et - timedelta(days=3, minutes=-1)
    else:
        start_et = end_et - timedelta(days=1, minutes=-1)
    
    return (start_et.astimezone(timezone.utc).strftime(fmt),
            end_et.astimezone(timezone.utc).strftime(fmt),
            end_et.strftime("%Y-%m-%d"))
    

def _result_to_minimal(r: arxiv.Result) -> Dict:
    arxiv_id = r.get_short_id() if hasattr(r, "get_short_id") else r.entry_id.split("/abs/")[-1]
    authors = [a.name for a in r.authors] if r.authors else []
    return {
        "title": (r.title or "").strip().replace("\n", " "),
        "authors": authors,
        "arxiv_id": arxiv_id,
        "summary": (r.summary or "").strip(),
    }


def query_arxiv(tags: List[str], time_range: Tuple[str, str], max_results: int = 500) -> Dict:
    start, end = time_range
    tag_clause = " OR ".join(f"cat:{t}" for t in tags)
    query = f"({tag_clause}) AND submittedDate:[{start} TO {end}]"

    client = arxiv.Client(page_size=200, delay_seconds=1.0, num_retries=3)

    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.SubmittedDate,
        sort_order=arxiv.SortOrder.Descending,
    )

    seen = set()
    papers = []
    for r in client.results(search):
        item = _result_to_minimal(r)
        if item["arxiv_id"] in seen:
            continue
        seen.add(item["arxiv_id"])
        papers.append(item)
    return {"count": len(papers), "papers": papers}

def get_today_arxiv(tags: List[str], max_results: int = 500) -> Dict:
    start, end, label_date = get_UTC_range()
    return query_arxiv(tags, (start, end), max_results=max_results), label_date


if __name__ == "__main__":
    tags = load_tags('../tags.json')
    result, label_date = get_today_arxiv(tags)
    print(f'Tags: {tags}')
    print(f"Date: {label_date}, Found {result['count']} papers")
