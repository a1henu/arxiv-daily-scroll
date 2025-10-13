#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse, json, os, re, sys, datetime
from pathlib import Path
from typing import List, Dict, Any, Tuple

# =============== 基础工具 ===============

def slugify(text: str, maxlen: int = 80) -> str:
    text = re.sub(r"[^\w\s-]", "", text, flags=re.U).strip().lower()
    text = re.sub(r"[\s_-]+", "-", text)
    return text[:maxlen] if maxlen else text

def read_json(p: Path) -> Dict[str, Any]:
    with p.open("r", encoding="utf-8") as f:
        return json.load(f)

def ensure_dir(p: Path):
    p.mkdir(parents=True, exist_ok=True)

def md_escape(s: str) -> str:
    return s.replace("|", r"\|")

def to_authors(auth_list) -> str:
    if isinstance(auth_list, list):
        return ", ".join(auth_list)
    return str(auth_list)

# =============== 渲染 ===============

def render_paper_md(p: Dict[str, Any]) -> str:
    title = p.get("title", "").strip()
    authors = to_authors(p.get("authors", []))
    arxiv_id = p.get("arxiv_id", "")
    headline = p.get("headline_zh", "").strip()
    intro = p.get("intro_zh", [])
    tags = p.get("tags_zh", [])
    summary = p.get("summary", "").strip()

    lines = []
    lines.append(f"# {md_escape(title)}")
    if arxiv_id:
        base_id = arxiv_id.split('v')[0]
        abs_url = f"https://arxiv.org/abs/{base_id}"
        pdf_url = f"https://arxiv.org/pdf/{base_id}.pdf"
        lines.append(f"**arXiv**：[{arxiv_id}]({abs_url}) · [PDF]({pdf_url})  ")
    lines.append(f"**作者**：{md_escape(authors)}  ")
    if headline:
        lines.append(f"\n**一句话要点**：{md_escape(headline)}")
    if tags:
        lines.append(f"\n**关键词**：{', '.join(tags)}")
    lines.append("")
    if intro and isinstance(intro, list):
        lines.append("## 3 点简述")
        for it in intro:
            lines.append(f"- {md_escape(str(it))}")
        lines.append("")
    lines.append("## 摘要（原文）")
    lines.append(f"\n> " + "\n> ".join(md_escape(summary).splitlines()))
    lines.append("")
    return "\n".join(lines)

def build_date_index_md(date_label: str, papers: List[Dict[str, Any]], site_title: str) -> str:
    lines = []
    lines.append(f"---\nlayout: default\ntitle: {site_title} - {date_label}\n---\n")
    lines.append(f"# {site_title}（{date_label}）\n")
    lines.append("| # | 题目 | 一句话要点 | 关键词 |")
    lines.append("|---:|---|---|---|")
    for i, p in enumerate(papers, 1):
        title = p.get("title", "").strip()
        slug = slugify(f"{p.get('arxiv_id','')}-{title}") or f"paper-{i}"
        headline = md_escape(p.get("headline_zh", ""))
        tags = p.get("tags_zh", [])
        tag_str = ", ".join(tags) if tags else ""
        lines.append(f"| {i} | [{md_escape(title)}](./papers/{slug}.html) | {headline} | {md_escape(tag_str)} |")
    lines.append("")
    lines.append("[返回首页](../index.html)")
    return "\n".join(lines)

def build_home_md(dates: List[str], latest_date: str, site_title: str) -> str:
    """
    首页：包含下拉选择器 + 自动跳转到所选日期；默认呈现最新日期的目录表的入口按钮。
    """
    # 生成下拉 options
    options_html = "\n".join(
        [f'<option value="dates/{d}/index.html" {"selected" if d == latest_date else ""}>{d}</option>'
         for d in dates]
    )
    # 内嵌一点 JS 做跳转
    html_block = f"""
<div class="date-switcher">
  <label for="date-select"><strong>选择日期：</strong></label>
  <select id="date-select" onchange="location.href=this.value;">
    {options_html}
  </select>
  <a class="btn" href="dates/{latest_date}/index.html">前往最新（{latest_date}）</a>
</div>
"""
    lines = []
    lines.append(f"---\nlayout: default\ntitle: {site_title}\n---\n")
    lines.append(f"# {site_title}\n")
    lines.append("> 支持多日期切换：从下拉菜单选择某一天进入该日目录页（含所有论文条目与详情页）。\n")
    lines.append(html_block)
    lines.append("\n---\n")
    lines.append("如果你想把首页直接展示最新日期的完整目录，也可以把该日的 `index.md` 内容复制到这里。")
    return "\n".join(lines)

