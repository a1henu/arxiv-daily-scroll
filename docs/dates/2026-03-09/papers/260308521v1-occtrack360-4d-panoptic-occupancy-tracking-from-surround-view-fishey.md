---
layout: default
title: OccTrack360: 4D Panoptic Occupancy Tracking from Surround-View Fisheye Cameras
---

# OccTrack360: 4D Panoptic Occupancy Tracking from Surround-View Fisheye Cameras
**arXiv**：[2603.08521v1](https://arxiv.org/abs/2603.08521) · [PDF](https://arxiv.org/pdf/2603.08521.pdf)  
**作者**：Yongzhi Lin, Kai Luo, Yuanfan Zheng, Hao Shi, Mengfei Duan, Yang Liu, Kailun Yang  

**一句话要点**：提出OccTrack360基准与FoSOcc框架，以解决环视鱼眼相机4D全景占用跟踪问题。

**关键词**：4D全景占用跟踪, 环视鱼眼相机, 体素可见性标注, 球面投影模型, 实例级跟踪, 长序列基准

## 3 点简述
- 核心问题：缺乏支持环视鱼眼感知、长序列和实例级体素跟踪的4D全景占用跟踪基准。
- 方法要点：引入OccTrack360基准，提供长序列和体素可见性标注；提出FoSOcc框架，包含中心聚焦模块和球面提升模块以处理鱼眼失真。
- 实验或效果：在Occ3D-Waymo和OccTrack360上验证，提升占用跟踪质量，尤其在几何规则类别上表现显著。

## 摘要（原文）

> Understanding dynamic 3D environments in a spatially continuous and temporally consistent manner is fundamental for robotics and autonomous driving. While recent advances in occupancy prediction provide a unified representation of scene geometry and semantics, progress in 4D panoptic occupancy tracking remains limited by the lack of benchmarks that support surround-view fisheye sensing, long temporal sequences, and instance-level voxel tracking. To address this gap, we present OccTrack360, a new benchmark for 4D panoptic occupancy tracking from surround-view fisheye cameras. OccTrack360 provides substantially longer and more diverse sequences (174~2234 frames) than prior benchmarks, together with principled voxel visibility annotations, including an all-direction occlusion mask and an MEI-based fisheye field-of-view mask. To establish a strong fisheye-oriented baseline, we further propose Focus on Sphere Occ (FoSOcc), a framework that addresses two core challenges in fisheye occupancy tracking: distorted spherical projection and inaccurate voxel-space localization. FoSOcc includes a Center Focusing Module (CFM) to enhance instance-aware spatial localization through supervised focus guidance, and a Spherical Lift Module (SLM) that extends perspective lifting to fisheye imaging under the Unified Projection Model. Extensive experiments on Occ3D-Waymo and OccTrack360 show that our method improves occupancy tracking quality with notable gains on geometrically regular categories, and establishes a strong baseline for future research on surround-view fisheye 4D occupancy tracking. The benchmark and source code will be made publicly available at https://github.com/YouthZest-Lin/OccTrack360.

