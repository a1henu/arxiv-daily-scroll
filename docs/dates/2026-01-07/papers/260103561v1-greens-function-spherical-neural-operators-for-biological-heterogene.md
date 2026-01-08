---
layout: default
title: Green's-Function Spherical Neural Operators for Biological Heterogeneity
---

# Green's-Function Spherical Neural Operators for Biological Heterogeneity
**arXiv**：[2601.03561v1](https://arxiv.org/abs/2601.03561) · [PDF](https://arxiv.org/pdf/2601.03561.pdf)  
**作者**：Hao Tang, Hao Chen, Hao Li, Chao Li  

**一句话要点**：提出Green's-Function Spherical Neural Operator以解决生物异质性建模问题

**关键词**：球形深度学习, Green's函数, 生物异质性建模, 等变算子, 各向异性系统, 神经算子

## 3 点简述
- 核心问题：现有球形深度学习方法难以平衡几何归纳偏置与真实世界异质性建模需求
- 方法要点：基于可设计Green's函数框架，融合等变、不变和各向异性算子解决方案
- 实验或效果：在球形MNIST、扩散MRI纤维预测等任务中展示优越性能

## 摘要（原文）

> Spherical deep learning has been widely applied to a broad range of real-world problems. Existing approaches often face challenges in balancing strong spherical geometric inductive biases with the need to model real-world heterogeneity. To solve this while retaining spherical geometry, we first introduce a designable Green's function framework (DGF) to provide new spherical operator solution strategy: Design systematic Green's functions under rotational group. Based on DGF, to model biological heterogeneity, we propose Green's-Function Spherical Neural Operator (GSNO) fusing 3 operator solutions: (1) Equivariant Solution derived from Equivariant Green's Function for symmetry-consistent modeling; (2) Invariant Solution derived from Invariant Green's Function to eliminate nuisance heterogeneity, e.g., consistent background field; (3) Anisotropic Solution derived from Anisotropic Green's Function to model anisotropic systems, especially fibers with preferred direction. Therefore, the resulting model, GSNO can adapt to real-world heterogeneous systems with nuisance variability and anisotropy while retaining spectral efficiency. Evaluations on spherical MNIST, Shallow Water Equation, diffusion MRI fiber prediction, cortical parcellation and molecule structure modeling demonstrate the superiority of GSNO.

