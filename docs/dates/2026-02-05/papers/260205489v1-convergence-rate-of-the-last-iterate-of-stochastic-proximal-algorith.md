---
layout: default
title: Convergence Rate of the Last Iterate of Stochastic Proximal Algorithms
---

# Convergence Rate of the Last Iterate of Stochastic Proximal Algorithms
**arXiv**：[2602.05489v1](https://arxiv.org/abs/2602.05489) · [PDF](https://arxiv.org/pdf/2602.05489.pdf)  
**作者**：Kevin Kurian Thomas Vaidyan, Michael P. Friedlander, Ahmet Alacaoglu  

**一句话要点**：分析随机近端算法末次迭代收敛率，放宽方差假设，适用于图引导正则化问题。

**关键词**：随机优化, 近端算法, 末次迭代收敛, 图引导正则化, 多任务学习, 联邦学习

## 3 点简述
- 研究随机近端梯度法和随机增量近端法的末次迭代收敛性，放宽常见的严格方差假设。
- 在分量凸性和光滑性下，证明末次迭代达到最优对数项内的收敛率。
- 结果直接适用于多任务和联邦学习中的图引导正则化问题，正则化为图边和。

## 摘要（原文）

> We analyze two classical algorithms for solving additively composite convex optimization problems where the objective is the sum of a smooth term and a nonsmooth regularizer: proximal stochastic gradient method for a single regularizer; and the randomized incremental proximal method, which uses the proximal operator of a randomly selected function when the regularizer is given as the sum of many nonsmooth functions. We focus on relaxing the bounded variance assumption that is common, yet stringent, for getting last iterate convergence rates. We prove the $\widetilde{O}(1/\sqrt{T})$ rate of convergence for the last iterate of both algorithms under componentwise convexity and smoothness, which is optimal up to log terms. Our results apply directly to graph-guided regularizers that arise in multi-task and federated learning, where the regularizer decomposes as a sum over edges of a collaboration graph.

