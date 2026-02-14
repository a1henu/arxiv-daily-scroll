---
layout: default
title: Decentralized Non-convex Stochastic Optimization with Heterogeneous Variance
---

# Decentralized Non-convex Stochastic Optimization with Heterogeneous Variance
**arXiv**：[2602.11789v1](https://arxiv.org/abs/2602.11789) · [PDF](https://arxiv.org/pdf/2602.11789.pdf)  
**作者**：Hongxu Chen, Ke Wei, Luo Luo  

**一句话要点**：提出D-NSS算法以解决去中心化非凸随机优化中的异质方差问题

**关键词**：去中心化优化, 非凸随机优化, 异质方差, 样本复杂度, 方差缩减

## 3 点简述
- 研究去中心化优化中节点间随机梯度方差差异的影响
- 提出节点特定采样算法，样本复杂度依赖局部标准差算术均值
- 数值实验验证了理论结果和算法有效性

## 摘要（原文）

> Decentralized optimization is critical for solving large-scale machine learning problems over distributed networks, where multiple nodes collaborate through local communication. In practice, the variances of stochastic gradient estimators often differ across nodes, yet their impact on algorithm design and complexity remains unclear. To address this issue, we propose D-NSS, a decentralized algorithm with node-specific sampling, and establish its sample complexity depending on the arithmetic mean of local standard deviations, achieving tighter bounds than existing methods that rely on the worst-case or quadratic mean. We further derive a matching sample complexity lower bound under heterogeneous variance, thereby proving the optimality of this dependence. Moreover, we extend the framework with a variance reduction technique and develop D-NSS-VR, which under the mean-squared smoothness assumption attains an improved sample complexity bound while preserving the arithmetic-mean dependence. Finally, numerical experiments validate the theoretical results and demonstrate the effectiveness of the proposed algorithms.

