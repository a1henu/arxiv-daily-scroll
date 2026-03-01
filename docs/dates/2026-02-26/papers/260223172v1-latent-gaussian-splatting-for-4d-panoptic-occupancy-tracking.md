---
layout: default
title: Latent Gaussian Splatting for 4D Panoptic Occupancy Tracking
---

# Latent Gaussian Splatting for 4D Panoptic Occupancy Tracking
**arXiv**：[2602.23172v1](https://arxiv.org/abs/2602.23172) · [PDF](https://arxiv.org/pdf/2602.23172.pdf)  
**作者**：Maximilian Luz, Rohit Mohan, Thomas Nürnberg, Yakov Miron, Daniele Cattaneo, Abhinav Valada  

**一句话要点**：提出LaGS方法，通过潜在高斯泼溅实现4D全景占用跟踪，以解决动态环境中时空场景理解问题。

**关键词**：4D全景占用跟踪, 潜在高斯泼溅, 多视图信息聚合, 时空场景理解, 动态环境感知

## 3 点简述
- 核心问题：现有方法在动态环境中仅提供粗略几何跟踪或缺乏时间关联的详细3D结构，难以实现高效时空场景理解。
- 方法要点：采用基于相机的端到端跟踪与基于掩码的多视图全景占用预测，通过潜在高斯泼溅高效聚合多视图信息到3D体素网格。
- 实验或效果：在Occ3D nuScenes和Waymo数据集上评估，达到4D全景占用跟踪的最先进性能。

## 摘要（原文）

> Capturing 4D spatiotemporal surroundings is crucial for the safe and reliable operation of robots in dynamic environments. However, most existing methods address only one side of the problem: they either provide coarse geometric tracking via bounding boxes, or detailed 3D structures like voxel-based occupancy that lack explicit temporal association. In this work, we present Latent Gaussian Splatting for 4D Panoptic Occupancy Tracking (LaGS) that advances spatiotemporal scene understanding in a holistic direction. Our approach incorporates camera-based end-to-end tracking with mask-based multi-view panoptic occupancy prediction, and addresses the key challenge of efficiently aggregating multi-view information into 3D voxel grids via a novel latent Gaussian splatting approach. Specifically, we first fuse observations into 3D Gaussians that serve as a sparse point-centric latent representation of the 3D scene, and then splat the aggregated features onto a 3D voxel grid that is decoded by a mask-based segmentation head. We evaluate LaGS on the Occ3D nuScenes and Waymo datasets, achieving state-of-the-art performance for 4D panoptic occupancy tracking. We make our code available at https://lags.cs.uni-freiburg.de/.

