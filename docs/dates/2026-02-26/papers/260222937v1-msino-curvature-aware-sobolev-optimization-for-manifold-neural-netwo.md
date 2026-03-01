---
layout: default
title: MSINO: Curvature-Aware Sobolev Optimization for Manifold Neural Networks
---

# MSINO: Curvature-Aware Sobolev Optimization for Manifold Neural Networks
**arXiv**：[2602.22937v1](https://arxiv.org/abs/2602.22937) · [PDF](https://arxiv.org/pdf/2602.22937.pdf)  
**作者**：Suresan Pareth  

**一句话要点**：提出MSINO框架，通过曲率感知的Sobolev优化解决黎曼流形上神经网络的训练问题。

**关键词**：黎曼流形优化, Sobolev训练, 曲率感知学习, 神经网络训练, 几何深度学习

## 3 点简述
- 核心问题：在黎曼流形上训练神经网络时，标准欧几里得导数监督可能导致梯度对齐和稳定性问题。
- 方法要点：使用协变Sobolev损失替代欧几里得导数，结合平行传输和Laplace Beltrami平滑正则化，提升训练稳定性。
- 实验或效果：在表面成像、物理信息学习和机器人学（如SO(3)和SE(3)）等应用中，提供曲率感知的收敛保证。

## 摘要（原文）

> We introduce Manifold Sobolev Informed Neural Optimization (MSINO), a curvature aware training framework for neural networks defined on Riemannian manifolds. The method replaces standard Euclidean derivative supervision with a covariant Sobolev loss that aligns gradients using parallel transport and improves stability via a Laplace Beltrami smoothness regularization term.
>   Building on classical results in Riemannian optimization and Sobolev theory on manifolds, we derive geometry dependent constants that yield (i) a Descent Lemma with a manifold Sobolev smoothness constant, (ii) a Sobolev Polyak Lojasiewicz inequality giving linear convergence guarantees for Riemannian gradient descent and stochastic gradient descent under explicit step size bounds, and (iii) a two step Newton Sobolev method with local quadratic contraction in curvature controlled neighborhoods.
>   Unlike prior Sobolev training in Euclidean space, MSINO provides training time guarantees that explicitly track curvature and transported Jacobians. Applications include surface imaging, physics informed learning settings, and robotics on Lie groups such as SO(3) and SE(3). The framework unifies value and gradient based learning with curvature aware convergence guarantees for neural training on manifolds.

