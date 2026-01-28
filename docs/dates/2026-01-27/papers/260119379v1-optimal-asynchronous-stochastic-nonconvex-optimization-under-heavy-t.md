---
layout: default
title: Optimal Asynchronous Stochastic Nonconvex Optimization under Heavy-Tailed Noise
---

# Optimal Asynchronous Stochastic Nonconvex Optimization under Heavy-Tailed Noise
**arXiv**：[2601.19379v1](https://arxiv.org/abs/2601.19379) · [PDF](https://arxiv.org/pdf/2601.19379.pdf)  
**作者**：Yidong Wu, Luo Luo  

**一句话要点**：提出异步归一化动量随机梯度下降算法，以解决重尾噪声和异构计算时间下的非凸优化问题。

**关键词**：异步优化, 随机梯度下降, 重尾噪声, 非凸优化, 异构计算, 动量方法

## 3 点简述
- 研究异步随机非凸优化问题，考虑重尾梯度噪声和异构计算时间。
- 提出异步归一化动量随机梯度下降算法，在p阶中心矩有界假设下达到最优时间复杂度。
- 通过数值实验验证了所提方法的有效性。

## 摘要（原文）

> This paper considers the problem of asynchronous stochastic nonconvex optimization with heavy-tailed gradient noise and arbitrarily heterogeneous computation times across workers. We propose an asynchronous normalized stochastic gradient descent algorithm with momentum. The analysis show that our method achieves the optimal time complexity under the assumption of bounded $p$th-order central moment with $p\in(1,2]$. We also provide numerical experiments to show the effectiveness of proposed method.

