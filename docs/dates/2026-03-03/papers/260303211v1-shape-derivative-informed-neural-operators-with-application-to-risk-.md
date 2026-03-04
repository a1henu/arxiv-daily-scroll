---
layout: default
title: Shape Derivative-Informed Neural Operators with Application to Risk-Averse Shape Optimization
---

# Shape Derivative-Informed Neural Operators with Application to Risk-Averse Shape Optimization
**arXiv**：[2603.03211v1](https://arxiv.org/abs/2603.03211) · [PDF](https://arxiv.org/pdf/2603.03211.pdf)  
**作者**：Xindi Gong, Dingcheng Luo, Thomas O'Leary-Roseberry, Ruanui Nicholson, Omar Ghattas  

**一句话要点**：提出Shape-DINO以加速不确定性下的形状优化，通过导数信息学习PDE解算子。

**关键词**：形状优化, 不确定性优化, 神经算子, 导数信息学习, PDE约束优化, 计算加速

## 3 点简述
- 核心问题：传统PDE方法在不确定性形状优化中计算成本高，标准神经代理无法提供准确梯度。
- 方法要点：使用微分同胚映射编码几何变化，结合导数信息学习PDE解及其Fréchet导数。
- 实验或效果：在Poisson和Navier-Stokes问题中实现3-8个数量级加速，减少PDE求解1-2个数量级。

## 摘要（原文）

> Shape optimization under uncertainty (OUU) is computationally intensive for classical PDE-based methods due to the high cost of repeated sampling-based risk evaluation across many uncertainty realizations and varying geometries, while standard neural surrogates often fail to provide accurate and efficient sensitivities for optimization. We introduce Shape-DINO, a derivative-informed neural operator framework for learning PDE solution operators on families of varying geometries, with a particular focus on accelerating PDE-constrained shape OUU. Shape-DINOs encode geometric variability through diffeomorphic mappings to a fixed reference domain and employ a derivative-informed operator learning objective that jointly learns the PDE solution and its Fréchet derivatives with respect to design variables and uncertain parameters, enabling accurate state predictions and reliable gradients for large-scale OUU. We establish a priori error bounds linking surrogate accuracy to optimization error and prove universal approximation results for multi-input reduced basis neural operators in suitable $C^1$ norms. We demonstrate efficiency and scalability on three representative shape OUU problems, including boundary design for a Poisson equation and shape design governed by steady-state Navier-Stokes exterior flows in two and three dimensions. Across these examples, Shape-DINOs produce more reliable optimization results than operator surrogates trained without derivative information. In our examples, Shape-DINOs achieve 3-8 orders-of-magnitude speedups in state and gradient evaluations. Counting training data generation, Shape-DINOs reduce necessary PDE solves by 1-2 orders-of-magnitude compared to a strictly PDE-based approach for a single OUU problem. Moreover, Shape-DINO construction costs can be amortized across many objectives and risk measures, enabling large-scale shape OUU for complex systems.

