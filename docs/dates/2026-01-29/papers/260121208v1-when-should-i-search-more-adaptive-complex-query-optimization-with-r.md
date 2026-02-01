---
layout: default
title: When should I search more: Adaptive Complex Query Optimization with Reinforcement Learning
---

# When should I search more: Adaptive Complex Query Optimization with Reinforcement Learning
**arXiv**：[2601.21208v1](https://arxiv.org/abs/2601.21208) · [PDF](https://arxiv.org/pdf/2601.21208.pdf)  
**作者**：Wei Wen, Sihang Deng, Tianjun Wei, Keyu Chen, Ruizhi Qiao, Xing Sun  

**一句话要点**：提出自适应复杂查询优化框架，以强化学习解决RAG系统中多策略搜索的优化难题。

**关键词**：查询优化, 强化学习, 检索增强生成, 自适应分解, 结果融合, 课程学习

## 3 点简述
- 核心问题：复杂查询需多策略处理，直接应用强化学习导致搜索空间大、奖励设计难和训练不稳定。
- 方法要点：引入自适应查询重构模块动态决定分解时机，结合排序-分数融合模块稳定结果聚合与奖励信号。
- 实验或效果：在三个复杂查询基准上实现最优性能，计算效率高且兼容不同检索架构。

## 摘要（原文）

> Query optimization is a crucial component for the efficacy of Retrieval-Augmented Generation (RAG) systems. While reinforcement learning (RL)-based agentic and reasoning methods have recently emerged as a promising direction on query optimization, most existing approaches focus on the expansion and abstraction of a single query. However, complex user queries are prevalent in real-world scenarios, often requiring multiple parallel and sequential search strategies to handle disambiguation and decomposition. Directly applying RL to these complex cases introduces significant hurdles. Determining the optimal number of sub-queries and effectively re-ranking and merging retrieved documents vastly expands the search space and complicates reward design, frequently leading to training instability. To address these challenges, we propose a novel RL framework called Adaptive Complex Query Optimization (ACQO). Our framework is designed to adaptively determine when and how to expand the search process. It features two core components: an Adaptive Query Reformulation (AQR) module that dynamically decides when to decompose a query into multiple sub-queries, and a Rank-Score Fusion (RSF) module that ensures robust result aggregation and provides stable reward signals for the learning agent. To mitigate training instabilities, we adopt a Curriculum Reinforcement Learning (CRL) approach, which stabilizes the training process by progressively introducing more challenging queries through a two-stage strategy. Our comprehensive experiments demonstrate that ACQO achieves state-of-the-art performance on three complex query benchmarks, significantly outperforming established baselines. The framework also showcases improved computational efficiency and broad compatibility with different retrieval architectures, establishing it as a powerful and generalizable solution for next-generation RAG systems.

