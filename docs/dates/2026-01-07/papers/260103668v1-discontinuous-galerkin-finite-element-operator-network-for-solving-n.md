---
layout: default
title: Discontinuous Galerkin finite element operator network for solving non-smooth PDEs
---

# Discontinuous Galerkin finite element operator network for solving non-smooth PDEs
**arXiv**：[2601.03668v1](https://arxiv.org/abs/2601.03668) · [PDF](https://arxiv.org/pdf/2601.03668.pdf)  
**作者**：Kapil Chawla, Youngjoon Hong, Jae Yong Lee, Sanghyun Lee  

**一句话要点**：提出DG-FEONet以解决非光滑偏微分方程的数据无关算子学习问题

**关键词**：间断伽辽金法, 算子学习, 非光滑偏微分方程, 数据无关训练, 神经网络, 收敛分析

## 3 点简述
- 核心问题：传统算子学习模型需大量配对数据，且在尖锐特征附近表现不佳
- 方法要点：结合间断伽辽金法和神经网络，基于SIPG方案最小化残差，实现无数据训练
- 实验或效果：在一维和二维PDE问题上验证，能准确恢复间断性，参数空间泛化强，收敛率可靠

## 摘要（原文）

> We introduce Discontinuous Galerkin Finite Element Operator Network (DG--FEONet), a data-free operator learning framework that combines the strengths of the discontinuous Galerkin (DG) method with neural networks to solve parametric partial differential equations (PDEs) with discontinuous coefficients and non-smooth solutions. Unlike traditional operator learning models such as DeepONet and Fourier Neural Operator, which require large paired datasets and often struggle near sharp features, our approach minimizes the residual of a DG-based weak formulation using the Symmetric Interior Penalty Galerkin (SIPG) scheme. DG-FEONet predicts element-wise solution coefficients via a neural network, enabling data-free training without the need for precomputed input-output pairs. We provide theoretical justification through convergence analysis and validate the model's performance on a series of one- and two-dimensional PDE problems, demonstrating accurate recovery of discontinuities, strong generalization across parameter space, and reliable convergence rates. Our results highlight the potential of combining local discretization schemes with machine learning to achieve robust, singularity-aware operator approximation in challenging PDE settings.

