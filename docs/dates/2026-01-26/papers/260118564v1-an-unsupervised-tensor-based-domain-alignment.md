---
layout: default
title: An Unsupervised Tensor-Based Domain Alignment
---

# An Unsupervised Tensor-Based Domain Alignment
**arXiv**：[2601.18564v1](https://arxiv.org/abs/2601.18564) · [PDF](https://arxiv.org/pdf/2601.18564.pdf)  
**作者**：Chong Hyun Lee, Kibae Lee, Hyun Hee Yim  

**一句话要点**：提出基于张量的无监督域对齐算法，通过斜流形优化提升复杂域适应任务的性能。

**关键词**：无监督域对齐, 张量对齐, 斜流形优化, 域适应, 分类精度提升

## 3 点简述
- 核心问题：无监督域对齐中源域和目标域张量的对齐，传统方法在流形约束上灵活性不足。
- 方法要点：使用对齐矩阵在不变子空间中对齐张量，基于斜流形迭代优化，并引入方差保持正则化项。
- 实验或效果：实验显示方法加速域转换并提高分类精度，优于现有先进技术，适用于复杂域适应任务。

## 摘要（原文）

> We propose a tensor-based domain alignment (DA) algorithm designed to align source and target tensors within an invariant subspace through the use of alignment matrices. These matrices along with the subspace undergo iterative optimization of which constraint is on oblique manifold, which offers greater flexibility and adaptability compared to the traditional Stiefel manifold. Moreover, regularization terms defined to preserve the variance of both source and target tensors, ensures robust performance. Our framework is versatile, effectively generalizing existing tensor-based DA methods as special cases. Through extensive experiments, we demonstrate that our approach not only enhances DA conversion speed but also significantly boosts classification accuracy. This positions our method as superior to current state-of-the-art techniques, making it a preferable choice for complex domain adaptation tasks.

