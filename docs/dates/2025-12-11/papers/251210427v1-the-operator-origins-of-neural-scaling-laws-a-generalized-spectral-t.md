---
layout: default
title: The Operator Origins of Neural Scaling Laws: A Generalized Spectral Transport Dynamics of Deep Learning
---

# The Operator Origins of Neural Scaling Laws: A Generalized Spectral Transport Dynamics of Deep Learning
**arXiv**：[2512.10427v1](https://arxiv.org/abs/2512.10427) · [PDF](https://arxiv.org/pdf/2512.10427.pdf)  
**作者**：Yizhou Zhang  

**一句话要点**：提出基于算子理论的谱输运动力学框架，统一解释深度学习的神经缩放定律与训练动态。

**关键词**：神经缩放定律, 算子理论, 谱输运动力学, 训练动态, 深度学习理论, 梯度下降分析

## 3 点简述
- 核心问题：现代深度网络在粗糙有限正则性下，雅可比算子谱重尾且基漂移，需统一理论描述训练动态。
- 方法要点：从梯度下降推导函数空间演化，应用Kato扰动理论得到谱输运-耗散PDE，分析自相似解与缩放指数。
- 实验或效果：理论预测缩放定律指数、双下降几何，并统一NTK训练与特征学习为PDE极限，提供谱框架连接算子几何与优化。

## 摘要（原文）

> Modern deep networks operate in a rough, finite-regularity regime where Jacobian-induced operators exhibit heavy-tailed spectra and strong basis drift. In this work, we derive a unified operator-theoretoretic description of neural training dynamics directly from gradient descent. Starting from the exact evolution $\dot e_t = -M(t)e_t$ in function space, we apply Kato perturbation theory to obtain a rigorous system of coupled mode ODEs and show that, after coarse-graining, these dynamics converge to a spectral transport-dissipation PDE \[ \partial_t g + \partial_λ(v g) = -λg + S, \] where $v$ captures eigenbasis drift and $S$ encodes nonlocal spectral coupling.
>   We prove that neural training preserves functional regularity, forcing the drift to take an asymptotic power-law form $v(λ,t)\sim -c(t)λ^b$. In the weak-coupling regime -- naturally induced by spectral locality and SGD noise -- the PDE admits self-similar solutions with a resolution frontier, polynomial amplitude growth, and power-law dissipation. This structure yields explicit scaling-law exponents, explains the geometry of double descent, and shows that the effective training time satisfies $τ(t)=t^αL(t)$ for slowly varying $L$.
>   Finally, we show that NTK training and feature learning arise as two limits of the same PDE: $v\equiv 0$ recovers lazy dynamics, while $v\neq 0$ produces representation drift. Our results provide a unified spectral framework connecting operator geometry, optimization dynamics, and the universal scaling behavior of modern deep networks.

