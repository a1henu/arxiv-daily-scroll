---
layout: default
title: DInf-Grid: A Neural Differential Equation Solver with Differentiable Feature Grids
---

# DInf-Grid: A Neural Differential Equation Solver with Differentiable Feature Grids
**arXiv**：[2601.10715v1](https://arxiv.org/abs/2601.10715) · [PDF](https://arxiv.org/pdf/2601.10715.pdf)  
**作者**：Navami Kairanda, Shanthika Naik, Marc Habermann, Avinash Sharma, Christian Theobalt, Vladislav Golyanik  

**一句话要点**：提出DInf-Grid，结合可微特征网格与径向基插值，高效求解微分方程。

**关键词**：微分方程求解, 可微表示, 特征网格, 径向基插值, 多分辨率分解, 物理场建模

## 3 点简述
- 现有神经求解器如坐标MLP计算慢，网格方法因线性插值无法计算高阶导数。
- DInf-Grid使用径向基插值实现无限可微，并引入多分辨率网格以捕获高频解。
- 实验在泊松、亥姆霍兹等方程上验证，速度提升5-20倍，保持精度与紧凑性。

## 摘要（原文）

> We present a novel differentiable grid-based representation for efficiently solving differential equations (DEs). Widely used architectures for neural solvers, such as sinusoidal neural networks, are coordinate-based MLPs that are both computationally intensive and slow to train. Although grid-based alternatives for implicit representations (e.g., Instant-NGP and K-Planes) train faster by exploiting signal structure, their reliance on linear interpolation restricts their ability to compute higher-order derivatives, rendering them unsuitable for solving DEs. Our approach overcomes these limitations by combining the efficiency of feature grids with radial basis function interpolation, which is infinitely differentiable. To effectively capture high-frequency solutions and enable stable and faster computation of global gradients, we introduce a multi-resolution decomposition with co-located grids. Our proposed representation, DInf-Grid, is trained implicitly using the differential equations as loss functions, enabling accurate modelling of physical fields. We validate DInf-Grid on a variety of tasks, including the Poisson equation for image reconstruction, the Helmholtz equation for wave fields, and the Kirchhoff-Love boundary value problem for cloth simulation. Our results demonstrate a 5-20x speed-up over coordinate-based MLP-based methods, solving differential equations in seconds or minutes while maintaining comparable accuracy and compactness.

