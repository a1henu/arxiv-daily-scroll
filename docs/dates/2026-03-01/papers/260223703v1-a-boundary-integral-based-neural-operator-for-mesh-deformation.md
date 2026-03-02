---
layout: default
title: A Boundary Integral-based Neural Operator for Mesh Deformation
---

# A Boundary Integral-based Neural Operator for Mesh Deformation
**arXiv**：[2602.23703v1](https://arxiv.org/abs/2602.23703) · [PDF](https://arxiv.org/pdf/2602.23703.pdf)  
**作者**：Zhengyu Wu, Jun Liu, Wei Wang  

**一句话要点**：提出基于边界积分与神经算子的网格变形方法，以解决线性弹性边界值问题中的计算效率与狄利克雷条件处理难题。

**关键词**：网格变形, 边界积分方法, 神经算子, 线性弹性, 参数化网格生成, 形状优化

## 3 点简述
- 核心问题：传统有限元方法计算成本高，现有神经算子在处理向量场狄利克雷边界条件时存在局限性。
- 方法要点：引入狄利克雷型格林张量进行直接边界积分表示，设计BINO学习几何与材料感知的格林牵引核，实现物理积分与几何表示的数学解耦。
- 实验或效果：数值实验验证了模型在大变形和刚体运动中的高精度、线性与叠加原理严格遵循，确保网格质量和计算效率。

## 摘要（原文）

> This paper presents an efficient mesh deformation method based on boundary integration and neural operators, formulating the problem as a linear elasticity boundary value problem (BVP). To overcome the high computational cost of traditional finite element methods and the limitations of existing neural operators in handling Dirichlet boundary conditions for vector fields, we introduce a direct boundary integral representation using a Dirichlet-type Green's tensor. This formulation expresses the internal displacement field solely as a function of boundary displacements, eliminating the need to solve for unknown tractions. Building on this, we design a Boundary-Integral-based Neural Operator (BINO) that learns the geometry- and material-aware Green's traction kernel. A key technical advantage of our framework is the mathematical decoupling of the physical integration process from the geometric representation via geometric descriptors. While this study primarily demonstrates robust generalization across diverse boundary conditions, the architecture inherently possesses potential for cross-geometry adaptation. Numerical experiments, including large deformations of flexible beams and rigid-body motions of NACA airfoils, confirm the model's high accuracy and strict adherence to the principles of linearity and superposition. The results demonstrate that the proposed framework ensures mesh quality and computational efficiency, providing a reliable new paradigm for parametric mesh generation and shape optimization in engineering.

