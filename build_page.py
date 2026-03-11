#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import datetime
import json
import os
import re
import shutil
import sys
from pathlib import Path
from typing import Any, Dict, List, Tuple


INDEX_HTML = """<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="color-scheme" content="light">
  <title>arXiv Daily Scroll</title>
  <link rel="stylesheet" href="./assets/style.css">
</head>
<body>
  <div class="page-shell">
    <header class="hero">
      <p class="eyebrow">arXiv Daily Scroll</p>
      <div class="hero-copy">
        <h1 id="site-title">加载中...</h1>
        <p id="site-subtitle" class="hero-subtitle">正在读取每日论文索引。</p>
      </div>
      <div class="hero-meta">
        <div class="hero-chip">
          <span class="chip-label">Latest Date</span>
          <strong id="hero-latest">-</strong>
        </div>
        <div class="hero-chip">
          <span class="chip-label">Papers</span>
          <strong id="hero-count">-</strong>
        </div>
      </div>
    </header>

    <main class="workspace">
      <aside class="panel sidebar">
        <div class="panel-head">
          <h2>Browse</h2>
          <p>按日期切换，按标题或关键词搜索。</p>
        </div>
        <label class="field">
          <span>日期</span>
          <select id="date-select"></select>
        </label>
        <label class="field">
          <span>搜索</span>
          <input id="search-input" type="search" placeholder="标题 / 作者 / 中文要点 / 关键词">
        </label>
        <div class="sidebar-stats">
          <div>
            <span class="stat-label">匹配结果</span>
            <strong id="result-count">0</strong>
          </div>
          <div>
            <span class="stat-label">生成时间</span>
            <strong id="generated-at">-</strong>
          </div>
        </div>
        <div class="tag-strip">
          <div class="tag-strip-head">
            <h3>热门关键词</h3>
            <button id="clear-tag" class="ghost-button" type="button" hidden>清除筛选</button>
          </div>
          <div id="tag-cloud" class="tag-cloud"></div>
        </div>
      </aside>

      <section class="panel list-panel">
        <div class="panel-head panel-head-row">
          <div>
            <h2 id="list-title">Papers</h2>
            <p id="list-subtitle">等待数据加载。</p>
          </div>
          <button id="copy-link" class="ghost-button" type="button">复制当前链接</button>
        </div>
        <div id="paper-list" class="paper-list"></div>
      </section>

      <section class="panel detail-panel">
        <div id="paper-detail" class="paper-detail empty-state">
          <p>选择一篇论文查看摘要与中文总结。</p>
        </div>
      </section>
    </main>
  </div>

  <script type="module" src="./assets/app.js"></script>
</body>
</html>
"""


