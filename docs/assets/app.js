const state = {
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
  const clean = String(text || '').replace(/\s+/g, ' ').trim();
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
