---
layout: default
title: DeepPlanning: Benchmarking Long-Horizon Agentic Planning with Verifiable Constraints
---

# DeepPlanning: Benchmarking Long-Horizon Agentic Planning with Verifiable Constraints
**arXiv**：[2601.18137v1](https://arxiv.org/abs/2601.18137) · [PDF](https://arxiv.org/pdf/2601.18137.pdf)  
**作者**：Yinger Zhang, Shutong Jiang, Renhao Li, Jianhong Tu, Yang Su, Lianghao Deng, Xudong Guo, Chenxu Lv, Junyang Lin  

**一句话要点**：提出DeepPlanning基准以评估长时域智能体规划能力，聚焦多日旅行与多产品购物任务。

**关键词**：长时域规划, 智能体基准, 约束优化, 主动信息获取, LLM评估, 多任务规划

## 3 点简述
- 核心问题：现有基准缺乏全局约束优化和主动信息获取，难以评估真实世界长时域规划。
- 方法要点：设计包含多日旅行和多产品购物的任务，要求主动信息采集、局部约束推理和全局优化。
- 实验或效果：前沿智能体LLM在DeepPlanning上表现不佳，突显显式推理模式和并行工具使用的重要性。

## 摘要（原文）

> While agent evaluation has shifted toward long-horizon tasks, most benchmarks still emphasize local, step-level reasoning rather than the global constrained optimization (e.g., time and financial budgets) that demands genuine planning ability. Meanwhile, existing LLM planning benchmarks underrepresent the active information gathering and fine-grained local constraints typical of real-world settings. To address this, we introduce DeepPlanning, a challenging benchmark for practical long-horizon agent planning. It features multi-day travel planning and multi-product shopping tasks that require proactive information acquisition, local constrained reasoning, and global constrained optimization. Evaluations on DeepPlanning show that even frontier agentic LLMs struggle with these problems, highlighting the importance of reliable explicit reasoning patterns and parallel tool use for achieving better effectiveness-efficiency trade-offs. Error analysis further points to promising directions for improving agentic LLMs over long planning horizons. We open-source the code and data to support future research.

