---
layout: default
title: Enabling Progressive Whole-slide Image Analysis with Multi-scale Pyramidal Network
---

# Enabling Progressive Whole-slide Image Analysis with Multi-scale Pyramidal Network
**arXiv**：[2602.01951v1](https://arxiv.org/abs/2602.01951) · [PDF](https://arxiv.org/pdf/2602.01951.pdf)  
**作者**：Shuyang Wu, Yifu Qiu, Ines P. Nearchou, Sandrine Prost, Jonathan A Fallowfield, Hakan Bilen, Timothy J Kendall  

**一句话要点**：提出多尺度金字塔网络以增强全切片图像分析中的渐进多尺度学习

**关键词**：全切片图像分析, 多实例学习, 多尺度特征, 渐进学习, 计算病理学, 注意力机制

## 3 点简述
- 核心问题：现有方法依赖固定放大倍率的多输入，特征融合晚，计算成本高且不灵活。
- 方法要点：引入基于网格的重映射和粗粒度指导网络，实现渐进式多尺度特征学习。
- 实验或效果：在4个临床任务和3类基础模型上，作为插件模块一致提升注意力多实例学习性能。

## 摘要（原文）

> Multiple-instance Learning (MIL) is commonly used to undertake computational pathology (CPath) tasks, and the use of multi-scale patches allows diverse features across scales to be learned. Previous studies using multi-scale features in clinical applications rely on multiple inputs across magnifications with late feature fusion, which does not retain the link between features across scales while the inputs are dependent on arbitrary, manufacturer-defined magnifications, being inflexible and computationally expensive. In this paper, we propose the Multi-scale Pyramidal Network (MSPN), which is plug-and-play over attention-based MIL that introduces progressive multi-scale analysis on WSI. Our MSPN consists of (1) grid-based remapping that uses high magnification features to derive coarse features and (2) the coarse guidance network (CGN) that learns coarse contexts. We benchmark MSPN as an add-on module to 4 attention-based frameworks using 4 clinically relevant tasks across 3 types of foundation model, as well as the pre-trained MIL framework. We show that MSPN consistently improves MIL across the compared configurations and tasks, while being lightweight and easy-to-use.

