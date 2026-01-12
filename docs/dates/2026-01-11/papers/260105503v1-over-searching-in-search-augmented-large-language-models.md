---
layout: default
title: Over-Searching in Search-Augmented Large Language Models
---

# Over-Searching in Search-Augmented Large Language Models
**arXiv**：[2601.05503v1](https://arxiv.org/abs/2601.05503) · [PDF](https://arxiv.org/pdf/2601.05503.pdf)  
**作者**：Roy Xie, Deepak Gopinath, David Qiu, Dong Lin, Haitian Sun, Saloni Potdar, Bhuwan Dhingra  

**一句话要点**：提出Tokens Per Correctness指标以量化搜索增强大语言模型中的过度搜索问题

**关键词**：搜索增强大语言模型, 过度搜索, 检索效率, 幻觉问题, 多轮对话, 性能评估

## 3 点简述
- 核心问题：搜索增强大语言模型存在过度搜索，导致计算低效和幻觉。
- 方法要点：系统评估过度搜索的多维度影响，并引入TPC指标衡量性能-成本权衡。
- 实验或效果：发现检索证据组成对弃权率有影响，并探索查询和检索层面的缓解方法。

## 摘要（原文）

> Search-augmented large language models (LLMs) excel at knowledge-intensive tasks by integrating external retrieval. However, they often over-search -- unnecessarily invoking search tool even when it does not improve response quality, which leads to computational inefficiency and hallucinations by incorporating irrelevant context. In this work, we conduct a systematic evaluation of over-searching across multiple dimensions, including query types, model categories, retrieval conditions, and multi-turn conversations. Our finding shows: (i) search generally improves answer accuracy on answerable queries but harms abstention on unanswerable ones; (ii) over-searching is more pronounced in complex reasoning models and deep research systems, is exacerbated by noisy retrieval, and compounds across turns in multi-turn conversations; and (iii) the composition of retrieved evidence is crucial, as the presence of negative evidence improves abstention. To quantify over-searching, we introduce Tokens Per Correctness (TPC), an evaluation metric that captures the performance-cost trade-off for search-augmented LLMs. Lastly, we investigate mitigation approaches at both the query and retrieval levels and release the OverSearchQA to foster continued research into efficient search-augmented LLMs.

