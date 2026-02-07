---
layout: default
title: Finite-Particle Rates for Regularized Stein Variational Gradient Descent
---

# Finite-Particle Rates for Regularized Stein Variational Gradient Descent
**arXiv**：[2602.05172v1](https://arxiv.org/abs/2602.05172) · [PDF](https://arxiv.org/pdf/2602.05172.pdf)  
**作者**：Ye He, Krishnakumar Balasubramanian, Sayan Banerjee, Promit Ghosal  

**一句话要点**：提出正则化Stein变分梯度下降以解决有限粒子收敛率问题

**关键词**：Stein变分梯度下降, 正则化方法, 有限粒子收敛率, Wasserstein梯度流, 非渐近分析, 交互粒子系统

## 3 点简述
- 核心问题：SVGD算法存在常数阶偏差，影响有限粒子系统的收敛分析。
- 方法要点：引入正则化预处理器修正核化Wasserstein梯度，建立非渐近收敛界。
- 实验或效果：在连续和离散时间下，量化正则化参数、步长等调优规则，平衡梯度流近似与估计误差。

## 摘要（原文）

> We derive finite-particle rates for the regularized Stein variational gradient descent (R-SVGD) algorithm introduced by He et al. (2024) that corrects the constant-order bias of the SVGD by applying a resolvent-type preconditioner to the kernelized Wasserstein gradient. For the resulting interacting $N$-particle system, we establish explicit non-asymptotic bounds for time-averaged (annealed) empirical measures, illustrating convergence in the \emph{true} (non-kernelized) Fisher information and, under a $\mathrm{W}_1\mathrm{I}$ condition on the target, corresponding $\mathrm{W}_1$ convergence for a large class of smooth kernels. Our analysis covers both continuous- and discrete-time dynamics and yields principled tuning rules for the regularization parameter, step size, and averaging horizon that quantify the trade-off between approximating the Wasserstein gradient flow and controlling finite-particle estimation error.

