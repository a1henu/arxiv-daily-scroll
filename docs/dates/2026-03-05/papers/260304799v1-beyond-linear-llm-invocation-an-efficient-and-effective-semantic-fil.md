---
layout: default
title: Beyond Linear LLM Invocation: An Efficient and Effective Semantic Filter Paradigm
---

# Beyond Linear LLM Invocation: An Efficient and Effective Semantic Filter Paradigm
**arXiv**：[2603.04799v1](https://arxiv.org/abs/2603.04799) · [PDF](https://arxiv.org/pdf/2603.04799.pdf)  
**作者**：Nan Hou, Kangfei Zhao, Jiadong Xie, Jeffrey Xu Yu  

**一句话要点**：提出CSV框架以解决大语言模型语义过滤中的线性调用效率问题

**关键词**：语义过滤, 大语言模型优化, 聚类采样, 投票策略, 亚线性复杂度, 查询处理

## 3 点简述
- 核心问题：语义过滤操作需逐元组调用LLM，导致线性扫描的高延迟和令牌成本
- 方法要点：基于聚类-采样-投票（CSV）框架，通过嵌入聚类、采样评估和投票策略实现亚线性复杂度
- 实验或效果：在真实数据集上，CSV将LLM调用减少1.28-355倍，同时保持准确率和F1分数

## 摘要（原文）

> Large language models (LLMs) are increasingly used for semantic query processing over large corpora. A set of semantic operators derived from relational algebra has been proposed to provide a unified interface for expressing such queries, among which the semantic filter operator serves as a cornerstone. Given a table T with a natural language predicate e, for each tuple in the relation, the execution of a semantic filter proceeds by constructing an input prompt that combines the predicate e with its content, querying the LLM, and obtaining the binary decision. However, this tuple-by-tuple evaluation necessitates a complete linear scan of the table, incurring prohibitive latency and token costs. Although recent work has attempted to optimize semantic filtering, it still does not break the linear LLM invocation barriers. To address this, we propose Clustering-Sampling-Voting (CSV), a new framework that reduces LLM invocations to sublinear complexity while providing error guarantees. CSV embeds tuples into semantic clusters, samples a small subset for LLM evaluation, and infers cluster-level labels via two proposed voting strategies: UniVote, which aggregates labels uniformly, and SimVote, which weights votes by semantic similarity. Moreover, CSV triggers re-clustering on ambiguous clusters to ensure robustness across diverse datasets. The results conducted on real-world datasets demonstrate that CSV reduces the number of LLM calls by 1.28-355x compared to the state-of-the-art approaches, while maintaining comparable effectiveness in terms of Accuracy and F1 score.

