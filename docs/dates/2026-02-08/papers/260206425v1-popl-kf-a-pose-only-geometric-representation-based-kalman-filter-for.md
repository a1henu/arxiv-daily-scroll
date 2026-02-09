---
layout: default
title: POPL-KF: A Pose-Only Geometric Representation-Based Kalman Filter for Point-Line-Based Visual-Inertial Odometry
---

# POPL-KF: A Pose-Only Geometric Representation-Based Kalman Filter for Point-Line-Based Visual-Inertial Odometry
**arXiv**：[2602.06425v1](https://arxiv.org/abs/2602.06425) · [PDF](https://arxiv.org/pdf/2602.06425.pdf)  
**作者**：Aiping Wang, Zhaolong Yang, Shuwen Chen, Hai Zhang  

**一句话要点**：提出POPL-KF，一种基于姿态几何表示的卡尔曼滤波器，用于点线视觉惯性里程计，以提升挑战场景性能。

**关键词**：视觉惯性里程计, 卡尔曼滤波器, 姿态几何表示, 点线特征, 实时定位, 挑战场景

## 3 点简述
- 主流VIO系统依赖点特征，在挑战场景中性能下降，且MSCKF存在线性化误差和延迟更新问题。
- 提出姿态几何表示消除特征坐标，设计统一基帧选择算法和线特征滤波器，实现即时测量更新。
- 在公开数据集和真实实验中，POPL-KF优于SOTA滤波和优化方法，保持实时性能。

## 摘要（原文）

> Mainstream Visual-inertial odometry 
> (VIO) systems rely on point features for motion estimation and localization. However, their performance degrades in challenging scenarios. Moreover, the localization accuracy of multi-state constraint Kalman filter (MSCKF)-based VIO systems suffers from linearization errors associated with feature 3D coordinates and delayed measurement updates. To improve the performance of VIO in challenging scenes, we first propose a pose-only geometric representation for line features. Building on this, we develop POPL-KF, a Kalman filter-based VIO system that employs a pose-only geometric representation for both point and line features. POPL-KF mitigates linearization errors by explicitly eliminating both point and line feature coordinates from the measurement equations, while enabling immediate update of visual measurements. We also design a unified base-frames selection algorithm for both point and line features to ensure optimal constraints on camera poses within the pose-only measurement model. To further improve line feature quality, a line feature filter based on image grid segmentation and bidirectional optical flow consistency is proposed. Our system is evaluated on public datasets and real-world experiments, demonstrating that POPL-KF outperforms the state-of-the-art (SOTA) filter-based methods (OpenVINS, PO-KF) and optimization-based methods (PL-VINS, EPLF-VINS), while maintaining real-time performance.

