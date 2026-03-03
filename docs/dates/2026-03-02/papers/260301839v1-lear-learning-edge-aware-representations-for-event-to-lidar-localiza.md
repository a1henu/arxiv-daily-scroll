---
layout: default
title: LEAR: Learning Edge-Aware Representations for Event-to-LiDAR Localization
---

# LEAR: Learning Edge-Aware Representations for Event-to-LiDAR Localization
**arXiv**：[2603.01839v1](https://arxiv.org/abs/2603.01839) · [PDF](https://arxiv.org/pdf/2603.01839.pdf)  
**作者**：Kuangyi Chen, Jun Zhang, Yuxi Hu, Yi Zhou, Friedrich Fraundorfer  

**一句话要点**：提出LEAR框架，通过联合估计边缘结构和事件-深度流场，解决事件相机与LiDAR点云在GPS拒止环境下的定位问题。

**关键词**：事件相机定位, LiDAR点云对齐, 跨模态融合, 边缘感知流场, 双任务学习, GPS拒止环境

## 3 点简述
- 核心问题：稀疏异步事件与密集LiDAR地图对齐存在模态差异，直接对应估计困难。
- 方法要点：采用双任务学习框架，通过跨模态融合和迭代细化策略，耦合边缘与流场估计以注入几何线索。
- 实验或效果：在多个挑战性数据集上优于现有方法，通过PnP求解器实现更稳健的位姿恢复。

## 摘要（原文）

> Event cameras offer high-temporal-resolution sensing that remains reliable under high-speed motion and challenging lighting, making them promising for localization from LiDAR point clouds in GPS-denied and visually degraded environments. However, aligning sparse, asynchronous events with dense LiDAR maps is fundamentally ill-posed, as direct correspondence estimation suffers from modality gaps. We propose LEAR, a dual-task learning framework that jointly estimates edge structures and dense event-depth flow fields to bridge the sensing-modality divide. Instead of treating edges as a post-hoc aid, LEAR couples them with flow estimation through a cross-modal fusion mechanism that injects modality-invariant geometric cues into the motion representation, and an iterative refinement strategy that enforces mutual consistency between the two tasks over multiple update steps. This synergy produces edge-aware, depth-aligned flow fields that enable more robust and accurate pose recovery via Perspective-n-Point (PnP) solvers. On several popular and challenging datasets, LEAR achieves superior performance over the best prior method. The source code, trained models, and demo videos are made publicly available online.

