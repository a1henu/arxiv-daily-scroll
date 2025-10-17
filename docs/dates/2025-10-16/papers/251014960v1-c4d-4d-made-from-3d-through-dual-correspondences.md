---
layout: default
title: C4D: 4D Made from 3D through Dual Correspondences
---

# C4D: 4D Made from 3D through Dual Correspondences
**arXiv**：[2510.14960v1](https://arxiv.org/abs/2510.14960) · [PDF](https://arxiv.org/pdf/2510.14960.pdf)  
**作者**：Shizun Wang, Zhenxiang Jiang, Xingyi Yang, Xinchao Wang  

**一句话要点**：提出C4D框架，利用双对应关系从单目视频恢复4D动态场景

**关键词**：4D重建, 单目视频, 点跟踪, 动态场景优化, 多视图几何

## 3 点简述
- 核心问题：单目视频中动态物体违反多视图几何约束，导致4D重建不准确
- 方法要点：结合短时光流和长时点跟踪，训练动态感知跟踪器分离运动元素
- 实验效果：在深度估计、相机姿态估计和点跟踪等任务中表现优异

## 摘要（原文）

> Recovering 4D from monocular video, which jointly estimates dynamic geometry
> and camera poses, is an inevitably challenging problem. While recent
> pointmap-based 3D reconstruction methods (e.g., DUSt3R) have made great
> progress in reconstructing static scenes, directly applying them to dynamic
> scenes leads to inaccurate results. This discrepancy arises because moving
> objects violate multi-view geometric constraints, disrupting the
> reconstruction. To address this, we introduce C4D, a framework that leverages
> temporal Correspondences to extend existing 3D reconstruction formulation to
> 4D. Specifically, apart from predicting pointmaps, C4D captures two types of
> correspondences: short-term optical flow and long-term point tracking. We train
> a dynamic-aware point tracker that provides additional mobility information,
> facilitating the estimation of motion masks to separate moving elements from
> the static background, thus offering more reliable guidance for dynamic scenes.
> Furthermore, we introduce a set of dynamic scene optimization objectives to
> recover per-frame 3D geometry and camera parameters. Simultaneously, the
> correspondences lift 2D trajectories into smooth 3D trajectories, enabling
> fully integrated 4D reconstruction. Experiments show that our framework
> achieves complete 4D recovery and demonstrates strong performance across
> multiple downstream tasks, including depth estimation, camera pose estimation,
> and point tracking. Project Page: https://littlepure2333.github.io/C4D

