---
layout: default
title: Divide and Predict: An Architecture for Input Space Partitioning and Enhanced Accuracy
---

# Divide and Predict: An Architecture for Input Space Partitioning and Enhanced Accuracy
**arXiv**：[2603.08649v1](https://arxiv.org/abs/2603.08649) · [PDF](https://arxiv.org/pdf/2603.08649.pdf)  
**作者**：Fenix W. Huang, Henning S. Mortveit, Christian M. Reidys  

**一句话要点**：提出基于方差的数据异质性度量，通过分区训练提升监督学习准确性

**关键词**：数据异质性度量, 监督学习, 数据分区, 方差分析, 训练数据净化, 块训练

## 3 点简述
- 核心问题：量化训练数据异质性，识别混合分布样本以优化模型训练
- 方法要点：定义方差度量捕获数据异质性，证明数据支持分区，提出基于方差的数据净化与块训练
- 实验或效果：在EMNIST图像和合成数据上验证方差与异质性关联，分区训练显著提高测试准确率

## 摘要（原文）

> In this article the authors develop an intrinsic measure for quantifying heterogeneity in training data for supervised learning. This measure is the variance of a random variable which factors through the influences of pairs of training points. The variance is shown to capture data heterogeneity and can thus be used to assess if a sample is a mixture of distributions. The authors prove that the data itself contains key information that supports a partitioning into blocks. Several proof of concept studies are provided that quantify the connection between variance and heterogeneity for EMNIST image data and synthetic data. The authors establish that variance is maximal for equal mixes of distributions, and detail how variance-based data purification followed by conventional training over blocks can lead to significant increases in test accuracy.

