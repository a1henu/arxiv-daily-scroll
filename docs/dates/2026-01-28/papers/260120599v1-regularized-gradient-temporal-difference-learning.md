---
layout: default
title: Regularized Gradient Temporal-Difference Learning
---

# Regularized Gradient Temporal-Difference Learning
**arXiv**：[2601.20599v1](https://arxiv.org/abs/2601.20599) · [PDF](https://arxiv.org/pdf/2601.20599.pdf)  
**作者**：Hyunjun Na, Donghwan Lee  

**一句话要点**：提出正则化GTD算法以解决特征交互矩阵奇异时的收敛问题

**关键词**：梯度时序差分学习, 正则化优化, 离策略策略评估, 函数逼近, 收敛分析

## 3 点简述
- 核心问题：传统GTD算法在特征交互矩阵奇异时可能不稳定或性能下降
- 方法要点：通过重构均方投影贝尔曼误差最小化，引入正则化优化目标
- 实验或效果：理论证明收敛性和误差界，并通过实验验证有效性

## 摘要（原文）

> Gradient temporal-difference (GTD) learning algorithms are widely used for off-policy policy evaluation with function approximation. However, existing convergence analyses rely on the restrictive assumption that the so-called feature interaction matrix (FIM) is nonsingular. In practice, the FIM can become singular and leads to instability or degraded performance. In this paper, we propose a regularized optimization objective by reformulating the mean-square projected Bellman error (MSPBE) minimization. This formulation naturally yields a regularized GTD algorithms, referred to as R-GTD, which guarantees convergence to a unique solution even when the FIM is singular. We establish theoretical convergence guarantees and explicit error bounds for the proposed method, and validate its effectiveness through empirical experiments.

