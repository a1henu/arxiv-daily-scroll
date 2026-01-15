---
layout: default
title: Discrete Solution Operator Learning for Geometry-Dependent PDEs
---

# Discrete Solution Operator Learning for Geometry-Dependent PDEs
**arXiv**：[2601.09143v1](https://arxiv.org/abs/2601.09143) · [PDF](https://arxiv.org/pdf/2601.09143.pdf)  
**作者**：Jinshuai Bai, Haolin Li, Zahra Sharif Khodaei, M. H. Aliabadi, YuanTong Gu, Xi-Qiao Feng  

**一句话要点**：提出离散解算子学习以解决几何依赖偏微分方程中离散结构变化问题

**关键词**：离散解算子学习, 几何依赖偏微分方程, 算子学习, 科学机器学习, 离散结构变化, 多尺度组装

## 3 点简述
- 核心问题：几何变化导致离散结构突变，如拓扑变化，破坏连续算子学习的平滑前提
- 方法要点：学习离散解过程，分解为局部贡献编码、多尺度组装和隐式重建等可学习阶段
- 实验或效果：在几何依赖的Poisson、弹性等问题中，稳定预测分布内和分布外几何，包括不连续边界

## 摘要（原文）

> Neural operator learning accelerates PDE solution by approximating operators as mappings between continuous function spaces. Yet in many engineering settings, varying geometry induces discrete structural changes, including topological changes, abrupt changes in boundary conditions or boundary types, and changes in the effective computational domain, which break the smooth-variation premise. Here we introduce Discrete Solution Operator Learning (DiSOL), a complementary paradigm that learns discrete solution procedures rather than continuous function-space operators. DiSOL factorizes the solver into learnable stages that mirror classical discretizations: local contribution encoding, multiscale assembly, and implicit solution reconstruction on an embedded grid, thereby preserving procedure-level consistency while adapting to geometry-dependent discrete structures. Across geometry-dependent Poisson, advection-diffusion, linear elasticity, as well as spatiotemporal heat-conduction problems, DiSOL produces stable and accurate predictions under both in-distribution and strongly out-of-distribution geometries, including discontinuous boundaries and topological changes. These results highlight the need for procedural operator representations in geometry-dominated regimes and position discrete solution operator learning as a distinct, complementary direction in scientific machine learning.

