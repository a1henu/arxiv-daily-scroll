---
layout: default
title: Fast $k$-means clustering in Riemannian manifolds via Fréchet maps: Applications to large-dimensional SPD matrices
---

# Fast $k$-means clustering in Riemannian manifolds via Fréchet maps: Applications to large-dimensional SPD matrices
**arXiv**：[2511.08993v1](https://arxiv.org/abs/2511.08993) · [PDF](https://arxiv.org/pdf/2511.08993.pdf)  
**作者**：Ji Shi, Nicolas Charon, Andreas Mang, Demetrio Labate, Robert Azencott  

**一句话要点**：提出基于Fréchet映射的快速k均值聚类方法，以解决高维黎曼流形数据计算难题

**关键词**：黎曼流形聚类, Fréchet映射, SPD矩阵, k均值算法, 降维嵌入

## 3 点简述
- 核心问题：高维非欧几里得流形数据聚类存在计算复杂度高的问题
- 方法要点：使用p-Fréchet映射将流形数据嵌入低维欧几里得空间，应用标准k均值聚类
- 实验或效果：在SPD矩阵数据上，运行时间减少两个数量级，同时保持高聚类精度

## 摘要（原文）

> We introduce a novel, efficient framework for clustering data on high-dimensional, non-Euclidean manifolds that overcomes the computational challenges associated with standard intrinsic methods. The key innovation is the use of the $p$-Fréchet map $F^p : \mathcal{M} \to \mathbb{R}^\ell$ -- defined on a generic metric space $\mathcal{M}$ -- which embeds the manifold data into a lower-dimensional Euclidean space $\mathbb{R}^\ell$ using a set of reference points $\{r_i\}_{i=1}^\ell$, $r_i \in \mathcal{M}$. Once embedded, we can efficiently and accurately apply standard Euclidean clustering techniques such as k-means. We rigorously analyze the mathematical properties of $F^p$ in the Euclidean space and the challenging manifold of $n \times n$ symmetric positive definite matrices $\mathit{SPD}(n)$. Extensive numerical experiments using synthetic and real $\mathit{SPD}(n)$ data demonstrate significant performance gains: our method reduces runtime by up to two orders of magnitude compared to intrinsic manifold-based approaches, all while maintaining high clustering accuracy, including scenarios where existing alternative methods struggle or fail.

