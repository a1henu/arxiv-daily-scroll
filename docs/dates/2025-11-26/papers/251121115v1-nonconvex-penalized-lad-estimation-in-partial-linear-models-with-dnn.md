---
layout: default
title: Nonconvex Penalized LAD Estimation in Partial Linear Models with DNNs: Asymptotic Analysis and Proximal Algorithms
---

# Nonconvex Penalized LAD Estimation in Partial Linear Models with DNNs: Asymptotic Analysis and Proximal Algorithms
**arXiv**：[2511.21115v1](https://arxiv.org/abs/2511.21115) · [PDF](https://arxiv.org/pdf/2511.21115.pdf)  
**作者**：Lechen Feng, Haoran Li, Lucky Li, Xingqiu Zhao  

**一句话要点**：提出非凸惩罚LAD估计结合DNNs，解决部分线性模型中的渐近分析与计算问题

**关键词**：部分线性模型, LAD回归, 深度神经网络, 非凸优化, 渐近分析, 近端算法

## 3 点简述
- 核心问题：非凸非光滑正则化与高维不连续优化，挑战渐近理论与计算
- 方法要点：使用DNNs参数化非参数项，建立一致性、收敛率和渐近正态性
- 实验或效果：分析oracle问题与连续松弛，比较近端次梯度方法的计算效率

## 摘要（原文）

> This paper investigates the partial linear model by Least Absolute Deviation (LAD) regression. We parameterize the nonparametric term using Deep Neural Networks (DNNs) and formulate a penalized LAD problem for estimation. Specifically, our model exhibits the following challenges. First, the regularization term can be nonconvex and nonsmooth, necessitating the introduction of infinite dimensional variational analysis and nonsmooth analysis into the asymptotic normality discussion. Second, our network must expand (in width, sparsity level and depth) as more samples are observed, thereby introducing additional difficulties for theoretical analysis. Third, the oracle of the proposed estimator is itself defined through a ultra high-dimensional, nonconvex, and discontinuous optimization problem, which already entails substantial computational and theoretical challenges. Under such the challenges, we establish the consistency, convergence rate, and asymptotic normality of the estimator. Furthermore, we analyze the oracle problem itself and its continuous relaxation. We study the convergence of a proximal subgradient method for both formulations, highlighting their structural differences lead to distinct computational subproblems along the iterations. In particular, the relaxed formulation admits significantly cheaper proximal updates, reflecting an inherent trade-off between statistical accuracy and computational tractability.

