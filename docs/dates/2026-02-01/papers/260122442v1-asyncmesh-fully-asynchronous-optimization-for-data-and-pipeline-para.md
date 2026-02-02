---
layout: default
title: AsyncMesh: Fully Asynchronous Optimization for Data and Pipeline Parallelism
---

# AsyncMesh: Fully Asynchronous Optimization for Data and Pipeline Parallelism
**arXiv**：[2601.22442v1](https://arxiv.org/abs/2601.22442) · [PDF](https://arxiv.org/pdf/2601.22442.pdf)  
**作者**：Thalaiyasingam Ajanthan, Sameera Ramasinghe, Gil Avraham, Hadi Mohaghegh Dolatabadi, Chamin P Hewa Koneputugodage, Violetta Shevchenko, Yan Zuo, Alexander Long  

**一句话要点**：提出异步优化方法AsyncMesh，以解决数据并行和流水线并行中的通信瓶颈问题。

**关键词**：异步优化, 数据并行, 流水线并行, 分布式训练, 通信效率, 收敛保证

## 3 点简述
- 核心问题：数据并行和流水线并行的高通信成本限制了分布式训练的可扩展性。
- 方法要点：引入跨并行轴的异步更新，采用权重前瞻和异步稀疏平均来缓解陈旧性。
- 实验或效果：在大型语言模型上匹配同步基线性能，显著降低通信开销。

## 摘要（原文）

> Data and pipeline parallelism are key strategies for scaling neural network training across distributed devices, but their high communication cost necessitates co-located computing clusters with fast interconnects, limiting their scalability. We address this communication bottleneck by introducing asynchronous updates across both parallelism axes, relaxing the co-location requirement at the expense of introducing staleness between pipeline stages and data parallel replicas. To mitigate staleness, for pipeline parallelism, we adopt a weight look-ahead approach, and for data parallelism, we introduce an asynchronous sparse averaging method equipped with an exponential moving average based correction mechanism. We provide convergence guarantees for both sparse averaging and asynchronous updates. Experiments on large-scale language models (up to \em 1B parameters) demonstrate that our approach matches the performance of the fully synchronous baseline, while significantly reducing communication overhead.

