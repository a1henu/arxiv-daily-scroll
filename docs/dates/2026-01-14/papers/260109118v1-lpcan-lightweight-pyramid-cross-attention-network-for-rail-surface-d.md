---
layout: default
title: LPCAN: Lightweight Pyramid Cross-Attention Network for Rail Surface Defect Detection Using RGB-D Data
---

# LPCAN: Lightweight Pyramid Cross-Attention Network for Rail Surface Defect Detection Using RGB-D Data
**arXiv**：[2601.09118v1](https://arxiv.org/abs/2601.09118) · [PDF](https://arxiv.org/pdf/2601.09118.pdf)  
**作者**：Jackie Alex, Guoqiang Huan  

**一句话要点**：提出轻量级金字塔交叉注意力网络，利用RGB-D数据高效检测钢轨表面缺陷。

**关键词**：钢轨缺陷检测, RGB-D数据, 轻量网络, 交叉注意力, 多模态融合, 工业视觉

## 3 点简述
- 针对钢轨缺陷检测方法计算复杂、参数多、精度不足的问题。
- 结合MobileNetv2、轻量金字塔模块、交叉注意力机制和空间特征提取器。
- 在三个RGB-D数据集上实现SOTA性能，参数仅9.90M，推理速度162.60 fps。

## 摘要（原文）

> This paper addresses the limitations of current vision-based rail defect detection methods, including high computational complexity, excessive parameter counts, and suboptimal accuracy. We propose a Lightweight Pyramid Cross-Attention Network (LPCANet) that leverages RGB-D data for efficient and accurate defect identification. The architecture integrates MobileNetv2 as a backbone for RGB feature extraction with a lightweight pyramid module (LPM) for depth processing, coupled with a cross-attention mechanism (CAM) for multimodal fusion and a spatial feature extractor (SFE) for enhanced structural analysis. Comprehensive evaluations on three unsupervised RGB-D rail datasets (NEU-RSDDS-AUG, RSDD-TYPE1, RSDD-TYPE2) demonstrate that LPCANet achieves state-of-the-art performance with only 9.90 million parameters, 2.50 G FLOPs, and 162.60 fps inference speed. Compared to 18 existing methods, LPCANet shows significant improvements, including +1.48\% in $S_α$, +0.86\% in IOU, and +1.77\% in MAE over the best-performing baseline. Ablation studies confirm the critical roles of CAM and SFE, while experiments on non-rail datasets (DAGM2007, MT, Kolektor-SDD2) validate its generalization capability. The proposed framework effectively bridges traditional and deep learning approaches, offering substantial practical value for industrial defect inspection. Future work will focus on further model compression for real-time deployment.

