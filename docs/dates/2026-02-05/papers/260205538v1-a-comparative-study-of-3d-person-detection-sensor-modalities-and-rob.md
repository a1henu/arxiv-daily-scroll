---
layout: default
title: A Comparative Study of 3D Person Detection: Sensor Modalities and Robustness in Diverse Indoor and Outdoor Environments
---

# A Comparative Study of 3D Person Detection: Sensor Modalities and Robustness in Diverse Indoor and Outdoor Environments
**arXiv**：[2602.05538v1](https://arxiv.org/abs/2602.05538) · [PDF](https://arxiv.org/pdf/2602.05538.pdf)  
**作者**：Malaz Tamim, Andrea Matic-Flierl, Karsten Roscher  

**一句话要点**：比较相机、LiDAR及融合方法在多样室内外环境中的3D行人检测性能与鲁棒性

**关键词**：3D行人检测, 传感器融合, 鲁棒性评估, 室内外场景, JRDB数据集, 多模态感知

## 3 点简述
- 核心问题：现有研究多关注自动驾驶，缺乏对多样室内外场景中3D行人检测性能与鲁棒性的系统评估。
- 方法要点：使用JRDB数据集，对比BEVDepth（相机）、PointPillars（LiDAR）和DAL（相机-LiDAR融合）三种代表性模型。
- 实验或效果：融合方法在挑战性场景中表现最佳，但易受传感器错位和LiDAR噪声影响；相机模型性能最低且对遮挡和距离敏感。

## 摘要（原文）

> Accurate 3D person detection is critical for safety in applications such as robotics, industrial monitoring, and surveillance. This work presents a systematic evaluation of 3D person detection using camera-only, LiDAR-only, and camera-LiDAR fusion. While most existing research focuses on autonomous driving, we explore detection performance and robustness in diverse indoor and outdoor scenes using the JRDB dataset. We compare three representative models - BEVDepth (camera), PointPillars (LiDAR), and DAL (camera-LiDAR fusion) - and analyze their behavior under varying occlusion and distance levels. Our results show that the fusion-based approach consistently outperforms single-modality models, particularly in challenging scenarios. We further investigate robustness against sensor corruptions and misalignments, revealing that while DAL offers improved resilience, it remains sensitive to sensor misalignment and certain LiDAR-based corruptions. In contrast, the camera-based BEVDepth model showed the lowest performance and was most affected by occlusion, distance, and noise. Our findings highlight the importance of utilizing sensor fusion for enhanced 3D person detection, while also underscoring the need for ongoing research to address the vulnerabilities inherent in these systems.

