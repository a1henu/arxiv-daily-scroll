---
layout: default
title: Persistent Multiscale Density-based Clustering
---

# Persistent Multiscale Density-based Clustering
**arXiv**：[2512.16558v1](https://arxiv.org/abs/2512.16558) · [PDF](https://arxiv.org/pdf/2512.16558.pdf)  
**作者**：Daniël Bot, Leland McInnes, Jan Aerts  

**一句话要点**：提出PLSCAN算法以解决密度聚类中参数选择困难的问题

**关键词**：密度聚类, 参数选择, 尺度空间聚类, HDBSCAN*, 聚类稳定性, 计算效率

## 3 点简述
- 核心问题：密度聚类算法如DBSCAN和HDBSCAN*需预设参数，缺乏先验知识时选择困难
- 方法要点：PLSCAN基于尺度空间聚类原理，高效识别HDBSCAN*稳定簇的最小尺寸
- 实验或效果：在真实数据集上，PLSCAN平均ARI更高，对参数变化更不敏感，计算成本与k-Means和HDBSCAN*竞争

## 摘要（原文）

> Clustering is a cornerstone of modern data analysis. Detecting clusters in exploratory data analyses (EDA) requires algorithms that make few assumptions about the data. Density-based clustering algorithms are particularly well-suited for EDA because they describe high-density regions, assuming only that a density exists. Applying density-based clustering algorithms in practice, however, requires selecting appropriate hyperparameters, which is difficult without prior knowledge of the data distribution. For example, DBSCAN requires selecting a density threshold, and HDBSCAN* relies on a minimum cluster size parameter. In this work, we propose Persistent Leaves Spatial Clustering for Applications with Noise (PLSCAN). This novel density-based clustering algorithm efficiently identifies all minimum cluster sizes for which HDBSCAN* produces stable (leaf) clusters. PLSCAN applies scale-space clustering principles and is equivalent to persistent homology on a novel metric space. We compare its performance to HDBSCAN* on several real-world datasets, demonstrating that it achieves a higher average ARI and is less sensitive to changes in the number of mutual reachability neighbours. Additionally, we compare PLSCAN's computational costs to k-Means, demonstrating competitive run-times on low-dimensional datasets. At higher dimensions, run times scale more similarly to HDBSCAN*.

