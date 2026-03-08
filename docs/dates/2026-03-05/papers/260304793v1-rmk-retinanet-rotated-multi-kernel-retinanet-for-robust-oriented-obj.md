---
layout: default
title: RMK RetinaNet: Rotated Multi-Kernel RetinaNet for Robust Oriented Object Detection in Remote Sensing Imagery
---

# RMK RetinaNet: Rotated Multi-Kernel RetinaNet for Robust Oriented Object Detection in Remote Sensing Imagery
**arXiv**：[2603.04793v1](https://arxiv.org/abs/2603.04793) · [PDF](https://arxiv.org/pdf/2603.04793.pdf)  
**作者**：Huiran Sun  

**一句话要点**：提出RMK RetinaNet以解决遥感图像中旋转目标检测的瓶颈问题

**关键词**：旋转目标检测, 遥感图像, 多尺度特征融合, 角度回归, 上下文建模, 自适应感受野

## 3 点简述
- 核心问题：非自适应感受野利用、长距离多尺度特征融合不足及角度回归不连续
- 方法要点：设计MSK块增强自适应多尺度特征提取，引入MDCAA机制提升跨尺度上下文建模，开发EAEM模块实现连续稳定角度回归
- 实验或效果：在DOTA-v1.0等数据集上性能媲美先进旋转目标检测器，提升多尺度多方向场景的鲁棒性

## 摘要（原文）

> Rotated object detection in remote sensing imagery is hindered by three major bottlenecks: non-adaptive receptive field utilization, inadequate long-range multi-scale feature fusion, and discontinuities in angle regression. To address these issues, we propose Rotated Multi-Kernel RetinaNet (RMK RetinaNet). First, we design a Multi-Scale Kernel (MSK) Block to strengthen adaptive multi-scale feature extraction. Second, we incorporate a Multi-Directional Contextual Anchor Attention (MDCAA) mechanism into the feature pyramid to enhance contextual modeling across scales and orientations. Third, we introduce a Bottom-up Path to preserve fine-grained spatial details that are often degraded during downsampling. Finally, we develop an Euler Angle Encoding Module (EAEM) to enable continuous and stable angle regression. Extensive experiments on DOTA-v1.0, HRSC2016, and UCAS-AOD show that RMK RetinaNet achieves performance comparable to state-of-the-art rotated object detectors while improving robustness in multi-scale and multi-orientation scenarios.

