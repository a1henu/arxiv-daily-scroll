---
layout: default
title: An Improved and Generalised Analysis for Spectral Clustering
---

# An Improved and Generalised Analysis for Spectral Clustering
**arXiv**：[2511.23261v1](https://arxiv.org/abs/2511.23261) · [PDF](https://arxiv.org/pdf/2511.23261.pdf)  
**作者**：George Tyler, Luca Zanetti  

**一句话要点**：改进谱聚类理论分析，扩展至有向图与多尺度聚类场景

**关键词**：谱聚类, 图划分, 特征值分析, 有向图, 多尺度聚类, 理论分析

## 3 点简述
- 核心问题：传统谱聚类分析未涵盖多尺度聚类层次等场景，理论通用性有限
- 方法要点：基于特征值分组分离条件，证明谱聚类有效性，并推广至有向图的Hermitian表示
- 实验或效果：在合成与真实数据集上验证理论预测准确性，应用于生态网络营养级分析

## 摘要（原文）

> We revisit the theoretical performances of Spectral Clustering, a classical algorithm for graph partitioning that relies on the eigenvectors of a matrix representation of the graph. Informally, we show that Spectral Clustering works well as long as the smallest eigenvalues appear in groups well separated from the rest of the matrix representation's spectrum. This arises, for example, whenever there exists a hierarchy of clusters at different scales, a regime not captured by previous analyses. Our results are very general and can be applied beyond the traditional graph Laplacian. In particular, we study Hermitian representations of digraphs and show Spectral Clustering can recover partitions where edges between clusters are oriented mostly in the same direction. This has applications in, for example, the analysis of trophic levels in ecological networks. We demonstrate that our results accurately predict the performances of Spectral Clustering on synthetic and real-world data sets.

