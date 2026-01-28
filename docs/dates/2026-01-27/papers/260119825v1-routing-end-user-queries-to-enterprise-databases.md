---
layout: default
title: Routing End User Queries to Enterprise Databases
---

# Routing End User Queries to Enterprise Databases
**arXiv**：[2601.19825v1](https://arxiv.org/abs/2601.19825) · [PDF](https://arxiv.org/pdf/2601.19825.pdf)  
**作者**：Saikrishna Sudarshan, Tanay Kulkarni, Manasi Patwardhan, Lovekesh Vig, Ashwin Srinivasan, Tanmay Tulsidas Verlekar  

**一句话要点**：提出模块化推理重排序策略，以解决多数据库企业环境中自然语言查询的路由问题。

**关键词**：自然语言查询路由, 多数据库环境, 推理重排序, NL-to-SQL, 企业数据库, 语义对齐

## 3 点简述
- 核心问题：多数据库企业环境中，自然语言查询路由因数据库规模大、领域重叠和查询模糊而具挑战性。
- 方法要点：通过显式建模模式覆盖、结构连接性和细粒度语义对齐，设计推理驱动的重排序策略。
- 实验或效果：在扩展的NL-to-SQL基准上，该方法在各项指标上均优于嵌入和直接LLM提示基线。

## 摘要（原文）

> We address the task of routing natural language queries in multi-database enterprise environments. We construct realistic benchmarks by extending existing NL-to-SQL datasets. Our study shows that routing becomes increasingly challenging with larger, domain-overlapping DB repositories and ambiguous queries, motivating the need for more structured and robust reasoning-based solutions. By explicitly modelling schema coverage, structural connectivity, and fine-grained semantic alignment, the proposed modular, reasoning-driven reranking strategy consistently outperforms embedding-only and direct LLM-prompting baselines across all the metrics.

