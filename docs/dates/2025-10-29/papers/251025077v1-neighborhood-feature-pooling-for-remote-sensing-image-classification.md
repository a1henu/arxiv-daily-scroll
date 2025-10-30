---
layout: default
title: Neighborhood Feature Pooling for Remote Sensing Image Classification
---

# Neighborhood Feature Pooling for Remote Sensing Image Classification
**arXiv**：[2510.25077v1](https://arxiv.org/abs/2510.25077) · [PDF](https://arxiv.org/pdf/2510.25077.pdf)  
**作者**：Fahimeh Orvati Nia, Amirmohammad Mohammadi, Salim Al Kharsa, Pragati Naikare, Zigfried Hampel-Arias, Joshua Peeples  

**一句话要点**：提出邻域特征池化方法以提升遥感图像分类性能

**关键词**：遥感图像分类, 特征提取, 邻域特征池化, 卷积神经网络, 纹理分析

## 3 点简述
- 核心问题：遥感图像分类中纹理特征提取不足，影响模型性能。
- 方法要点：NFP层通过卷积捕获邻域输入关系，高效聚合局部相似特征。
- 实验或效果：NFP在多种数据集和架构中一致提升性能，参数开销小。

## 摘要（原文）

> In this work, we propose neighborhood feature pooling (NFP) as a novel
> texture feature extraction method for remote sensing image classification. The
> NFP layer captures relationships between neighboring inputs and efficiently
> aggregates local similarities across feature dimensions. Implemented using
> convolutional layers, NFP can be seamlessly integrated into any network.
> Results comparing the baseline models and the NFP method indicate that NFP
> consistently improves performance across diverse datasets and architectures
> while maintaining minimal parameter overhead.

