---
layout: default
title: Leveraging Cycle-Consistent Anchor Points for Self-Supervised RGB-D Registration
---

# Leveraging Cycle-Consistent Anchor Points for Self-Supervised RGB-D Registration
**arXiv**：[2510.14354v1](https://arxiv.org/abs/2510.14354) · [PDF](https://arxiv.org/pdf/2510.14354.pdf)  
**作者**：Siddharth Tourani, Jayaram Reddy, Sarvesh Thakur, K Madhava Krishna, Muhammad Haris Khan, N Dinesh Reddy  

**一句话要点**：提出基于循环一致锚点的自监督RGB-D配准方法，提升场景几何推理精度。

**关键词**：RGB-D配准, 自监督学习, 循环一致性, 关键点检测, 变换同步, 多视图融合

## 3 点简述
- 核心问题：如何利用未标记RGB-D数据进行场景几何推理，避免依赖几何或特征相似性。
- 方法要点：使用循环一致关键点增强空间一致性，结合GRU与变换同步融合历史与多视图数据。
- 实验或效果：在ScanNet和3DMatch上超越先前自监督方法，部分优于旧有监督方法。

## 摘要（原文）

> With the rise in consumer depth cameras, a wealth of unlabeled RGB-D data has
> become available. This prompts the question of how to utilize this data for
> geometric reasoning of scenes. While many RGB-D registration meth- ods rely on
> geometric and feature-based similarity, we take a different approach. We use
> cycle-consistent keypoints as salient points to enforce spatial coherence
> constraints during matching, improving correspondence accuracy. Additionally,
> we introduce a novel pose block that combines a GRU recurrent unit with
> transformation synchronization, blending historical and multi-view data. Our
> approach surpasses previous self- supervised registration methods on ScanNet
> and 3DMatch, even outperforming some older supervised methods. We also
> integrate our components into existing methods, showing their effectiveness.

