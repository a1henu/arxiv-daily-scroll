---
layout: default
title: Analytical Search
---

# Analytical Search
**arXiv**：[2602.11581v1](https://arxiv.org/abs/2602.11581) · [PDF](https://arxiv.org/pdf/2602.11581.pdf)  
**作者**：Yiteng Tu, Shuo Miao, Weihang Su, Yiqun Liu, Qingyao Ai  

**一句话要点**：提出分析搜索范式以支持跨领域分析性信息需求

**关键词**：分析搜索, 信息检索, 证据融合, 可验证推理, 端到端工作流

## 3 点简述
- 现有检索范式难以满足分析性查询的端到端需求，如趋势分析和因果影响评估
- 分析搜索将搜索重构为证据驱动、过程导向的工作流，包括意图建模、证据融合和可验证推理
- 未知实验或效果，但讨论了构建分析搜索引擎的潜在研究方向

## 摘要（原文）

> Analytical information needs, such as trend analysis and causal impact assessment, are prevalent across various domains including law, finance, science, and much more. However, existing information retrieval paradigms, whether based on relevance-oriented document ranking or retrieval-augmented generation (RAG) with large language models (LLMs), often struggle to meet the end-to-end requirements of such tasks at the corpus scale. They either emphasize information finding rather than end-to-end problem solving, or simply treat everything as naive question answering, offering limited control over reasoning, evidence usage, and verifiability. As a result, they struggle to support analytical queries that have diverse utility concepts and high accountability requirements.
>   In this paper, we propose analytical search as a distinct and emerging search paradigm designed to fulfill these analytical information needs. Analytical search reframes search as an evidence-governed, process-oriented analytical workflow that explicitly models analytical intent, retrieves evidence for fusion, and produces verifiable conclusions through structured, multi-step inference. We position analytical search in contrast to existing paradigms, and present a unified system framework that integrates query understanding, recall-oriented retrieval, reasoning-aware fusion, and adaptive verification. We also discuss potential research directions for the construction of analytical search engines. In this way, we highlight the conceptual significance and practical importance of analytical search and call on efforts toward the next generation of search engines that support analytical information needs.