STYLE_CSS = """:root{
  --bg: #f6f0e8;
  --paper: rgba(255,255,255,0.86);
  --paper-strong: #fffaf4;
  --ink: #1f1a17;
  --muted: #665f58;
  --line: rgba(61,42,26,0.14);
  --accent: #b84d22;
  --accent-strong: #8f3410;
  --accent-soft: rgba(184,77,34,0.12);
  --shadow: 0 18px 48px rgba(61,42,26,0.12);
  --radius-lg: 28px;
  --radius-md: 18px;
  --radius-sm: 12px;
}

*{box-sizing:border-box}

html{
  min-height:100%;
  background:
    radial-gradient(circle at top left, rgba(184,77,34,0.18), transparent 30%),
    radial-gradient(circle at top right, rgba(65,105,77,0.12), transparent 26%),
    linear-gradient(180deg, #f9f4ec 0%, #f3eadf 100%);
}

body{
  margin:0;
  color:var(--ink);
  font:16px/1.6 "Avenir Next","Segoe UI Variable","Segoe UI",sans-serif;
}

a{color:inherit}

.page-shell{
  width:min(1440px, calc(100vw - 32px));
  margin:24px auto 40px;
}

.hero{
  display:grid;
  gap:18px;
  grid-template-columns: 1.8fr 1fr;
  padding:28px;
  border:1px solid var(--line);
  border-radius:var(--radius-lg);
  background:
    linear-gradient(135deg, rgba(255,250,244,0.95), rgba(255,243,228,0.88)),
    rgba(255,255,255,0.7);
  box-shadow:var(--shadow);
  overflow:hidden;
  position:relative;
}

.hero::after{
  content:"";
  position:absolute;
  inset:auto -80px -90px auto;
  width:260px;
  height:260px;
  border-radius:999px;
  background:radial-gradient(circle, rgba(184,77,34,0.18), transparent 65%);
  pointer-events:none;
}

.eyebrow{
  margin:0 0 6px;
  letter-spacing:.22em;
  text-transform:uppercase;
  font-size:12px;
  color:var(--accent-strong);
}

.hero-copy h1,
.panel-head h2,
.tag-strip-head h3{
  margin:0;
  font-family:"Iowan Old Style","Palatino Linotype","Book Antiqua",Georgia,serif;
  font-weight:700;
  letter-spacing:-0.02em;
}

.hero-copy h1{
  font-size:clamp(32px, 5vw, 56px);
  line-height:1.02;
  max-width:14ch;
}

.hero-subtitle{
  margin:14px 0 0;
  max-width:58ch;
  color:var(--muted);
}

.hero-meta{
  display:grid;
  gap:14px;
  align-content:start;
}

.hero-chip,
.panel{
  border:1px solid var(--line);
  background:var(--paper);
  box-shadow:var(--shadow);
}

.hero-chip{
  padding:18px 20px;
  border-radius:var(--radius-md);
  backdrop-filter: blur(14px);
}

.chip-label,
.stat-label,
.field span{
  display:block;
  margin-bottom:6px;
  font-size:12px;
  letter-spacing:.08em;
  text-transform:uppercase;
  color:var(--muted);
}

.hero-chip strong{
  font-size:28px;
}

.workspace{
  display:grid;
  grid-template-columns: 280px minmax(360px, 520px) minmax(0, 1fr);
  gap:18px;
  margin-top:18px;
}

.panel{
  border-radius:var(--radius-lg);
  padding:22px;
  backdrop-filter: blur(10px);
}

.panel-head{
  margin-bottom:18px;
}

.panel-head p,
.paper-meta,
.paper-summary,
.paper-intro li,
.empty-state{
  color:var(--muted);
}

.panel-head-row{
  display:flex;
  justify-content:space-between;
  gap:12px;
  align-items:flex-start;
}

.field{
  display:block;
  margin-bottom:16px;
}

.field select,
.field input{
  width:100%;
  padding:12px 14px;
  border:1px solid rgba(61,42,26,0.18);
  border-radius:var(--radius-sm);
  background:#fffdf9;
  color:var(--ink);
  font:inherit;
}

.field select:focus,
.field input:focus{
  outline:2px solid rgba(184,77,34,0.18);
  border-color:rgba(184,77,34,0.4);
}

.sidebar-stats{
  display:grid;
  grid-template-columns:1fr 1fr;
  gap:12px;
  margin:18px 0 22px;
}

.sidebar-stats div{
  padding:14px;
  border-radius:var(--radius-sm);
  background:rgba(255,250,244,0.82);
  border:1px solid rgba(61,42,26,0.08);
}

.tag-strip-head{
  display:flex;
  justify-content:space-between;
  gap:12px;
  align-items:center;
  margin-bottom:12px;
}

.tag-cloud,
.paper-tags{
  display:flex;
  flex-wrap:wrap;
  gap:10px;
}

.tag-button,
.paper-tag,
.ghost-button{
  border:1px solid rgba(184,77,34,0.18);
  border-radius:999px;
  background:#fffaf4;
  color:var(--accent-strong);
  padding:8px 12px;
  font:600 13px/1 "Avenir Next","Segoe UI Variable","Segoe UI",sans-serif;
}

.tag-button.active{
  background:var(--accent);
  color:#fff;
  border-color:var(--accent);
}

.ghost-button{
  cursor:pointer;
  transition:transform .18s ease, background-color .18s ease;
}

.ghost-button:hover{
  transform:translateY(-1px);
  background:var(--paper-strong);
}

.paper-list{
  display:grid;
  gap:12px;
  max-height:calc(100vh - 280px);
  overflow:auto;
  padding-right:4px;
}

.paper-card{
  border:1px solid rgba(61,42,26,0.1);
  border-radius:20px;
  padding:16px 18px;
  background:rgba(255,252,246,0.94);
  cursor:pointer;
  transition:transform .18s ease, border-color .18s ease, box-shadow .18s ease;
}

.paper-card:hover{
  transform:translateY(-2px);
  border-color:rgba(184,77,34,0.36);
  box-shadow:0 12px 26px rgba(61,42,26,0.08);
}

.paper-card.active{
  border-color:rgba(184,77,34,0.58);
  background:linear-gradient(180deg, rgba(255,247,239,0.98), rgba(255,253,249,0.98));
}

.paper-card h3{
  margin:0 0 8px;
  font-size:18px;
  line-height:1.3;
}

.paper-card p{
  margin:0;
}

.paper-card .headline{
  margin-top:10px;
  color:var(--ink);
  font-weight:600;
}

.paper-card .card-tags{
  margin-top:12px;
  display:flex;
  flex-wrap:wrap;
  gap:8px;
}

.paper-card .card-tags span{
  padding:5px 9px;
  border-radius:999px;
  background:var(--accent-soft);
  color:var(--accent-strong);
  font-size:12px;
}

.detail-panel{
  min-height:700px;
}

.paper-detail{
  animation:fadeUp .35s ease;
}

.paper-detail h2{
  margin:0;
  font-family:"Iowan Old Style","Palatino Linotype","Book Antiqua",Georgia,serif;
  font-size:clamp(28px, 4vw, 42px);
  line-height:1.08;
}

.paper-links{
  display:flex;
  flex-wrap:wrap;
  gap:10px;
  margin:20px 0;
}

.paper-link{
  display:inline-flex;
  align-items:center;
  gap:8px;
  padding:9px 14px;
  border-radius:999px;
  background:#fffaf4;
  border:1px solid rgba(61,42,26,0.12);
  text-decoration:none;
}

.paper-lead{
  margin:18px 0 22px;
  padding:18px 20px;
  border-radius:22px;
  background:linear-gradient(135deg, rgba(184,77,34,0.14), rgba(184,77,34,0.04));
}

.paper-lead strong{
  display:block;
  margin-bottom:8px;
  font-size:12px;
  letter-spacing:.08em;
  text-transform:uppercase;
  color:var(--accent-strong);
}

.paper-intro{
  padding-left:20px;
}

.paper-intro li + li{
  margin-top:10px;
}

.paper-summary{
  white-space:pre-wrap;
  padding:18px 20px;
  border-radius:22px;
  background:rgba(255,250,244,0.9);
  border:1px solid rgba(61,42,26,0.08);
}

.empty-state,
.loading-state,
.error-state{
  display:grid;
  place-items:center;
  min-height:280px;
  text-align:center;
}

@keyframes fadeUp{
  from{
    opacity:0;
    transform:translateY(12px);
  }
  to{
    opacity:1;
    transform:translateY(0);
  }
}

@media (max-width: 1180px){
  .workspace{
    grid-template-columns: 280px 1fr;
  }

  .detail-panel{
    grid-column: 1 / -1;
  }
}

@media (max-width: 860px){
  .page-shell{
    width:min(100vw - 18px, 100%);
    margin:10px auto 22px;
  }

  .hero{
    grid-template-columns:1fr;
    padding:22px;
  }

  .workspace{
    grid-template-columns:1fr;
  }

  .panel{
    padding:18px;
  }

  .paper-list{
    max-height:none;
  }

  .panel-head-row{
    flex-direction:column;
    align-items:stretch;
  }
}
"""


