---
layout: default
title: kNN-Graph: An adaptive graph model for $k$-nearest neighbors
---

# kNN-Graph: An adaptive graph model for $k$-nearest neighbors
**arXiv**：[2601.16509v1](https://arxiv.org/abs/2601.16509) · [PDF](https://arxiv.org/pdf/2601.16509.pdf)  
**作者**：Jiaye Li, Gang Chen, Hang Xu, Shichao Zhang  

**一句话要点**：提出自适应图模型kNN-Graph，以解决kNN在大规模应用中推理速度与精度的权衡问题。

**关键词**：k近邻算法, 自适应图模型, HNSW图, 非参数分类, 推理加速, 大规模应用

## 3 点简述
- 核心问题：kNN算法在大规模应用中面临推理速度与分类精度的计算权衡，现有近似方法常牺牲精度且缺乏邻域大小自适应性。
- 方法要点：集成HNSW图与预计算投票机制，将邻居选择和权重计算完全转移至训练阶段，通过分层拓扑实现快速导航和自适应决策边界。
- 实验或效果：在六个数据集上对比八个基线，显著加速推理至实时性能，同时保持分类精度，提供可扩展的解决方案。

## 摘要（原文）

> The k-nearest neighbors (kNN) algorithm is a cornerstone of non-parametric classification in artificial intelligence, yet its deployment in large-scale applications is persistently constrained by the computational trade-off between inference speed and accuracy. Existing approximate nearest neighbor solutions accelerate retrieval but often degrade classification precision and lack adaptability in selecting the optimal neighborhood size (k). Here, we present an adaptive graph model that decouples inference latency from computational complexity. By integrating a Hierarchical Navigable Small World (HNSW) graph with a pre-computed voting mechanism, our framework completely transfers the computational burden of neighbor selection and weighting to the training phase. Within this topological structure, higher graph layers enable rapid navigation, while lower layers encode precise, node-specific decision boundaries with adaptive neighbor counts. Benchmarking against eight state-of-the-art baselines across six diverse datasets, we demonstrate that this architecture significantly accelerates inference speeds, achieving real-time performance, without compromising classification accuracy. These findings offer a scalable, robust solution to the long-standing inference bottleneck of kNN, establishing a new structural paradigm for graph-based nonparametric learning.

