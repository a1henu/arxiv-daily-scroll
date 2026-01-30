---
layout: default
title: Solving the Offline and Online Min-Max Problem of Non-smooth Submodular-Concave Functions: A Zeroth-Order Approach
---

# Solving the Offline and Online Min-Max Problem of Non-smooth Submodular-Concave Functions: A Zeroth-Order Approach
**arXiv**：[2601.21243v1](https://arxiv.org/abs/2601.21243) · [PDF](https://arxiv.org/pdf/2601.21243.pdf)  
**作者**：Amir Ali Farzin, Yuen-Man Pun, Philipp Braun, Tyler Summers, Iman Shames  

**一句话要点**：提出零阶方法解决非光滑子模-凹函数的离线与在线最小-最大问题

**关键词**：最小-最大优化, 零阶方法, 子模函数, 非光滑优化, 在线学习, 鞍点收敛

## 3 点简述
- 核心问题：处理目标函数非光滑、对最小化变量子模、对最大化变量凹的最小-最大优化问题。
- 方法要点：结合Lovász扩展的次梯度与高斯平滑梯度估计，设计零阶算法。
- 实验或效果：理论证明离线收敛至ε-鞍点，在线获得O(√(N·路径长度))对偶间隙，数值实验验证。

## 摘要（原文）

> We consider max-min and min-max problems with objective functions that are possibly non-smooth, submodular with respect to the minimiser and concave with respect to the maximiser. We investigate the performance of a zeroth-order method applied to this problem. The method is based on the subgradient of the Lovász extension of the objective function with respect to the minimiser and based on Gaussian smoothing to estimate the smoothed function gradient with respect to the maximiser. In expectation sense, we prove the convergence of the algorithm to an $ε$-saddle point in the offline case. Moreover, we show that, in the expectation sense, in the online setting, the algorithm achieves $O(\sqrt{N\bar{P}_N})$ online duality gap, where $N$ is the number of iterations and $\bar{P}_N$ is the path length of the sequence of optimal decisions. The complexity analysis and hyperparameter selection are presented for all the cases. The theoretical results are illustrated via numerical examples.

