---
layout: default
title: Decentralized Federated Learning by Partial Message Exchange
---

# Decentralized Federated Learning by Partial Message Exchange
**arXiv**：[2603.01730v1](https://arxiv.org/abs/2603.01730) · [PDF](https://arxiv.org/pdf/2603.01730.pdf)  
**作者**：Shan Sha, Shenglong Zhou, Xin Wang, Lingchen Kong, Geoffrey Ye Li  

**一句话要点**：提出PaME算法以解决去中心化联邦学习中的通信成本与数据异构问题

**关键词**：去中心化联邦学习, 部分消息交换, 通信优化, 数据异构, 隐私保护, 线性收敛

## 3 点简述
- 核心问题：去中心化联邦学习面临数据异构、理论假设严格、通信或隐私技术应用时收敛性下降的挑战。
- 方法要点：通过随机选择稀疏坐标进行部分消息交换，降低通信成本并保持隐私，无需牺牲准确性。
- 实验或效果：在梯度局部Lipschitz连续和通信矩阵双随机假设下，算法线性收敛，数值实验显示优于现有方法。

## 摘要（原文）

> Decentralized federated learning (DFL) has emerged as a transformative server-free paradigm that enables collaborative learning over large-scale heterogeneous networks. However, it continues to face fundamental challenges, including data heterogeneity, restrictive assumptions for theoretical analysis, and degraded convergence when standard communication- or privacyenhancing techniques are applied. To overcome these drawbacks, this paper develops a novel algorithm, PaME (DFL by Partial Message Exchange). The central principle is to allow only randomly selected sparse coordinates to be exchanged between two neighbor nodes. Consequently, PaME achieves substantial reductions in communication costs while still preserving a high level of privacy, without sacrificing accuracy. Moreover, grounded in rigorous analysis, the algorithm is shown to converge at a linear rate under the gradient to be locally Lipschitz continuous and the communication matrix to be doubly stochastic. These two mild assumptions not only dispense with many restrictive conditions commonly imposed by existing DFL methods but also enables PaME to effectively address data heterogeneity. Furthermore, comprehensive numerical experiments demonstrate its superior performance compared with several representative decentralized learning algorithms.

