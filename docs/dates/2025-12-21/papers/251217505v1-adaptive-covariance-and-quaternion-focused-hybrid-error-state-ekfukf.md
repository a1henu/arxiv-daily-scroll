---
layout: default
title: Adaptive Covariance and Quaternion-Focused Hybrid Error-State EKF/UKF for Visual-Inertial Odometry
---

# Adaptive Covariance and Quaternion-Focused Hybrid Error-State EKF/UKF for Visual-Inertial Odometry
**arXiv**：[2512.17505v1](https://arxiv.org/abs/2512.17505) · [PDF](https://arxiv.org/pdf/2512.17505.pdf)  
**作者**：Ufuk Asil, Efendi Nasibov  

**一句话要点**：提出自适应协方差与四元数聚焦混合误差状态EKF/UKF方法，以提升无人机在复杂环境中的视觉惯性里程计性能。

**关键词**：视觉惯性里程计, 误差状态卡尔曼滤波, 四元数估计, 传感器融合, 无人机定位, 自适应协方差

## 3 点简述
- 核心问题：无人机视觉惯性里程计在环境挑战和传感器可靠性变化下，姿态估计精度和计算效率难以平衡。
- 方法要点：采用松散耦合传感器融合，结合误差状态EKF传播全状态和缩放无迹卡尔曼滤波精炼方向，动态评估视觉测量可靠性。
- 实验或效果：在EuRoC MAV数据集上，位置和旋转精度显著提升，计算成本降低约48%，平衡了效率与准确性。

## 摘要（原文）

> This study presents an innovative hybrid Visual-Inertial Odometry (VIO) method for Unmanned Aerial Vehicles (UAVs) that is resilient to environmental challenges and capable of dynamically assessing sensor reliability. Built upon a loosely coupled sensor fusion architecture, the system utilizes a novel hybrid Quaternion-focused Error-State EKF/UKF (Qf-ES-EKF/UKF) architecture to process inertial measurement unit (IMU) data. This architecture first propagates the entire state using an Error-State Extended Kalman Filter (ESKF) and then applies a targeted Scaled Unscented Kalman Filter (SUKF) step to refine only the orientation. This sequential process blends the accuracy of SUKF in quaternion estimation with the overall computational efficiency of ESKF. The reliability of visual measurements is assessed via a dynamic sensor confidence score based on metrics, such as image entropy, intensity variation, motion blur, and inference quality, adapting the measurement noise covariance to ensure stable pose estimation even under challenging conditions. Comprehensive experimental analyses on the EuRoC MAV dataset demonstrate key advantages: an average improvement of 49% in position accuracy in challenging scenarios, an average of 57% in rotation accuracy over ESKF-based methods, and SUKF-comparable accuracy achieved with approximately 48% lower computational cost than a full SUKF implementation. These findings demonstrate that the presented approach strikes an effective balance between computational efficiency and estimation accuracy, and significantly enhances UAV pose estimation performance in complex environments with varying sensor reliability.

