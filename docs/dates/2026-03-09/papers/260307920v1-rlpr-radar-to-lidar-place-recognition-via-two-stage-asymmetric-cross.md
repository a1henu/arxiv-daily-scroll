---
layout: default
title: RLPR: Radar-to-LiDAR Place Recognition via Two-Stage Asymmetric Cross-Modal Alignment for Autonomous Driving
---

# RLPR: Radar-to-LiDAR Place Recognition via Two-Stage Asymmetric Cross-Modal Alignment for Autonomous Driving
**arXiv**：[2603.07920v1](https://arxiv.org/abs/2603.07920) · [PDF](https://arxiv.org/pdf/2603.07920.pdf)  
**作者**：Zhangshuo Qi, Jingyi Xu, Luqi Cheng, Shichen Wen, Guangming Xiong  

**一句话要点**：提出RLPR框架，通过两阶段非对称跨模态对齐实现雷达到激光雷达的地点识别，以增强自动驾驶的全天候定位能力。

**关键词**：自动驾驶定位, 跨模态对齐, 雷达激光雷达融合, 地点识别, 全天候感知

## 3 点简述
- 核心问题：雷达到激光雷达地点识别中，模态间特征提取困难，数据稀缺且信号异构。
- 方法要点：设计双流网络提取结构特征，并引入两阶段非对称跨模态对齐策略，利用预训练雷达分支引导对齐。
- 实验或效果：在四个数据集上实现最先进识别精度，具备强零样本泛化能力，兼容多种雷达类型。

## 摘要（原文）

> All-weather autonomy is critical for autonomous driving, which necessitates reliable localization across diverse scenarios. While LiDAR place recognition is widely deployed for this task, its performance degrades in adverse weather. Conversely, radar-based methods, though weather-resilient, are hindered by the general unavailability of radar maps. To bridge this gap, radar-to-LiDAR place recognition, which localizes radar scans within existing LiDAR maps, has garnered increasing interest. However, extracting discriminative and generalizable features shared between modalities remains challenging, compounded by the scarcity of large-scale paired training data and the signal heterogeneity across radar types. In this work, we propose RLPR, a robust radar-to-LiDAR place recognition framework compatible with single-chip, scanning, and 4D radars. We first design a dual-stream network to extract structural features that abstract away from sensor-specific signal properties (e.g., Doppler or RCS). Subsequently, motivated by our task-specific asymmetry observation between radar and LiDAR, we introduce a two-stage asymmetric cross-modal alignment (TACMA) strategy, which leverages the pre-trained radar branch as a discriminative anchor to guide the alignment process. Experiments on four datasets demonstrate that RLPR achieves state-of-the-art recognition accuracy with strong zero-shot generalization capabilities.

