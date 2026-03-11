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
    <header class="masthead">
      <div class="masthead-copy">
        <p class="eyebrow">Daily Research Dispatch</p>
        <h1 id="site-title">加载中...</h1>
        <p id="site-subtitle" class="masthead-subtitle">正在读取每日论文索引。</p>
      </div>
      <div class="stat-grid">
        <article class="stat-card">
          <span class="stat-label">Latest Update</span>
          <strong id="hero-latest">-</strong>
        </article>
        <article class="stat-card">
          <span class="stat-label">Archive Size</span>
          <strong id="hero-count">-</strong>
        </article>
        <article class="stat-card accent">
          <span class="stat-label">Active Day</span>
          <strong id="hero-active">-</strong>
        </article>
      </div>
    </header>

    <section class="control-deck">
      <section class="control-main panel">
        <div class="section-head">
          <div>
            <p class="section-kicker">Control Room</p>
            <h2>快速切换日期、搜索主题、聚焦标签</h2>
          </div>
          <span id="generated-at" class="generated-at">-</span>
        </div>
        <div class="control-grid">
          <label class="field">
            <span>日期</span>
            <select id="date-select"></select>
          </label>
          <label class="field">
            <span>搜索</span>
            <input id="search-input" type="search" placeholder="标题 / 作者 / 中文要点 / 关键词 / 摘要">
          </label>
        </div>
        <div class="control-actions">
          <button id="clear-filters" class="ghost-button" type="button">清空搜索与标签</button>
          <button id="copy-link" class="ghost-button" type="button">复制当前链接</button>
        </div>
        <div id="active-filters" class="filter-pills"></div>
      </section>

      <div class="control-side">
        <section class="quick-panel panel">
          <div class="section-head compact">
            <div>
              <p class="section-kicker">Recent Drops</p>
              <h3>最近更新</h3>
            </div>
            <strong id="result-count">0</strong>
          </div>
          <div id="recent-dates" class="recent-dates"></div>
        </section>

        <section class="quick-panel panel">
          <div class="section-head compact">
            <div>
              <p class="section-kicker">Tag Lens</p>
              <h3>热门关键词</h3>
            </div>
            <button id="clear-tag" class="ghost-button" type="button" hidden>清除标签</button>
          </div>
          <div id="tag-cloud" class="tag-cloud"></div>
        </section>
      </div>
    </section>

    <main class="reading-room">
      <section class="panel library-panel">
        <div class="panel-head">
          <div>
            <p class="section-kicker" id="list-kicker">Archive</p>
            <h2 id="list-title">Papers</h2>
            <p id="list-subtitle">等待数据加载。</p>
          </div>
        </div>
        <div id="paper-list" class="paper-list"></div>
      </section>

      <section class="panel detail-panel">
        <div class="detail-toolbar">
          <div>
            <p class="section-kicker" id="detail-kicker">Selected Paper</p>
            <h2>Paper Notes</h2>
          </div>
          <div class="detail-nav">
            <button id="prev-paper" class="ghost-button" type="button">上一篇</button>
            <button id="next-paper" class="ghost-button" type="button">下一篇</button>
          </div>
        </div>
        <div id="paper-detail" class="paper-detail empty-state">
          <p>选择一篇论文查看摘要、中文总结与关键词。</p>
        </div>
      </section>
    </main>
  </div>

  <script type="module" src="./assets/app.js"></script>
</body>
</html>
"""


STYLE_CSS = """:root{
  --bg: #f4efe6;
  --panel: rgba(255, 250, 242, 0.82);
  --panel-strong: rgba(255, 252, 247, 0.94);
  --panel-soft: rgba(255, 247, 236, 0.8);
  --ink: #1d1814;
  --muted: #6c645a;
  --line: rgba(49, 35, 21, 0.11);
  --accent: #bb5c2b;
  --accent-strong: #8f3912;
  --accent-soft: rgba(187, 92, 43, 0.12);
  --secondary: #18493d;
  --secondary-soft: rgba(24, 73, 61, 0.1);
  --shadow: 0 28px 80px rgba(69, 45, 24, 0.12);
  --shadow-soft: 0 14px 38px rgba(69, 45, 24, 0.08);
  --radius-xl: 34px;
  --radius-lg: 24px;
  --radius-md: 18px;
  --radius-sm: 12px;
}

