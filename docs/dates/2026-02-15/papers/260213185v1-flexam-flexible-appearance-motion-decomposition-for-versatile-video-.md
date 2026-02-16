---
layout: default
title: FlexAM: Flexible Appearance-Motion Decomposition for Versatile Video Generation Control
---

# FlexAM: Flexible Appearance-Motion Decomposition for Versatile Video Generation Control
**arXiv**：[2602.13185v1](https://arxiv.org/abs/2602.13185) · [PDF](https://arxiv.org/pdf/2602.13185.pdf)  
**作者**：Mingzhi Sheng, Zekai Gu, Peng Li, Cheng Lin, Hao-Xiang Guo, Ying-Cong Chen, Yuan Liu  

**一句话要点**：提出FlexAM框架，通过点云表示视频动态，实现外观与运动解耦以增强视频生成控制

**关键词**：视频生成控制, 外观运动解耦, 3D点云表示, 多频位置编码, 深度感知编码, 灵活控制信号

## 3 点简述
- 核心问题：视频生成中缺乏有效且通用的控制方法，现有方法依赖模糊或任务特定信号
- 方法要点：基于3D点云控制信号，引入多频位置编码和深度感知编码，灵活平衡精度与生成质量
- 实验或效果：在I2V/V2V编辑、相机控制和空间对象编辑等任务中表现优异

## 摘要（原文）

> Effective and generalizable control in video generation remains a significant challenge. While many methods rely on ambiguous or task-specific signals, we argue that a fundamental disentanglement of "appearance" and "motion" provides a more robust and scalable pathway. We propose FlexAM, a unified framework built upon a novel 3D control signal. This signal represents video dynamics as a point cloud, introducing three key enhancements: multi-frequency positional encoding to distinguish fine-grained motion, depth-aware positional encoding, and a flexible control signal for balancing precision and generative quality. This representation allows FlexAM to effectively disentangle appearance and motion, enabling a wide range of tasks including I2V/V2V editing, camera control, and spatial object editing. Extensive experiments demonstrate that FlexAM achieves superior performance across all evaluated tasks.

