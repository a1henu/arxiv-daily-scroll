---
layout: default
title: Semi-distributed Cross-modal Air-Ground Relative Localization
---

# Semi-distributed Cross-modal Air-Ground Relative Localization
**arXiv**：[2511.06749v1](https://arxiv.org/abs/2511.06749) · [PDF](https://arxiv.org/pdf/2511.06749.pdf)  
**作者**：Weining Lu, Deer Bin, Lian Ma, Ming Ma, Zhihao Ma, Xiangyang Chen, Longfei Wang, Yixiao Feng, Zhouxian Jiang, Yongliang Shi, Bin Liang  

**一句话要点**：提出半分布式跨模态空地相对定位框架，以提升协作任务中的灵活性与准确性。

**关键词**：相对定位, 跨模态SLAM, 半分布式系统, 深度学习关键点, 通信带宽优化

## 3 点简述
- 核心问题：传统多机器人SLAM系统传感器配置相同，耦合状态估计，限制灵活性与准确性。
- 方法要点：UGV和UAV独立SLAM，提取深度学习关键点与描述符，解耦相对定位与状态估计。
- 实验效果：方法在精度和效率上表现优异，通信带宽控制在0.3 Mbps以下。

## 摘要（原文）

> Efficient, accurate, and flexible relative localization is crucial in
> air-ground collaborative tasks. However, current approaches for robot relative
> localization are primarily realized in the form of distributed multi-robot SLAM
> systems with the same sensor configuration, which are tightly coupled with the
> state estimation of all robots, limiting both flexibility and accuracy. To this
> end, we fully leverage the high capacity of Unmanned Ground Vehicle (UGV) to
> integrate multiple sensors, enabling a semi-distributed cross-modal air-ground
> relative localization framework. In this work, both the UGV and the Unmanned
> Aerial Vehicle (UAV) independently perform SLAM while extracting deep
> learning-based keypoints and global descriptors, which decouples the relative
> localization from the state estimation of all agents. The UGV employs a local
> Bundle Adjustment (BA) with LiDAR, camera, and an IMU to rapidly obtain
> accurate relative pose estimates. The BA process adopts sparse keypoint
> optimization and is divided into two stages: First, optimizing camera poses
> interpolated from LiDAR-Inertial Odometry (LIO), followed by estimating the
> relative camera poses between the UGV and UAV. Additionally, we implement an
> incremental loop closure detection algorithm using deep learning-based
> descriptors to maintain and retrieve keyframes efficiently. Experimental
> results demonstrate that our method achieves outstanding performance in both
> accuracy and efficiency. Unlike traditional multi-robot SLAM approaches that
> transmit images or point clouds, our method only transmits keypoint pixels and
> their descriptors, effectively constraining the communication bandwidth under
> 0.3 Mbps. Codes and data will be publicly available on
> https://github.com/Ascbpiac/cross-model-relative-localization.git.

