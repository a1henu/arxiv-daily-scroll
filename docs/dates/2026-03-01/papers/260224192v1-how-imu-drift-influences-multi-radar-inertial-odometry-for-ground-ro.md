---
layout: default
title: How IMU Drift Influences Multi-Radar Inertial Odometry for Ground Robots in Subterranean Terrains
---

# How IMU Drift Influences Multi-Radar Inertial Odometry for Ground Robots in Subterranean Terrains
**arXiv**：[2602.24192v1](https://arxiv.org/abs/2602.24192) · [PDF](https://arxiv.org/pdf/2602.24192.pdf)  
**作者**：Moumita Mukherjee, Magnus Norén, Anton Koval, Avijit Banerjee, George Nikolakopoulos  

**一句话要点**：提出两阶段多雷达惯性里程计框架，以解决地下环境中IMU漂移对低成本雷达惯性里程计的影响。

**关键词**：雷达惯性里程计, IMU漂移校正, 地下环境定位, 多传感器融合, EKF滤波, 开源框架

## 3 点简述
- 核心问题：低成本IMU漂移和雷达数据稀疏噪声导致地下环境雷达惯性里程计不稳定。
- 方法要点：结合IMU偏差估计器和EKF在线校正，融合多雷达与IMU测量优化里程计。
- 实验或效果：地下实地试验中优于EKF-RIO，支持低成本雷达和不同IMU，提供开源代码。

## 摘要（原文）

> Reliable radar inertial odometry (RIO) requires mitigating IMU bias drift, a challenge that intensifies in subterranean environments due to extreme temperatures and gravity-induced accelerations. Cost-effective IMUs such as the Pixhawk, when paired with FMCW TI IWR6843AOP EVM radars, suffer from drift-induced degradation compounded by sparse, noisy, and flickering radar returns, making fusion less stable than LiDAR-based odometry. Yet, LiDAR fails under smoke, dust, and aerosols, whereas FMCW radars remain compact, lightweight, cost-effective, and robust in these situations. To address these challenges, we propose a two-stage MRIO framework that combines an IMU bias estimator for resilient localization and mapping in GPS-denied subterranean environments affected by smoke. Radar-based ego-velocity estimation is formulated through a least-squares approach and incorporated into an EKF for online IMU bias correction; the corrected IMU accelerations are fused with heterogeneous measurements from multiple radars and an IMU to refine odometry. The proposed framework further supports radar-only mapping by exploiting the robot's estimated translational and rotational displacements. In subterranean field trials, MRIO delivers robust localization and mapping, outperforming EKF-RIO. It maintains accuracy across cost-efficient FMCW radar setups and different IMUs, showing resilience with Pixhawk and higher-grade units such as VectorNav. The implementation will be provided as an open-source resource to the community (code available at https://github.com/LTU-RAI/MRIO

