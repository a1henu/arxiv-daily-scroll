---
layout: default
title: Numerical exploration of the range of shape functionals using neural networks
---

# Numerical exploration of the range of shape functionals using neural networks
**arXiv**：[2602.14881v1](https://arxiv.org/abs/2602.14881) · [PDF](https://arxiv.org/pdf/2602.14881.pdf)  
**作者**：Eloi Martinet, Ilias Ftouhi  

**一句话要点**：提出基于神经网络的数值框架以探索Blaschke–Santaló图，用于形状泛函不等式分析。

**关键词**：Blaschke–Santaló图, 形状泛函, 神经网络参数化, 凸体优化, 交互粒子系统, 数值探索

## 3 点简述
- 核心问题：探索Blaschke–Santaló图，描述形状泛函间的不等式关系。
- 方法要点：使用基于规范函数的可逆神经网络参数化凸体，保持凸性；引入交互粒子系统均匀采样图。
- 实验或效果：在二维和三维凸体上验证，涉及体积、周长、惯性矩、扭转刚度、Willmore能量和Neumann特征值。

## 摘要（原文）

> We introduce a novel numerical framework for the exploration of Blaschke--Santaló diagrams, which are efficient tools characterizing the possible inequalities relating some given shape functionals. We introduce a parametrization of convex bodies in arbitrary dimensions using a specific invertible neural network architecture based on gauge functions, allowing an intrinsic conservation of the convexity of the sets during the shape optimization process. To achieve a uniform sampling inside the diagram, and thus a satisfying description of it, we introduce an interacting particle system that minimizes a Riesz energy functional via automatic differentiation in PyTorch. The effectiveness of the method is demonstrated on several diagrams involving both geometric and PDE-type functionals for convex bodies of $\mathbb{R}^2$ and $\mathbb{R}^3$, namely, the volume, the perimeter, the moment of inertia, the torsional rigidity, the Willmore energy, and the first two Neumann eigenvalues of the Laplacian.

