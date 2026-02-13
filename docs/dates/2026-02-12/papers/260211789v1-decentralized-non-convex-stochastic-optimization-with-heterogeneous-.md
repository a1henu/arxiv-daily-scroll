---
layout: default
title: Decentralized Non-convex Stochastic Optimization with Heterogeneous Variance
---

# Decentralized Non-convex Stochastic Optimization with Heterogeneous Variance
**arXiv**：[2602.11789v1](https://arxiv.org/abs/2602.11789) · [PDF](https://arxiv.org/pdf/2602.11789.pdf)  
**作者**：Hongxu Chen, Ke Wei, Luo Luo  

**一句话要点**：提出D-NSS算法以解决分布式网络中节点方差异构的非凸随机优化问题

**关键词**：分布式优化, 非凸随机优化, 方差异构, 样本复杂度, 节点特定采样, 方差缩减

## 3 点简述
- 核心问题：分布式优化中节点随机梯度方差异构对算法设计和复杂度的影响未知
- 方法要点：设计节点特定采样的D-NSS算法，样本复杂度依赖局部标准差算术均值，优于现有方法
- 实验或效果：数值实验验证理论结果，并扩展D-NSS-VR算法在均方光滑假设下改进复杂度

## 摘要（原文）

> Decentralized optimization is critical for solving large-scale machine learning problems over distributed networks, where multiple nodes collaborate through local communication. In practice, the variances of stochastic gradient estimators often differ across nodes, yet their impact on algorithm design and complexity remains unclear. To address this issue, we propose D-NSS, a decentralized algorithm with node-specific sampling, and establish its sample complexity depending on the arithmetic mean of local standard deviations, achieving tighter bounds than existing methods that rely on the worst-case or quadratic mean. We further derive a matching sample complexity lower bound under heterogeneous variance, thereby proving the optimality of this dependence. Moreover, we extend the framework with a variance reduction technique and develop D-NSS-VR, which under the mean-squared smoothness assumption attains an improved sample complexity bound while preserving the arithmetic-mean dependence. Finally, numerical experiments validate the theoretical results and demonstrate the effectiveness of the proposed algorithms.

