---
layout: default
title: RanSOM: Second-Order Momentum with Randomized Scaling for Constrained and Unconstrained Optimization
---

# RanSOM: Second-Order Momentum with Randomized Scaling for Constrained and Unconstrained Optimization
**arXiv**：[2602.06824v1](https://arxiv.org/abs/2602.06824) · [PDF](https://arxiv.org/pdf/2602.06824.pdf)  
**作者**：El Mahdi Chayti  

**一句话要点**：提出RanSOM框架，通过随机步长消除动量方法在随机优化中的曲率偏差，实现最优收敛率。

**关键词**：随机优化, 动量方法, 收敛率分析, Hessian-向量积, 无偏估计, 约束优化

## 3 点简述
- 动量方法在随机设置下因曲率偏差导致收敛率受限至次优水平。
- 引入随机步长，利用Stein恒等式通过单次Hessian-向量积无偏估计偏差，避免额外采样。
- 理论分析显示在标准有界噪声下恢复最优收敛率，并在重尾噪声下无需梯度裁剪达到最优。

## 摘要（原文）

> Momentum methods, such as Polyak's Heavy Ball, are the standard for training deep networks but suffer from curvature-induced bias in stochastic settings, limiting convergence to suboptimal $\mathcal{O}(ε^{-4})$ rates. Existing corrections typically require expensive auxiliary sampling or restrictive smoothness assumptions. We propose \textbf{RanSOM}, a unified framework that eliminates this bias by replacing deterministic step sizes with randomized steps drawn from distributions with mean $η_t$. This modification allows us to leverage Stein-type identities to compute an exact, unbiased estimate of the momentum bias using a single Hessian-vector product computed jointly with the gradient, avoiding auxiliary queries. We instantiate this framework in two algorithms: \textbf{RanSOM-E} for unconstrained optimization (using exponentially distributed steps) and \textbf{RanSOM-B} for constrained optimization (using beta-distributed steps to strictly preserve feasibility). Theoretical analysis confirms that RanSOM recovers the optimal $\mathcal{O}(ε^{-3})$ convergence rate under standard bounded noise, and achieves optimal rates for heavy-tailed noise settings ($p \in (1, 2]$) without requiring gradient clipping.

