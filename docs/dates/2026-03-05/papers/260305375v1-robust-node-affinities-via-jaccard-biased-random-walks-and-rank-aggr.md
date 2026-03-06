---
layout: default
title: Robust Node Affinities via Jaccard-Biased Random Walks and Rank Aggregation
---

# Robust Node Affinities via Jaccard-Biased Random Walks and Rank Aggregation
**arXiv**：[2603.05375v1](https://arxiv.org/abs/2603.05375) · [PDF](https://arxiv.org/pdf/2603.05375.pdf)  
**作者**：Bastian Pfeifer, Michael G. Schimek  

**一句话要点**：提出TopKGraphs方法，基于Jaccard偏置随机游走和鲁棒排序聚合，用于网络分析和机器学习中的节点相似性估计。

**关键词**：节点相似性估计, 随机游走, Jaccard相似性, 鲁棒排序聚合, 网络分析, 机器学习

## 3 点简述
- 核心问题：网络分析中节点相似性估计是基础任务，应用于聚类、社区检测等场景。
- 方法要点：使用起始节点锚定的随机游走，基于Jaccard相似性偏置转移，通过鲁棒排序聚合构建可解释的节点亲和矩阵。
- 实验或效果：在合成图、表格数据k近邻图和蛋白质相互作用网络中，TopKGraphs表现优于或媲美标准相似性度量、扩散方法和嵌入方法。

## 摘要（原文）

> Estimating node similarity is a fundamental task in network analysis and graph-based machine learning, with applications in clustering, community detection, classification, and recommendation. We propose TopKGraphs, a method based on start-node-anchored random walks that bias transitions toward nodes with structurally similar neighborhoods, measured via Jaccard similarity. Rather than computing stationary distributions, walks are treated as stochastic neighborhood samplers, producing partial node rankings that are aggregated using robust rank aggregation to construct interpretable node-to-node affinity matrices. TopKGraphs provides a non-parametric, interpretable, and general-purpose representation of node similarity that can be applied in both network analysis and machine learning workflows. We evaluate the method on synthetic graphs (stochastic block models, Lancichinetti-Fortunato-Radicchi benchmark graphs), k-nearest-neighbor graphs from tabular datasets, and a curated high-confidence protein-protein interaction network. Across all scenarios, TopKGraphs achieves competitive or superior performance compared to standard similarity measures (Jaccard, Dice), a diffusion-based method (personalized PageRank), and an embedding-based approach (Node2Vec), demonstrating robustness in sparse, noisy, or heterogeneous networks. These results suggest that TopKGraphs is a versatile and interpretable tool for bridging simple local similarity measures with more complex embedding-based approaches, facilitating both data mining and network analysis applications.

