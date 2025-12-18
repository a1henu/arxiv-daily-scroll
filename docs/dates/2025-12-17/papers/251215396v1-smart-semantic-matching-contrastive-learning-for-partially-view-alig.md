---
layout: default
title: SMART: Semantic Matching Contrastive Learning for Partially View-Aligned Clustering
---

# SMART: Semantic Matching Contrastive Learning for Partially View-Aligned Clustering
**arXiv**：[2512.15396v1](https://arxiv.org/abs/2512.15396) · [PDF](https://arxiv.org/pdf/2512.15396.pdf)  
**作者**：Liang Peng, Yixuan Ye, Cheng Liu, Hangjun Che, Fei Wang, Zhiwen Yu, Si Wu, Hau-San Wong  

**一句话要点**：提出SMART模型以解决部分视图对齐聚类中的跨视图分布偏移问题

**关键词**：部分视图对齐聚类, 语义匹配, 对比学习, 跨视图分布偏移, 多视图聚类

## 3 点简述
- 核心问题：部分视图对齐聚类中，跨视图分布偏移导致语义匹配不准确，影响聚类效果
- 方法要点：通过语义匹配对比学习，缓解分布偏移，利用对齐和未对齐数据的语义关系
- 实验或效果：在八个基准数据集上验证，SMART优于现有方法，提升聚类性能

## 摘要（原文）

> Multi-view clustering has been empirically shown to improve learning performance by leveraging the inherent complementary information across multiple views of data. However, in real-world scenarios, collecting strictly aligned views is challenging, and learning from both aligned and unaligned data becomes a more practical solution. Partially View-aligned Clustering aims to learn correspondences between misaligned view samples to better exploit the potential consistency and complementarity across views, including both aligned and unaligned data. However, most existing PVC methods fail to leverage unaligned data to capture the shared semantics among samples from the same cluster. Moreover, the inherent heterogeneity of multi-view data induces distributional shifts in representations, leading to inaccuracies in establishing meaningful correspondences between cross-view latent features and, consequently, impairing learning effectiveness. To address these challenges, we propose a Semantic MAtching contRasTive learning model (SMART) for PVC. The main idea of our approach is to alleviate the influence of cross-view distributional shifts, thereby facilitating semantic matching contrastive learning to fully exploit semantic relationships in both aligned and unaligned data. Extensive experiments on eight benchmark datasets demonstrate that our method consistently outperforms existing approaches on the PVC problem.

