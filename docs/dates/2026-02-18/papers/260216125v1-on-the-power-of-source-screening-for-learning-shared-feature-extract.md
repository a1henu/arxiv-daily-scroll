---
layout: default
title: On the Power of Source Screening for Learning Shared Feature Extractors
---

# On the Power of Source Screening for Learning Shared Feature Extractors
**arXiv**：[2602.16125v1](https://arxiv.org/abs/2602.16125) · [PDF](https://arxiv.org/pdf/2602.16125.pdf)  
**作者**：Leo, Wang, Connor Mclaughlin, Lili Su  

**一句话要点**：提出源筛选方法以优化共享特征提取器学习，在线性设置下实现统计最优子空间估计。

**关键词**：共享表示学习, 源筛选, 子空间估计, 线性模型, 极小极大最优性, 异质数据源

## 3 点简述
- 核心问题：传统方法包含所有数据源可能因低相关性或低质量源阻碍共享表示学习。
- 方法要点：在线性设置中，通过筛选信息性子集，丢弃部分数据仍可达到极小极大最优性。
- 实验或效果：理论分析和合成与真实数据集验证了算法和启发式方法的有效性。

## 摘要（原文）

> Learning with shared representation is widely recognized as an effective way to separate commonalities from heterogeneity across various heterogeneous sources. Most existing work includes all related data sources via simultaneously training a common feature extractor and source-specific heads. It is well understood that data sources with low relevance or poor quality may hinder representation learning. In this paper, we further dive into the question of which data sources should be learned jointly by focusing on the traditionally deemed ``good'' collection of sources, in which individual sources have similar relevance and qualities with respect to the true underlying common structure. Towards tractability, we focus on the linear setting where sources share a low-dimensional subspace. We find that source screening can play a central role in statistically optimal subspace estimation. We show that, for a broad class of problem instances, training on a carefully selected subset of sources suffices to achieve minimax optimality, even when a substantial portion of data is discarded. We formalize the notion of an informative subpopulation, develop algorithms and practical heuristics for identifying such subsets, and validate their effectiveness through both theoretical analysis and empirical evaluations on synthetic and real-world datasets.

