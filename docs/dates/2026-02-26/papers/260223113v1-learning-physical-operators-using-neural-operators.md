---
layout: default
title: Learning Physical Operators using Neural Operators
---

# Learning Physical Operators using Neural Operators
**arXiv**：[2602.23113v1](https://arxiv.org/abs/2602.23113) · [PDF](https://arxiv.org/pdf/2602.23113.pdf)  
**作者**：Vignesh Gopakumar, Ander Gray, Dan Giles, Lorenzo Zanisi, Matt J. Kusner, Timo Betcke, Stanislas Pamela, Marc Peter Deisenroth  

**一句话要点**：提出基于算子分裂的物理信息训练框架，以提升神经算子在PDE求解中的泛化能力与时间连续性。

**关键词**：神经算子, 偏微分方程求解, 物理信息训练, 算子分裂, 时间连续性, 泛化性能

## 3 点简述
- 神经算子作为PDE代理模型，面临泛化差和固定时间离散化限制。
- 采用算子分裂方法分解PDE，训练神经算子学习非线性物理算子，线性算子用有限差分卷积近似。
- 在Navier-Stokes方程上验证，实现更好收敛、泛化性能，支持时间外推和可解释性。

## 摘要（原文）

> Neural operators have emerged as promising surrogate models for solving partial differential equations (PDEs), but struggle to generalise beyond training distributions and are often constrained to a fixed temporal discretisation. This work introduces a physics-informed training framework that addresses these limitations by decomposing PDEs using operator splitting methods, training separate neural operators to learn individual non-linear physical operators while approximating linear operators with fixed finite-difference convolutions. This modular mixture-of-experts architecture enables generalisation to novel physical regimes by explicitly encoding the underlying operator structure. We formulate the modelling task as a neural ordinary differential equation (ODE) where these learned operators constitute the right-hand side, enabling continuous-in-time predictions through standard ODE solvers and implicitly enforcing PDE constraints. Demonstrated on incompressible and compressible Navier-Stokes equations, our approach achieves better convergence and superior performance when generalising to unseen physics. The method remains parameter-efficient, enabling temporal extrapolation beyond training horizons, and provides interpretable components whose behaviour can be verified against known physics.

