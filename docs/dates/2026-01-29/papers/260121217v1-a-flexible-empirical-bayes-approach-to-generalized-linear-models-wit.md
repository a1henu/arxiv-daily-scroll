---
layout: default
title: A Flexible Empirical Bayes Approach to Generalized Linear Models, with Applications to Sparse Logistic Regression
---

# A Flexible Empirical Bayes Approach to Generalized Linear Models, with Applications to Sparse Logistic Regression
**arXiv**：[2601.21217v1](https://arxiv.org/abs/2601.21217) · [PDF](https://arxiv.org/pdf/2601.21217.pdf)  
**作者**：Dongyue Xie, Wanrong Zhu, Matthew Stephens  

**一句话要点**：提出灵活经验贝叶斯方法以拟合广义线性模型，应用于稀疏逻辑回归。

**关键词**：经验贝叶斯, 变分推断, 广义线性模型, 稀疏逻辑回归, 免调参方法

## 3 点简述
- 核心问题：传统变分推断方法需调参且假设高斯变分，限制应用范围。
- 方法要点：采用新变分推断直接优化后验均值和先验参数，实现免调参和可扩展。
- 实验或效果：在稀疏逻辑回归中展示优越预测性能，优于现有方法。

## 摘要（原文）

> We introduce a flexible empirical Bayes approach for fitting Bayesian generalized linear models. Specifically, we adopt a novel mean-field variational inference (VI) method and the prior is estimated within the VI algorithm, making the method tuning-free. Unlike traditional VI methods that optimize the posterior density function, our approach directly optimizes the posterior mean and prior parameters. This formulation reduces the number of parameters to optimize and enables the use of scalable algorithms such as L-BFGS and stochastic gradient descent. Furthermore, our method automatically determines the optimal posterior based on the prior and likelihood, distinguishing it from existing VI methods that often assume a Gaussian variational. Our approach represents a unified framework applicable to a wide range of exponential family distributions, removing the need to develop unique VI methods for each combination of likelihood and prior distributions. We apply the framework to solve sparse logistic regression and demonstrate the superior predictive performance of our method in extensive numerical studies, by comparing it to prevalent sparse logistic regression approaches.

