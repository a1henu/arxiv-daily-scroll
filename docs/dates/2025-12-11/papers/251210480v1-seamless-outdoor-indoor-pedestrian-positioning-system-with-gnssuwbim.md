---
layout: default
title: Seamless Outdoor-Indoor Pedestrian Positioning System with GNSS/UWB/IMU Fusion: A Comparison of EKF, FGO, and PF
---

# Seamless Outdoor-Indoor Pedestrian Positioning System with GNSS/UWB/IMU Fusion: A Comparison of EKF, FGO, and PF
**arXiv**：[2512.10480v1](https://arxiv.org/abs/2512.10480) · [PDF](https://arxiv.org/pdf/2512.10480.pdf)  
**作者**：Jiaqiang Zhang, Xianjia Yu, Sier Ha, Paola Torrico Moron, Sahar Salimpour, Farhad Kerama, Haizhou Zhang, Tomi Westerlund  

**一句话要点**：提出GNSS/UWB/IMU融合框架，比较EKF、FGO和PF在无缝室外-室内行人定位中的性能。

**关键词**：行人定位, 传感器融合, 扩展卡尔曼滤波, 因子图优化, 粒子滤波, 室外-室内无缝定位

## 3 点简述
- 核心问题：室外-室内行人定位因GNSS、UWB和IMU信号脆弱而难以连续准确。
- 方法要点：融合GNSS/UWB/IMU，引入基于OpenStreetMap的轻量级地图约束增强过渡鲁棒性。
- 实验或效果：在ROS 2实时平台上评估，ESKF在实现中表现最一致。

## 摘要（原文）

> Accurate and continuous pedestrian positioning across outdoor-indoor environments remains challenging because GNSS, UWB, and inertial PDR are complementary yet individually fragile under signal blockage, multipath, and drift. This paper presents a unified GNSS/UWB/IMU fusion framework for seamless pedestrian localization and provides a controlled comparison of three probabilistic back-ends: an error-state extended Kalman filter, sliding-window factor graph optimization, and a particle filter. The system uses chest-mounted IMU-based PDR as the motion backbone and integrates absolute updates from GNSS outdoors and UWB indoors. To enhance transition robustness and mitigate urban GNSS degradation, we introduce a lightweight map-based feasibility constraint derived from OpenStreetMap building footprints, treating most building interiors as non-navigable while allowing motion inside a designated UWB-instrumented building. The framework is implemented in ROS 2 and runs in real time on a wearable platform, with visualization in Foxglove. We evaluate three scenarios: indoor (UWB+PDR), outdoor (GNSS+PDR), and seamless outdoor-indoor (GNSS+UWB+PDR). Results show that the ESKF provides the most consistent overall performance in our implementation.

