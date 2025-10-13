from utils.scrapy import load_tags, get_today_arxiv

import json
import os

if __name__ == '__main__':
    tags = load_tags('tags.json')
    result, label_date = get_today_arxiv(tags, max_results=1000)
    os.makedirs(f'data/{label_date}', exist_ok=True)
    with open(f'data/{label_date}/arxiv_{label_date}.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
        