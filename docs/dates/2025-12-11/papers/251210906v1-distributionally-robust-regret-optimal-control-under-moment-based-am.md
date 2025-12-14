---
layout: default
title: Distributionally Robust Regret Optimal Control Under Moment-Based Ambiguity Sets
---

# Distributionally Robust Regret Optimal Control Under Moment-Based Ambiguity Sets
**arXiv**：[2512.10906v1](https://arxiv.org/abs/2512.10906) · [PDF](https://arxiv.org/pdf/2512.10906.pdf)  
**作者**：Feras Al Taha, Eilyan Bitar  

**一句话要点**：提出基于矩模糊集的分布鲁棒遗憾最优控制方法，用于线性二次随机控制问题。

**关键词**：分布鲁棒控制, 线性二次控制, 矩模糊集, 遗憾最小化, 凸优化, 可扩展算法

## 3 点简述
- 研究有限时域线性二次随机控制问题，噪声分布未知但属于基于矩的模糊集。
- 设计因果仿射控制策略，最小化模糊集内最坏情况期望遗憾，问题可转化为易处理凸规划。
- 提出可扩展对偶投影次梯度方法计算最优控制器，数值实验对比现有数据驱动与分布鲁棒方法。

## 摘要（原文）

> In this paper, we consider a class of finite-horizon, linear-quadratic stochastic control problems, where the probability distribution governing the noise process is unknown but assumed to belong to an ambiguity set consisting of all distributions whose mean and covariance lie within norm balls centered at given nominal values. To address the distributional ambiguity, we explore the design of causal affine control policies to minimize the worst-case expected regret over all distributions in the given ambiguity set. The resulting minimax optimal control problem is shown to admit an equivalent reformulation as a tractable convex program that corresponds to a regularized version of the nominal linear-quadratic stochastic control problem. While this convex program can be recast as a semidefinite program, semidefinite programs are typically solved using primal-dual interior point methods that scale poorly with the problem size in practice. To address this limitation, we propose a scalable dual projected subgradient method to compute optimal controllers to an arbitrary accuracy. Numerical experiments are presented to benchmark the proposed method against state-of-the-art data-driven and distributionally robust control design approaches.

