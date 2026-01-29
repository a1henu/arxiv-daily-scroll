---
layout: default
title: SA-PEF: Step-Ahead Partial Error Feedback for Efficient Federated Learning
---

# SA-PEF: Step-Ahead Partial Error Feedback for Efficient Federated Learning
**arXiv**：[2601.20738v1](https://arxiv.org/abs/2601.20738) · [PDF](https://arxiv.org/pdf/2601.20738.pdf)  
**作者**：Dawit Kiros Redie, Reza Arablouei, Stefan Werner  

**一句话要点**：提出步进部分误差反馈以提升非IID数据下联邦学习的通信效率与收敛速度

**关键词**：联邦学习, 梯度压缩, 误差反馈, 非凸优化, 非IID数据, 收敛分析

## 3 点简述
- 核心问题：非IID数据下，带误差反馈的梯度压缩可能导致早期训练停滞
- 方法要点：结合步进校正与部分误差反馈，理论分析保证收敛并加速早期阶段
- 实验或效果：在多种架构和数据集上，比标准误差反馈更快达到目标精度

## 摘要（原文）

> Biased gradient compression with error feedback (EF) reduces communication in federated learning (FL), but under non-IID data, the residual error can decay slowly, causing gradient mismatch and stalled progress in the early rounds. We propose step-ahead partial error feedback (SA-PEF), which integrates step-ahead (SA) correction with partial error feedback (PEF). SA-PEF recovers EF when the step-ahead coefficient $α=0$ and step-ahead EF (SAEF) when $α=1$. For non-convex objectives and $δ$-contractive compressors, we establish a second-moment bound and a residual recursion that guarantee convergence to stationarity under heterogeneous data and partial client participation. The resulting rates match standard non-convex Fed-SGD guarantees up to constant factors, achieving $O((η,η_0TR)^{-1})$ convergence to a variance/heterogeneity floor with a fixed inner step size. Our analysis reveals a step-ahead-controlled residual contraction $ρ_r$ that explains the observed acceleration in the early training phase. To balance SAEF's rapid warm-up with EF's long-term stability, we select $α$ near its theory-predicted optimum. Experiments across diverse architectures and datasets show that SA-PEF consistently reaches target accuracy faster than EF.

