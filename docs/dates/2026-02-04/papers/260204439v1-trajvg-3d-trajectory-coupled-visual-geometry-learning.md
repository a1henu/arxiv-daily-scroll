---
layout: default
title: TrajVG: 3D Trajectory-Coupled Visual Geometry Learning
---

# TrajVG: 3D Trajectory-Coupled Visual Geometry Learning
**arXiv**：[2602.04439v1](https://arxiv.org/abs/2602.04439) · [PDF](https://arxiv.org/pdf/2602.04439.pdf)  
**作者**：Xingyu Miao, Weiguang Zhao, Tao Lu, Linning Yu, Mulin Yu, Yang Long, Jiangmiao Pang, Junting Dong  

**一句话要点**：提出TrajVG框架，通过估计相机坐标系3D轨迹解决视频中物体运动导致的多帧3D重建退化问题。

**关键词**：3D重建, 视频几何学习, 轨迹耦合, 几何一致性, 混合监督训练, 多帧对齐

## 3 点简述
- 核心问题：前馈多帧3D重建模型在物体运动视频中性能下降，全局参考模糊，局部点图依赖相对位姿估计易漂移。
- 方法要点：耦合稀疏轨迹、逐帧局部点图和相对相机位姿，引入几何一致性目标，包括双向轨迹-点图一致性和静态锚点驱动的位姿一致性。
- 实验或效果：在3D跟踪、位姿估计、点图重建和视频深度任务上超越前馈性能基线，支持混合监督训练。

## 摘要（原文）

> Feed-forward multi-frame 3D reconstruction models often degrade on videos with object motion. Global-reference becomes ambiguous under multiple motions, while the local pointmap relies heavily on estimated relative poses and can drift, causing cross-frame misalignment and duplicated structures. We propose TrajVG, a reconstruction framework that makes cross-frame 3D correspondence an explicit prediction by estimating camera-coordinate 3D trajectories. We couple sparse trajectories, per-frame local point maps, and relative camera poses with geometric consistency objectives: (i) bidirectional trajectory-pointmap consistency with controlled gradient flow, and (ii) a pose consistency objective driven by static track anchors that suppresses gradients from dynamic regions. To scale training to in-the-wild videos where 3D trajectory labels are scarce, we reformulate the same coupling constraints into self-supervised objectives using only pseudo 2D tracks, enabling unified training with mixed supervision. Extensive experiments across 3D tracking, pose estimation, pointmap reconstruction, and video depth show that TrajVG surpasses the current feedforward performance baseline.

