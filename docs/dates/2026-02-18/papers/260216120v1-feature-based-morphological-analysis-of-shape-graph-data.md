---
layout: default
title: Feature-based morphological analysis of shape graph data
---

# Feature-based morphological analysis of shape graph data
**arXiv**：[2602.16120v1](https://arxiv.org/abs/2602.16120) · [PDF](https://arxiv.org/pdf/2602.16120.pdf)  
**作者**：Murad Hossen, Demetrio Labate, Nicolas Charon  

**一句话要点**：提出基于特征提取的计算流程，用于形状图数据的形态统计分析。

**关键词**：形状图分析, 特征提取, 形态统计, 几何网络, 拓扑特征

## 3 点简述
- 核心问题：分析嵌入2D/3D空间的形状图数据，兼顾连接结构和分支几何差异。
- 方法要点：提取拓扑、几何和方向特征集，满足关键不变性，用于比较、聚类和分类。
- 实验或效果：在道路网络、神经元追踪等真实数据集上评估，与多种方法对比验证有效性。

## 摘要（原文）

> This paper introduces and demonstrates a computational pipeline for the statistical analysis of shape graph datasets, namely geometric networks embedded in 2D or 3D spaces. Unlike traditional abstract graphs, our purpose is not only to retrieve and distinguish variations in the connectivity structure of the data but also geometric differences of the network branches. Our proposed approach relies on the extraction of a specifically curated and explicit set of topological, geometric and directional features, designed to satisfy key invariance properties. We leverage the resulting feature representation for tasks such as group comparison, clustering and classification on cohorts of shape graphs. The effectiveness of this representation is evaluated on several real-world datasets including urban road/street networks, neuronal traces and astrocyte imaging. These results are benchmarked against several alternative methods, both feature-based and not.

