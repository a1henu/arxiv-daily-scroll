---
layout: default
title: HotelQuEST: Balancing Quality and Efficiency in Agentic Search
---

# HotelQuEST: Balancing Quality and Efficiency in Agentic Search
**arXiv**：[2602.23949v1](https://arxiv.org/abs/2602.23949) · [PDF](https://arxiv.org/pdf/2602.23949.pdf)  
**作者**：Guy Hadad, Shadi Iskander, Oren Kalinsky, Sofia Tolmach, Ran Levy, Haggai Roitman  

**一句话要点**：提出HotelQuEST基准以平衡代理搜索的质量与效率，并评估未明确偏好查询。

**关键词**：代理搜索, 基准评估, 效率优化, 未明确偏好, 酒店查询, LLM代理

## 3 点简述
- 核心问题：现有代理搜索基准忽视效率，且未充分处理用户查询中的未明确偏好，影响实际部署。
- 方法要点：构建包含214个酒店搜索查询的基准，涵盖从简单到复杂的难度范围，并收集澄清以显式化偏好用于评估。
- 实验或效果：发现基于LLM的代理比传统检索器准确率更高，但成本显著增加，暴露冗余工具调用和路由不优等低效问题。

## 摘要（原文）

> Agentic search has emerged as a promising paradigm for adaptive retrieval systems powered by large language models (LLMs). However, existing benchmarks primarily focus on quality, overlooking efficiency factors that are critical for real-world deployment. Moreover, real-world user queries often contain underspecified preferences, a challenge that remains largely underexplored in current agentic search evaluation. As a result, many agentic search systems remain impractical despite their impressive performance. In this work, we introduce HotelQuEST, a benchmark comprising 214 hotel search queries that range from simple factual requests to complex queries, enabling evaluation across the full spectrum of query difficulty. We further address the challenge of evaluating underspecified user preferences by collecting clarifications that make annotators' implicit preferences explicit for evaluation. We find that LLM-based agents achieve higher accuracy than traditional retrievers, but at substantially higher costs due to redundant tool calls and suboptimal routing that fails to match query complexity to model capability. Our analysis exposes inefficiencies in current agentic search systems and demonstrates substantial potential for cost-aware optimization.

