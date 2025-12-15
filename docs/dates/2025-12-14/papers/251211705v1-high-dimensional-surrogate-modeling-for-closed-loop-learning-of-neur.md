---
layout: default
title: High-Dimensional Surrogate Modeling for Closed-Loop Learning of Neural-Network-Parameterized Model Predictive Control
---

# High-Dimensional Surrogate Modeling for Closed-Loop Learning of Neural-Network-Parameterized Model Predictive Control
**arXiv**：[2512.11705v1](https://arxiv.org/abs/2512.11705) · [PDF](https://arxiv.org/pdf/2512.11705.pdf)  
**作者**：Sebastian Hirt, Valentinus Suwanto, Hendrik Alsmeier, Maik Pfefferkorn, Rolf Findeisen  

**一句话要点**：提出贝叶斯神经网络代理模型以解决高维控制器参数学习中的收敛问题

**关键词**：贝叶斯优化, 代理建模, 模型预测控制, 高维参数学习, 贝叶斯神经网络

## 3 点简述
- 核心问题：贝叶斯优化在密集高维控制器参数化中因标准代理模型失效而收敛困难
- 方法要点：使用贝叶斯神经网络作为代理模型，包括有限宽和无限宽变体
- 实验或效果：在cart-pole任务中，贝叶斯神经网络实现更快收敛，支持超千维参数优化

## 摘要（原文）

> Learning controller parameters from closed-loop data has been shown to improve closed-loop performance. Bayesian optimization, a widely used black-box and sample-efficient learning method, constructs a probabilistic surrogate of the closed-loop performance from few experiments and uses it to select informative controller parameters. However, it typically struggles with dense high-dimensional controller parameterizations, as they may appear, for example, in tuning model predictive controllers, because standard surrogate models fail to capture the structure of such spaces. This work suggests that the use of Bayesian neural networks as surrogate models may help to mitigate this limitation. Through a comparison between Gaussian processes with Matern kernels, finite-width Bayesian neural networks, and infinite-width Bayesian neural networks on a cart-pole task, we find that Bayesian neural network surrogate models achieve faster and more reliable convergence of the closed-loop cost and enable successful optimization of parameterizations with hundreds of dimensions. Infinite-width Bayesian neural networks also maintain performance in settings with more than one thousand parameters, whereas Matern-kernel Gaussian processes rapidly lose effectiveness. These results indicate that Bayesian neural network surrogate models may be suitable for learning dense high-dimensional controller parameterizations and offer practical guidance for selecting surrogate models in learning-based controller design.

