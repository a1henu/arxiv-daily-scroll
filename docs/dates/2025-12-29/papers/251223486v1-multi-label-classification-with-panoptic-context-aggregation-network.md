---
layout: default
title: Multi-label Classification with Panoptic Context Aggregation Networks
---

# Multi-label Classification with Panoptic Context Aggregation Networks
**arXiv**：[2512.23486v1](https://arxiv.org/abs/2512.23486) · [PDF](https://arxiv.org/pdf/2512.23486.pdf)  
**作者**：Mingyuan Jiu, Hailong Zhu, Wenchuan Wei, Hichem Sahbi, Rongrong Ji, Mingliang Xu  

**一句话要点**：提出PanCAN网络，通过跨尺度特征聚合增强多标签分类中的上下文建模。

**关键词**：多标签分类, 上下文建模, 跨尺度特征聚合, 注意力机制, 希尔伯特空间

## 3 点简述
- 核心问题：现有方法忽视跨尺度对象交互，限制复杂场景理解。
- 方法要点：在希尔伯特空间中结合随机游走和注意力，分层整合多阶几何上下文。
- 实验或效果：在多个基准测试中优于先进技术，提升分类性能。

## 摘要（原文）

> Context modeling is crucial for visual recognition, enabling highly discriminative image representations by integrating both intrinsic and extrinsic relationships between objects and labels in images. A limitation in current approaches is their focus on basic geometric relationships or localized features, often neglecting cross-scale contextual interactions between objects. This paper introduces the Deep Panoptic Context Aggregation Network (PanCAN), a novel approach that hierarchically integrates multi-order geometric contexts through cross-scale feature aggregation in a high-dimensional Hilbert space. Specifically, PanCAN learns multi-order neighborhood relationships at each scale by combining random walks with an attention mechanism. Modules from different scales are cascaded, where salient anchors at a finer scale are selected and their neighborhood features are dynamically fused via attention. This enables effective cross-scale modeling that significantly enhances complex scene understanding by combining multi-order and cross-scale context-aware features. Extensive multi-label classification experiments on NUS-WIDE, PASCAL VOC2007, and MS-COCO benchmarks demonstrate that PanCAN consistently achieves competitive results, outperforming state-of-the-art techniques in both quantitative and qualitative evaluations, thereby substantially improving multi-label classification performance.

