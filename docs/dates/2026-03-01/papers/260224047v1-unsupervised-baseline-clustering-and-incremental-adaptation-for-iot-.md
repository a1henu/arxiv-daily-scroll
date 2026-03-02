---
layout: default
title: Unsupervised Baseline Clustering and Incremental Adaptation for IoT Device Traffic Profiling
---

# Unsupervised Baseline Clustering and Incremental Adaptation for IoT Device Traffic Profiling
**arXiv**：[2602.24047v1](https://arxiv.org/abs/2602.24047) · [PDF](https://arxiv.org/pdf/2602.24047.pdf)  
**作者**：Sean M. Alderman, John D. Hastings  

**一句话要点**：提出基于流特征的两阶段无监督管道，用于物联网设备流量画像和增量模型更新

**关键词**：物联网设备流量画像, 无监督聚类, 增量模型更新, 密度聚类, 流式聚类, 流量演变适应

## 3 点简述
- 核心问题：物联网设备增长和异构性导致静态识别模型在流量演变时性能下降
- 方法要点：使用密度聚类进行基线画像，并评估流式聚类方法进行增量适应
- 实验或效果：基线聚类在Deakin数据集上NMI达0.78，增量适应中BIRCH更新快但存在准确度权衡

## 摘要（原文）

> The growth and heterogeneity of IoT devices create security challenges where static identification models can degrade as traffic evolves. This paper presents a two-stage, flow-feature-based pipeline for unsupervised IoT device traffic profiling and incremental model updating, evaluated on selected long-duration captures from the Deakin IoT dataset. For baseline profiling, density-based clustering (DBSCAN) isolates a substantial outlier portion of the data and produces the strongest alignment with ground-truth device labels among tested classical methods (NMI 0.78), outperforming centroid-based clustering on cluster purity. For incremental adaptation, we evaluate stream-oriented clustering approaches and find that BIRCH supports efficient updates (0.13 seconds per update) and forms comparatively coherent clusters for a held-out novel device (purity 0.87), but with limited capture of novel traffic (share 0.72) and a measurable trade-off in known-device accuracy after adaptation (0.71). Overall, the results highlight a practical trade-off between high-purity static profiling and the flexibility of incremental clustering for evolving IoT environments.

