---
layout: default
title: The Catastrophic Failure of The k-Means Algorithm in High Dimensions, and How Hartigan's Algorithm Avoids It
---

# The Catastrophic Failure of The k-Means Algorithm in High Dimensions, and How Hartigan's Algorithm Avoids It
**arXiv**：[2602.09936v1](https://arxiv.org/abs/2602.09936) · [PDF](https://arxiv.org/pdf/2602.09936.pdf)  
**作者**：Roy R. Lederman, David Silva-Sánchez, Ziling Chen, Gilles Mordant, Amnon Balanov, Tamir Bendory  

**一句话要点**：揭示高维噪声下k-means算法灾难性失效，证明Hartigan算法可避免此问题

**关键词**：k-means聚类, 高维数据分析, 算法稳定性, 聚类算法比较, 噪声鲁棒性

## 3 点简述
- Lloyd的k-means算法在高维高噪声场景下会灾难性失效，几乎所有数据划分都成为不动点
- Hartigan的k-means算法不会出现这种病理现象，能有效避免灾难性失效
- 理论分析解释了k-means在高维数据中常遇到的实证困难，对比了两种算法的差异

## 摘要（原文）

> Lloyd's k-means algorithm is one of the most widely used clustering methods. We prove that in high-dimensional, high-noise settings, the algorithm exhibits catastrophic failure: with high probability, essentially every partition of the data is a fixed point. Consequently, Lloyd's algorithm simply returns its initial partition - even when the underlying clusters are trivially recoverable by other methods. In contrast, we prove that Hartigan's k-means algorithm does not exhibit this pathology. Our results show the stark difference between these algorithms and offer a theoretical explanation for the empirical difficulties often observed with k-means in high dimensions.

