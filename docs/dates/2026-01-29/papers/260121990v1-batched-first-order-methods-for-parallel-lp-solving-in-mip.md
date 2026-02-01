---
layout: default
title: Batched First-Order Methods for Parallel LP Solving in MIP
---

# Batched First-Order Methods for Parallel LP Solving in MIP
**arXiv**：[2601.21990v1](https://arxiv.org/abs/2601.21990) · [PDF](https://arxiv.org/pdf/2601.21990.pdf)  
**作者**：Nicolas Blin, Stefano Gualandi, Christopher Maes, Andrea Lodi, Bartolomeo Stellato  

**一句话要点**：提出批处理一阶方法，在GPU上并行求解混合整数规划中的线性规划问题。

**关键词**：批处理优化, GPU并行计算, 线性规划求解, 混合整数规划, 原始-对偶混合梯度

## 3 点简述
- 核心问题：混合整数规划中强分支和边界收紧等操作需并行求解多个相关线性规划问题。
- 方法要点：扩展原始-对偶混合梯度算法，利用矩阵-矩阵运算替代重复矩阵-向量运算，优化GPU计算效率。
- 实验或效果：通过案例研究验证方法有效性，识别一阶方法优于传统单纯形求解器的问题规模与计算环境条件。

## 摘要（原文）

> We present a batched first-order method for solving multiple linear programs in parallel on GPUs. Our approach extends the primal-dual hybrid gradient algorithm to efficiently solve batches of related linear programming problems that arise in mixed-integer programming techniques such as strong branching and bound tightening. By leveraging matrix-matrix operations instead of repeated matrix-vector operations, we obtain significant computational advantages on GPU architectures. We demonstrate the effectiveness of our approach on various case studies and identify the problem sizes where first-order methods outperform traditional simplex-based solvers depending on the computational environment one can use. This is a significant step for the design and development of integer programming algorithms tightly exploiting GPU capabilities where we argue that some specific operations should be allocated to GPUs and performed in full instead of using light-weight heuristic approaches on CPUs.