APP_JS = """const state = {
  manifest: null,
  activeDate: null,
  activeTag: '',
  query: '',
  papers: [],
  selectedPaperId: null,
};

const nodes = {
  siteTitle: document.getElementById('site-title'),
  siteSubtitle: document.getElementById('site-subtitle'),
  heroLatest: document.getElementById('hero-latest'),
  heroCount: document.getElementById('hero-count'),
  dateSelect: document.getElementById('date-select'),
  searchInput: document.getElementById('search-input'),
  resultCount: document.getElementById('result-count'),
  generatedAt: document.getElementById('generated-at'),
  tagCloud: document.getElementById('tag-cloud'),
  clearTag: document.getElementById('clear-tag'),
  listTitle: document.getElementById('list-title'),
  listSubtitle: document.getElementById('list-subtitle'),
  paperList: document.getElementById('paper-list'),
  paperDetail: document.getElementById('paper-detail'),
  copyLink: document.getElementById('copy-link'),
};

const urlState = () => {
  const params = new URLSearchParams(window.location.search);
  return {
    date: params.get('date') || '',
    paper: params.get('paper') || '',
    q: params.get('q') || '',
    tag: params.get('tag') || '',
  };
};

function formatDate(value) {
  if (!value) return '-';
  return value;
}

function escapeHtml(value) {
  return String(value).replace(/[&<>\"']/g, (char) => ({
    '&': '&amp;',
    '<': '&lt;',
    '>': '&gt;',
    '\"': '&quot;',
    \"'\": '&#39;',
  }[char]));
}

function buildPaperUrl() {
  const params = new URLSearchParams();
  if (state.activeDate) params.set('date', state.activeDate);
  if (state.selectedPaperId) params.set('paper', state.selectedPaperId);
  if (state.query) params.set('q', state.query);
  if (state.activeTag) params.set('tag', state.activeTag);
  const query = params.toString();
  return query ? `${window.location.pathname}?${query}` : window.location.pathname;
}

function syncHistory(replace = false) {
  const url = buildPaperUrl();
  if (replace) {
    history.replaceState(null, '', url);
  } else {
    history.pushState(null, '', url);
  }
}

function searchIndex(paper) {
  return [
    paper.title,
    paper.authors.join(' '),
    paper.headline_zh,
    paper.summary,
    paper.tags_zh.join(' '),
    paper.intro_zh.join(' '),
  ].join(' ').toLowerCase();
}

function filteredPapers() {
  const q = state.query.trim().toLowerCase();
  return state.papers.filter((paper) => {
    const tagOk = !state.activeTag || paper.tags_zh.includes(state.activeTag);
    const queryOk = !q || searchIndex(paper).includes(q);
    return tagOk && queryOk;
  });
}

function topTags(papers) {
  const counts = new Map();
  for (const paper of papers) {
    for (const tag of paper.tags_zh) {
      counts.set(tag, (counts.get(tag) || 0) + 1);
    }
  }
  return [...counts.entries()]
    .sort((a, b) => b[1] - a[1] || a[0].localeCompare(b[0], 'zh-CN'))
    .slice(0, 18);
}

function ensureSelectedPaper(list) {
  if (!list.length) {
    state.selectedPaperId = null;
    return;
  }
  const exists = list.some((paper) => paper.arxiv_id === state.selectedPaperId);
  if (!exists) {
    state.selectedPaperId = list[0].arxiv_id;
  }
}

function renderTags() {
  const tags = topTags(state.papers);
  if (!tags.length) {
    nodes.tagCloud.innerHTML = '<p class="empty-state">这一日期没有可用关键词。</p>';
    nodes.clearTag.hidden = true;
    return;
  }
  nodes.clearTag.hidden = !state.activeTag;
  nodes.tagCloud.innerHTML = tags.map(([tag, count]) => `
    <button class="tag-button ${tag === state.activeTag ? 'active' : ''}" type="button" data-tag="${escapeHtml(tag)}">
      ${escapeHtml(tag)} <span aria-hidden="true">·</span> ${count}
    </button>
  `).join('');
  nodes.tagCloud.querySelectorAll('[data-tag]').forEach((button) => {
    button.addEventListener('click', () => {
      state.activeTag = button.dataset.tag === state.activeTag ? '' : button.dataset.tag;
      render();
      syncHistory();
    });
  });
}

function renderList() {
  const list = filteredPapers();
  ensureSelectedPaper(list);
  nodes.resultCount.textContent = String(list.length);
  nodes.listTitle.textContent = `${state.activeDate || '-'} Papers`;
  nodes.listSubtitle.textContent = list.length
    ? `共 ${state.papers.length} 篇，当前筛出 ${list.length} 篇。`
    : '当前筛选条件下没有匹配结果。';

  if (!list.length) {
    nodes.paperList.innerHTML = '<div class="empty-state"><p>换个日期、关键词或标签试试。</p></div>';
    return;
  }

  nodes.paperList.innerHTML = list.map((paper) => `
    <article class="paper-card ${paper.arxiv_id === state.selectedPaperId ? 'active' : ''}" data-paper-id="${escapeHtml(paper.arxiv_id)}">
      <p class="paper-meta">${escapeHtml(paper.arxiv_id)} · ${escapeHtml(paper.authors_text)}</p>
      <h3>${escapeHtml(paper.title)}</h3>
      <p class="headline">${escapeHtml(paper.headline_zh || '暂无中文一句话要点')}</p>
      <div class="card-tags">${paper.tags_zh.slice(0, 4).map((tag) => `<span>${escapeHtml(tag)}</span>`).join('')}</div>
    </article>
  `).join('');

  nodes.paperList.querySelectorAll('[data-paper-id]').forEach((card) => {
    card.addEventListener('click', () => {
      state.selectedPaperId = card.dataset.paperId;
      renderDetail();
      renderList();
      syncHistory();
    });
  });
}

function renderDetail() {
  const paper = state.papers.find((item) => item.arxiv_id === state.selectedPaperId);
  if (!paper) {
    nodes.paperDetail.className = 'paper-detail empty-state';
    nodes.paperDetail.innerHTML = '<p>选择一篇论文查看摘要与中文总结。</p>';
    return;
  }

  nodes.paperDetail.className = 'paper-detail';
  nodes.paperDetail.innerHTML = `
    <p class="paper-meta">${escapeHtml(paper.arxiv_id)} · ${escapeHtml(paper.authors_text)}</p>
    <h2>${escapeHtml(paper.title)}</h2>
    <div class="paper-links">
      <a class="paper-link" href="${escapeHtml(paper.abs_url)}" target="_blank" rel="noreferrer">arXiv Abstract</a>
      <a class="paper-link" href="${escapeHtml(paper.pdf_url)}" target="_blank" rel="noreferrer">PDF</a>
    </div>
    <div class="paper-lead">
      <strong>中文一句话要点</strong>
      <div>${escapeHtml(paper.headline_zh || '暂无')}</div>
    </div>
    <div class="paper-tags">${paper.tags_zh.map((tag) => `<span class="paper-tag">${escapeHtml(tag)}</span>`).join('')}</div>
    <section>
      <h3>3 点简述</h3>
      <ol class="paper-intro">${paper.intro_zh.map((item) => `<li>${escapeHtml(item)}</li>`).join('')}</ol>
    </section>
    <section>
      <h3>原始摘要</h3>
      <div class="paper-summary">${escapeHtml(paper.summary || '暂无摘要')}</div>
    </section>
  `;
}

function renderHeader() {
  document.title = state.manifest.site.title;
  nodes.siteTitle.textContent = state.manifest.site.title;
  nodes.siteSubtitle.textContent = `共收录 ${state.manifest.summary.total_dates} 天、${state.manifest.summary.total_papers} 篇论文。点击左侧日期可即时切换，无需 GitHub Pages 再跑 Jekyll。`;
  nodes.heroLatest.textContent = formatDate(state.manifest.summary.latest_date);
  nodes.heroCount.textContent = String(state.manifest.summary.total_papers);
  nodes.generatedAt.textContent = state.manifest.generated_at;
}

function renderDateSelect() {
  nodes.dateSelect.innerHTML = state.manifest.dates.map((item) => `
    <option value="${escapeHtml(item.date)}" ${item.date === state.activeDate ? 'selected' : ''}>
      ${escapeHtml(item.date)} (${item.paper_count})
    </option>
  `).join('');
}

function render() {
  renderHeader();
  renderDateSelect();
  renderTags();
  renderList();
  renderDetail();
}

async function loadDate(date, replace = false) {
  const entry = state.manifest.dates.find((item) => item.date === date) || state.manifest.dates[0];
  if (!entry) {
    nodes.paperList.innerHTML = '<div class="error-state"><p>没有可用日期。</p></div>';
    return;
  }

  state.activeDate = entry.date;
  nodes.paperList.innerHTML = '<div class="loading-state"><p>正在加载该日期的数据...</p></div>';

  const response = await fetch(`./${entry.data_path}`, { cache: 'no-store' });
  if (!response.ok) {
    throw new Error(`Failed to fetch ${entry.data_path}`);
  }

  const payload = await response.json();
  state.papers = payload.papers || [];
  const params = urlState();
  if (params.paper && params.date === state.activeDate) {
    state.selectedPaperId = params.paper;
  }
  ensureSelectedPaper(filteredPapers());
  render();
  syncHistory(replace);
}

async function init() {
  try {
    const response = await fetch('./data/manifest.json', { cache: 'no-store' });
    if (!response.ok) {
      throw new Error('manifest load failed');
    }
    state.manifest = await response.json();
    const params = urlState();
    state.query = params.q;
    state.activeTag = params.tag;
    nodes.searchInput.value = state.query;
    renderHeader();
    await loadDate(params.date || state.manifest.summary.latest_date, true);
  } catch (error) {
    nodes.paperList.innerHTML = '<div class="error-state"><p>站点索引加载失败，请检查 docs/data/manifest.json 是否存在。</p></div>';
    nodes.paperDetail.className = 'paper-detail error-state';
    nodes.paperDetail.innerHTML = `<p>${escapeHtml(error.message)}</p>`;
  }
}

nodes.dateSelect.addEventListener('change', async (event) => {
  state.selectedPaperId = null;
  await loadDate(event.target.value);
});

nodes.searchInput.addEventListener('input', (event) => {
  state.query = event.target.value;
  renderList();
  renderDetail();
  syncHistory(true);
});

nodes.clearTag.addEventListener('click', () => {
  state.activeTag = '';
  render();
  syncHistory();
});

nodes.copyLink.addEventListener('click', async () => {
  const url = `${window.location.origin}${buildPaperUrl()}`;
  try {
    await navigator.clipboard.writeText(url);
    nodes.copyLink.textContent = '已复制';
  } catch (error) {
    nodes.copyLink.textContent = '复制失败';
  }
  window.setTimeout(() => {
    nodes.copyLink.textContent = '复制当前链接';
  }, 1400);
});

window.addEventListener('popstate', async () => {
  const params = urlState();
  state.query = params.q;
  state.activeTag = params.tag;
  nodes.searchInput.value = state.query;
  if (params.date && params.date !== state.activeDate) {
    state.selectedPaperId = params.paper;
    await loadDate(params.date, true);
    return;
  }
  state.selectedPaperId = params.paper || state.selectedPaperId;
  render();
});

init();
"""


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def read_json(path: Path) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def sanitize_text(value: Any) -> str:
    if value is None:
        return ""
    return str(value).strip()


