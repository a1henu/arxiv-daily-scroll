---
layout: default
title: MINPO: Memory-Informed Neural Pseudo-Operator to Resolve Nonlocal Spatiotemporal Dynamics
---

# MINPO: Memory-Informed Neural Pseudo-Operator to Resolve Nonlocal Spatiotemporal Dynamics
**arXiv**：[2512.17273v1](https://arxiv.org/abs/2512.17273) · [PDF](https://arxiv.org/pdf/2512.17273.pdf)  
**作者**：Farinaz Mostajeran, Aruzhan Tleubek, Salah A Faroughi  

**一句话要点**：提出MINPO框架以统一解决非局部时空动力学中的积分-微分方程计算问题

**关键词**：非局部算子学习, 积分-微分方程求解, 时空动力学建模, 神经伪算子, 一致性损失, 泛化框架

## 3 点简述
- 核心问题：非局部时空行为需解积分-微分方程，传统方法计算成本高且现有神经求解器泛化性差
- 方法要点：MINPO通过神经编码器学习非局部算子及其逆，并引入一致性损失确保解与算子的一致性
- 实验或效果：在多种核类型、维度和计算需求下，MINPO相比经典方法和先进神经策略展现出高精度与鲁棒性

## 摘要（原文）

> Many physical systems exhibit nonlocal spatiotemporal behaviors described by integro-differential equations (IDEs). Classical methods for solving IDEs require repeatedly evaluating convolution integrals, whose cost increases quickly with kernel complexity and dimensionality. Existing neural solvers can accelerate selected instances of these computations, yet they do not generalize across diverse nonlocal structures. In this work, we introduce the Memory-Informed Neural Pseudo-Operator (MINPO), a unified framework for modeling nonlocal dynamics arising from long-range spatial interactions and/or long-term temporal memory. MINPO, employing either Kolmogorov-Arnold Networks (KANs) or multilayer perceptron networks (MLPs) as encoders, learns the nonlocal operator and its inverse directly through neural representations, and then explicitly reconstruct the unknown solution fields. The learning is guarded by a lightweight nonlocal consistency loss term to enforce coherence between the learned operator and reconstructed solution. The MINPO formulation allows to naturally capture and efficiently resolve nonlocal spatiotemporal dependencies governed by a wide spectrum of IDEs and their subsets, including fractional PDEs. We evaluate the efficacy of MINPO in comparison with classical techniques and state-of-the-art neural-based strategies based on MLPs, such as A-PINN and fPINN, along with their newly-developed KAN variants, A-PIKAN and fPIKAN, designed to facilitate a fair comparison. Our study offers compelling evidence of the accuracy of MINPO and demonstrates its robustness in handling (i) diverse kernel types, (ii) different kernel dimensionalities, and (iii) the substantial computational demands arising from repeated evaluations of kernel integrals. MINPO, thus, generalizes beyond problem-specific formulations, providing a unified framework for systems governed by nonlocal operators.

