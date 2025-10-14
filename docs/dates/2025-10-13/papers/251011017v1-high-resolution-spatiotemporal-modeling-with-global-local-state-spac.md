---
layout: default
title: High-Resolution Spatiotemporal Modeling with Global-Local State Space Models for Video-Based Human Pose Estimation
---

# High-Resolution Spatiotemporal Modeling with Global-Local State Space Models for Video-Based Human Pose Estimation
**arXiv**：[2510.11017v1](https://arxiv.org/abs/2510.11017) · [PDF](https://arxiv.org/pdf/2510.11017.pdf)  
**作者**：Runyang Feng, Hyung Jin Chang, Tze Ho Elden Tse, Boeun Kim, Yi Chang, Yixing Gao  

**一句话要点**：提出全局-局部状态空间模型以解决视频人体姿态估计中的高分辨率时空建模问题

**关键词**：视频人体姿态估计, 状态空间模型, 高分辨率时空建模, 全局-局部动态建模, 线性复杂度, Mamba扩展

## 3 点简述
- 现有方法难以平衡全局与局部动态建模，且全局依赖捕获复杂度高
- 扩展Mamba模型，分别设计全局和局部模块以高效提取时空表示
- 在多个基准数据集上优于现有方法，并实现更好的计算权衡

## 摘要（原文）

> Modeling high-resolution spatiotemporal representations, including both
> global dynamic contexts (e.g., holistic human motion tendencies) and local
> motion details (e.g., high-frequency changes of keypoints), is essential for
> video-based human pose estimation (VHPE). Current state-of-the-art methods
> typically unify spatiotemporal learning within a single type of modeling
> structure (convolution or attention-based blocks), which inherently have
> difficulties in balancing global and local dynamic modeling and may bias the
> network to one of them, leading to suboptimal performance. Moreover, existing
> VHPE models suffer from quadratic complexity when capturing global
> dependencies, limiting their applicability especially for high-resolution
> sequences. Recently, the state space models (known as Mamba) have demonstrated
> significant potential in modeling long-range contexts with linear complexity;
> however, they are restricted to 1D sequential data. In this paper, we present a
> novel framework that extends Mamba from two aspects to separately learn global
> and local high-resolution spatiotemporal representations for VHPE.
> Specifically, we first propose a Global Spatiotemporal Mamba, which performs 6D
> selective space-time scan and spatial- and temporal-modulated scan merging to
> efficiently extract global representations from high-resolution sequences. We
> further introduce a windowed space-time scan-based Local Refinement Mamba to
> enhance the high-frequency details of localized keypoint motions. Extensive
> experiments on four benchmark datasets demonstrate that the proposed model
> outperforms state-of-the-art VHPE approaches while achieving better
> computational trade-offs.

