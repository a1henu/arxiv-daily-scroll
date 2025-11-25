---
layout: default
title: Stable Multi-Drone GNSS Tracking System for Marine Robots
---

# Stable Multi-Drone GNSS Tracking System for Marine Robots
**arXiv**：[2511.18694v1](https://arxiv.org/abs/2511.18694) · [PDF](https://arxiv.org/pdf/2511.18694.pdf)  
**作者**：Shuo Wen, Edwin Meriaux, Mariana Sosa Guzmán, Zhizun Wang, Junming Shi, Gregory Dudek  

**一句话要点**：提出多无人机GNSS跟踪系统以解决海洋机器人水下定位不可靠问题

**关键词**：海洋机器人定位, 多无人机跟踪, GNSS三角定位, 扩展卡尔曼滤波, 视觉检测, 跨无人机ID对齐

## 3 点简述
- 核心问题：GNSS信号在水下不可靠，传统方法存在误差累积或依赖基础设施
- 方法要点：结合视觉检测、多目标跟踪、GNSS三角定位和置信度加权EKF
- 实验或效果：在多样化复杂环境中验证了系统的可扩展性和鲁棒性

## 摘要（原文）

> Accurate localization is essential for marine robotics, yet Global Navigation Satellite System (GNSS) signals are unreliable or unavailable even at a very short distance below the water surface. Traditional alternatives, such as inertial navigation, Doppler Velocity Loggers (DVL), SLAM, and acoustic methods, suffer from error accumulation, high computational demands, or infrastructure dependence. In this work, we present a scalable multi-drone GNSS-based tracking system for surface and near-surface marine robots. Our approach combines efficient visual detection, lightweight multi-object tracking, GNSS-based triangulation, and a confidence-weighted Extended Kalman Filter (EKF) to provide stable GNSS estimation in real time. We further introduce a cross-drone tracking ID alignment algorithm that enforces global consistency across views, enabling robust multi-robot tracking with redundant aerial coverage. We validate our system in diversified complex settings to show the scalability and robustness of the proposed algorithm.

