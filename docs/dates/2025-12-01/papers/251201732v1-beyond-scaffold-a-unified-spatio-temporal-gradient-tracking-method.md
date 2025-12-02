---
layout: default
title: Beyond Scaffold: A Unified Spatio-Temporal Gradient Tracking Method
---

# Beyond Scaffold: A Unified Spatio-Temporal Gradient Tracking Method
**arXiv**：[2512.01732v1](https://arxiv.org/abs/2512.01732) · [PDF](https://arxiv.org/pdf/2512.01732.pdf)  
**作者**：Yan Huang, Jinming Xu, Jiming Chen, Karl Henrik Johansson  

**一句话要点**：提出统一时空梯度跟踪算法ST-GT，以解决分布式随机优化中数据异构和噪声导致的模型漂移问题。

**关键词**：分布式学习, 梯度跟踪, 数据异构, 通信效率, 随机优化, 时变图

## 3 点简述
- 核心问题：分布式学习中多轮本地更新导致模型漂移，源于数据异构和本地梯度噪声。
- 方法要点：通过邻居节点跟踪全局梯度缓解异构，本地梯度平均抑制噪声，支持时变图。
- 实验或效果：理论证明强凸问题线性收敛，非凸次线性收敛，通信复杂度首次实现线性加速。

## 摘要（原文）

> In distributed and federated learning algorithms, communication overhead is often reduced by performing multiple local updates between communication rounds. However, due to data heterogeneity across nodes and the local gradient noise within each node, this strategy can lead to the drift of local models away from the global optimum. To address this issue, we revisit the well-known federated learning method Scaffold (Karimireddy et al., 2020) under a gradient tracking perspective, and propose a unified spatio-temporal gradient tracking algorithm, termed ST-GT, for distributed stochastic optimization over time-varying graphs. ST-GT tracks the global gradient across neighboring nodes to mitigate data heterogeneity, while maintaining a running average of local gradients to substantially suppress noise, with slightly more storage overhead. Without assuming bounded data heterogeneity, we prove that ST-GT attains a linear convergence rate for strongly convex problems and a sublinear rate for nonconvex cases. Notably, ST-GT achieves the first linear speed-up in communication complexity with respect to the number of local updates per round $τ$ for the strongly-convex setting. Compared to traditional gradient tracking methods, ST-GT reduces the topology-dependent noise term from $σ^2$ to $σ^2/τ$, where $σ^2$ denotes the noise level, thereby improving communication efficiency.