def write_site_scaffold(docs_dir: Path):
    ensure_dir(docs_dir)
    ensure_dir(docs_dir / "assets")
    (docs_dir / "_config.yml").write_text(
        "theme: jekyll-theme-cayman\nmarkdown: kramdown\nkramdown:\n  input: GFM\n",
        encoding="utf-8"
    )
    (docs_dir / "_layouts").mkdir(exist_ok=True)
    (docs_dir / "_layouts" / "default.html").write_text(
        """<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<title>{{ page.title }}</title>
<link rel="stylesheet" href="{{ '/assets/style.css' | relative_url }}">
<meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
<main class="container">
  {{ content }}
</main>
<footer class="footer">
  <p>Powered by GitHub Pages · Generated on {{ site.time | date: "%Y-%m-%d" }}</p>
</footer>
</body>
</html>
""",
        encoding="utf-8"
    )
    (docs_dir / "assets" / "style.css").write_text(
        """.container{max-width:960px;margin:2rem auto;padding:0 1rem;font:16px/1.6 -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial;}
h1,h2,h3{line-height:1.25}
table{border-collapse:collapse;width:100%;margin:1rem 0}
th,td{border:1px solid #ddd;padding:.5rem;vertical-align:top}
code,pre{background:#f6f8fa;padding:.2rem .4rem;border-radius:6px}
.footer{margin:2rem 0;color:#666;font-size:.9rem;text-align:center}
a{color:#0366d6}
.date-switcher{display:flex;gap:.5rem;align-items:center;margin:1rem 0}
.date-switcher .btn{padding:.4rem .8rem;border:1px solid #ccc;border-radius:6px;text-decoration:none}
""",
        encoding="utf-8"
    )

# =============== 站点生成 ===============

def collect_dates(data_root: Path) -> List[Tuple[str, Path]]:
    """
    扫描 data/*/ai_summary*.json，返回 [(date_label, json_path), ...]，按日期升序。
    """
    items = []
    for p in sorted(data_root.glob("*/ai_summary*.json")):
        # 从路径或文件名中抽日期
        m = re.search(r"(\d{4}-\d{2}-\d{2})", str(p))
        if not m:
            # 兼容没有日期的路径，用父目录名兜底
            m = re.search(r"(\d{4}-\d{2}-\d{2})", p.parent.name)
        if m:
            date_label = m.group(1)
        else:
            # 实在取不到，用文件修改日期
            ts = datetime.date.fromtimestamp(p.stat().st_mtime).isoformat()
            date_label = ts
        items.append((date_label, p))
    # 去重 & 排序
    items = sorted(list({(d, str(p)): (d, Path(p)) for d, p in items}.values()), key=lambda x: x[0])
    return items

def save_date_site(docs_dir: Path, date_label: str, papers: List[Dict[str, Any]], site_title: str):
    """生成某一天的目录页 + 详情页"""
    day_dir = docs_dir / "dates" / date_label
    ensure_dir(day_dir)
    ensure_dir(day_dir / "papers")

    # date index
    date_md = build_date_index_md(date_label, papers, site_title)
    (day_dir / "index.md").write_text(date_md, encoding="utf-8")

    # per-paper pages
    for i, p in enumerate(papers, 1):
        title = p.get("title", "").strip()
        slug = slugify(f"{p.get('arxiv_id','')}-{title}") or f"paper-{i}"
        body_md = render_paper_md(p)
        md = f"---\nlayout: default\ntitle: {title}\n---\n\n{body_md}\n"
        (day_dir / "papers" / f"{slug}.md").write_text(md, encoding="utf-8")

def main():
    ap = argparse.ArgumentParser(description="Build multi-date GitHub Pages with date switcher.")
    ap.add_argument("--data", default="data", help="数据根目录（默认 data/）")
    ap.add_argument("--outdir", default="docs", help="输出站点目录（默认 docs/）")
    ap.add_argument("--title", default="arXiv·cs.CV 中文要点汇总（with DeepSeek）", help="站点标题")
    args = ap.parse_args()

    data_root = Path(args.data)
    docs_dir = Path(args.outdir)
    site_title = args.title

    pairs = collect_dates(data_root)
    if not pairs:
        print("[ERR] 未找到 data/*/ai_summary*.json", file=sys.stderr)
        sys.exit(2)

    write_site_scaffold(docs_dir)

    # 生成每个日期的页面
    all_dates = []
    for date_label, json_path in pairs:
        data = read_json(json_path)
        papers = data.get("papers", [])
        if not isinstance(papers, list) or not papers:
            print(f"[WARN] {json_path} 中 papers 为空，跳过 {date_label}")
            continue
        all_dates.append(date_label)
        save_date_site(docs_dir, date_label, papers, site_title)

    if not all_dates:
        print("[ERR] 没有可用的日期页面生成", file=sys.stderr)
        sys.exit(3)

    latest_date = sorted(all_dates)[-1]
    # 首页：日期下拉 + 按钮跳到最新
    home_md = build_home_md(sorted(all_dates), latest_date, site_title)
    (docs_dir / "index.md").write_text(home_md, encoding="utf-8")

    print(f"[OK] 生成完成。共 {len(all_dates)} 个日期。首页：{docs_dir}/index.md")
    print("👉 打开 GitHub → Settings → Pages，Source 选 Branch，目录选 docs/，保存即可。")

if __name__ == "__main__":
    main()
