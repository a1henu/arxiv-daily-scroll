---
layout: default
title: MCGI: Manifold-Consistent Graph Indexing for Billion-Scale Disk-Resident Vector Search
---

# MCGI: Manifold-Consistent Graph Indexing for Billion-Scale Disk-Resident Vector Search
**arXiv**：[2601.01930v1](https://arxiv.org/abs/2601.01930) · [PDF](https://arxiv.org/pdf/2601.01930.pdf)  
**作者**：Dongfang Zhao  

**一句话要点**：提出MCGI以解决高维向量搜索中的欧几里得-测地线不匹配问题，实现磁盘驻留索引。

**关键词**：高维向量搜索, 图索引, 局部本征维度, 磁盘驻留索引, 近似最近邻搜索

## 3 点简述
- 核心问题：图近似最近邻搜索在高维空间因欧几里得-测地线不匹配导致性能下降。
- 方法要点：利用局部本征维度动态调整搜索策略，适应数据内在几何结构。
- 实验或效果：在GIST1M上实现5.8倍吞吐提升，SIFT1B上降低3倍查询延迟。

## 摘要（原文）

> Graph-based Approximate Nearest Neighbor (ANN) search often suffers from performance degradation in high-dimensional spaces due to the ``Euclidean-Geodesic mismatch,'' where greedy routing diverges from the underlying data manifold. To address this, we propose Manifold-Consistent Graph Indexing (MCGI), a geometry-aware and disk-resident indexing method that leverages Local Intrinsic Dimensionality (LID) to dynamically adapt search strategies to the data's intrinsic geometry. Unlike standard algorithms that treat dimensions uniformly, MCGI modulates its beam search budget based on in situ geometric analysis, eliminating dependency on static hyperparameters. Theoretical analysis confirms that MCGI enables improved approximation guarantees by preserving manifold-consistent topological connectivity. Empirically, MCGI achieves 5.8$\times$ higher throughput at 95\% recall on high-dimensional GIST1M compared to state-of-the-art DiskANN. On the billion-scale SIFT1B dataset, MCGI further validates its scalability by reducing high-recall query latency by 3$\times$, while maintaining performance parity on standard lower-dimensional datasets.

