---
layout: default
title: AgriGS-SLAM: Orchard Mapping Across Seasons via Multi-View Gaussian Splatting SLAM
---

# AgriGS-SLAM: Orchard Mapping Across Seasons via Multi-View Gaussian Splatting SLAM
**arXiv**：[2510.26358v1](https://arxiv.org/abs/2510.26358) · [PDF](https://arxiv.org/pdf/2510.26358.pdf)  
**作者**：Mirko Usuelli, David Rapado-Rincon, Gert Kootstra, Matteo Matteucci  

**一句话要点**：提出AgriGS-SLAM，结合视觉-LiDAR SLAM与多视角3D高斯泼溅，以解决果园跨季节映射问题。

**关键词**：视觉-LiDAR SLAM, 3D高斯泼溅, 果园映射, 多模态感知, 实时重建

## 3 点简述
- 核心问题：果园环境中重复几何、季节外观变化和风驱动叶动，需实时3D场景理解。
- 方法要点：耦合LiDAR里程计与多相机3D高斯泼溅渲染，通过批量栅格化和梯度驱动地图生命周期优化。
- 实验或效果：在苹果和梨园跨季节部署，提供更锐利重建和稳定轨迹，优于现有3DGS-SLAM基线。

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

