---
layout: default
title: Matrix Editing Meets Fair Clustering: Parameterized Algorithms and Complexity
---

# Matrix Editing Meets Fair Clustering: Parameterized Algorithms and Complexity
**arXiv**：[2512.03718v1](https://arxiv.org/abs/2512.03718) · [PDF](https://arxiv.org/pdf/2512.03718.pdf)  
**作者**：Robert Ganian, Hung P. Hoang, Simon Wietheger  

**一句话要点**：研究公平聚类与矩阵编辑的复杂性，提出参数化算法以规避下界限制

**关键词**：公平聚类, 矩阵编辑, 参数化复杂性, 固定参数算法, NP难问题, 树状矩阵

## 3 点简述
- 核心问题：公平均值聚类等价于编辑彩色矩阵为颜色平衡行，NP难且排除固定参数算法
- 方法要点：通过实例约束、固定参数近似或树状矩阵参数化实现可处理性
- 实验或效果：建立完整复杂性图景，展示三种规避下界的途径

## 摘要（原文）

> We study the computational problem of computing a fair means clustering of discrete vectors, which admits an equivalent formulation as editing a colored matrix into one with few distinct color-balanced rows by changing at most $k$ values. While NP-hard in both the fairness-oblivious and the fair settings, the problem is well-known to admit a fixed-parameter algorithm in the former ``vanilla'' setting. As our first contribution, we exclude an analogous algorithm even for highly restricted fair means clustering instances. We then proceed to obtain a full complexity landscape of the problem, and establish tractability results which capture three means of circumventing our obtained lower bound: placing additional constraints on the problem instances, fixed-parameter approximation, or using an alternative parameterization targeting tree-like matrices.