def sanitize_list(values: Any) -> List[str]:
    if not isinstance(values, list):
        return []
    return [sanitize_text(item) for item in values if sanitize_text(item)]


def collect_dates(data_root: Path) -> List[Tuple[str, Path]]:
    items: List[Tuple[str, Path]] = []
    for path in sorted(data_root.glob("*/ai_summary*.json")):
        match = re.search(r"(\d{4}-\d{2}-\d{2})", str(path))
        if not match:
            match = re.search(r"(\d{4}-\d{2}-\d{2})", path.parent.name)
        if match:
            date_label = match.group(1)
        else:
            date_label = datetime.date.fromtimestamp(path.stat().st_mtime).isoformat()
        items.append((date_label, path))
    return sorted(items, key=lambda item: item[0])


def normalize_paper(meta: Dict[str, Any]) -> Dict[str, Any]:
    arxiv_id = sanitize_text(meta.get("arxiv_id"))
    base_id = arxiv_id.split("v")[0] if arxiv_id else ""
    authors = sanitize_list(meta.get("authors"))
    return {
        "title": sanitize_text(meta.get("title")),
        "authors": authors,
        "authors_text": ", ".join(authors) if authors else "Unknown authors",
        "arxiv_id": arxiv_id,
        "base_id": base_id,
        "abs_url": f"https://arxiv.org/abs/{base_id}" if base_id else "",
        "pdf_url": f"https://arxiv.org/pdf/{base_id}.pdf" if base_id else "",
        "summary": sanitize_text(meta.get("summary")),
        "headline_zh": sanitize_text(meta.get("headline_zh")),
        "intro_zh": sanitize_list(meta.get("intro_zh")),
        "tags_zh": sanitize_list(meta.get("tags_zh")),
    }


