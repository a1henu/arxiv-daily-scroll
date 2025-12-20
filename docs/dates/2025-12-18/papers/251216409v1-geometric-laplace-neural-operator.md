---
layout: default
title: Geometric Laplace Neural Operator
---

# Geometric Laplace Neural Operator
**arXiv**：[2512.16409v1](https://arxiv.org/abs/2512.16409) · [PDF](https://arxiv.org/pdf/2512.16409.pdf)  
**作者**：Hao Tang, Jiongyu Zhu, Zimeng Feng, Hao Li, Chao Li  

**一句话要点**：提出几何拉普拉斯神经算子以解决非周期激励和黎曼流形上的算子学习问题

**关键词**：神经算子, 拉普拉斯谱表示, 黎曼流形, 非周期激励, 算子学习, 网格不变网络

## 3 点简述
- 核心问题：现有神经算子难以处理非周期激励、瞬态响应及不规则几何上的信号
- 方法要点：基于极点-残差分解和指数基函数，嵌入拉普拉斯谱表示到拉普拉斯-贝尔特拉米算子的特征基中
- 实验或效果：在偏微分方程/常微分方程和真实数据集上展示优于其他先进模型的稳健性能

## 摘要（原文）

> Neural operators have emerged as powerful tools for learning mappings between function spaces, enabling efficient solutions to partial differential equations across varying inputs and domains. Despite the success, existing methods often struggle with non-periodic excitations, transient responses, and signals defined on irregular or non-Euclidean geometries. To address this, we propose a generalized operator learning framework based on a pole-residue decomposition enriched with exponential basis functions, enabling expressive modeling of aperiodic and decaying dynamics. Building on this formulation, we introduce the Geometric Laplace Neural Operator (GLNO), which embeds the Laplace spectral representation into the eigen-basis of the Laplace-Beltrami operator, extending operator learning to arbitrary Riemannian manifolds without requiring periodicity or uniform grids. We further design a grid-invariant network architecture (GLNONet) that realizes GLNO in practice. Extensive experiments on PDEs/ODEs and real-world datasets demonstrate our robust performance over other state-of-the-art models.

