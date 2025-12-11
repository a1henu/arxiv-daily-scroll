---
layout: default
title: Traffic Scene Small Target Detection Method Based on YOLOv8n-SPTS Model for Autonomous Driving
---

# Traffic Scene Small Target Detection Method Based on YOLOv8n-SPTS Model for Autonomous Driving
**arXiv**：[2512.09296v1](https://arxiv.org/abs/2512.09296) · [PDF](https://arxiv.org/pdf/2512.09296.pdf)  
**作者**：Songhan Wu  

**一句话要点**：提出YOLOv8n-SPTS模型以提升自动驾驶场景中小目标检测性能

**关键词**：自动驾驶, 小目标检测, YOLOv8改进, 特征融合, 多尺度特征

## 3 点简述
- 核心问题：自动驾驶动态感知中小目标识别困难，现有算法因信息丢失、尺度不平衡和遮挡导致检测性能差。
- 方法要点：通过SPD-Conv模块优化特征提取，引入SPPFCSPC模块增强特征融合，设计TSFP结构专注小目标检测。
- 实验或效果：在VisDrone2019-DET数据集上，模型在精度、召回率和mAP指标上排名第一，可视化显示遮挡密集场景中小目标漏检率显著降低。

## 摘要（原文）

> This paper focuses on the key issue in autonomous driving: small target recognition in dynamic perception. Existing algorithms suffer from poor detection performance due to missing small target information, scale imbalance, and occlusion. We propose an improved YOLOv8n-SPTS model, which enhances the detection accuracy of small traffic targets through three key innovations: First, optimizing the feature extraction module. In the Backbone Bottleneck structure of YOLOv8n, 4 traditional convolution modules are replaced with Space-to-Depth Convolution (SPD-Conv) modules. This module retains fine-grained information through space-to-depth conversion, reduces information loss, and enhances the ability to capture features of low-resolution small targets. Second, enhancing feature fusion capability. The Spatial Pyramid Pooling - Fast Cross Stage Partial Connection (SPPFCSPC) module is introduced to replace the original SPPF module, integrating the multi-scale feature extraction from Spatial Pyramid Pooling (SPP) and the feature fusion mechanism of Cross Stage Partial Connection (CSP), thereby improving the model's contextual understanding of complex scenes and multi-scale feature expression ability. Third, designing a dedicated detection structure for small targets. A Triple-Stage Feature Pyramid (TSFP) structure is proposed, which adds a 160*160 small target detection head to the original detection heads to fully utilize high-resolution features in shallow layers; meanwhile, redundant large target detection heads are removed to balance computational efficiency. Comparative experiments on the VisDrone2019-DET dataset show that YOLOv8n-SPTS model ranks first in precision (61.9%), recall (48.3%), mAP@0.5 (52.6%), and mAP@0.5:0.95 (32.6%). Visualization results verify that the miss rate of small targets such as pedestrians and bicycles in occluded and dense scenes is significantly reduced.

