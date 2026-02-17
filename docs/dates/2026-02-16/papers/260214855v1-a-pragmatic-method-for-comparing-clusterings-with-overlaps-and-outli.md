---
layout: default
title: A Pragmatic Method for Comparing Clusterings with Overlaps and Outliers
---

# A Pragmatic Method for Comparing Clusterings with Overlaps and Outliers
**arXiv**：[2602.14855v1](https://arxiv.org/abs/2602.14855) · [PDF](https://arxiv.org/pdf/2602.14855.pdf)  
**作者**：Ryan DeWolfe, Paweł Prałat, François Théberge  

**一句话要点**：提出一种实用相似度度量，用于比较包含重叠和异常值的聚类结果。

**关键词**：聚类比较, 重叠聚类, 异常值处理, 相似度度量, 无监督学习

## 3 点简述
- 核心问题：现有方法无法比较包含重叠聚类和异常值的聚类结果。
- 方法要点：定义一种相似度度量，具有多个理想性质，避免常见偏差。
- 实验或效果：通过实验验证该度量不受其他聚类比较方法常见偏差影响。

## 摘要（原文）

> Clustering algorithms are an essential part of the unsupervised data science ecosystem, and extrinsic evaluation of clustering algorithms requires a method for comparing the detected clustering to a ground truth clustering. In a general setting, the detected and ground truth clusterings may have outliers (objects belonging to no cluster), overlapping clusters (objects may belong to more than one cluster), or both, but methods for comparing these clusterings are currently undeveloped. In this note, we define a pragmatic similarity measure for comparing clusterings with overlaps and outliers, show that it has several desirable properties, and experimentally confirm that it is not subject to several common biases afflicting other clustering comparison measures.

