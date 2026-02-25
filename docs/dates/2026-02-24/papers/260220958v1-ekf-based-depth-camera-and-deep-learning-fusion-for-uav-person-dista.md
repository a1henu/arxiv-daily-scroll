---
layout: default
title: EKF-Based Depth Camera and Deep Learning Fusion for UAV-Person Distance Estimation and Following in SAR Operations
---

# EKF-Based Depth Camera and Deep Learning Fusion for UAV-Person Distance Estimation and Following in SAR Operations
**arXiv**：[2602.20958v1](https://arxiv.org/abs/2602.20958) · [PDF](https://arxiv.org/pdf/2602.20958.pdf)  
**作者**：Luka Šiktar, Branimir Ćaran, Bojan Šekoranja, Marko Švaco  

**一句话要点**：提出基于EKF的深度相机与深度学习融合方法，用于无人机在搜救中估计和跟随人员距离。

**关键词**：无人机跟随, 距离估计, 深度相机融合, 扩展卡尔曼滤波, 搜救操作

## 3 点简述
- 核心问题：搜救中无人机需准确估计与目标人员的距离以确保安全跟随。
- 方法要点：融合深度相机测量和单目相机距离估计，使用YOLO-pose和EKF进行实时数据融合。
- 实验或效果：室内实时测试中，距离估计的平均误差、RMSE和标准差降低达15.3%。

## 摘要（原文）

> Search and rescue (SAR) operations require rapid responses to save lives or property. Unmanned Aerial Vehicles (UAVs) equipped with vision-based systems support these missions through prior terrain investigation or real-time assistance during the mission itself. Vision-based UAV frameworks aid human search tasks by detecting and recognizing specific individuals, then tracking and following them while maintaining a safe distance. A key safety requirement for UAV following is the accurate estimation of the distance between camera and target object under real-world conditions, achieved by fusing multiple image modalities. UAVs with deep learning-based vision systems offer a new approach to the planning and execution of SAR operations. As part of the system for automatic people detection and face recognition using deep learning, in this paper we present the fusion of depth camera measurements and monocular camera-to-body distance estimation for robust tracking and following. Deep learning-based filtering of depth camera data and estimation of camera-to-body distance from a monocular camera are achieved with YOLO-pose, enabling real-time fusion of depth information using the Extended Kalman Filter (EKF) algorithm. The proposed subsystem, designed for use in drones, estimates and measures the distance between the depth camera and the human body keypoints, to maintain the safe distance between the drone and the human target. Our system provides an accurate estimated distance, which has been validated against motion capture ground truth data. The system has been tested in real time indoors, where it reduces the average errors, root mean square error (RMSE) and standard deviations of distance estimation up to 15,3\% in three tested scenarios.

