const state = {
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
  return String(value).replace(/[&<>"']/g, (char) => ({
    '&': '&amp;',
    '<': '&lt;',
    '>': '&gt;',
    '"': '&quot;',
    "'": '&#39;',
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
