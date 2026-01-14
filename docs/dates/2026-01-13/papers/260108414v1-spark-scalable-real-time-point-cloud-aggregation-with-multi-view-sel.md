---
layout: default
title: SPARK: Scalable Real-Time Point Cloud Aggregation with Multi-View Self-Calibration
---

# SPARK: Scalable Real-Time Point Cloud Aggregation with Multi-View Self-Calibration
**arXiv**：[2601.08414v1](https://arxiv.org/abs/2601.08414) · [PDF](https://arxiv.org/pdf/2601.08414.pdf)  
**作者**：Chentian Sun  

**一句话要点**：提出SPARK框架以解决多相机实时点云重建中的外参不确定性和融合问题

**关键词**：多相机3D重建, 点云融合, 外参自校准, 实时系统, 几何一致性

## 3 点简述
- 核心问题：多相机实时3D重建面临外参不确定性、融合困难和可扩展性挑战
- 方法要点：结合在线外参自校准和置信度驱动的点云融合策略，提升几何一致性和稳定性
- 实验或效果：在真实多相机系统中，SPARK在外参精度、几何一致性、时间稳定性和实时性能上优于现有方法

## 摘要（原文）

> Real-time multi-camera 3D reconstruction is crucial for 3D perception, immersive interaction, and robotics. Existing methods struggle with multi-view fusion, camera extrinsic uncertainty, and scalability for large camera setups. We propose SPARK, a self-calibrating real-time multi-camera point cloud reconstruction framework that jointly handles point cloud fusion and extrinsic uncertainty. SPARK consists of: (1) a geometry-aware online extrinsic estimation module leveraging multi-view priors and enforcing cross-view and temporal consistency for stable self-calibration, and (2) a confidence-driven point cloud fusion strategy modeling depth reliability and visibility at pixel and point levels to suppress noise and view-dependent inconsistencies. By performing frame-wise fusion without accumulation, SPARK produces stable point clouds in dynamic scenes while scaling linearly with the number of cameras. Extensive experiments on real-world multi-camera systems show that SPARK outperforms existing approaches in extrinsic accuracy, geometric consistency, temporal stability, and real-time performance, demonstrating its effectiveness and scalability for large-scale multi-camera 3D reconstruction.

