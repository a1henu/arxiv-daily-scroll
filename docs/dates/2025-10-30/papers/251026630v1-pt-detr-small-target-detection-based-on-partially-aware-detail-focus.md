---
layout: default
title: PT-DETR: Small Target Detection Based on Partially-Aware Detail Focus
---

# PT-DETR: Small Target Detection Based on Partially-Aware Detail Focus
**arXiv**：[2510.26630v1](https://arxiv.org/abs/2510.26630) · [PDF](https://arxiv.org/pdf/2510.26630.pdf)  
**作者**：Bingcong Huo, Zhiming Wang  

**一句话要点**：提出PT-DETR以解决无人机图像中小目标检测的挑战

**关键词**：小目标检测, 无人机图像, 特征融合, 目标检测算法, RT-DETR改进

## 3 点简述
- 核心问题：无人机图像中复杂背景、遮挡、密集小目标和光照变化导致检测困难
- 方法要点：引入PADF模块增强小目标特征提取，设计MFFF模块融合细节与上下文信息
- 实验或效果：在VisDrone2019数据集上mAP提升1.6-1.7%，计算复杂度与参数更少

## 摘要（原文）

> To address the challenges in UAV object detection, such as complex
> backgrounds, severe occlusion, dense small objects, and varying lighting
> conditions,this paper proposes PT-DETR based on RT-DETR, a novel detection
> algorithm specifically designed for small objects in UAV imagery. In the
> backbone network, we introduce the Partially-Aware Detail Focus (PADF) Module
> to enhance feature extraction for small objects. Additionally,we design the
> Median-Frequency Feature Fusion (MFFF) module,which effectively improves the
> model's ability to capture small-object details and contextual information.
> Furthermore,we incorporate Focaler-SIoU to strengthen the model's bounding box
> matching capability and increase its sensitivity to small-object features,
> thereby further enhancing detection accuracy and robustness. Compared with
> RT-DETR, our PT-DETR achieves mAP improvements of 1.6% and 1.7% on the
> VisDrone2019 dataset with lower computational complexity and fewer parameters,
> demonstrating its robustness and feasibility for small-object detection tasks.