def write_static_shell(docs_dir: Path) -> None:
    ensure_dir(docs_dir / "assets")
    ensure_dir(docs_dir / "data")
    (docs_dir / ".nojekyll").write_text("", encoding="utf-8")
    (docs_dir / "index.html").write_text(INDEX_HTML, encoding="utf-8")
    (docs_dir / "assets" / "style.css").write_text(STYLE_CSS, encoding="utf-8")
    (docs_dir / "assets" / "app.js").write_text(APP_JS, encoding="utf-8")


def write_json(path: Path, payload: Dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def build_site(data_root: Path, docs_dir: Path, site_title: str) -> Tuple[int, int]:
    pairs = collect_dates(data_root)
    if not pairs:
        print("[ERR] 未找到 data/*/ai_summary*.json", file=sys.stderr)
        sys.exit(2)

    shutil.rmtree(docs_dir, ignore_errors=True)
    write_static_shell(docs_dir)

    manifest_dates: List[Dict[str, Any]] = []
    total_papers = 0

    for date_label, json_path in pairs:
        payload = read_json(json_path)
        raw_papers = payload.get("papers", [])
        if not isinstance(raw_papers, list) or not raw_papers:
            print(f"[WARN] {json_path} 中 papers 为空，跳过 {date_label}")
            continue

        papers = [normalize_paper(paper) for paper in raw_papers]
        total_papers += len(papers)
        out_path = docs_dir / "data" / f"{date_label}.json"
        write_json(
            out_path,
            {
                "date": date_label,
                "paper_count": len(papers),
                "papers": papers,
            },
        )
        manifest_dates.append(
            {
                "date": date_label,
                "paper_count": len(papers),
                "data_path": f"data/{date_label}.json",
            }
        )

    if not manifest_dates:
        print("[ERR] 没有可用的日期页面生成", file=sys.stderr)
        sys.exit(3)

    manifest_dates.sort(key=lambda item: item["date"], reverse=True)
    write_json(
        docs_dir / "data" / "manifest.json",
        {
            "site": {"title": site_title},
            "generated_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "summary": {
                "total_dates": len(manifest_dates),
                "total_papers": total_papers,
                "latest_date": manifest_dates[0]["date"],
            },
            "dates": manifest_dates,
        },
    )
    return len(manifest_dates), total_papers


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build a JSON-driven static site for GitHub Pages.")
    parser.add_argument("--data", default=os.getenv("DATA_DIR", "data"), help="数据根目录（默认 data/）")
    parser.add_argument("--outdir", default=os.getenv("DOCS_DIR", "docs"), help="输出站点目录（默认 docs/）")
    parser.add_argument(
        "--title",
        default=os.getenv("SITE_TITLE", "arXiv·cs.CV 中文要点汇总（with DeepSeek）"),
        help="站点标题",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    date_count, paper_count = build_site(Path(args.data), Path(args.outdir), args.title)
    print(f"[OK] 生成完成。日期数：{date_count}，论文数：{paper_count}。")
    print(f"👉 静态站点已输出到 {args.outdir}/，GitHub Pages 直接托管该目录即可。")


if __name__ == "__main__":
    main()
