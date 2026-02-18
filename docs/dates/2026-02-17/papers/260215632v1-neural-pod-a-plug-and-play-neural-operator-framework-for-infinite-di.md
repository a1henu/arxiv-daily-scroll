---
layout: default
title: Neural-POD: A Plug-and-Play Neural Operator Framework for Infinite-Dimensional Functional Nonlinear Proper Orthogonal Decomposition
---

# Neural-POD: A Plug-and-Play Neural Operator Framework for Infinite-Dimensional Functional Nonlinear Proper Orthogonal Decomposition
**arXiv**：[2602.15632v1](https://arxiv.org/abs/2602.15632) · [PDF](https://arxiv.org/pdf/2602.15632.pdf)  
**作者**：Changhong Mou, Binghang Lu, Guang Lin  

**一句话要点**：提出Neural-POD框架，通过神经网络构建无限维非线性正交基函数，以解决AI for Science中离散化限制问题。

**关键词**：神经算子, 正交基函数, 降阶建模, 无限维空间, 非线性结构, AI for Science

## 3 点简述
- 核心问题：AI for Science常受限于训练网格或分辨率的离散化，导致学习表示泛化能力不足。
- 方法要点：将基函数构建转化为残差最小化序列问题，通过神经网络训练实现非线性正交基，类似Gram-Schmidt正交化过程。
- 实验或效果：在Burgers'和Navier-Stokes方程等复杂时空系统中验证了框架的鲁棒性，并集成到降阶建模和算子学习框架中。

## 摘要（原文）

> The rapid development of AI for Science is often hindered by the "discretization", where learned representations remain restricted to the specific grids or resolutions used during training. We propose the Neural Proper Orthogonal Decomposition (Neural-POD), a plug-and-play neural operator framework that constructs nonlinear, orthogonal basis functions in infinite-dimensional space using neural networks. Unlike the classical Proper Orthogonal Decomposition (POD), which is limited to linear subspace approximations obtained through singular value decomposition (SVD), Neural-POD formulates basis construction as a sequence of residual minimization problems solved through neural network training. Each basis function is obtained by learning to represent the remaining structure in the data, following a process analogous to Gram--Schmidt orthogonalization. This neural formulation introduces several key advantages over classical POD: it enables optimization in arbitrary norms (e.g., $L^2$, $L^1$), learns mappings between infinite-dimensional function spaces that is resolution-invariant, generalizes effectively to unseen parameter regimes, and inherently captures nonlinear structures in complex spatiotemporal systems. The resulting basis functions are interpretable, reusable, and enabling integration into both reduced order modeling (ROM) and operator learning frameworks such as deep operator learning (DeepONet). We demonstrate the robustness of Neural-POD with different complex spatiotemporal systems, including the Burgers' and Navier-Stokes equations. We further show that Neural-POD serves as a high performance, plug-and-play bridge between classical Galerkin projection and operator learning that enables consistent integration with both projection-based reduced order models and DeepONet frameworks.

