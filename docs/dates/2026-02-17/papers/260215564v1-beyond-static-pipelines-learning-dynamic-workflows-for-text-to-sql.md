---
layout: default
title: Beyond Static Pipelines: Learning Dynamic Workflows for Text-to-SQL
---

# Beyond Static Pipelines: Learning Dynamic Workflows for Text-to-SQL
**arXiv**：[2602.15564v1](https://arxiv.org/abs/2602.15564) · [PDF](https://arxiv.org/pdf/2602.15564.pdf)  
**作者**：Yihan Wang, Peiyu Liu, Runyu Chen, Wei Xu  

**一句话要点**：提出SquRL强化学习框架，通过动态工作流构建提升Text-to-SQL在复杂和分布外场景的性能

**关键词**：Text-to-SQL, 动态工作流, 强化学习, 分布外泛化, 自适应推理, 工作流优化

## 3 点简述
- 核心问题：静态工作流在真实场景中难以适应分布外和长尾查询，限制Text-to-SQL的可扩展性。
- 方法要点：基于强化学习设计SquRL框架，引入动态演员掩码和伪奖励机制，优化推理时自适应工作流构建。
- 实验或效果：在广泛基准测试中，动态策略持续优于最佳静态工作流，尤其在复杂和分布外查询上增益显著。

## 摘要（原文）

> Text-to-SQL has recently achieved impressive progress, yet remains difficult to apply effectively in real-world scenarios. This gap stems from the reliance on single static workflows, fundamentally limiting scalability to out-of-distribution and long-tail scenarios. Instead of requiring users to select suitable methods through extensive experimentation, we attempt to enable systems to adaptively construct workflows at inference time. Through theoretical and empirical analysis, we demonstrate that optimal dynamic policies consistently outperform the best static workflow, with performance gains fundamentally driven by heterogeneity across candidate workflows. Motivated by this, we propose SquRL, a reinforcement learning framework that enhances LLMs' reasoning capability in adaptive workflow construction. We design a rule-based reward function and introduce two effective training mechanisms: dynamic actor masking to encourage broader exploration, and pseudo rewards to improve training efficiency. Experiments on widely-used Text-to-SQL benchmarks demonstrate that dynamic workflow construction consistently outperforms the best static workflow methods, with especially pronounced gains on complex and out-of-distribution queries. The codes are available at https://github.com/Satissss/SquRL

