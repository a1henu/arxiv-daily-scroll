---
layout: default
title: Generalized Spherical Neural Operators: Green's Function Formulation
---

# Generalized Spherical Neural Operators: Green's Function Formulation
**arXiv**：[2512.10723v1](https://arxiv.org/abs/2512.10723) · [PDF](https://arxiv.org/pdf/2512.10723.pdf)  
**作者**：Hao Tang, Hao Chen, Chao Li  

**一句话要点**：提出基于可设计球面格林函数的广义球面神经算子，以解决球面域上参数偏微分方程建模的几何失真与灵活性不足问题。

**关键词**：球面神经算子, 格林函数, 参数偏微分方程, 谱学习, 几何建模, 多尺度架构

## 3 点简述
- 核心问题：现有球面神经算子依赖旋转等变性，但难以平衡几何保持与真实世界复杂建模的灵活性。
- 方法要点：基于球面格林函数及其谐波展开，设计绝对与相对位置依赖的格林函数，实现等变性与不变性的灵活平衡。
- 实验或效果：在扩散MRI、浅水动力学和全球天气预报任务中，GSNO和GSHNet架构均优于现有方法。

## 摘要（原文）

> Neural operators offer powerful approaches for solving parametric partial differential equations, but extending them to spherical domains remains challenging due to the need to preserve intrinsic geometry while avoiding distortions that break rotational consistency. Existing spherical operators rely on rotational equivariance but often lack the flexibility for real-world complexity. We propose a general operator-design framework based on the designable spherical Green's function and its harmonic expansion, establishing a solid operator-theoretic foundation for spherical learning. Based on this, we propose an absolute and relative position-dependent Green's function that enables flexible balance of equivariance and invariance for real-world modeling. The resulting operator, Green's-function Spherical Neural Operator (GSNO) with a novel spectral learning method, can adapt to anisotropic, constraint-rich systems while retaining spectral efficiency. To exploit GSNO, we develop GSHNet, a hierarchical architecture that combines multi-scale spectral modeling with spherical up-down sampling, enhancing global feature representation. Evaluations on diffusion MRI, shallow water dynamics, and global weather forecasting, GSNO and GSHNet consistently outperform state-of-the-art methods. Our results position GSNO as a principled and general framework for spherical operator learning, bridging rigorous theory with real-world complexity.

