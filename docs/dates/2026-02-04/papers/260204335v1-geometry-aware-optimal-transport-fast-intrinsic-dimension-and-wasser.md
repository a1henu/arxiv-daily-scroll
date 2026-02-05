---
layout: default
title: Geometry-Aware Optimal Transport: Fast Intrinsic Dimension and Wasserstein Distance Estimation
---

# Geometry-Aware Optimal Transport: Fast Intrinsic Dimension and Wasserstein Distance Estimation
**arXiv**：[2602.04335v1](https://arxiv.org/abs/2602.04335) · [PDF](https://arxiv.org/pdf/2602.04335.pdf)  
**作者**：Ferdinand Genans, Olivier Wintenberger  

**一句话要点**：提出几何感知最优传输框架，以解决大规模最优传输中的采样误差瓶颈问题。

**关键词**：最优传输, 内在维度估计, Wasserstein距离, 采样误差, 几何感知, 计算效率

## 3 点简述
- 核心问题：大规模最优传输中采样误差的收敛率受数据内在维度影响，成为计算瓶颈。
- 方法要点：引入无需最优传输求解器的采样误差估计器，并从中推导快速内在维度估计器。
- 实验或效果：数值实验表明该框架能有效缓解离散化误差，保持计算效率，并改进Wasserstein距离估计。

## 摘要（原文）

> Solving large scale Optimal Transport (OT) in machine learning typically relies on sampling measures to obtain a tractable discrete problem. While the discrete solver's accuracy is controllable, the rate of convergence of the discretization error is governed by the intrinsic dimension of our data. Therefore, the true bottleneck is the knowledge and control of the sampling error. In this work, we tackle this issue by introducing novel estimators for both sampling error and intrinsic dimension. The key finding is a simple, tuning-free estimator of $\text{OT}_c(ρ, \hatρ)$ that utilizes the semi-dual OT functional and, remarkably, requires no OT solver. Furthermore, we derive a fast intrinsic dimension estimator from the multi-scale decay of our sampling error estimator. This framework unlocks significant computational and statistical advantages in practice, enabling us to (i) quantify the convergence rate of the discretization error, (ii) calibrate the entropic regularization of Sinkhorn divergences to the data's intrinsic geometry, and (iii) introduce a novel, intrinsic-dimension-based Richardson extrapolation estimator that strongly debiases Wasserstein distance estimation. Numerical experiments demonstrate that our geometry-aware pipeline effectively mitigates the discretization error bottleneck while maintaining computational efficiency.

