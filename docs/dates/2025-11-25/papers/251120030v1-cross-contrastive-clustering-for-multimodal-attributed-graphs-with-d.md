---
layout: default
title: Cross-Contrastive Clustering for Multimodal Attributed Graphs with Dual Graph Filtering
---

# Cross-Contrastive Clustering for Multimodal Attributed Graphs with Dual Graph Filtering
**arXiv**：[2511.20030v1](https://arxiv.org/abs/2511.20030) · [PDF](https://arxiv.org/pdf/2511.20030.pdf)  
**作者**：Haoran Zheng, Renchi Yang, Hongtao Wang, Jianliang Xu  

**一句话要点**：提出双图滤波与跨对比聚类以提升多模态属性图聚类性能

**关键词**：多模态属性图, 图聚类, 双图滤波, 跨对比学习, 特征去噪, 节点表示学习

## 3 点简述
- 多模态属性图中模态间相关性低且特征噪声强，现有方法聚类效果不佳
- 引入双图滤波进行特征去噪，并采用三跨对比学习优化节点表示
- 在八个基准数据集上实验，聚类质量显著优于现有先进方法

## 摘要（原文）

> Multimodal Attributed Graphs (MMAGs) are an expressive data model for representing the complex interconnections among entities that associate attributes from multiple data modalities (text, images, etc.). Clustering over such data finds numerous practical applications in real scenarios, including social community detection, medical data analytics, etc. However, as revealed by our empirical studies, existing multi-view clustering solutions largely rely on the high correlation between attributes across various views and overlook the unique characteristics (e.g., low modality-wise correlation and intense feature-wise noise) of multimodal attributes output by large pre-trained language and vision models in MMAGs, leading to suboptimal clustering performance.
>   Inspired by foregoing empirical observations and our theoretical analyses with graph signal processing, we propose the Dual Graph Filtering (DGF) scheme, which innovatively incorporates a feature-wise denoising component into node representation learning, thereby effectively overcoming the limitations of traditional graph filters adopted in the extant multi-view graph clustering approaches. On top of that, DGF includes a tri-cross contrastive training strategy that employs instance-level contrastive learning across modalities, neighborhoods, and communities for learning robust and discriminative node representations. Our comprehensive experiments on eight benchmark MMAG datasets exhibit that DGF is able to outperform a wide range of state-of-the-art baselines consistently and significantly in terms of clustering quality measured against ground-truth labels.

