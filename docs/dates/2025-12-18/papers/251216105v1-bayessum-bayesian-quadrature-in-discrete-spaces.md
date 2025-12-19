---
layout: default
title: BayesSum: Bayesian Quadrature in Discrete Spaces
---

# BayesSum: Bayesian Quadrature in Discrete Spaces
**arXiv**：[2512.16105v1](https://arxiv.org/abs/2512.16105) · [PDF](https://arxiv.org/pdf/2512.16105.pdf)  
**作者**：Sophia Seulkee Kang, François-Xavier Briol, Toni Karvonen, Zonghao Chen  

**一句话要点**：提出BayesSum以高效估计离散域上的难解期望

**关键词**：贝叶斯求积, 离散域期望估计, 高斯过程, 样本效率, 参数估计

## 3 点简述
- 核心问题：估计离散域上的难解期望，现有方法如蒙特卡洛采样效率低
- 方法要点：扩展贝叶斯求积至离散域，利用高斯过程整合先验信息提升样本效率
- 实验或效果：理论证明收敛速度优于蒙特卡洛，合成与真实模型实验验证样本需求更少

## 摘要（原文）

> This paper addresses the challenging computational problem of estimating intractable expectations over discrete domains. Existing approaches, including Monte Carlo and Russian Roulette estimators, are consistent but often require a large number of samples to achieve accurate results. We propose a novel estimator, \emph{BayesSum}, which is an extension of Bayesian quadrature to discrete domains. It is more sample efficient than alternatives due to its ability to make use of prior information about the integrand through a Gaussian process. We show this through theory, deriving a convergence rate significantly faster than Monte Carlo in a broad range of settings. We also demonstrate empirically that our proposed method does indeed require fewer samples on several synthetic settings as well as for parameter estimation for Conway-Maxwell-Poisson and Potts models.

