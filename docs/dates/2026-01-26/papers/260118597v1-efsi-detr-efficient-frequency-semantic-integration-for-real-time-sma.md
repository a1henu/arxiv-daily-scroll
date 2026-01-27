---
layout: default
title: EFSI-DETR: Efficient Frequency-Semantic Integration for Real-Time Small Object Detection in UAV Imagery
---

# EFSI-DETR: Efficient Frequency-Semantic Integration for Real-Time Small Object Detection in UAV Imagery
**arXiv**：[2601.18597v1](https://arxiv.org/abs/2601.18597) · [PDF](https://arxiv.org/pdf/2601.18597.pdf)  
**作者**：Yu Xia, Chang Liu, Tianqi Xiang, Zhigang Tu  

**一句话要点**：提出EFSI-DETR框架，通过动态频率-空间协同与高效语义提取，实现无人机图像实时小目标检测。

**关键词**：无人机图像检测, 小目标检测, 频率-空间融合, 实时检测, DETR框架

## 3 点简述
- 核心问题：无人机图像小目标检测中特征表示有限、多尺度融合效果差，现有方法未充分利用频率信息。
- 方法要点：结合DyFusNet动态融合频率与空间线索，ESFC高效提取深层语义，FFR策略保留细粒度细节。
- 实验或效果：在VisDrone和CODrone基准上达到SOTA，AP提升1.6%，AP_s提升5.8%，推理速度188 FPS。

## 摘要（原文）

> Real-time small object detection in Unmanned Aerial Vehicle (UAV) imagery remains challenging due to limited feature representation and ineffective multi-scale fusion. Existing methods underutilize frequency information and rely on static convolutional operations, which constrain the capacity to obtain rich feature representations and hinder the effective exploitation of deep semantic features. To address these issues, we propose EFSI-DETR, a novel detection framework that integrates efficient semantic feature enhancement with dynamic frequency-spatial guidance. EFSI-DETR comprises two main components: (1) a Dynamic Frequency-Spatial Unified Synergy Network (DyFusNet) that jointly exploits frequency and spatial cues for robust multi-scale feature fusion, (2) an Efficient Semantic Feature Concentrator (ESFC) that enables deep semantic extraction with minimal computational cost. Furthermore, a Fine-grained Feature Retention (FFR) strategy is adopted to incorporate spatially rich shallow features during fusion to preserve fine-grained details, crucial for small object detection in UAV imagery. Extensive experiments on VisDrone and CODrone benchmarks demonstrate that our EFSI-DETR achieves the state-of-the-art performance with real-time efficiency, yielding improvement of \textbf{1.6}\% and \textbf{5.8}\% in AP and AP$_{s}$ on VisDrone, while obtaining \textbf{188} FPS inference speed on a single RTX 4090 GPU.

