---
layout: default
title: RADE-Net: Robust Attention Network for Radar-Only Object Detection in Adverse Weather
---

# RADE-Net: Robust Attention Network for Radar-Only Object Detection in Adverse Weather
**arXiv**：[2602.19994v1](https://arxiv.org/abs/2602.19994) · [PDF](https://arxiv.org/pdf/2602.19994.pdf)  
**作者**：Christof Leitgeb, Thomas Puchleitner, Max Peter Ronecker, Daniel Watzenig  

**一句话要点**：提出RADE-Net，一种基于3D投影的轻量级雷达注意力网络，用于恶劣天气下的物体检测。

**关键词**：雷达物体检测, 恶劣天气感知, 3D投影, 注意力机制, 轻量级网络, 4D张量处理

## 3 点简述
- 问题：雷达全张量数据量大且数据集少，现有方法使用稀疏点云或2D投影导致信息丢失。
- 方法：提出3D投影方法处理4D RADE张量，保留多普勒和高度特征，数据量减少91.9%；设计RADE-Net，结合空间和通道注意力提取特征，解耦检测头预测物体中心点和3D边界框。
- 效果：在K-Radar数据集上，相比基线提升16.7%，优于当前雷达模型，并在恶劣天气下超越多个激光雷达方法。

## 摘要（原文）

> Automotive perception systems are obligated to meet high requirements. While optical sensors such as Camera and Lidar struggle in adverse weather conditions, Radar provides a more robust perception performance, effectively penetrating fog, rain, and snow. Since full Radar tensors have large data sizes and very few datasets provide them, most Radar-based approaches work with sparse point clouds or 2D projections, which can result in information loss. Additionally, deep learning methods show potential to extract richer and more dense features from low level Radar data and therefore significantly increase the perception performance. Therefore, we propose a 3D projection method for fast-Fourier-transformed 4D Range-Azimuth-Doppler-Elevation (RADE) tensors. Our method preserves rich Doppler and Elevation features while reducing the required data size for a single frame by 91.9% compared to a full tensor, thus achieving higher training and inference speed as well as lower model complexity. We introduce RADE-Net, a lightweight model tailored to 3D projections of the RADE tensor. The backbone enables exploitation of low-level and high-level cues of Radar tensors with spatial and channel-attention. The decoupled detection heads predict object center-points directly in the Range-Azimuth domain and regress rotated 3D bounding boxes from rich feature maps in the cartesian scene. We evaluate the model on scenes with multiple different road users and under various weather conditions on the large-scale K-Radar dataset and achieve a 16.7% improvement compared to their baseline, as well as 6.5% improvement over current Radar-only models. Additionally, we outperform several Lidar approaches in scenarios with adverse weather conditions. The code is available under https://github.com/chr-is-tof/RADE-Net.

