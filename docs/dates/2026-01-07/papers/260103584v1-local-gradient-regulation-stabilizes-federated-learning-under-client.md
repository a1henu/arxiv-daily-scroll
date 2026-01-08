---
layout: default
title: Local Gradient Regulation Stabilizes Federated Learning under Client Heterogeneity
---

# Local Gradient Regulation Stabilizes Federated Learning under Client Heterogeneity
**arXiv**：[2601.03584v1](https://arxiv.org/abs/2601.03584) · [PDF](https://arxiv.org/pdf/2601.03584.pdf)  
**作者**：Ping Luo, Jiahuan Wang, Ziqing Wen, Tao Sun, Dongsheng Li  

**一句话要点**：提出局部梯度调控方法以解决联邦学习在客户端异构性下的稳定性问题

**关键词**：联邦学习, 客户端异构性, 梯度调控, 稳定性优化, 医学影像分析

## 3 点简述
- 核心问题：客户端异构性导致局部梯度动态失真，引发系统性漂移，阻碍全局收敛
- 方法要点：基于客户端视角调控局部梯度贡献，通过ECGR平衡对齐与未对齐梯度分量
- 实验或效果：理论分析和广泛实验验证，在LC25000医学影像数据集上稳定多种先进方法

## 摘要（原文）

> Federated learning (FL) enables collaborative model training across distributed clients without sharing raw data, yet its stability is fundamentally challenged by statistical heterogeneity in realistic deployments. Here, we show that client heterogeneity destabilizes FL primarily by distorting local gradient dynamics during client-side optimization, causing systematic drift that accumulates across communication rounds and impedes global convergence. This observation highlights local gradients as a key regulatory lever for stabilizing heterogeneous FL systems. Building on this insight, we develop a general client-side perspective that regulates local gradient contributions without incurring additional communication overhead. Inspired by swarm intelligence, we instantiate this perspective through Exploratory--Convergent Gradient Re-aggregation (ECGR), which balances well-aligned and misaligned gradient components to preserve informative updates while suppressing destabilizing effects. Theoretical analysis and extensive experiments, including evaluations on the LC25000 medical imaging dataset, demonstrate that regulating local gradient dynamics consistently stabilizes federated learning across state-of-the-art methods under heterogeneous data distributions.

