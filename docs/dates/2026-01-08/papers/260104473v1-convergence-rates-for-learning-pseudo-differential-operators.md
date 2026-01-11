---
layout: default
title: Convergence Rates for Learning Pseudo-Differential Operators
---

# Convergence Rates for Learning Pseudo-Differential Operators
**arXiv**：[2601.04473v1](https://arxiv.org/abs/2601.04473) · [PDF](https://arxiv.org/pdf/2601.04473.pdf)  
**作者**：Jiaheng Chen, Daniel Sanz-Alonso  

**一句话要点**：提出稀疏估计器以学习椭圆伪微分算子，实现收敛率分析与高效求解器构建

**关键词**：算子学习, 小波方法, 收敛率分析, 稀疏估计, 伽辽金求解器, 伪微分算子

## 3 点简述
- 核心问题：学习椭圆伪微分算子的收敛率，应用于偏微分方程和数学物理
- 方法要点：基于小波-伽辽金框架，设计稀疏估计器，结合矩阵压缩和嵌套支撑策略
- 实验或效果：获得收敛率，学习算子诱导高效稳定伽辽金求解器，匹配统计与数值误差

## 摘要（原文）

> This paper establishes convergence rates for learning elliptic pseudo-differential operators, a fundamental operator class in partial differential equations and mathematical physics. In a wavelet-Galerkin framework, we formulate learning over this class as a structured infinite-dimensional regression problem with multiscale sparsity. Building on this structure, we propose a sparse, data- and computation-efficient estimator, which leverages a novel matrix compression scheme tailored to the learning task and a nested-support strategy to balance approximation and estimation errors. In addition to obtaining convergence rates for the estimator, we show that the learned operator induces an efficient and stable Galerkin solver whose numerical error matches its statistical accuracy. Our results therefore contribute to bringing together operator learning, data-driven solvers, and wavelet methods in scientific computing.

