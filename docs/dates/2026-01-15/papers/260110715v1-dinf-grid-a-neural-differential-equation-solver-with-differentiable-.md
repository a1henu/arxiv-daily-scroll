---
layout: default
title: DInf-Grid: A Neural Differential Equation Solver with Differentiable Feature Grids
---

# DInf-Grid: A Neural Differential Equation Solver with Differentiable Feature Grids
**arXiv**：[2601.10715v1](https://arxiv.org/abs/2601.10715) · [PDF](https://arxiv.org/pdf/2601.10715.pdf)  
**作者**：Navami Kairanda, Shanthika Naik, Marc Habermann, Avinash Sharma, Christian Theobalt, Vladislav Golyanik  

**一句话要点**：提出DInf-Grid，一种结合可微特征网格与径向基插值的神经微分方程求解器，以高效解决物理场建模问题。

**关键词**：神经微分方程求解, 可微特征网格, 径向基函数插值, 多分辨率分解, 物理场建模, 高效计算

## 3 点简述
- 核心问题：现有网格表示依赖线性插值，无法计算高阶导数，不适用于求解微分方程。
- 方法要点：采用径向基函数插值实现无限可微性，结合多分辨率网格分解以捕获高频解并加速全局梯度计算。
- 实验或效果：在泊松方程、亥姆霍兹方程等任务中，相比基于坐标的MLP方法提速5-20倍，保持精度与紧凑性。

## 摘要（原文）

> We present a novel differentiable grid-based representation for efficiently solving differential equations (DEs). Widely used architectures for neural solvers, such as sinusoidal neural networks, are coordinate-based MLPs that are both computationally intensive and slow to train. Although grid-based alternatives for implicit representations (e.g., Instant-NGP and K-Planes) train faster by exploiting signal structure, their reliance on linear interpolation restricts their ability to compute higher-order derivatives, rendering them unsuitable for solving DEs. Our approach overcomes these limitations by combining the efficiency of feature grids with radial basis function interpolation, which is infinitely differentiable. To effectively capture high-frequency solutions and enable stable and faster computation of global gradients, we introduce a multi-resolution decomposition with co-located grids. Our proposed representation, DInf-Grid, is trained implicitly using the differential equations as loss functions, enabling accurate modelling of physical fields. We validate DInf-Grid on a variety of tasks, including the Poisson equation for image reconstruction, the Helmholtz equation for wave fields, and the Kirchhoff-Love boundary value problem for cloth simulation. Our results demonstrate a 5-20x speed-up over coordinate-based MLP-based methods, solving differential equations in seconds or minutes while maintaining comparable accuracy and compactness.

