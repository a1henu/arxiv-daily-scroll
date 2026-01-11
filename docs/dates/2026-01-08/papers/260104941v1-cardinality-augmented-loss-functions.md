---
layout: default
title: Cardinality augmented loss functions
---

# Cardinality augmented loss functions
**arXiv**：[2601.04941v1](https://arxiv.org/abs/2601.04941) · [PDF](https://arxiv.org/pdf/2601.04941.pdf)  
**作者**：Miguel O'Malley  

**一句话要点**：提出基数增强损失函数以解决神经网络训练中的类别不平衡问题

**关键词**：类别不平衡, 损失函数, 基数不变量, 神经网络训练, 材料科学数据集

## 3 点简述
- 类别不平衡是神经网络训练中的常见问题，多数类可能主导训练，导致分类器性能偏向多数类。
- 方法基于现代数学中的基数类不变量（如magnitude和spread），通过评估度量空间的“有效多样性”来增强损失函数。
- 在人工不平衡数据集和真实世界材料科学数据集上实验，少数类性能显著提升，整体指标改善。

## 摘要（原文）

> Class imbalance is a common and pernicious issue for the training of neural networks. Often, an imbalanced majority class can dominate training to skew classifier performance towards the majority outcome. To address this problem we introduce cardinality augmented loss functions, derived from cardinality-like invariants in modern mathematics literature such as magnitude and the spread. These invariants enrich the concept of cardinality by evaluating the `effective diversity' of a metric space, and as such represent a natural solution to overly homogeneous training data. In this work, we establish a methodology for applying cardinality augmented loss functions in the training of neural networks and report results on both artificially imbalanced datasets as well as a real-world imbalanced material science dataset. We observe significant performance improvement among minority classes, as well as improvement in overall performance metrics.

