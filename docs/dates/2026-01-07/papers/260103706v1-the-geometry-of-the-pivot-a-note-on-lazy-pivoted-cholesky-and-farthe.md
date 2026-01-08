---
layout: default
title: The Geometry of the Pivot: A Note on Lazy Pivoted Cholesky and Farthest Point Sampling
---

# The Geometry of the Pivot: A Note on Lazy Pivoted Cholesky and Farthest Point Sampling
**arXiv**：[2601.03706v1](https://arxiv.org/abs/2601.03706) · [PDF](https://arxiv.org/pdf/2601.03706.pdf)  
**作者**：Gil Shabat  

**一句话要点**：揭示Pivoted Cholesky分解在RKHS中的几何等价性，连接Farthest Point Sampling与Gram-Schmidt正交化

**关键词**：Pivoted Cholesky分解, Farthest Point Sampling, 核方法, 低秩近似, 高斯过程, 再生核希尔伯特空间

## 3 点简述
- 核心问题：Pivoted Cholesky分解在核方法中的几何直觉不明确，影响其在机器学习中的应用理解
- 方法要点：证明枢轴选择等价于核度量下的Farthest Point Sampling，Cholesky因子构建隐含Gram-Schmidt正交化
- 实验或效果：提供简洁推导和Python实现，以弥合理论与实践的差距

## 摘要（原文）

> Low-rank approximations of large kernel matrices are ubiquitous in machine learning, particularly for scaling Gaussian Processes to massive datasets. The Pivoted Cholesky decomposition is a standard tool for this task, offering a computationally efficient, greedy low-rank approximation. While its algebraic properties are well-documented in numerical linear algebra, its geometric intuition within the context of kernel methods often remains obscure. In this note, we elucidate the geometric interpretation of the algorithm within the Reproducing Kernel Hilbert Space (RKHS). We demonstrate that the pivotal selection step is mathematically equivalent to Farthest Point Sampling (FPS) using the kernel metric, and that the Cholesky factor construction is an implicit Gram-Schmidt orthogonalization. We provide a concise derivation and a minimalist Python implementation to bridge the gap between theory and practice.

