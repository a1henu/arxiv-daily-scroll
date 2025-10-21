---
layout: default
title: Matricial Free Energy as a Gaussianizing Regularizer: Enhancing Autoencoders for Gaussian Code Generation
---

# Matricial Free Energy as a Gaussianizing Regularizer: Enhancing Autoencoders for Gaussian Code Generation
**arXiv**：[2510.17120v1](https://arxiv.org/abs/2510.17120) · [PDF](https://arxiv.org/pdf/2510.17120.pdf)  
**作者**：Rishi Sonthalia, Raj Rao Nadakuditi  

**一句话要点**：提出基于矩阵自由能的正则化方法，增强自编码器生成高斯代码

**关键词**：自编码器, 矩阵自由能, 高斯代码生成, 正则化方法, 随机矩阵理论

## 3 点简述
- 核心问题：自编码器代码分布需高斯化以提升泛化能力
- 方法要点：定义矩阵自由能损失，优化代码矩阵奇异值分布
- 实验或效果：经验模拟显示高斯代码在训练和测试集上泛化良好

## 摘要（原文）

> We introduce a novel regularization scheme for autoencoders based on
> matricial free energy. Our approach defines a differentiable loss function in
> terms of the singular values of the code matrix (code dimension x batch size).
> From the standpoint of free probability an d random matrix theory, this loss
> achieves its minimum when the singular value distribution of the code matrix
> coincides with that of an appropriately sculpted random metric with i.i.d.
> Gaussian entries. Empirical simulations demonstrate that minimizing the
> negative matricial free energy through standard stochastic gradient-based
> training yields Gaussian-like codes that generalize across training and test
> sets. Building on this foundation, we propose a matricidal free energy
> maximizing autoencoder that reliably produces Gaussian codes and show its
> application to underdetermined inverse problems.