*{box-sizing:border-box}

html{
  min-height:100%;
  background:
    radial-gradient(circle at 10% 0%, rgba(187, 92, 43, 0.18), transparent 24%),
    radial-gradient(circle at 100% 10%, rgba(24, 73, 61, 0.16), transparent 22%),
    linear-gradient(180deg, #faf5ed 0%, #f1e7dc 100%);
}

body{
  margin:0;
  color:var(--ink);
  font:16px/1.6 "Avenir Next","Segoe UI Variable","Segoe UI",sans-serif;
  background:
    linear-gradient(180deg, rgba(255,255,255,0.14), rgba(255,255,255,0));
}

button,
input,
select{
  font:inherit;
}

a{
  color:inherit;
}

.page-shell{
  width:min(1500px, calc(100vw - 30px));
  margin:18px auto 34px;
}

.masthead{
  display:grid;
  grid-template-columns:minmax(0, 1.7fr) minmax(320px, 0.95fr);
  gap:20px;
  padding:30px;
  border:1px solid var(--line);
  border-radius:var(--radius-xl);
  background:
    linear-gradient(150deg, rgba(255,252,246,0.95), rgba(255,240,222,0.84)),
    rgba(255,255,255,0.7);
  box-shadow:var(--shadow);
  position:relative;
  overflow:hidden;
}

.masthead::before{
  content:"";
  position:absolute;
  inset:auto -110px -120px auto;
  width:320px;
  height:320px;
  border-radius:999px;
  background:radial-gradient(circle, rgba(187, 92, 43, 0.2), transparent 65%);
  pointer-events:none;
}

.eyebrow,
.section-kicker{
  margin:0 0 8px;
  letter-spacing:.2em;
  text-transform:uppercase;
  font-size:12px;
  color:var(--accent-strong);
}

.masthead-copy h1,
.panel-head h2,
.detail-toolbar h2,
.section-head h2,
.section-head h3{
  margin:0;
  font-family:"Iowan Old Style","Palatino Linotype","Book Antiqua",Georgia,serif;
  font-weight:700;
  letter-spacing:-0.025em;
}

.masthead-copy h1{
  font-size:clamp(38px, 5vw, 68px);
  line-height:.95;
  max-width:13ch;
}

.masthead-subtitle{
  margin:16px 0 0;
  max-width:62ch;
  color:var(--muted);
  font-size:17px;
}

.stat-grid{
  display:grid;
  gap:14px;
  align-content:start;
}

.stat-card,
.panel{
  border:1px solid var(--line);
  background:var(--panel);
  box-shadow:var(--shadow-soft);
  backdrop-filter:blur(18px);
}

.stat-card{
  padding:20px 22px;
  border-radius:var(--radius-lg);
}

.stat-card.accent{
  background:linear-gradient(135deg, rgba(24, 73, 61, 0.14), rgba(24, 73, 61, 0.05));
}

.stat-label,
.field span{
  display:block;
  margin-bottom:8px;
  font-size:12px;
  letter-spacing:.08em;
  text-transform:uppercase;
  color:var(--muted);
}

.stat-card strong{
  font-size:30px;
  line-height:1.05;
}

.control-deck{
  display:grid;
  grid-template-columns:minmax(0, 1.35fr) minmax(320px, 0.95fr);
  gap:18px;
  margin-top:18px;
}

.control-main,
.quick-panel,
.library-panel,
.detail-panel{
  border-radius:var(--radius-xl);
}

.panel{
  padding:22px;
}

.control-main{
  background:
    linear-gradient(160deg, rgba(255,252,247,0.92), rgba(253,244,232,0.78));
}

.control-side{
  display:grid;
  gap:18px;
}

.section-head{
  display:flex;
  justify-content:space-between;
  gap:16px;
  align-items:flex-start;
  margin-bottom:18px;
}

.section-head.compact{
  align-items:center;
  margin-bottom:14px;
}

.section-head h2{
  font-size:26px;
  line-height:1.05;
}

.section-head h3{
  font-size:22px;
  line-height:1.1;
}

.generated-at{
  align-self:center;
  color:var(--muted);
  font-size:14px;
}

.control-grid{
  display:grid;
  grid-template-columns:minmax(200px, 280px) minmax(0, 1fr);
  gap:14px;
}

.field{
  display:block;
}

.field select,
.field input{
  width:100%;
  min-height:52px;
  padding:12px 16px;
  border:1px solid rgba(49, 35, 21, 0.14);
  border-radius:var(--radius-md);
  background:rgba(255,255,255,0.9);
  color:var(--ink);
  box-shadow:inset 0 1px 0 rgba(255,255,255,0.8);
}

.field select:focus,
.field input:focus{
  outline:2px solid rgba(187, 92, 43, 0.18);
  border-color:rgba(187, 92, 43, 0.42);
}

.control-actions{
  display:flex;
  flex-wrap:wrap;
  gap:10px;
  margin-top:14px;
}

.ghost-button,
.date-pill,
.tag-button,
.filter-chip,
.paper-link,
.paper-tag{
  border-radius:999px;
  border:1px solid rgba(49, 35, 21, 0.12);
  background:rgba(255,252,247,0.88);
  color:var(--ink);
}

.ghost-button{
  min-height:42px;
  padding:10px 14px;
  cursor:pointer;
  transition:transform .18s ease, border-color .18s ease, background-color .18s ease;
}

.ghost-button:hover:not(:disabled),
.date-pill:hover,
.tag-button:hover{
  transform:translateY(-1px);
  border-color:rgba(187, 92, 43, 0.36);
  background:rgba(255,247,239,0.98);
}

.ghost-button:disabled{
  opacity:.45;
  cursor:not-allowed;
}

.filter-pills,
.tag-cloud,
.paper-tags,
.paper-links{
  display:flex;
  flex-wrap:wrap;
  gap:10px;
}

.filter-pills{
  margin-top:16px;
}

.filter-chip{
  display:inline-flex;
  align-items:center;
  gap:8px;
  min-height:38px;
  padding:8px 12px;
  color:var(--accent-strong);
  background:rgba(255,248,241,0.96);
}

.filter-chip.static{
  color:var(--secondary);
  background:rgba(24, 73, 61, 0.08);
}

.filter-chip.empty{
  color:var(--muted);
}

.date-pill{
  display:flex;
  justify-content:space-between;
  align-items:center;
  gap:12px;
  width:100%;
  min-height:54px;
  padding:12px 14px;
  text-align:left;
  cursor:pointer;
}

.date-pill.active{
  border-color:rgba(187, 92, 43, 0.48);
  background:linear-gradient(135deg, rgba(255,239,225,0.98), rgba(255,248,241,0.98));
}

.date-pill .date-pill-meta{
  display:flex;
  flex-direction:column;
  min-width:0;
}

.date-pill .date-pill-label{
  font-weight:700;
}

.date-pill .date-pill-count{
  color:var(--muted);
  font-size:13px;
}

.date-pill .date-pill-badge{
  padding:4px 8px;
  border-radius:999px;
  background:var(--accent-soft);
  color:var(--accent-strong);
  font-size:12px;
}

.recent-dates{
  display:grid;
  gap:10px;
}

.tag-button{
  display:inline-flex;
  align-items:center;
  gap:8px;
  min-height:38px;
  padding:8px 12px;
  cursor:pointer;
  color:var(--accent-strong);
}

.tag-button.active{
  background:var(--accent);
  border-color:var(--accent);
  color:#fff;
}

.tag-count{
  padding:2px 7px;
  border-radius:999px;
  background:rgba(255,255,255,0.65);
  font-size:12px;
}

.tag-button.active .tag-count{
  background:rgba(255,255,255,0.18);
}

.reading-room{
  display:grid;
  grid-template-columns:minmax(380px, 470px) minmax(0, 1fr);
  gap:18px;
  margin-top:18px;
}

.library-panel,
.detail-panel{
  display:flex;
  flex-direction:column;
  min-height:0;
}

.panel-head{
  margin-bottom:18px;
}

.panel-head p,
.paper-meta,
.paper-snippet,
.paper-summary,
.paper-intro li,
.empty-state,
.mini-meta,
.detail-authors,
.info-card p{
  color:var(--muted);
}

.paper-list{
  display:grid;
  gap:12px;
  overflow:auto;
  max-height:calc(100vh - 410px);
  padding-right:6px;
}

.paper-card{
  position:relative;
  display:grid;
  gap:12px;
  padding:18px;
  border:1px solid rgba(49, 35, 21, 0.08);
  border-radius:22px;
  background:var(--panel-strong);
  cursor:pointer;
  transition:transform .18s ease, border-color .18s ease, box-shadow .18s ease;
}

.paper-card::before{
  content:"";
  position:absolute;
  inset:14px auto 14px 0;
  width:4px;
  border-radius:999px;
  background:transparent;
}

.paper-card:hover{
  transform:translateY(-2px);
  border-color:rgba(187, 92, 43, 0.34);
  box-shadow:0 14px 30px rgba(69, 45, 24, 0.1);
}

.paper-card.active{
  border-color:rgba(187, 92, 43, 0.5);
  background:linear-gradient(180deg, rgba(255,246,235,0.98), rgba(255,252,247,0.98));
}

.paper-card.active::before{
  background:linear-gradient(180deg, var(--accent), #df9a61);
}

.paper-card-head{
  display:flex;
  justify-content:space-between;
  gap:16px;
  align-items:flex-start;
}

.paper-rank{
  font:700 12px/1 "Avenir Next","Segoe UI Variable","Segoe UI",sans-serif;
  letter-spacing:.12em;
  text-transform:uppercase;
  color:var(--accent-strong);
}

.mini-meta{
  font-size:13px;
}

.paper-card h3{
  margin:0;
  font-family:"Iowan Old Style","Palatino Linotype","Book Antiqua",Georgia,serif;
  font-size:22px;
  line-height:1.18;
}

.paper-headline{
  color:var(--ink);
  font-weight:700;
}

.paper-snippet{
  display:-webkit-box;
  -webkit-line-clamp:3;
  -webkit-box-orient:vertical;
  overflow:hidden;
}

.card-tags{
  display:flex;
  flex-wrap:wrap;
  gap:8px;
}

.card-tags span{
  padding:6px 10px;
  border-radius:999px;
  background:var(--accent-soft);
  color:var(--accent-strong);
  font-size:12px;
}

.detail-toolbar{
  display:flex;
  justify-content:space-between;
  gap:16px;
  align-items:flex-start;
  padding-bottom:16px;
  border-bottom:1px solid var(--line);
  margin-bottom:18px;
}

.detail-toolbar h2{
  font-size:34px;
  line-height:1;
}

.detail-nav{
  display:flex;
  flex-wrap:wrap;
  gap:10px;
}

.paper-detail{
  overflow:auto;
  max-height:calc(100vh - 410px);
  padding-right:6px;
  animation:fadeUp .28s ease;
}

.detail-meta-bar{
  display:flex;
  flex-wrap:wrap;
  gap:10px;
  margin-bottom:12px;
}

.detail-badge{
  display:inline-flex;
  align-items:center;
  min-height:34px;
  padding:6px 11px;
  border-radius:999px;
  background:rgba(24, 73, 61, 0.08);
  color:var(--secondary);
  font-size:13px;
}

.detail-badge.alt{
  background:var(--accent-soft);
  color:var(--accent-strong);
}

.paper-detail h3{
  margin:0;
  font-family:"Iowan Old Style","Palatino Linotype","Book Antiqua",Georgia,serif;
  font-size:clamp(30px, 4vw, 48px);
  line-height:1.02;
}

.detail-authors{
  margin:14px 0 0;
  font-size:15px;
}

.paper-links{
  margin:22px 0;
}

.paper-link{
  display:inline-flex;
  align-items:center;
  min-height:42px;
  padding:10px 14px;
  text-decoration:none;
}

.info-grid{
  display:grid;
  grid-template-columns:1.2fr .8fr;
  gap:14px;
  margin:0 0 20px;
}

.info-card{
  padding:18px 18px 16px;
  border-radius:22px;
  border:1px solid rgba(49, 35, 21, 0.09);
  background:var(--panel-soft);
}

.info-card strong{
  display:block;
  margin-bottom:10px;
  font-size:12px;
  letter-spacing:.08em;
  text-transform:uppercase;
  color:var(--accent-strong);
}

.info-card p{
  margin:0;
}

.paper-tags{
  gap:8px;
}

.paper-tag{
  display:inline-flex;
  align-items:center;
  min-height:34px;
  padding:6px 10px;
  color:var(--secondary);
  background:rgba(24, 73, 61, 0.08);
}

.paper-tag.empty{
  color:var(--muted);
  background:rgba(49, 35, 21, 0.05);
}

.detail-section{
  margin-top:20px;
}

.detail-section h4{
  margin:0 0 10px;
  font:700 16px/1.2 "Avenir Next","Segoe UI Variable","Segoe UI",sans-serif;
  letter-spacing:.06em;
  text-transform:uppercase;
  color:var(--accent-strong);
}

.paper-intro{
  margin:0;
  padding-left:20px;
}

.paper-intro li + li{
  margin-top:10px;
}

.paper-summary{
  margin:0;
  padding:18px 20px;
  border-radius:24px;
  border:1px solid rgba(49, 35, 21, 0.08);
  background:rgba(255,252,247,0.92);
  white-space:pre-wrap;
}

.empty-state,
.loading-state,
.error-state{
  display:grid;
  place-items:center;
  min-height:260px;
  text-align:center;
}

@keyframes fadeUp{
  from{
    opacity:0;
    transform:translateY(10px);
  }
  to{
    opacity:1;
    transform:translateY(0);
  }
}

@media (max-width: 1240px){
  .masthead,
  .control-deck,
  .reading-room{
    grid-template-columns:1fr;
  }

  .paper-list,
  .paper-detail{
    max-height:none;
  }
}

@media (max-width: 820px){
  .page-shell{
    width:min(100vw - 14px, 100%);
    margin:8px auto 20px;
  }

  .masthead,
  .panel{
    padding:18px;
    border-radius:26px;
  }

  .masthead-copy h1{
    max-width:none;
    font-size:42px;
  }

  .section-head,
  .detail-toolbar,
  .paper-card-head{
    flex-direction:column;
    align-items:flex-start;
  }

  .control-grid,
  .info-grid{
    grid-template-columns:1fr;
  }

  .detail-nav,
  .control-actions{
    width:100%;
  }

  .detail-nav .ghost-button,
  .control-actions .ghost-button{
    flex:1 1 auto;
  }
}
"""


APP_JS = """const state = {
  manifest: null,
  activeDate: null,
  activeTag: '',
  query: '',
  papers: [],
  filtered: [],
  selectedPaperId: null,
};

const nodes = {
  siteTitle: document.getElementById('site-title'),
  siteSubtitle: document.getElementById('site-subtitle'),
  heroLatest: document.getElementById('hero-latest'),
  heroCount: document.getElementById('hero-count'),
  heroActive: document.getElementById('hero-active'),
  dateSelect: document.getElementById('date-select'),
  searchInput: document.getElementById('search-input'),
  generatedAt: document.getElementById('generated-at'),
  resultCount: document.getElementById('result-count'),
  recentDates: document.getElementById('recent-dates'),
  activeFilters: document.getElementById('active-filters'),
  clearFilters: document.getElementById('clear-filters'),
  tagCloud: document.getElementById('tag-cloud'),
  clearTag: document.getElementById('clear-tag'),
  listKicker: document.getElementById('list-kicker'),
  listTitle: document.getElementById('list-title'),
  listSubtitle: document.getElementById('list-subtitle'),
  paperList: document.getElementById('paper-list'),
  detailKicker: document.getElementById('detail-kicker'),
  paperDetail: document.getElementById('paper-detail'),
  copyLink: document.getElementById('copy-link'),
  prevPaper: document.getElementById('prev-paper'),
  nextPaper: document.getElementById('next-paper'),
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

function escapeHtml(value) {
  return String(value).replace(/[&<>"']/g, (char) => ({
    '&': '&amp;',
    '<': '&lt;',
    '>': '&gt;',
    '"': '&quot;',
    "'": '&#39;',
  }[char]));
}

function excerpt(text, maxLen = 160) {
  const clean = String(text || '').replace(/\\s+/g, ' ').trim();
  if (!clean) return '暂无额外摘要预览。';
  return clean.length > maxLen ? `${clean.slice(0, maxLen - 1)}…` : clean;
}

function compactAuthors(authors) {
  if (!authors.length) return 'Unknown authors';
  if (authors.length <= 3) return authors.join(', ');
  return `${authors.slice(0, 3).join(', ')} 等 ${authors.length} 位作者`;
}

function activeDateEntry() {
  if (!state.manifest) return null;
  return state.manifest.dates.find((item) => item.date === state.activeDate) || state.manifest.dates[0] || null;
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

function selectedPaperIndex() {
  return state.filtered.findIndex((paper) => paper.arxiv_id === state.selectedPaperId);
}

function scrollActiveCardIntoView() {
  const activeCard = nodes.paperList.querySelector('.paper-card.active');
  if (activeCard) {
    activeCard.scrollIntoView({ block: 'nearest' });
  }
}

function renderDateSelect() {
  nodes.dateSelect.innerHTML = state.manifest.dates.map((item) => `
    <option value="${escapeHtml(item.date)}" ${item.date === state.activeDate ? 'selected' : ''}>
      ${escapeHtml(item.date)} (${item.paper_count})
    </option>
  `).join('');
}

function renderRecentDates() {
  const dates = state.manifest?.dates || [];
  const recent = dates.slice(0, 10);
  if (state.activeDate && !recent.some((item) => item.date === state.activeDate)) {
    const activeItem = dates.find((item) => item.date === state.activeDate);
    if (activeItem) {
      recent.pop();
      recent.push(activeItem);
    }
  }

  nodes.recentDates.innerHTML = recent.map((item, index) => `
    <button class="date-pill ${item.date === state.activeDate ? 'active' : ''}" type="button" data-date="${escapeHtml(item.date)}">
      <span class="date-pill-meta">
        <span class="date-pill-label">${escapeHtml(item.date)}</span>
        <span class="date-pill-count">${item.paper_count} papers</span>
      </span>
      <span class="date-pill-badge">${index === 0 ? 'Latest' : 'Open'}</span>
    </button>
  `).join('');

  nodes.recentDates.querySelectorAll('[data-date]').forEach((button) => {
    button.addEventListener('click', async () => {
      state.selectedPaperId = null;
      await loadDate(button.dataset.date);
    });
  });
}

function renderActiveFilters() {
  const chips = [];
  const entry = activeDateEntry();
  if (entry) {
    chips.push(`<span class="filter-chip static">日期 ${escapeHtml(entry.date)} · ${entry.paper_count} 篇</span>`);
  }
  if (state.query) {
    chips.push(`<button class="filter-chip" type="button" data-clear="query">搜索：${escapeHtml(state.query)}</button>`);
  }
  if (state.activeTag) {
    chips.push(`<button class="filter-chip" type="button" data-clear="tag">标签：${escapeHtml(state.activeTag)}</button>`);
  }
  if (!state.query && !state.activeTag) {
    chips.push('<span class="filter-chip empty">当前展示该日期的全部论文。按 / 可快速聚焦搜索框。</span>');
  }

  nodes.activeFilters.innerHTML = chips.join('');
  nodes.activeFilters.querySelectorAll('[data-clear]').forEach((button) => {
    button.addEventListener('click', () => {
      const kind = button.dataset.clear;
      if (kind === 'query') {
        state.query = '';
        nodes.searchInput.value = '';
      }
      if (kind === 'tag') {
        state.activeTag = '';
      }
      render();
      syncHistory();
    });
  });
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
      <span>${escapeHtml(tag)}</span>
      <span class="tag-count">${count}</span>
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
  state.filtered = list;
  ensureSelectedPaper(list);

  const entry = activeDateEntry();
  nodes.resultCount.textContent = String(list.length);
  nodes.listKicker.textContent = entry ? `${entry.date} · ${entry.paper_count} papers` : 'Archive';
  nodes.listTitle.textContent = list.length ? 'Filtered Notes' : 'No Matches';
  nodes.listSubtitle.textContent = list.length
    ? `共 ${state.papers.length} 篇，当前筛出 ${list.length} 篇。支持键盘 / 搜索，j / k 切换论文。`
    : '当前筛选条件下没有匹配结果。可以清空搜索或切换日期。';

  if (!list.length) {
    nodes.paperList.innerHTML = '<div class="empty-state"><p>没有匹配项。试试换个日期、移除标签或缩短关键词。</p></div>';
    return;
  }

  nodes.paperList.innerHTML = list.map((paper, index) => `
    <article class="paper-card ${paper.arxiv_id === state.selectedPaperId ? 'active' : ''}" data-paper-id="${escapeHtml(paper.arxiv_id)}">
      <div class="paper-card-head">
        <div>
          <div class="paper-rank">No. ${String(index + 1).padStart(2, '0')}</div>
          <div class="mini-meta">${escapeHtml(paper.arxiv_id)} · ${escapeHtml(compactAuthors(paper.authors))}</div>
        </div>
      </div>
      <h3>${escapeHtml(paper.title)}</h3>
      <div class="paper-headline">${escapeHtml(paper.headline_zh || '暂无中文一句话要点')}</div>
      <div class="paper-snippet">${escapeHtml(excerpt(paper.intro_zh[0] || paper.summary, 150))}</div>
      <div class="card-tags">${(paper.tags_zh.length ? paper.tags_zh : ['暂无关键词']).slice(0, 4).map((tag) => `<span>${escapeHtml(tag)}</span>`).join('')}</div>
    </article>
  `).join('');

  nodes.paperList.querySelectorAll('[data-paper-id]').forEach((card) => {
    card.addEventListener('click', () => {
      state.selectedPaperId = card.dataset.paperId;
      renderList();
      renderDetail();
      syncHistory();
      scrollActiveCardIntoView();
    });
  });
}

function updateDetailNav() {
  const index = selectedPaperIndex();
  nodes.prevPaper.disabled = index <= 0;
  nodes.nextPaper.disabled = index === -1 || index >= state.filtered.length - 1;
}

function renderDetail() {
  const paper = state.filtered.find((item) => item.arxiv_id === state.selectedPaperId);
  if (!paper) {
    nodes.detailKicker.textContent = 'Selected Paper';
    nodes.paperDetail.className = 'paper-detail empty-state';
    nodes.paperDetail.innerHTML = '<p>选择一篇论文查看摘要、中文总结与关键词。</p>';
    updateDetailNav();
    return;
  }

  const index = selectedPaperIndex();
  const introItems = paper.intro_zh.length
    ? paper.intro_zh.map((item) => `<li>${escapeHtml(item)}</li>`).join('')
    : '<li>暂无 3 点简述。</li>';
  const tags = paper.tags_zh.length
    ? paper.tags_zh.map((tag) => `<span class="paper-tag">${escapeHtml(tag)}</span>`).join('')
    : '<span class="paper-tag empty">暂无关键词</span>';

  nodes.detailKicker.textContent = `Selected Paper · ${index + 1}/${state.filtered.length}`;
  nodes.paperDetail.className = 'paper-detail';
  nodes.paperDetail.innerHTML = `
    <div class="detail-meta-bar">
      <span class="detail-badge">${escapeHtml(paper.arxiv_id)}</span>
      <span class="detail-badge alt">${escapeHtml(compactAuthors(paper.authors))}</span>
    </div>
    <h3>${escapeHtml(paper.title)}</h3>
    <p class="detail-authors">${escapeHtml(paper.authors.join(', ') || 'Unknown authors')}</p>

    <div class="paper-links">
      <a class="paper-link" href="${escapeHtml(paper.abs_url)}" target="_blank" rel="noreferrer">Open arXiv Abstract</a>
      <a class="paper-link" href="${escapeHtml(paper.pdf_url)}" target="_blank" rel="noreferrer">Open PDF</a>
    </div>

    <div class="info-grid">
      <section class="info-card">
        <strong>中文一句话要点</strong>
        <p>${escapeHtml(paper.headline_zh || '暂无中文一句话要点')}</p>
      </section>
      <section class="info-card">
        <strong>关键词</strong>
        <div class="paper-tags">${tags}</div>
      </section>
    </div>

    <section class="detail-section">
      <h4>3 点简述</h4>
      <ol class="paper-intro">${introItems}</ol>
    </section>

    <section class="detail-section">
      <h4>原始摘要</h4>
      <p class="paper-summary">${escapeHtml(paper.summary || '暂无摘要')}</p>
    </section>
  `;

  updateDetailNav();
}

function renderHeader() {
  const entry = activeDateEntry();
  document.title = state.manifest.site.title;
  nodes.siteTitle.textContent = state.manifest.site.title;
  nodes.siteSubtitle.textContent = `面向你关注的 arXiv 标签做每日自动抓取与中文总结。当前归档 ${state.manifest.summary.total_dates} 天、${state.manifest.summary.total_papers} 篇论文，可按日期、关键词与全文摘要即时筛选。`;
  nodes.heroLatest.textContent = state.manifest.summary.latest_date;
  nodes.heroCount.textContent = `${state.manifest.summary.total_papers}`;
  nodes.heroActive.textContent = entry ? `${entry.date} · ${entry.paper_count}` : '-';
  nodes.generatedAt.textContent = `Generated ${state.manifest.generated_at}`;
}

function render() {
  renderHeader();
  renderDateSelect();
  renderRecentDates();
  renderActiveFilters();
  renderTags();
  renderList();
  renderDetail();
}

function navigateSelection(delta) {
  const index = selectedPaperIndex();
  if (index === -1) return;
  const target = state.filtered[index + delta];
  if (!target) return;
  state.selectedPaperId = target.arxiv_id;
  renderList();
  renderDetail();
  syncHistory();
  scrollActiveCardIntoView();
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
  } else {
    state.selectedPaperId = null;
  }

  ensureSelectedPaper(filteredPapers());
  render();
  syncHistory(replace);
  scrollActiveCardIntoView();
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
  render();
  syncHistory(true);
});

nodes.searchInput.addEventListener('keydown', (event) => {
  if (event.key === 'Escape') {
    state.query = '';
    nodes.searchInput.value = '';
    render();
    syncHistory(true);
  }
});

nodes.clearFilters.addEventListener('click', () => {
  state.query = '';
  state.activeTag = '';
  nodes.searchInput.value = '';
  render();
  syncHistory();
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

nodes.prevPaper.addEventListener('click', () => navigateSelection(-1));
nodes.nextPaper.addEventListener('click', () => navigateSelection(1));

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

document.addEventListener('keydown', (event) => {
  if (event.metaKey || event.ctrlKey || event.altKey) return;
  const activeTag = document.activeElement?.tagName;
  if (event.key === '/') {
    event.preventDefault();
    nodes.searchInput.focus();
    nodes.searchInput.select();
    return;
  }
  if (activeTag === 'INPUT' || activeTag === 'TEXTAREA' || activeTag === 'SELECT') {
    return;
  }
  if (event.key === 'j' || event.key === 'ArrowDown') {
    event.preventDefault();
    navigateSelection(1);
  }
  if (event.key === 'k' || event.key === 'ArrowUp') {
    event.preventDefault();
    navigateSelection(-1);
  }
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
