---
layout: default
title: LiM-YOLO: Less is More with Pyramid Level Shift and Normalized Auxiliary Branch for Ship Detection in Optical Remote Sensing Imagery
---

# LiM-YOLO: Less is More with Pyramid Level Shift and Normalized Auxiliary Branch for Ship Detection in Optical Remote Sensing Imagery
**arXiv**：[2512.09700v1](https://arxiv.org/abs/2512.09700) · [PDF](https://arxiv.org/pdf/2512.09700.pdf)  
**作者**：Seon-Hoon Kim, Hyeji Sim, Youeyun Jung, Ok-Chul Jung, Yerin Kim  

**一句话要点**：提出LiM-YOLO，通过金字塔层级偏移与归一化辅助分支解决遥感图像中船舶检测的尺度差异问题。

**关键词**：船舶检测, 遥感图像, 金字塔层级偏移, 归一化辅助分支, 目标检测, 尺度差异

## 3 点简述
- 核心问题：遥感图像中船舶目标尺度差异大且形态各向异性，导致通用检测器在小目标上性能下降。
- 方法要点：基于统计分析，采用金字塔层级偏移策略调整检测头至P2-P4，并引入GN-CBLinear模块增强训练稳定性。
- 实验或效果：在多个数据集上验证，LiM-YOLO在检测精度和效率上优于现有先进模型。

## 摘要（原文）

> Applying general-purpose object detectors to ship detection in satellite imagery presents significant challenges due to the extreme scale disparity and morphological anisotropy of maritime targets. Standard architectures utilizing stride-32 (P5) layers often fail to resolve narrow vessels, resulting in spatial feature dilution. In this work, we propose LiM-YOLO, a specialized detector designed to resolve these domain-specific conflicts. Based on a statistical analysis of ship scales, we introduce a Pyramid Level Shift Strategy that reconfigures the detection head to P2-P4. This shift ensures compliance with Nyquist sampling criteria for small objects while eliminating the computational redundancy of deep layers. To further enhance training stability on high-resolution inputs, we incorporate a Group Normalized Convolutional Block for Linear Projection (GN-CBLinear), which mitigates gradient volatility in micro-batch settings. Validated on SODA-A, DOTA-v1.5, FAIR1M-v2.0, and ShipRSImageNet-V1, LiM-YOLO demonstrates superior detection accuracy and efficiency compared to state-of-the-art models. The code is available at https://github.com/egshkim/LiM-YOLO.

