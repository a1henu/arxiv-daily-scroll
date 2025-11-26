---
layout: default
title: AMB3R: Accurate Feed-forward Metric-scale 3D Reconstruction with Backend
---

# AMB3R: Accurate Feed-forward Metric-scale 3D Reconstruction with Backend
**arXiv**：[2511.20343v1](https://arxiv.org/abs/2511.20343) · [PDF](https://arxiv.org/pdf/2511.20343.pdf)  
**作者**：Hengyi Wang, Lourdes Agapito  

**一句话要点**：提出AMB3R模型以解决多视角度量尺度3D重建问题

**关键词**：多视角3D重建, 度量尺度估计, 前馈模型, 体素表示, 视觉里程计, 结构从运动

## 3 点简述
- 核心问题：多视角3D重建在度量尺度下的密集重建与泛化任务挑战
- 方法要点：使用稀疏紧凑体素后端实现前馈几何推理，无需任务微调
- 实验或效果：在相机位姿、深度估计和3D重建上超越现有方法，优于优化SLAM

## 摘要（原文）

> We present AMB3R, a multi-view feed-forward model for dense 3D reconstruction on a metric-scale that addresses diverse 3D vision tasks. The key idea is to leverage a sparse, yet compact, volumetric scene representation as our backend, enabling geometric reasoning with spatial compactness. Although trained solely for multi-view reconstruction, we demonstrate that AMB3R can be seamlessly extended to uncalibrated visual odometry (online) or large-scale structure from motion without the need for task-specific fine-tuning or test-time optimization. Compared to prior pointmap-based models, our approach achieves state-of-the-art performance in camera pose, depth, and metric-scale estimation, 3D reconstruction, and even surpasses optimization-based SLAM and SfM methods with dense reconstruction priors on common benchmarks.

