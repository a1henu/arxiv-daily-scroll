---
layout: default
title: Towards Continuous-Time Approximations for Stochastic Gradient Descent without Replacement
---

# Towards Continuous-Time Approximations for Stochastic Gradient Descent without Replacement
**arXiv**：[2512.04703v1](https://arxiv.org/abs/2512.04703) · [PDF](https://arxiv.org/pdf/2512.04703.pdf)  
**作者**：Stefan Perko  

**一句话要点**：提出基于Young微分方程的连续时间近似，以分析无放回随机梯度下降的收敛性。

**关键词**：随机梯度下降, 连续时间近似, Young微分方程, 收敛分析, 机器学习优化

## 3 点简述
- 核心问题：无放回随机梯度下降（SGDo）的理论分析不足，相比有放回和单次遍历版本。
- 方法要点：使用“分时段布朗运动”驱动的Young微分方程，构建带加性噪声的连续时间近似模型。
- 实验或效果：证明强凸目标下连续时间近似几乎必然收敛，并给出收敛速率上界，优于先前结果。

## 摘要（原文）

> Gradient optimization algorithms using epochs, that is those based on stochastic gradient descent without replacement (SGDo), are predominantly used to train machine learning models in practice. However, the mathematical theory of SGDo and related algorithms remain underexplored compared to their "with replacement" and "one-pass" counterparts. In this article, we propose a stochastic, continuous-time approximation to SGDo with additive noise based on a Young differential equation driven by a stochastic process we call an "epoched Brownian motion". We show its usefulness by proving the almost sure convergence of the continuous-time approximation for strongly convex objectives and learning rate schedules of the form $u_t = \frac{1}{(1+t)^β}, β\in (0,1)$. Moreover, we compute an upper bound on the asymptotic rate of almost sure convergence, which is as good or better than previous results for SGDo.

