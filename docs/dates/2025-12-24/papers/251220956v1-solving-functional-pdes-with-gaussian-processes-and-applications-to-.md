---
layout: default
title: Solving Functional PDEs with Gaussian Processes and Applications to Functional Renormalization Group Equations
---

# Solving Functional PDEs with Gaussian Processes and Applications to Functional Renormalization Group Equations
**arXiv**：[2512.20956v1](https://arxiv.org/abs/2512.20956) · [PDF](https://arxiv.org/pdf/2512.20956.pdf)  
**作者**：Xianjin Yang, Matthieu Darcy, Matthew Hudes, Francis J. Alexander, Gregory Eyink, Houman Owhadi  

**一句话要点**：提出高斯过程算子学习框架以求解非微扰泛函重整化群方程

**关键词**：泛函偏微分方程, 高斯过程算子学习, 泛函重整化群, 非微扰方法, 算子学习框架

## 3 点简述
- 核心问题：解决定义在泛函上的非微扰泛函重整化群方程，这些是积分-微分方程。
- 方法要点：使用高斯过程算子学习直接在函数空间构建灵活泛函表示，独立于特定方程或离散化。
- 实验或效果：在Wetterich和Wilson-Polchinski方程上验证，性能优于或等于局部势近似，并能处理非恒定场。

## 摘要（原文）

> We present an operator learning framework for solving non-perturbative functional renormalization group equations, which are integro-differential equations defined on functionals. Our proposed approach uses Gaussian process operator learning to construct a flexible functional representation formulated directly on function space, making it independent of a particular equation or discretization. Our method is flexible, and can apply to a broad range of functional differential equations while still allowing for the incorporation of physical priors in either the prior mean or the kernel design. We demonstrate the performance of our method on several relevant equations, such as the Wetterich and Wilson--Polchinski equations, showing that it achieves equal or better performance than existing approximations such as the local-potential approximation, while being significantly more flexible. In particular, our method can handle non-constant fields, making it promising for the study of more complex field configurations, such as instantons.

