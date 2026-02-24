---
layout: default
title: Generalized Random Direction Newton Algorithms for Stochastic Optimization
---

# Generalized Random Direction Newton Algorithms for Stochastic Optimization
**arXiv**：[2602.19893v1](https://arxiv.org/abs/2602.19893) · [PDF](https://arxiv.org/pdf/2602.19893.pdf)  
**作者**：Soumen Pachal, Prashanth L. A., Shalabh Bhatnagar, Avinash Achar  

**一句话要点**：提出广义随机方向牛顿算法，利用噪声函数测量估计Hessian矩阵以优化随机优化问题。

**关键词**：随机优化, Hessian估计, 随机方向逼近, 牛顿算法, 收敛分析

## 3 点简述
- 核心问题：随机优化中仅基于噪声函数测量高效估计Hessian矩阵的挑战。
- 方法要点：通过随机方向逼近构建广义Hessian估计器，函数测量数影响估计偏差阶数。
- 实验或效果：理论分析收敛性，数值实验验证估计器性能与算法有效性。

## 摘要（原文）

> We present a family of generalized Hessian estimators of the objective using random direction stochastic approximation (RDSA) by utilizing only noisy function measurements. The form of each estimator and the order of the bias depend on the number of function measurements. In particular, we demonstrate that estimators with more function measurements exhibit lower-order estimation bias. We show the asymptotic unbiasedness of the estimators. We also perform asymptotic and non-asymptotic convergence analyses for stochastic Newton methods that incorporate our generalized Hessian estimators. Finally, we perform numerical experiments to validate our theoretical findings.

