---
layout: default
title: Towards Zero-Shot Point Cloud Registration Across Diverse Scales, Scenes, and Sensor Setups
---

# Towards Zero-Shot Point Cloud Registration Across Diverse Scales, Scenes, and Sensor Setups
**arXiv**：[2601.02759v1](https://arxiv.org/abs/2601.02759) · [PDF](https://arxiv.org/pdf/2601.02759.pdf)  
**作者**：Hyungtae Lim, Minkyun Seo, Luca Carlone, Jaesik Park  

**一句话要点**：提出BUFFER-X框架实现零样本点云配准，解决跨尺度、场景和传感器设置的泛化问题

**关键词**：点云配准, 零样本学习, 跨域泛化, 多尺度匹配, 传感器融合, 几何引导

## 3 点简述
- 核心问题：现有方法在零样本泛化时受固定参数、关键点检测器跨域迁移差和绝对坐标尺度不匹配限制
- 方法要点：通过几何引导超参数估计、分布感知采样和补丁级坐标归一化实现训练自由配准
- 实验效果：在12个数据集上验证跨传感器配准能力，无需手动调参或测试域先验知识

## 摘要（原文）

> Some deep learning-based point cloud registration methods struggle with zero-shot generalization, often requiring dataset-specific hyperparameter tuning or retraining for new environments. We identify three critical limitations: (a) fixed user-defined parameters (e.g., voxel size, search radius) that fail to generalize across varying scales, (b) learned keypoint detectors exhibit poor cross-domain transferability, and (c) absolute coordinates amplify scale mismatches between datasets. To address these three issues, we present BUFFER-X, a training-free registration framework that achieves zero-shot generalization through: (a) geometric bootstrapping for automatic hyperparameter estimation, (b) distribution-aware farthest point sampling to replace learned detectors, and (c) patch-level coordinate normalization to ensure scale consistency. Our approach employs hierarchical multi-scale matching to extract correspondences across local, middle, and global receptive fields, enabling robust registration in diverse environments. For efficiency-critical applications, we introduce BUFFER-X-Lite, which reduces total computation time by 43% (relative to BUFFER-X) through early exit strategies and fast pose solvers while preserving accuracy. We evaluate on a comprehensive benchmark comprising 12 datasets spanning object-scale, indoor, and outdoor scenes, including cross-sensor registration between heterogeneous LiDAR configurations. Results demonstrate that our approach generalizes effectively without manual tuning or prior knowledge of test domains. Code: https://github.com/MIT-SPARK/BUFFER-X.

