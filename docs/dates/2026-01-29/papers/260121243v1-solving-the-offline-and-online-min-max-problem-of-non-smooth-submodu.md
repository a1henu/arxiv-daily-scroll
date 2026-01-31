---
layout: default
title: Solving the Offline and Online Min-Max Problem of Non-smooth Submodular-Concave Functions: A Zeroth-Order Approach
---

# Solving the Offline and Online Min-Max Problem of Non-smooth Submodular-Concave Functions: A Zeroth-Order Approach
**arXiv**：[2601.21243v1](https://arxiv.org/abs/2601.21243) · [PDF](https://arxiv.org/pdf/2601.21243.pdf)  
**作者**：Amir Ali Farzin, Yuen-Man Pun, Philipp Braun, Tyler Summers, Iman Shames  

**一句话要点**：提出零阶方法解决非光滑子模-凹函数的离线与在线最小-最大问题

**关键词**：最小-最大优化, 零阶方法, 子模函数, 非光滑优化, 在线学习, 高斯平滑

## 3 点简述
- 研究非光滑、子模-凹目标函数的最小-最大优化问题，适用于离线与在线场景。
- 基于Lovász扩展子梯度和高斯平滑梯度估计，设计零阶算法，证明收敛到ε-鞍点。
- 理论分析包括复杂度与超参数选择，并通过数值实验验证算法性能。

## 摘要（原文）

> We consider max-min and min-max problems with objective functions that are possibly non-smooth, submodular with respect to the minimiser and concave with respect to the maximiser. We investigate the performance of a zeroth-order method applied to this problem. The method is based on the subgradient of the Lovász extension of the objective function with respect to the minimiser and based on Gaussian smoothing to estimate the smoothed function gradient with respect to the maximiser. In expectation sense, we prove the convergence of the algorithm to an $ε$-saddle point in the offline case. Moreover, we show that, in the expectation sense, in the online setting, the algorithm achieves $O(\sqrt{N\bar{P}_N})$ online duality gap, where $N$ is the number of iterations and $\bar{P}_N$ is the path length of the sequence of optimal decisions. The complexity analysis and hyperparameter selection are presented for all the cases. The theoretical results are illustrated via numerical examples.

