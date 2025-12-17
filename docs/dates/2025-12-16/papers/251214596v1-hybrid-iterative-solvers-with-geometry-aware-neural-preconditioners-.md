---
layout: default
title: Hybrid Iterative Solvers with Geometry-Aware Neural Preconditioners for Parametric PDEs
---

# Hybrid Iterative Solvers with Geometry-Aware Neural Preconditioners for Parametric PDEs
**arXiv**：[2512.14596v1](https://arxiv.org/abs/2512.14596) · [PDF](https://arxiv.org/pdf/2512.14596.pdf)  
**作者**：Youngkyu Lee, Francesc Levrero Florencio, Jay Pathak, George Em Karniadakis  

**一句话要点**：提出几何感知神经预条件器以增强参数PDE混合迭代求解器的鲁棒性

**关键词**：参数偏微分方程, 神经算子, 几何感知学习, 混合迭代求解器, 非结构化网格

## 3 点简述
- 参数PDE求解器收敛性对几何和离散化敏感，传统混合方法泛化性差
- 引入Geo-DeepONet，利用有限元离散化提取几何信息，实现跨任意非结构化网格的算子学习
- 结合传统迭代方法，实验证明在多样非结构化域上提升求解器的鲁棒性和效率

## 摘要（原文）

> The convergence behavior of classical iterative solvers for parametric partial differential equations (PDEs) is often highly sensitive to the domain and specific discretization of PDEs. Previously, we introduced hybrid solvers by combining the classical solvers with neural operators for a specific geometry 1, but they tend to under-perform in geometries not encountered during training. To address this challenge, we introduce Geo-DeepONet, a geometry-aware deep operator network that incorporates domain information extracted from finite element discretizations. Geo-DeepONet enables accurate operator learning across arbitrary unstructured meshes without requiring retraining. Building on this, we develop a class of geometry-aware hybrid preconditioned iterative solvers by coupling Geo-DeepONet with traditional methods such as relaxation schemes and Krylov subspace algorithms. Through numerical experiments on parametric PDEs posed over diverse unstructured domains, we demonstrate the enhanced robustness and efficiency of the proposed hybrid solvers for multiple real-world applications.

