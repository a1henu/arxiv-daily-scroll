---
layout: default
title: A Stein Identity for q-Gaussians with Bounded Support
---

# A Stein Identity for q-Gaussians with Bounded Support
**arXiv**：[2603.03673v1](https://arxiv.org/abs/2603.03673) · [PDF](https://arxiv.org/pdf/2603.03673.pdf)  
**作者**：Sophia Sklaviadis, Thomas Moellenhoff, Andre F. T. Martins, Mario A. T. Figueiredo, Mohammad Emtiyaz Khan  

**一句话要点**：提出有界支撑q-高斯分布的Stein恒等式，以简化非高斯期望问题的梯度估计。

**关键词**：Stein恒等式, q-高斯分布, 梯度估计, 有界支撑分布, 贝叶斯深度学习, 锐度感知最小化

## 3 点简述
- 核心问题：Stein恒等式在非高斯分布中的应用受限，尤其是有界支撑分布。
- 方法要点：扩展先前结果，推导新Bonnet-和Price型定理，利用伴随分布简化形式。
- 实验或效果：有界支撑分布可降低梯度估计方差，适用于贝叶斯深度学习和锐度感知最小化。

## 摘要（原文）

> Stein's identity is a fundamental tool in machine learning with applications in generative models, stochastic optimization, and other problems involving gradients of expectations under Gaussian distributions. Less attention has been paid to problems with non-Gaussian expectations. Here, we consider the class of bounded-support $q$-Gaussians and derive a new Stein identity leading to gradient estimators which have nearly identical forms to the Gaussian ones, and which are similarly easy to implement. We do this by extending the previous results of Landsman, Vanduffel, and Yao (2013) to prove new Bonnet- and Price-type theorems for q-Gaussians. We also simplify their forms by using escort distributions. Our experiments show that bounded-support distributions can reduce the variance of gradient estimators, which can potentially be useful for Bayesian deep learning and sharpness-aware minimization. Overall, our work simplifies the application of Stein's identity for an important class of non-Gaussian distributions.

