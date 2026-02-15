---
layout: default
title: UMAP Is Spectral Clustering on the Fuzzy Nearest-Neighbor Graph
---

# UMAP Is Spectral Clustering on the Fuzzy Nearest-Neighbor Graph
**arXiv**：[2602.11662v1](https://arxiv.org/abs/2602.11662) · [PDF](https://arxiv.org/pdf/2602.11662.pdf)  
**作者**：Yang Yang  

**一句话要点**：证明UMAP等价于模糊k近邻图上的谱聚类，统一降维与聚类框架

**关键词**：UMAP, 谱聚类, 降维可视化, 对比学习, 模糊近邻图, 理论证明

## 3 点简述
- 核心问题：UMAP与经典谱方法的关系不明确，缺乏形式化证明
- 方法要点：通过三步证明UMAP优化目标等价于谱聚类，适用于高斯核和柯西核
- 实验或效果：理论统一UMAP、对比学习和谱聚类，解释其行为经验观察

## 摘要（原文）

> UMAP (Uniform Manifold Approximation and Projection) is among the most widely used algorithms for non linear dimensionality reduction and data visualisation. Despite its popularity, and despite being presented through the lens of algebraic topology, the exact relationship between UMAP and classical spectral methods has remained informal. In this work, we prove that UMAP performs spectral clustering on the fuzzy k nearest neighbour graph. Our proof proceeds in three steps: (1) we show that UMAP's stochastic optimisation with negative sampling is a contrastive learning objective on the similarity graph; (2) we invoke the result of HaoChen et al. [8], establishing that contrastive learning on a similarity graph is equivalent to spectral clustering; and (3) we verify that UMAP's spectral initialisation computes the exact linear solution to this spectral problem. The equivalence is exact for Gaussian kernels, and holds as a first order approximation for UMAP's default Cauchy type kernel. Our result unifies UMAP, contrastive learning, and spectral clustering under a single framework, and provides theoretical grounding for several empirical observations about UMAP's behaviour.

