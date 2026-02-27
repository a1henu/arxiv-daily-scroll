---
layout: default
title: MSINO: Curvature-Aware Sobolev Optimization for Manifold Neural Networks
---

# MSINO: Curvature-Aware Sobolev Optimization for Manifold Neural Networks
**arXiv**：[2602.22937v1](https://arxiv.org/abs/2602.22937) · [PDF](https://arxiv.org/pdf/2602.22937.pdf)  
**作者**：Suresan Pareth  

**一句话要点**：提出MSINO框架，通过曲率感知的Sobolev优化解决黎曼流形上神经网络训练的稳定性与收敛性问题。

**关键词**：黎曼流形优化, Sobolev训练, 曲率感知学习, 神经网络稳定性, 平行传输, Laplace Beltrami正则化

## 3 点简述
- 核心问题：黎曼流形上神经网络训练因曲率影响梯度对齐与稳定性，传统欧氏方法不适用。
- 方法要点：引入协变Sobolev损失替代欧氏导数监督，结合平行传输和Laplace Beltrami正则化提升稳定性。
- 实验或效果：理论推导曲率依赖常数，提供线性收敛保证，应用于表面成像、物理学习及SO(3)/SE(3)机器人等领域。

## 摘要（原文）

> We introduce Manifold Sobolev Informed Neural Optimization (MSINO), a curvature aware training framework for neural networks defined on Riemannian manifolds. The method replaces standard Euclidean derivative supervision with a covariant Sobolev loss that aligns gradients using parallel transport and improves stability via a Laplace Beltrami smoothness regularization term.
>   Building on classical results in Riemannian optimization and Sobolev theory on manifolds, we derive geometry dependent constants that yield (i) a Descent Lemma with a manifold Sobolev smoothness constant, (ii) a Sobolev Polyak Lojasiewicz inequality giving linear convergence guarantees for Riemannian gradient descent and stochastic gradient descent under explicit step size bounds, and (iii) a two step Newton Sobolev method with local quadratic contraction in curvature controlled neighborhoods.
>   Unlike prior Sobolev training in Euclidean space, MSINO provides training time guarantees that explicitly track curvature and transported Jacobians. Applications include surface imaging, physics informed learning settings, and robotics on Lie groups such as SO(3) and SE(3). The framework unifies value and gradient based learning with curvature aware convergence guarantees for neural training on manifolds.

