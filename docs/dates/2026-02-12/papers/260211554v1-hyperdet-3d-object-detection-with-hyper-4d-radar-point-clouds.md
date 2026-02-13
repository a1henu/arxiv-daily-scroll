---
layout: default
title: HyperDet: 3D Object Detection with Hyper 4D Radar Point Clouds
---

# HyperDet: 3D Object Detection with Hyper 4D Radar Point Clouds
**arXiv**：[2602.11554v1](https://arxiv.org/abs/2602.11554) · [PDF](https://arxiv.org/pdf/2602.11554.pdf)  
**作者**：Yichun Xiao, Runwei Guan, Fangqiang Ding  

**一句话要点**：提出HyperDet框架，通过构建超4D雷达点云以提升雷达仅3D检测性能

**关键词**：4D毫米波雷达, 3D目标检测, 点云增强, 一致性验证, 扩散模型, 知识蒸馏

## 3 点简述
- 核心问题：4D雷达点云稀疏、不规则且受多径噪声影响，导致几何信息弱且不稳定，雷达仅3D检测落后于激光雷达系统。
- 方法要点：聚合多雷达多帧数据，应用几何感知跨传感器一致性验证，集成前景聚焦扩散模块与混合雷达-激光雷达监督训练。
- 实验或效果：在MAN TruckScenes数据集上，HyperDet改进原始雷达输入，部分缩小雷达与激光雷达检测差距，无需修改检测器架构。

## 摘要（原文）

> 4D mmWave radar provides weather-robust, velocity-aware measurements and is more cost-effective than LiDAR. However, radar-only 3D detection still trails LiDAR-based systems because radar point clouds are sparse, irregular, and often corrupted by multipath noise, yielding weak and unstable geometry. We present HyperDet, a detector-agnostic radar-only 3D detection framework that constructs a task-aware hyper 4D radar point cloud for standard LiDAR-oriented detectors. HyperDet aggregates returns from multiple surround-view 4D radars over consecutive frames to improve coverage and density, then applies geometry-aware cross-sensor consensus validation with a lightweight self-consistency check outside overlap regions to suppress inconsistent returns. It further integrates a foreground-focused diffusion module with training-time mixed radar-LiDAR supervision to densify object structures while lifting radar attributes (e.g., Doppler, RCS); the model is distilled into a consistency model for single-step inference. On MAN TruckScenes, HyperDet consistently improves over raw radar inputs with VoxelNeXt and CenterPoint, partially narrowing the radar-LiDAR gap. These results show that input-level refinement enables radar to better leverage LiDAR-oriented detectors without architectural modifications.

