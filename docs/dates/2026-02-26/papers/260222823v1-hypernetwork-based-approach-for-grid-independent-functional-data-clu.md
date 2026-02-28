---
layout: default
title: Hypernetwork-based approach for grid-independent functional data clustering
---

# Hypernetwork-based approach for grid-independent functional data clustering
**arXiv**：[2602.22823v1](https://arxiv.org/abs/2602.22823) · [PDF](https://arxiv.org/pdf/2602.22823.pdf)  
**作者**：Anirudh Thatipelli, Ali Siahkoohi  

**一句话要点**：提出基于超网络的框架，用于实现网格无关的函数数据聚类

**关键词**：函数数据聚类, 超网络, 隐式神经表示, 网格无关表示, 自编码架构, 高维数据

## 3 点简述
- 核心问题：现有函数聚类方法依赖采样网格，导致聚类结果受分辨率、密度或预处理影响
- 方法要点：使用超网络编码坐标-值对，通过隐式神经表示解码，生成与网格无关的紧凑向量表示
- 实验或效果：在合成和真实高维数据上展示竞争性聚类性能，对采样分辨率变化鲁棒，可泛化到未见分辨率

## 摘要（原文）

> Functional data clustering is concerned with grouping functions that share similar structure, yet most existing methods implicitly operate on sampled grids, causing cluster assignments to depend on resolution, sampling density, or preprocessing choices rather than on the underlying functions themselves. To address this limitation, we introduce a framework that maps discretized function observations -- at arbitrary resolution and on arbitrary grids -- into a fixed-dimensional vector space via an auto-encoding architecture. The encoder is a hypernetwork that maps coordinate-value pairs to the weight space of an implicit neural representation (INR), which serves as the decoder. Because INRs represent functions with very few parameters, this design yields compact representations that are decoupled from the sampling grid, while the hypernetwork amortizes weight prediction across the dataset. Clustering is then performed in this weight space using standard algorithms, making the approach agnostic to both the discretization and the choice of clustering method. By means of synthetic and real-world experiments in high-dimensional settings, we demonstrate competitive clustering performance that is robust to changes in sampling resolution -- including generalization to resolutions not seen during training.

