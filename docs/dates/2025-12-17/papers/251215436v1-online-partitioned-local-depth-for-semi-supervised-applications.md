---
layout: default
title: Online Partitioned Local Depth for semi-supervised applications
---

# Online Partitioned Local Depth for semi-supervised applications
**arXiv**：[2512.15436v1](https://arxiv.org/abs/2512.15436) · [PDF](https://arxiv.org/pdf/2512.15436.pdf)  
**作者**：John D. Foley, Justin T. Lee  

**一句话要点**：提出在线分区局部深度算法以扩展半监督应用，支持在线异常检测和分类。

**关键词**：在线学习, 半监督学习, 异常检测, 凝聚网络, 医疗数据分析

## 3 点简述
- 核心问题：传统分区局部深度算法难以适应在线场景，如半监督预测。
- 方法要点：扩展算法为在线版本，通过预计算凝聚网络，新数据点扩展复杂度为O(n²)。
- 实验或效果：应用于医疗数据集，展示在线异常检测和半监督分类效果。

## 摘要（原文）

> We introduce an extension of the partitioned local depth (PaLD) algorithm that is adapted to online applications such as semi-supervised prediction. The new algorithm we present, online PaLD, is well-suited to situations where it is a possible to pre-compute a cohesion network from a reference dataset. After $O(n^3)$ steps to construct a queryable data structure, online PaLD can extend the cohesion network to a new data point in $O(n^2)$ time. Our approach complements previous speed up approaches based on approximation and parallelism. For illustrations, we present applications to online anomaly detection and semi-supervised classification for health-care datasets.

