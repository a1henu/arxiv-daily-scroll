---
layout: default
title: Adaptive Matrix Online Learning through Smoothing with Guarantees for Nonsmooth Nonconvex Optimization
---

# Adaptive Matrix Online Learning through Smoothing with Guarantees for Nonsmooth Nonconvex Optimization
**arXiv**：[2602.08232v1](https://arxiv.org/abs/2602.08232) · [PDF](https://arxiv.org/pdf/2602.08232.pdf)  
**作者**：Ruichen Jiang, Zakaria Mhammedi, Mehryar Mohri, Aryan Mokhtari  

**一句话要点**：提出自适应矩阵在线学习框架，通过平滑核范数解决非光滑非凸优化问题。

**关键词**：矩阵在线学习, 自适应优化, 非光滑非凸优化, 核范数平滑, 在线到非凸转换, 算子范数约束

## 3 点简述
- 研究矩阵变量在线线性优化，算子范数约束下自适应算法设计挑战。
- 扩展梯度预测方案，基于平滑核范数构建高效方法，避免二次投影。
- 实例化FTPL和FAML方法，匹配Shampoo遗憾界，降低计算成本。

## 摘要（原文）

> We study online linear optimization with matrix variables constrained by the operator norm, a setting where the geometry renders designing data-dependent and efficient adaptive algorithms challenging. The best-known adaptive regret bounds are achieved by Shampoo-like methods, but they require solving a costly quadratic projection subproblem. To address this, we extend the gradient-based prediction scheme to adaptive matrix online learning and cast algorithm design as constructing a family of smoothed potentials for the nuclear norm. We define a notion of admissibility for such smoothings and prove any admissible smoothing yields a regret bound matching the best-known guarantees of one-sided Shampoo. We instantiate this framework with two efficient methods that avoid quadratic projections. The first is an adaptive Follow-the-Perturbed-Leader (FTPL) method using Gaussian stochastic smoothing. The second is Follow-the-Augmented-Matrix-Leader (FAML), which uses a deterministic hyperbolic smoothing in an augmented matrix space. By analyzing the admissibility of these smoothings, we show both methods admit closed-form updates and match one-sided Shampoo's regret up to a constant factor, while significantly reducing computational cost. Lastly, using the online-to-nonconvex conversion, we derive two matrix-based optimizers, Pion (from FTPL) and Leon (from FAML). We prove convergence guarantees for these methods in nonsmooth nonconvex settings, a guarantee that the popular Muon optimizer lacks.

