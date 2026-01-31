---
layout: default
title: Mean-Field Control on Sparse Graphs: From Local Limits to GNNs via Neighborhood Distributions
---

# Mean-Field Control on Sparse Graphs: From Local Limits to GNNs via Neighborhood Distributions
**arXiv**：[2601.21477v1](https://arxiv.org/abs/2601.21477) · [PDF](https://arxiv.org/pdf/2601.21477.pdf)  
**作者**：Tobias Schmidt, Kai Cui  

**一句话要点**：提出基于稀疏图的平均场控制框架，通过邻域分布实现可扩展强化学习。

**关键词**：平均场控制, 稀疏图, 邻域分布, 图神经网络, 强化学习, 动态规划原理

## 3 点简述
- 核心问题：传统平均场控制依赖密集交互，难以应用于现实稀疏网络结构。
- 方法要点：重新定义系统状态为装饰根邻域的概率测度，证明有限时域下的局部性原理。
- 实验或效果：理论支持图神经网络在演员-评论家算法中的应用，并在稀疏拓扑上实现高效控制。

## 摘要（原文）

> Mean-field control (MFC) offers a scalable solution to the curse of dimensionality in multi-agent systems but traditionally hinges on the restrictive assumption of exchangeability via dense, all-to-all interactions. In this work, we bridge the gap to real-world network structures by proposing a rigorous framework for MFC on large sparse graphs. We redefine the system state as a probability measure over decorated rooted neighborhoods, effectively capturing local heterogeneity. Our central contribution is a theoretical foundation for scalable reinforcement learning in this setting. We prove horizon-dependent locality: for finite-horizon problems, an agent's optimal policy at time t depends strictly on its (T-t)-hop neighborhood. This result renders the infinite-dimensional control problem tractable and underpins a novel Dynamic Programming Principle (DPP) on the lifted space of neighborhood distributions. Furthermore, we formally and experimentally justify the use of Graph Neural Networks (GNNs) for actor-critic algorithms in this context. Our framework naturally recovers classical MFC as a degenerate case while enabling efficient, theoretically grounded control on complex sparse topologies.

