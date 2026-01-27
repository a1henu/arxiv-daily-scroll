---
layout: default
title: FastInsight: Fast and Insightful Retrieval via Fusion Operators for Graph RAG
---

# FastInsight: Fast and Insightful Retrieval via Fusion Operators for Graph RAG
**arXiv**：[2601.18579v1](https://arxiv.org/abs/2601.18579) · [PDF](https://arxiv.org/pdf/2601.18579.pdf)  
**作者**：Seonho An, Chaejeong Hyun, Min-Soo Kim  

**一句话要点**：提出FastInsight融合算子以解决图RAG中检索效率与洞察力不足的问题

**关键词**：图检索增强生成, 融合算子, 检索效率, 语义拓扑融合, 帕累托改进

## 3 点简述
- 现有图RAG方法依赖LLM推理，导致时间密集型检索过程，效率低下
- FastInsight通过图检索分类法识别拓扑盲与语义盲，引入GRanker和STeX融合算子
- 实验表明在广泛数据集上显著提升检索准确性和生成质量，实现效果与效率的帕累托改进

## 摘要（原文）

> Existing Graph RAG methods aiming for insightful retrieval on corpus graphs typically rely on time-intensive processes that interleave Large Language Model (LLM) reasoning. To enable time-efficient insightful retrieval, we propose FastInsight. We first introduce a graph retrieval taxonomy that categorizes existing methods into three fundamental operations: vector search, graph search, and model-based search. Through this taxonomy, we identify two critical limitations in current approaches: the topology-blindness of model-based search and the semantics-blindness of graph search. FastInsight overcomes these limitations by interleaving two novel fusion operators: the Graph-based Reranker (GRanker), which functions as a graph model-based search, and Semantic-Topological eXpansion (STeX), which operates as a vector-graph search. Extensive experiments on broad retrieval and generation datasets demonstrate that FastInsight significantly improves both retrieval accuracy and generation quality compared to state-of-the-art baselines, achieving a substantial Pareto improvement in the trade-off between effectiveness and efficiency.

