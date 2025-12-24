---
layout: default
title: Drift-Corrected Monocular VIO and Perception-Aware Planning for Autonomous Drone Racing
---

# Drift-Corrected Monocular VIO and Perception-Aware Planning for Autonomous Drone Racing
**arXiv**：[2512.20475v1](https://arxiv.org/abs/2512.20475) · [PDF](https://arxiv.org/pdf/2512.20475.pdf)  
**作者**：Maulana Bisyir Azhari, Donghun Han, Je In You, Sungjun Park, David Hyunchul Shim  

**一句话要点**：提出融合VIO与YOLO门检测的漂移校正方法及感知感知规划器，用于单目视觉自主无人机竞速。

**关键词**：单目视觉惯性里程计, 漂移校正, 感知感知规划, 无人机竞速, 卡尔曼滤波, YOLO目标检测

## 3 点简述
- 核心问题：单目相机和低质量IMU在高速飞行中易导致VIO漂移，影响定位精度。
- 方法要点：使用卡尔曼滤波器融合VIO输出与基于YOLO的门检测全局位置，校正漂移；设计感知感知规划器平衡速度与门可见性。
- 实验或效果：在A2RL x DCL竞赛中获多项佳绩，如AI Grand Challenge第三名（最高速43.2 km/h），验证系统高性能。

## 摘要（原文）

> The Abu Dhabi Autonomous Racing League(A2RL) x Drone Champions League competition(DCL) requires teams to perform high-speed autonomous drone racing using only a single camera and a low-quality inertial measurement unit -- a minimal sensor set that mirrors expert human drone racing pilots. This sensor limitation makes the system susceptible to drift from Visual-Inertial Odometry (VIO), particularly during long and fast flights with aggressive maneuvers. This paper presents the system developed for the championship, which achieved a competitive performance. Our approach corrected VIO drift by fusing its output with global position measurements derived from a YOLO-based gate detector using a Kalman filter. A perception-aware planner generated trajectories that balance speed with the need to keep gates visible for the perception system. The system demonstrated high performance, securing podium finishes across multiple categories: third place in the AI Grand Challenge with top speed of 43.2 km/h, second place in the AI Drag Race with over 59 km/h, and second place in the AI Multi-Drone Race. We detail the complete architecture and present a performance analysis based on experimental data from the competition, contributing our insights on building a successful system for monocular vision-based autonomous drone flight.

