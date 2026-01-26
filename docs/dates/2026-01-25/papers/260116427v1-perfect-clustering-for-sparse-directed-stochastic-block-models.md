---
layout: default
title: Perfect Clustering for Sparse Directed Stochastic Block Models
---

# Perfect Clustering for Sparse Directed Stochastic Block Models
**arXiv**：[2601.16427v1](https://arxiv.org/abs/2601.16427) · [PDF](https://arxiv.org/pdf/2601.16427.pdf)  
**作者**：Behzad Aalipur, Yichen Qin  

**一句话要点**：提出非谱邻域平滑方法，实现稀疏有向随机块模型的精确社区恢复。

**关键词**：有向随机块模型, 社区检测, 非谱方法, 邻域平滑, 精确恢复, 稀疏网络

## 3 点简述
- 核心问题：有向稀疏随机块模型的社区检测在非对称、低度网络中谱方法不稳定。
- 方法要点：采用两阶段非谱方法，先通过邻域平滑估计概率矩阵，再应用K均值聚类。
- 实验或效果：模拟显示方法在高度有向稀疏非对称结构中可靠，优于现有谱和基于分数的方法。

## 摘要（原文）

> Exact recovery in stochastic block models (SBMs) is well understood in undirected settings, but remains considerably less developed for directed and sparse networks, particularly when the number of communities diverges. Spectral methods for directed SBMs often lack stability in asymmetric, low-degree regimes, and existing non-spectral approaches focus primarily on undirected or dense settings.
>   We propose a fully non-spectral, two-stage procedure for community detection in sparse directed SBMs with potentially growing numbers of communities. The method first estimates the directed probability matrix using a neighborhood-smoothing scheme tailored to the asymmetric setting, and then applies $K$-means clustering to the estimated rows, thereby avoiding the limitations of eigen- or singular value decompositions in sparse, asymmetric networks. Our main theoretical contribution is a uniform row-wise concentration bound for the smoothed estimator, obtained through new arguments that control asymmetric neighborhoods and separate in- and out-degree effects. These results imply the exact recovery of all community labels with probability tending to one, under mild sparsity and separation conditions that allow both $γ_n \to 0$ and $K_n \to \infty$.
>   Simulation studies, including highly directed, sparse, and non-symmetric block structures, demonstrate that the proposed procedure performs reliably in regimes where directed spectral and score-based methods deteriorate. To the best of our knowledge, this provides the first exact recovery guarantee for this class of non-spectral, neighborhood-smoothing methods in the sparse, directed setting.

