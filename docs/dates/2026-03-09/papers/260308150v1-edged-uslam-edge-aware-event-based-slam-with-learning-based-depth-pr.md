---
layout: default
title: Edged USLAM: Edge-Aware Event-Based SLAM with Learning-Based Depth Priors
---

# Edged USLAM: Edge-Aware Event-Based SLAM with Learning-Based Depth Priors
**arXiv**：[2603.08150v1](https://arxiv.org/abs/2603.08150) · [PDF](https://arxiv.org/pdf/2603.08150.pdf)  
**作者**：Şebnem Sarıözkan, Hürkan Şahin, Olaya Álvarez-Tuñón, Erdal Kayacan  

**一句话要点**：提出Edged USLAM，结合边缘感知前端与深度先验，提升事件相机在结构化场景下的SLAM稳定性。

**关键词**：事件相机SLAM, 视觉-惯性融合, 边缘感知处理, 深度先验学习, 无人机导航

## 3 点简述
- 核心问题：传统视觉SLAM在快速运动或光照变化下易失效，事件相机输出稀疏异步，集成困难。
- 方法要点：扩展USLAM，前端增强事件帧以补偿非线性运动，深度模块提供粗粒度深度先验。
- 实验或效果：在慢速或结构化轨迹中表现稳定，无人机飞行验证了在挑战性光照下的定位准确性。

## 摘要（原文）

> Conventional visual simultaneous localization and mapping (SLAM) algorithms often fail under rapid motion, low illumination, or abrupt lighting transitions due to motion blur and limited dynamic range. Event cameras mitigate these issues with high temporal resolution and high dynamic range (HDR), but their sparse, asynchronous outputs complicate feature extraction and integration with other sensors; e.g. inertial measurement units (IMUs) and standard cameras. We present Edged USLAM, a hybrid visual-inertial system that extends Ultimate SLAM (USLAM) with an edge-aware front-end and a lightweight depth module. The frontend enhances event frames for robust feature tracking and nonlinear motion compensation, while the depth module provides coarse, region-of-interest (ROI)-based scene depth to improve motion compensation and scale consistency. Evaluations across public benchmarks and real-world unmanned air vehicle (UAV) flights demonstrate that performance varies significantly by scenario. For instance, event-only methods like point-line event-based visual-inertial odometry (PL-EVIO) or learning-based pipelines such as deep event-based visual odometry (DEVO) excel in highly aggressive or extreme HDR conditions. In contrast, Edged USLAM provides superior stability and minimal drift in slow or structured trajectories, ensuring consistently accurate localization on real flights under challenging illumination. These findings highlight the complementary strengths of event-only, learning-based, and hybrid approaches, while positioning Edged USLAM as a robust solution for diverse aerial navigation tasks.

