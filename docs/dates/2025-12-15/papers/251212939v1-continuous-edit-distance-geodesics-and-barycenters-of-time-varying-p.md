---
layout: default
title: Continuous Edit Distance, Geodesics and Barycenters of Time-varying Persistence Diagrams
---

# Continuous Edit Distance, Geodesics and Barycenters of Time-varying Persistence Diagrams
**arXiv**：[2512.12939v1](https://arxiv.org/abs/2512.12939) · [PDF](https://arxiv.org/pdf/2512.12939.pdf)  
**作者**：Sebastien Tchitchek, Mohamed Kissi, Julien Tierny  

**一句话要点**：提出连续编辑距离以分析时变持久图，支持对齐、比较和聚类。

**关键词**：时变持久图, 连续编辑距离, 测地线, 重心计算, 聚类分析, 拓扑数据分析

## 3 点简述
- 核心问题：时变持久图缺乏原则性距离，难以直接进行对齐和平均。
- 方法要点：引入连续编辑距离，结合局部替换成本和惩罚删除/插入，提供显式测地线构造。
- 实验或效果：在真实数据集上，聚类性能优于标准弹性差异，基于重心的方法提升分类结果。

## 摘要（原文）

> We introduce the Continuous Edit Distance (CED), a geodesic and elastic distance for time-varying persistence diagrams (TVPDs). The CED extends edit-distance ideas to TVPDs by combining local substitution costs with penalized deletions/insertions, controlled by two parameters: \(α\) (trade-off between temporal misalignment and diagram discrepancy) and \(β\) (gap penalty). We also provide an explicit construction of CED-geodesics. Building on these ingredients, we present two practical barycenter solvers, one stochastic and one greedy, that monotonically decrease the CED Frechet energy. Empirically, the CED is robust to additive perturbations (both temporal and spatial), recovers temporal shifts, and supports temporal pattern search. On real-life datasets, the CED achieves clustering performance comparable or better than standard elastic dissimilarities, while our clustering based on CED-barycenters yields superior classification results. Overall, the CED equips TVPD analysis with a principled distance, interpretable geodesics, and practical barycenters, enabling alignment, comparison, averaging, and clustering directly in the space of TVPDs. A C++ implementation is provided for reproducibility at the following address https://github.com/sebastien-tchitchek/ContinuousEditDistance.

