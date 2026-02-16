---
layout: default
title: Random Forests as Statistical Procedures: Design, Variance, and Dependence
---

# Random Forests as Statistical Procedures: Design, Variance, and Dependence
**arXiv**：[2602.13104v1](https://arxiv.org/abs/2602.13104) · [PDF](https://arxiv.org/pdf/2602.13104.pdf)  
**作者**：Nathaniel S. O'Connell  

**一句话要点**：提出随机森林的有限样本设计框架，解析预测方差与树间依赖机制。

**关键词**：随机森林, 统计设计, 方差分解, 树间依赖, 有限样本分析, 预测稳定性

## 3 点简述
- 核心问题：随机森林通常被算法化描述，缺乏固定数据集上的统计设计视角。
- 方法要点：将每棵树建模为随机化条件回归函数，推导预测方差的精确分解公式。
- 实验或效果：揭示训练数据重用和自适应划分对齐导致协方差下限，限制预测稳定性。

## 摘要（原文）

> Random forests are widely used prediction procedures, yet are typically described algorithmically rather than as statistical designs acting on a fixed dataset. We develop a finite-sample, design-based formulation of random forests in which each tree is an explicit randomized conditional regression function. This perspective yields an exact variance identity for the forest predictor that separates finite-aggregation variability from a structural dependence term that persists even under infinite aggregation. We further decompose both single-tree dispersion and inter-tree covariance using the laws of total variance and covariance, isolating two fundamental design mechanisms-reuse of training observations and alignment of data-adaptive partitions. These mechanisms induce a strict covariance floor, demonstrating that predictive variability cannot be eliminated by increasing the number of trees alone. The resulting framework clarifies how resampling, feature-level randomization, and split selection govern resolution, tree variability, and dependence, and establishes random forests as explicit finite-sample statistical designs whose behavior is determined by their underlying randomized construction.

