---
layout: default
title: Differentiable Tripartite Modularity for Clustering Heterogeneous Graphs
---

# Differentiable Tripartite Modularity for Clustering Heterogeneous Graphs
**arXiv**：[2602.09864v1](https://arxiv.org/abs/2602.09864) · [PDF](https://arxiv.org/pdf/2602.09864.pdf)  
**作者**：Benoît Hurpeau  

**一句话要点**：提出可微分三方模块度以聚类异构图，解决高阶关系结构社区检测问题。

**关键词**：异构图聚类, 可微分模块度, 三方图, 社区检测, 图神经网络, 高阶关系

## 3 点简述
- 核心问题：异构图聚类挑战在于处理超过两种实体类型的高阶关系，现有方法难以扩展。
- 方法要点：引入三方模块度的可微分公式，基于加权共路径定义社区结构，避免显式构建稠密张量。
- 实验或效果：在大规模城市地籍数据上验证，展示稳健收敛和空间一致分区，支持端到端优化。

## 摘要（原文）

> Clustering heterogeneous relational data remains a central challenge in graph learning, particularly when interactions involve more than two types of entities. While differentiable modularity objectives such as DMoN have enabled end-to-end community detection on homogeneous and bipartite graphs, extending these approaches to higher-order relational structures remains non-trivial.
>   In this work, we introduce a differentiable formulation of tripartite modularity for graphs composed of three node types connected through mediated interactions. Community structure is defined in terms of weighted co-paths across the tripartite graph, together with an exact factorized computation that avoids the explicit construction of dense third-order tensors. A structural normalization at pivot nodes is introduced to control extreme degree heterogeneity and ensure stable optimization.
>   The resulting objective can be optimized jointly with a graph neural network in an end-to-end manner, while retaining linear complexity in the number of edges. We validate the proposed framework on large-scale urban cadastral data, where it exhibits robust convergence behavior and produces spatially coherent partitions. These results highlight differentiable tripartite modularity as a generic methodological building block for unsupervised clustering of heterogeneous graphs.

