---
layout: default
title: AgriGS-SLAM: Orchard Mapping Across Seasons via Multi-View Gaussian Splatting SLAM
---

# AgriGS-SLAM: Orchard Mapping Across Seasons via Multi-View Gaussian Splatting SLAM
**arXiv**：[2510.26358v1](https://arxiv.org/abs/2510.26358) · [PDF](https://arxiv.org/pdf/2510.26358.pdf)  
**作者**：Mirko Usuelli, David Rapado-Rincon, Gert Kootstra, Matteo Matteucci  

**一句话要点**：提出AgriGS-SLAM以解决果园多季节实时3D建图问题

**关键词**：视觉-LiDAR SLAM, 3D高斯泼溅, 果园建图, 多季节鲁棒性, 实时系统

## 3 点简述
- 果园机器人需应对重复几何、季节变化和风动干扰的实时3D感知挑战
- 结合LiDAR里程计与多视角3D高斯泼溅渲染，优化姿态和地图细节
- 在苹果和梨园多季节测试中，重建更清晰稳定，保持实时性能

## 摘要（原文）

> Autonomous robots in orchards require real-time 3D scene understanding
> despite repetitive row geometry, seasonal appearance changes, and wind-driven
> foliage motion. We present AgriGS-SLAM, a Visual--LiDAR SLAM framework that
> couples direct LiDAR odometry and loop closures with multi-camera 3D Gaussian
> Splatting (3DGS) rendering. Batch rasterization across complementary viewpoints
> recovers orchard structure under occlusions, while a unified gradient-driven
> map lifecycle executed between keyframes preserves fine details and bounds
> memory. Pose refinement is guided by a probabilistic LiDAR-based depth
> consistency term, back-propagated through the camera projection to tighten
> geometry-appearance coupling. We deploy the system on a field platform in apple
> and pear orchards across dormancy, flowering, and harvesting, using a
> standardized trajectory protocol that evaluates both training-view and
> novel-view synthesis to reduce 3DGS overfitting in evaluation. Across seasons
> and sites, AgriGS-SLAM delivers sharper, more stable reconstructions and
> steadier trajectories than recent state-of-the-art 3DGS-SLAM baselines while
> maintaining real-time performance on-tractor. While demonstrated in orchard
> monitoring, the approach can be applied to other outdoor domains requiring
> robust multimodal perception.

