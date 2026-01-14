---
layout: default
title: One-Shot Federated Ridge Regression: Exact Recovery via Sufficient Statistic Aggregation
---

# One-Shot Federated Ridge Regression: Exact Recovery via Sufficient Statistic Aggregation
**arXiv**：[2601.08216v1](https://arxiv.org/abs/2601.08216) · [PDF](https://arxiv.org/pdf/2601.08216.pdf)  
**作者**：Zahir Alsulaimawi  

**一句话要点**：提出一次性联邦岭回归，通过充分统计聚合实现精确恢复，减少通信开销。

**关键词**：联邦学习, 岭回归, 充分统计, 通信效率, 差分隐私, 随机投影

## 3 点简述
- 核心问题：分布式线性回归是否必须迭代通信？本文证明无需迭代。
- 方法要点：客户端计算本地充分统计（Gram矩阵和矩向量），服务器单次矩阵求逆重构全局解。
- 实验或效果：在合成异构回归实验中，一次性融合匹配FedAvg精度，通信减少达38倍。

## 摘要（原文）

> Federated learning protocols require repeated synchronization between clients and a central server, with convergence rates depending on learning rates, data heterogeneity, and client sampling. This paper asks whether iterative communication is necessary for distributed linear regression. We show it is not. We formulate federated ridge regression as a distributed equilibrium problem where each client computes local sufficient statistics -- the Gram matrix and moment vector -- and transmits them once. The server reconstructs the global solution through a single matrix inversion. We prove exact recovery: under a coverage condition on client feature matrices, one-shot aggregation yields the centralized ridge solution, not an approximation. For heterogeneous distributions violating coverage, we derive non-asymptotic error bounds depending on spectral properties of the aggregated Gram matrix. Communication reduces from $\mathcal{O}(Rd)$ in iterative methods to $\mathcal{O}(d^2)$ total; for high-dimensional settings, we propose and experimentally validate random projection techniques reducing this to $\mathcal{O}(m^2)$ where $m \ll d$. We establish differential privacy guarantees where noise is injected once per client, eliminating the composition penalty that degrades privacy in multi-round protocols. We further address practical considerations including client dropout robustness, federated cross-validation for hyperparameter selection, and comparison with gradient-based alternatives. Comprehensive experiments on synthetic heterogeneous regression demonstrate that one-shot fusion matches FedAvg accuracy while requiring up to $38\times$ less communication. The framework applies to kernel methods and random feature models but not to general nonlinear architectures.

