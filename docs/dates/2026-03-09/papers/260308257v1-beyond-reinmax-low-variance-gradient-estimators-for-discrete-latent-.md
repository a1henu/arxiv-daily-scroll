---
layout: default
title: Beyond ReinMax: Low-Variance Gradient Estimators for Discrete Latent Variables
---

# Beyond ReinMax: Low-Variance Gradient Estimators for Discrete Latent Variables
**arXiv**：[2603.08257v1](https://arxiv.org/abs/2603.08257) · [PDF](https://arxiv.org/pdf/2603.08257.pdf)  
**作者**：Daniel Wang, Thang D. Bui  

**一句话要点**：提出ReinMax-Rao和ReinMax-CV梯度估计器，以降低ReinMax方差，优化离散隐变量模型训练。

**关键词**：离散隐变量, 梯度估计, 变分自编码器, Rao-Blackwellisation, 控制变量, 数值方法

## 3 点简述
- 核心问题：ReinMax梯度估计器在离散隐变量模型中存在高方差问题，影响训练效率。
- 方法要点：通过Rao-Blackwellisation和控制变量技术，构建低方差梯度估计器ReinMax-Rao和ReinMax-CV。
- 实验或效果：在离散隐空间的变分自编码器训练中，新估计器表现出更优性能。

## 摘要（原文）

> Machine learning models involving discrete latent variables require gradient estimators to facilitate backpropagation in a computationally efficient manner. The most recent addition to the Straight-Through family of estimators, ReinMax, can be viewed from a numerical ODE perspective as incorporating an approximation via Heun's method to reduce bias, but at the cost of high variance. In this work, we introduce the ReinMax-Rao and ReinMax-CV estimators which incorporate Rao-Blackwellisation and control variate techniques into ReinMax to reduce its variance. Our estimators demonstrate superior performance on training variational autoencoders with discrete latent spaces. Furthermore, we investigate the possibility of leveraging alternative numerical methods for constructing more accurate gradient approximations and present an alternative view of ReinMax from a simpler numerical integration perspective.

