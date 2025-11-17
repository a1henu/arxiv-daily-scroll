---
layout: default
title: Simulating an Autonomous System in CARLA using ROS 2
---

# Simulating an Autonomous System in CARLA using ROS 2
**arXiv**：[2511.11310v1](https://arxiv.org/abs/2511.11310) · [PDF](https://arxiv.org/pdf/2511.11310.pdf)  
**作者**：Joseph Abdo, Aditya Shibu, Moaiz Saeed, Abdul Maajid Aga, Apsara Sivaprazad, Mohamed Al-Musleh  

**一句话要点**：提出基于ROS 2的自主赛车软件栈，在CARLA中模拟高速竞速场景。

**关键词**：自主竞速, ROS 2集成, 传感器融合, 轨迹优化, CARLA模拟

## 3 点简述
- 核心问题：在高速自主竞速中，感知、规划与控制面临不确定性和动态挑战。
- 方法要点：使用LiDAR、相机、GNSS和IMU传感器，通过ROS 2实现轨迹优化和边界检测。
- 实验或效果：在CARLA中验证系统，检测锥桶距离达35米，并移植到实际硬件。

## 摘要（原文）

> Autonomous racing offers a rigorous setting to stress test perception, planning, and control under high speed and uncertainty. This paper proposes an approach to design and evaluate a software stack for an autonomous race car in CARLA: Car Learning to Act simulator, targeting competitive driving performance in the Formula Student UK Driverless (FS-AI) 2025 competition. By utilizing a 360° light detection and ranging (LiDAR), stereo camera, global navigation satellite system (GNSS), and inertial measurement unit (IMU) sensor via ROS 2 (Robot Operating System), the system reliably detects the cones marking the track boundaries at distances of up to 35 m. Optimized trajectories are computed considering vehicle dynamics and simulated environmental factors such as visibility and lighting to navigate the track efficiently. The complete autonomous stack is implemented in ROS 2 and validated extensively in CARLA on a dedicated vehicle (ADS-DV) before being ported to the actual hardware, which includes the Jetson AGX Orin 64GB, ZED2i Stereo Camera, Robosense Helios 16P LiDAR, and CHCNAV Inertial Navigation System (INS).

