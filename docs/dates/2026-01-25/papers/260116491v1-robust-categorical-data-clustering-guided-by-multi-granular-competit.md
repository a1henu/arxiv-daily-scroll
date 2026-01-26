---
layout: default
title: Robust Categorical Data Clustering Guided by Multi-Granular Competitive Learning
---

# Robust Categorical Data Clustering Guided by Multi-Granular Competitive Learning
**arXiv**：[2601.16491v1](https://arxiv.org/abs/2601.16491) · [PDF](https://arxiv.org/pdf/2601.16491.pdf)  
**作者**：Shenghong Cai, Yiqun Zhang, Xiaopeng Luo, Yiu-Ming Cheung, Hong Jia, Peng Liu  

**一句话要点**：提出MCDC方法以解决分类数据聚类中的嵌套粒度簇效应问题

**关键词**：分类数据聚类, 多粒度学习, 竞争学习, 鲁棒聚类, 大规模数据处理

## 3 点简述
- 核心问题：分类数据因定性值导致距离空间定义困难，存在嵌套粒度簇效应
- 方法要点：设计MGCPL算法实现多粒度竞争惩罚学习，结合CAME策略进行编码与聚类
- 实验或效果：在多个真实数据集上优于现有方法，具有线性时间复杂度和高鲁棒性

## 摘要（原文）

> Data set composed of categorical features is very common in big data analysis tasks. Since categorical features are usually with a limited number of qualitative possible values, the nested granular cluster effect is prevalent in the implicit discrete distance space of categorical data. That is, data objects frequently overlap in space or subspace to form small compact clusters, and similar small clusters often form larger clusters. However, the distance space cannot be well-defined like the Euclidean distance due to the qualitative categorical data values, which brings great challenges to the cluster analysis of categorical data. In view of this, we design a Multi-Granular Competitive Penalization Learning (MGCPL) algorithm to allow potential clusters to interactively tune themselves and converge in stages with different numbers of naturally compact clusters. To leverage MGCPL, we also propose a Cluster Aggregation strategy based on MGCPL Encoding (CAME) to first encode the data objects according to the learned multi-granular distributions, and then perform final clustering on the embeddings. It turns out that the proposed MGCPL-guided Categorical Data Clustering (MCDC) approach is competent in automatically exploring the nested distribution of multi-granular clusters and highly robust to categorical data sets from various domains. Benefiting from its linear time complexity, MCDC is scalable to large-scale data sets and promising in pre-partitioning data sets or compute nodes for boosting distributed computing. Extensive experiments with statistical evidence demonstrate its superiority compared to state-of-the-art counterparts on various real public data sets.

