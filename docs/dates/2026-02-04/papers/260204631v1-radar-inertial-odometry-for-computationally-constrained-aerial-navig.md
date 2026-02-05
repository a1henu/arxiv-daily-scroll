---
layout: default
title: Radar-Inertial Odometry For Computationally Constrained Aerial Navigation
---

# Radar-Inertial Odometry For Computationally Constrained Aerial Navigation
**arXiv**：[2602.04631v1](https://arxiv.org/abs/2602.04631) · [PDF](https://arxiv.org/pdf/2602.04631.pdf)  
**作者**：Jan Michalczyk  

**一句话要点**：提出雷达-惯性里程计算法，用于资源受限无人机在极端环境下的实时导航

**关键词**：雷达-惯性里程计, 无人机导航, 传感器融合, 扩展卡尔曼滤波, 因子图, 深度学习

## 3 点简述
- 核心问题：传统外感传感器在极端环境（如烟雾、光照变化）中失效，影响无人机自主导航精度。
- 方法要点：基于多状态紧耦合EKF和因子图，融合低成本FMCW雷达的3D点云速度与距离信息及IMU数据。
- 实验或效果：算法能在便携式资源受限嵌入式计算机上实时运行，利用深度学习改进稀疏噪声雷达点云的3D点对应关系。

## 摘要（原文）

> Recently, the progress in the radar sensing technology consisting in the miniaturization of the packages and increase in measuring precision has drawn the interest of the robotics research community. Indeed, a crucial task enabling autonomy in robotics is to precisely determine the pose of the robot in space. To fulfill this task sensor fusion algorithms are often used, in which data from one or several exteroceptive sensors like, for example, LiDAR, camera, laser ranging sensor or GNSS are fused together with the Inertial Measurement Unit (IMU) measurements to obtain an estimate of the navigation states of the robot. Nonetheless, owing to their particular sensing principles, some exteroceptive sensors are often incapacitated in extreme environmental conditions, like extreme illumination or presence of fine particles in the environment like smoke or fog. Radars are largely immune to aforementioned factors thanks to the characteristics of electromagnetic waves they use. In this thesis, we present Radar-Inertial Odometry (RIO) algorithms to fuse the information from IMU and radar in order to estimate the navigation states of a (Uncrewed Aerial Vehicle) UAV capable of running on a portable resource-constrained embedded computer in real-time and making use of inexpensive, consumer-grade sensors. We present novel RIO approaches relying on the multi-state tightly-coupled Extended Kalman Filter (EKF) and Factor Graphs (FG) fusing instantaneous velocities of and distances to 3D points delivered by a lightweight, low-cost, off-the-shelf Frequency Modulated Continuous Wave (FMCW) radar with IMU readings. We also show a novel way to exploit advances in deep learning to retrieve 3D point correspondences in sparse and noisy radar point clouds.

