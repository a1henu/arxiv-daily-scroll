---
layout: default
title: Robust Distributed Learning under Resource Constraints: Decentralized Quantile Estimation via (Asynchronous) ADMM
---

# Robust Distributed Learning under Resource Constraints: Decentralized Quantile Estimation via (Asynchronous) ADMM
**arXiv**：[2601.20571v1](https://arxiv.org/abs/2601.20571) · [PDF](https://arxiv.org/pdf/2601.20571.pdf)  
**作者**：Anna van Elst, Igor Colin, Stephan Clémençon  

**一句话要点**：提出AsylADMM算法以解决资源受限边缘设备上的去中心化中位数和分位数估计问题

**关键词**：去中心化学习, 中位数估计, 分位数估计, 异步ADMM, 资源受限设备, 抗污染修剪

## 3 点简述
- 核心问题：去中心化学习需通信高效、抗数据污染且内存轻量，现有方法内存需求随节点度增长
- 方法要点：基于异步ADMM的gossip算法，每节点仅需两个变量，支持中位数和分位数估计
- 实验或效果：理论分析同步变体，异步算法快速收敛，分位数修剪优于现有基于秩的方法

## 摘要（原文）

> Specifications for decentralized learning on resource-constrained edge devices require algorithms that are communication-efficient, robust to data corruption, and lightweight in memory usage. While state-of-the-art gossip-based methods satisfy the first requirement, achieving robustness remains challenging. Asynchronous decentralized ADMM-based methods have been explored for estimating the median, a statistical centrality measure that is notoriously more robust than the mean. However, existing approaches require memory that scales with node degree, making them impractical when memory is limited. In this paper, we propose AsylADMM, a novel gossip algorithm for decentralized median and quantile estimation, primarily designed for asynchronous updates and requiring only two variables per node. We analyze a synchronous variant of AsylADMM to establish theoretical guarantees and empirically demonstrate fast convergence for the asynchronous algorithm. We then show that our algorithm enables quantile-based trimming, geometric median estimation, and depth-based trimming, with quantile-based trimming empirically outperforming existing rank-based methods. Finally, we provide a novel theoretical analysis of rank-based trimming via Markov chain theory.

