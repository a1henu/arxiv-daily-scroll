---
layout: default
title: Learning Vision-Based Omnidirectional Navigation: A Teacher-Student Approach Using Monocular Depth Estimation
---

# Learning Vision-Based Omnidirectional Navigation: A Teacher-Student Approach Using Monocular Depth Estimation
**arXiv**：[2603.01999v1](https://arxiv.org/abs/2603.01999) · [PDF](https://arxiv.org/pdf/2603.01999.pdf)  
**作者**：Jan Finke, Wayne Paul Martis, Adrian Schmelter, Lars Erbach, Christian Jestel, Marvin Wiedemann  

**一句话要点**：提出基于视觉的全向导航师生框架，利用单目深度估计替代2D LiDAR解决工业场景障碍物检测问题。

**关键词**：视觉导航, 师生蒸馏, 单目深度估计, 移动机器人, 障碍物避免, 工业应用

## 3 点简述
- 核心问题：2D LiDAR仅感知水平切片，易遗漏三维障碍物，如悬垂或低矮物体。
- 方法要点：教师策略用PPO训练，学生策略蒸馏至仅依赖四摄像头RGB的单目深度图。
- 实验效果：仿真成功率82-96.5%，优于2D LiDAR教师；实机测试在复杂三维障碍物导航中表现更优。

## 摘要（原文）

> Reliable obstacle avoidance in industrial settings demands 3D scene understanding, but widely used 2D LiDAR sensors perceive only a single horizontal slice of the environment, missing critical obstacles above or below the scan plane. We present a teacher-student framework for vision-based mobile robot navigation that eliminates the need for LiDAR sensors. A teacher policy trained via Proximal Policy Optimization (PPO) in NVIDIA Isaac Lab leverages privileged 2D LiDAR observations that account for the full robot footprint to learn robust navigation. The learned behavior is distilled into a student policy that relies solely on monocular depth maps predicted by a fine-tuned Depth Anything V2 model from four RGB cameras. The complete inference pipeline, comprising monocular depth estimation (MDE), policy execution, and motor control, runs entirely onboard an NVIDIA Jetson Orin AGX mounted on a DJI RoboMaster platform, requiring no external computation for inference. In simulation, the student achieves success rates of 82-96.5%, consistently outperforming the standard 2D LiDAR teacher (50-89%). In real-world experiments, the MDE-based student outperforms the 2D LiDAR teacher when navigating around obstacles with complex 3D geometries, such as overhanging structures and low-profile objects, that fall outside the single scan plane of a 2D LiDAR.

