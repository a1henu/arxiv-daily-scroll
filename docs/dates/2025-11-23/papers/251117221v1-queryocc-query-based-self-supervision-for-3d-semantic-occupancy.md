---
layout: default
title: QueryOcc: Query-based Self-Supervision for 3D Semantic Occupancy
---

# QueryOcc: Query-based Self-Supervision for 3D Semantic Occupancy
**arXiv**：[2511.17221v1](https://arxiv.org/abs/2511.17221) · [PDF](https://arxiv.org/pdf/2511.17221.pdf)  
**作者**：Adam Lilja, Ji Lan, Junsheng Fu, Lars Hammarstrand  

**一句话要点**：提出QueryOcc框架，通过4D查询实现自监督3D语义占据学习，用于自动驾驶场景。

**关键词**：3D语义占据, 自监督学习, 查询机制, 自动驾驶, 4D时空建模, 压缩场景表示

## 3 点简述
- 核心问题：从图像学习3D场景几何与语义，但大规模3D标注成本高，现有方法空间精度和可扩展性有限。
- 方法要点：使用独立4D时空查询直接学习连续3D语义占据，支持伪点云或原始激光雷达监督。
- 实验效果：在自监督Occ3D-nuScenes基准上，语义RayIoU提升26%，运行速度11.6 FPS。

## 摘要（原文）

> Learning 3D scene geometry and semantics from images is a core challenge in computer vision and a key capability for autonomous driving. Since large-scale 3D annotation is prohibitively expensive, recent work explores self-supervised learning directly from sensor data without manual labels. Existing approaches either rely on 2D rendering consistency, where 3D structure emerges only implicitly, or on discretized voxel grids from accumulated lidar point clouds, limiting spatial precision and scalability. We introduce QueryOcc, a query-based self-supervised framework that learns continuous 3D semantic occupancy directly through independent 4D spatio-temporal queries sampled across adjacent frames. The framework supports supervision from either pseudo-point clouds derived from vision foundation models or raw lidar data. To enable long-range supervision and reasoning under constant memory, we introduce a contractive scene representation that preserves near-field detail while smoothly compressing distant regions. QueryOcc surpasses previous camera-based methods by 26% in semantic RayIoU on the self-supervised Occ3D-nuScenes benchmark while running at 11.6 FPS, demonstrating that direct 4D query supervision enables strong self-supervised occupancy learning. https://research.zenseact.com/publications/queryocc/

