---
layout: default
title: Cross-Layer Feature Self-Attention Module for Multi-Scale Object Detection
---

# Cross-Layer Feature Self-Attention Module for Multi-Scale Object Detection
**arXiv**：[2510.14726v1](https://arxiv.org/abs/2510.14726) · [PDF](https://arxiv.org/pdf/2510.14726.pdf)  
**作者**：Dingzhou Xie, Rushi Lan, Cheng Pang, Enhao Ning, Jiahao Zeng, Wei Zheng  

**一句话要点**：提出跨层特征自注意力模块以提升多尺度目标检测性能

**关键词**：多尺度目标检测, 跨层注意力, 特征融合, 自注意力机制, Transformer模型

## 3 点简述
- 现有方法忽视多尺度特征间的跨层依赖，限制检测大尺度变化物体的能力
- CFSAM结合卷积局部特征提取、Transformer全局建模和特征融合，增强多尺度特征表示
- 集成SSD300框架，在PASCAL VOC和COCO数据集上显著提升mAP，并加速训练收敛

## 摘要（原文）

> Recent object detection methods have made remarkable progress by leveraging
> attention mechanisms to improve feature discriminability. However, most
> existing approaches are confined to refining single-layer or fusing dual-layer
> features, overlooking the rich inter-layer dependencies across multi-scale
> representations. This limits their ability to capture comprehensive contextual
> information essential for detecting objects with large scale variations. In
> this paper, we propose a novel Cross-Layer Feature Self-Attention Module
> (CFSAM), which holistically models both local and global dependencies within
> multi-scale feature maps. CFSAM consists of three key components: a
> convolutional local feature extractor, a Transformer-based global modeling unit
> that efficiently captures cross-layer interactions, and a feature fusion
> mechanism to restore and enhance the original representations. When integrated
> into the SSD300 framework, CFSAM significantly boosts detection performance,
> achieving 78.6% mAP on PASCAL VOC (vs. 75.5% baseline) and 52.1% mAP on COCO
> (vs. 43.1% baseline), outperforming existing attention modules. Moreover, the
> module accelerates convergence during training without introducing substantial
> computational overhead. Our work highlights the importance of explicit
> cross-layer attention modeling in advancing multi-scale object detection.

