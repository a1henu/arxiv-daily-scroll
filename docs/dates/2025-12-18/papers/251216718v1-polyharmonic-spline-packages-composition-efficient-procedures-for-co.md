---
layout: default
title: Polyharmonic Spline Packages: Composition, Efficient Procedures for Computation and Differentiation
---

# Polyharmonic Spline Packages: Composition, Efficient Procedures for Computation and Differentiation
**arXiv**：[2512.16718v1](https://arxiv.org/abs/2512.16718) · [PDF](https://arxiv.org/pdf/2512.16718.pdf)  
**作者**：Yuriy N. Bakhvalov  

**一句话要点**：提出级联多调和样条包架构以解决高维回归中的计算可扩展性问题

**关键词**：多调和样条, 级联架构, 回归分析, 计算效率, 高维数据

## 3 点简述
- 核心问题：直接应用多调和样条回归存在O(N^3)计算成本和理论假设在高维输入空间失效的限制
- 方法要点：构建级联架构，使用多调和样条包，适用于未知内在低维问题，提供高效矩阵计算和端到端微分
- 实验或效果：未知

## 摘要（原文）

> In a previous paper it was shown that a machine learning regression problem can be solved within the framework of random function theory, with the optimal kernel analytically derived from symmetry and indifference principles and coinciding with a polyharmonic spline. However, a direct application of that solution is limited by O(N^3) computational cost and by a breakdown of the original theoretical assumptions when the input space has excessive dimensionality. This paper proposes a cascade architecture built from packages of polyharmonic splines that simultaneously addresses scalability and is theoretically justified for problems with unknown intrinsic low dimensionality. Efficient matrix procedures are presented for forward computation and end-to-end differentiation through the cascade.

