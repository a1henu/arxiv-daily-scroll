---
layout: default
title: YOPO-Nav: Visual Navigation using 3DGS Graphs from One-Pass Videos
---

# YOPO-Nav: Visual Navigation using 3DGS Graphs from One-Pass Videos
**arXiv**：[2512.09903v1](https://arxiv.org/abs/2512.09903) · [PDF](https://arxiv.org/pdf/2512.09903.pdf)  
**作者**：Ryan Meegan, Adam D'Souza, Bryan Bo Cao, Shubham Jain, Kristin Dana  

**一句话要点**：提出YOPO-Nav方法，利用单次视频构建3DGS图实现视觉导航

**关键词**：视觉导航, 3D高斯泼溅, 单次视频学习, 视觉地点识别, 机器人控制

## 3 点简述
- 核心问题：视觉导航依赖3D地图构建，计算和内存开销大，需高效替代方案。
- 方法要点：使用单次探索视频编码为局部3DGS模型图，结合VPR粗定位和3DGS精调进行导航控制。
- 实验或效果：在YOPO-Campus数据集上测试，物理机器人实验显示在真实场景中性能优异。

## 摘要（原文）

> Visual navigation has emerged as a practical alternative to traditional robotic navigation pipelines that rely on detailed mapping and path planning. However, constructing and maintaining 3D maps is often computationally expensive and memory-intensive. We address the problem of visual navigation when exploration videos of a large environment are available. The videos serve as a visual reference, allowing a robot to retrace the explored trajectories without relying on metric maps. Our proposed method, YOPO-Nav (You Only Pass Once), encodes an environment into a compact spatial representation composed of interconnected local 3D Gaussian Splatting (3DGS) models. During navigation, the framework aligns the robot's current visual observation with this representation and predicts actions that guide it back toward the demonstrated trajectory. YOPO-Nav employs a hierarchical design: a visual place recognition (VPR) module provides coarse localization, while the local 3DGS models refine the goal and intermediate poses to generate control actions. To evaluate our approach, we introduce the YOPO-Campus dataset, comprising 4 hours of egocentric video and robot controller inputs from over 6 km of human-teleoperated robot trajectories. We benchmark recent visual navigation methods on trajectories from YOPO-Campus using a Clearpath Jackal robot. Experimental results show YOPO-Nav provides excellent performance in image-goal navigation for real-world scenes on a physical robot. The dataset and code will be made publicly available for visual navigation and scene representation research.

