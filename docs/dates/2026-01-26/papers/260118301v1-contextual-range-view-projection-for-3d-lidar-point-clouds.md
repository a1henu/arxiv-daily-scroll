---
layout: default
title: Contextual Range-View Projection for 3D LiDAR Point Clouds
---

# Contextual Range-View Projection for 3D LiDAR Point Clouds
**arXiv**：[2601.18301v1](https://arxiv.org/abs/2601.18301) · [PDF](https://arxiv.org/pdf/2601.18301.pdf)  
**作者**：Seyedali Mousavi, Seyedhamidreza Mousavi, Masoud Daneshtalab  

**一句话要点**：提出上下文感知的投影方法以解决LiDAR点云投影中的信息丢失问题

**关键词**：LiDAR点云处理, 范围视图投影, 上下文感知, 实例分割, 语义分割, 深度学习

## 3 点简述
- 核心问题：现有LiDAR点云投影方法因深度优先选择导致语义和实例信息丢失
- 方法要点：引入基于实例中心距离和类别权重的投影机制CAP和CWAP
- 实验或效果：在SemanticKITTI数据集上，CAP提升mIoU达3.1%，CWAP可针对性增强特定类别性能

## 摘要（原文）

> Range-view projection provides an efficient method for transforming 3D LiDAR point clouds into 2D range image representations, enabling effective processing with 2D deep learning models. However, a major challenge in this projection is the many-to-one conflict, where multiple 3D points are mapped onto the same pixel in the range image, requiring a selection strategy. Existing approaches typically retain the point with the smallest depth (closest to the LiDAR), disregarding semantic relevance and object structure, which leads to the loss of important contextual information. In this paper, we extend the depth-based selection rule by incorporating contextual information from both instance centers and class labels, introducing two mechanisms: \textit{Centerness-Aware Projection (CAP)} and \textit{Class-Weighted-Aware Projection (CWAP)}. In CAP, point depths are adjusted according to their distance from the instance center, thereby prioritizing central instance points over noisy boundary and background points. In CWAP, object classes are prioritized through user-defined weights, offering flexibility in the projection strategy. Our evaluations on the SemanticKITTI dataset show that CAP preserves more instance points during projection, achieving up to a 3.1\% mIoU improvement compared to the baseline. Furthermore, CWAP enhances the performance of targeted classes while having a negligible impact on the performance of other classes

