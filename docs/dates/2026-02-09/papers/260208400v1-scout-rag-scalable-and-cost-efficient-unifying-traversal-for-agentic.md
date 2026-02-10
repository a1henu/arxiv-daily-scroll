---
layout: default
title: SCOUT-RAG: Scalable and Cost-Efficient Unifying Traversal for Agentic Graph-RAG over Distributed Domains
---

# SCOUT-RAG: Scalable and Cost-Efficient Unifying Traversal for Agentic Graph-RAG over Distributed Domains
**arXiv**：[2602.08400v1](https://arxiv.org/abs/2602.08400) · [PDF](https://arxiv.org/pdf/2602.08400.pdf)  
**作者**：Longkun Li, Yuanben Zou, Jinghan Wu, Yuqing Wen, Jing Li, Hangwei Qian, Ivor Tsang  

**一句话要点**：提出SCOUT-RAG框架以解决分布式受限场景下Graph-RAG的检索效率与成本问题

**关键词**：分布式检索, 知识图谱增强, 代理协作, 成本优化, 多领域推理

## 3 点简述
- 核心问题：传统Graph-RAG依赖集中式知识图谱，在分布式受限环境中难以高效检索多领域知识
- 方法要点：采用渐进式跨域检索，通过四个协作代理估计相关性、控制扩展、调整深度并合成答案
- 实验或效果：在性能接近集中式基线的同时，显著减少跨域调用、处理令牌数和延迟

## 摘要（原文）

> Graph-RAG improves LLM reasoning using structured knowledge, yet conventional designs rely on a centralized knowledge graph. In distributed and access-restricted settings (e.g., hospitals or multinational organizations), retrieval must select relevant domains and appropriate traversal depth without global graph visibility or exhaustive querying. To address this challenge, we introduce \textbf{SCOUT-RAG} (\textit{\underline{S}calable and \underline{CO}st-efficient \underline{U}nifying \underline{T}raversal}), a distributed agentic Graph-RAG framework that performs progressive cross-domain retrieval guided by incremental utility goals. SCOUT-RAG employs four cooperative agents that: (i) estimate domain relevance, (ii) decide when to expand retrieval to additional domains, (iii) adapt traversal depth to avoid unnecessary graph exploration, and (iv) synthesize the high-quality answers. The framework is designed to minimize retrieval regret, defined as missing useful domain information, while controlling latency and API cost. Across multi-domain knowledge settings, SCOUT-RAG achieves performance comparable to centralized baselines, including DRIFT and exhaustive domain traversal, while substantially reducing cross-domain calls, total tokens processed, and latency.

