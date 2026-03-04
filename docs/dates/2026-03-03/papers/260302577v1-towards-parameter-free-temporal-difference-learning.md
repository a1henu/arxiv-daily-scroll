---
layout: default
title: Towards Parameter-Free Temporal Difference Learning
---

# Towards Parameter-Free Temporal Difference Learning
**arXiv**：[2603.02577v1](https://arxiv.org/abs/2603.02577) · [PDF](https://arxiv.org/pdf/2603.02577.pdf)  
**作者**：Yunxiang Li, Mark Schmidt, Reza Babanezhad, Sharan Vaswani  

**一句话要点**：提出指数步长TD(0)算法以解决强化学习中参数依赖问题

**关键词**：时序差分学习, 强化学习, 参数无关算法, 指数步长, 马尔可夫采样, 值函数估计

## 3 点简述
- 核心问题：传统TD学习需依赖难以估计的问题参数，如特征协方差最小特征值或马尔可夫链混合时间
- 方法要点：采用指数步长调度，在i.i.d.采样下无需问题参数，在马尔可夫采样下结合正则化
- 实验或效果：在i.i.d.设置下达到最优偏差-方差权衡，在马尔可夫设置下实现可比收敛率且无需额外假设

## 摘要（原文）

> Temporal difference (TD) learning is a fundamental algorithm for estimating value functions in reinforcement learning. Recent finite-time analyses of TD with linear function approximation quantify its theoretical convergence rate. However, they often require setting the algorithm parameters using problem-dependent quantities that are difficult to estimate in practice -- such as the minimum eigenvalue of the feature covariance (\(ω\)) or the mixing time of the underlying Markov chain (\(τ_{\text{mix}}\)). In addition, some analyses rely on nonstandard and impractical modifications, exacerbating the gap between theory and practice. To address these limitations, we use an exponential step-size schedule with the standard TD(0) algorithm. We analyze the resulting method under two sampling regimes: independent and identically distributed (i.i.d.) sampling from the stationary distribution, and the more practical Markovian sampling along a single trajectory. In the i.i.d.\ setting, the proposed algorithm does not require knowledge of problem-dependent quantities such as \(ω\), and attains the optimal bias-variance trade-off for the last iterate. In the Markovian setting, we propose a regularized TD(0) algorithm with an exponential step-size schedule. The resulting algorithm achieves a comparable convergence rate to prior works, without requiring projections, iterate averaging, or knowledge of \(τ_{\text{mix}}\) or \(ω\).

