---
layout: default
title: Convergence Rate of the Last Iterate of Stochastic Proximal Algorithms
---

# Convergence Rate of the Last Iterate of Stochastic Proximal Algorithms
**arXiv**：[2602.05489v1](https://arxiv.org/abs/2602.05489) · [PDF](https://arxiv.org/pdf/2602.05489.pdf)  
**作者**：Kevin Kurian Thomas Vaidyan, Michael P. Friedlander, Ahmet Alacaoglu  

**一句话要点**：分析随机近端算法末次迭代收敛率，放宽方差假设，适用于多任务与联邦学习

**关键词**：随机优化, 末次迭代收敛, 近端算法, 多任务学习, 联邦学习, 图正则化

## 3 点简述
- 核心问题：放宽随机优化中末次迭代收敛所需的严格方差假设
- 方法要点：在分量凸性与光滑性下，证明末次迭代最优收敛率O~(1/√T)
- 实验或效果：直接应用于图引导正则化器，支持多任务与联邦学习场景

## 摘要（原文）

> We analyze two classical algorithms for solving additively composite convex optimization problems where the objective is the sum of a smooth term and a nonsmooth regularizer: proximal stochastic gradient method for a single regularizer; and the randomized incremental proximal method, which uses the proximal operator of a randomly selected function when the regularizer is given as the sum of many nonsmooth functions. We focus on relaxing the bounded variance assumption that is common, yet stringent, for getting last iterate convergence rates. We prove the $\widetilde{O}(1/\sqrt{T})$ rate of convergence for the last iterate of both algorithms under componentwise convexity and smoothness, which is optimal up to log terms. Our results apply directly to graph-guided regularizers that arise in multi-task and federated learning, where the regularizer decomposes as a sum over edges of a collaboration graph.

