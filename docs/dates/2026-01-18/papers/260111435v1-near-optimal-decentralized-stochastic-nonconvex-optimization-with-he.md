---
layout: default
title: Near-Optimal Decentralized Stochastic Nonconvex Optimization with Heavy-Tailed Noise
---

# Near-Optimal Decentralized Stochastic Nonconvex Optimization with Heavy-Tailed Noise
**arXiv**：[2601.11435v1](https://arxiv.org/abs/2601.11435) · [PDF](https://arxiv.org/pdf/2601.11435.pdf)  
**作者**：Menglian Wang, Zhuanghua Liu, Luo Luo  

**一句话要点**：提出去中心化归一化随机梯度下降与Pull-Diag梯度跟踪方法，以解决重尾噪声下的非凸优化问题。

**关键词**：去中心化优化, 重尾噪声, 非凸优化, 梯度跟踪, 样本复杂度, 通信复杂度

## 3 点简述
- 研究去中心化随机非凸优化问题，关注重尾梯度噪声，常见于实际应用。
- 提出新方法，实现最优样本复杂度和近最优通信复杂度，达到近似平稳点。
- 扩展至无向网络设置，获得紧上界复杂度，并通过实验验证方法实用性。

## 摘要（原文）

> This paper studies decentralized stochastic nonconvex optimization problem over row-stochastic networks. We consider the heavy-tailed gradient noise which is empirically observed in many popular real-world applications. Specifically, we propose a decentralized normalized stochastic gradient descent with Pull-Diag gradient tracking, which achieves approximate stationary points with the optimal sample complexity and the near-optimal communication complexity. We further follow our framework to study the setting of undirected networks, also achieving the nearly tight upper complexity bounds. Moreover, we conduct empirical studies to show the practical superiority of the proposed methods.

