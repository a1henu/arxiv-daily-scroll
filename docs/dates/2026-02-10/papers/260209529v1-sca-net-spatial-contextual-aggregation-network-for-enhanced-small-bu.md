---
layout: default
title: SCA-Net: Spatial-Contextual Aggregation Network for Enhanced Small Building and Road Change Detection
---

# SCA-Net: Spatial-Contextual Aggregation Network for Enhanced Small Building and Road Change Detection
**arXiv**：[2602.09529v1](https://arxiv.org/abs/2602.09529) · [PDF](https://arxiv.org/pdf/2602.09529.pdf)  
**作者**：Emad Gholibeigi, Abbas Koochari, Azadeh ZamaniFar  

**一句话要点**：提出SCA-Net以增强遥感图像中建筑物与道路变化检测的精度与效率

**关键词**：遥感变化检测, 多尺度分析, 注意力机制, 动态损失函数, 小物体检测

## 3 点简述
- 针对遥感变化检测中模型对小物体敏感度低和计算成本高的问题
- 引入差异金字塔块、自适应多尺度处理模块和多级注意力机制提升性能
- 在LEVIR数据集上实现mIoU显著提升，训练时间减少61%

## 摘要（原文）

> Automated change detection in remote sensing imagery is critical for urban management, environmental monitoring, and disaster assessment. While deep learning models have advanced this field, they often struggle with challenges like low sensitivity to small objects and high computational costs. This paper presents SCA-Net, an enhanced architecture built upon the Change-Agent framework for precise building and road change detection in bi-temporal images. Our model incorporates several key innovations: a novel Difference Pyramid Block for multi-scale change analysis, an Adaptive Multi-scale Processing module combining shape-aware and high-resolution enhancement blocks, and multi-level attention mechanisms (PPM and CSAGate) for joint contextual and detail processing. Furthermore, a dynamic composite loss function and a four-phase training strategy are introduced to stabilize training and accelerate convergence. Comprehensive evaluations on the LEVIR-CD and LEVIR-MCI datasets demonstrate SCA-Net's superior performance over Change-Agent and other state-of-the-art methods. Our approach achieves a significant 2.64% improvement in mean Intersection over Union (mIoU) on LEVIR-MCI and a remarkable 57.9% increase in IoU for small buildings, while reducing the training time by 61%. This work provides an efficient, accurate, and robust solution for practical change detection applications.

