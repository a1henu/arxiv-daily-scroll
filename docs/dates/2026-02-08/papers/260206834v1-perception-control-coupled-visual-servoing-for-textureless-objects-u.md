---
layout: default
title: Perception-Control Coupled Visual Servoing for Textureless Objects Using Keypoint-Based EKF
---

# Perception-Control Coupled Visual Servoing for Textureless Objects Using Keypoint-Based EKF
**arXiv**：[2602.06834v1](https://arxiv.org/abs/2602.06834) · [PDF](https://arxiv.org/pdf/2602.06834.pdf)  
**作者**：Allen Tao, Jun Yang, Stanko Oparnica, Wenjie Xue  

**一句话要点**：提出基于关键点EKF的感知-控制耦合视觉伺服方法，以解决纹理缺失物体在遮挡等恶劣条件下的定位与控制问题。

**关键词**：视觉伺服, 纹理缺失物体, 扩展卡尔曼滤波器, 关键点检测, 感知-控制耦合, 概率控制

## 3 点简述
- 核心问题：纹理缺失物体因缺乏可靠视觉特征，在遮挡等恶劣条件下视觉伺服精度低、不稳定。
- 方法要点：采用扩展卡尔曼滤波器整合关键点检测，估计6D位姿驱动位姿基视觉伺服，并引入概率控制律计算相机速度及不确定性。
- 实验或效果：在真实机器人平台上验证，方法在精度和实际应用中优于传统视觉伺服技术。

## 摘要（原文）

> Visual servoing is fundamental to robotic applications, enabling precise positioning and control. However, applying it to textureless objects remains a challenge due to the absence of reliable visual features. Moreover, adverse visual conditions, such as occlusions, often corrupt visual feedback, leading to reduced accuracy and instability in visual servoing. In this work, we build upon learning-based keypoint detection for textureless objects and propose a method that enhances robustness by tightly integrating perception and control in a closed loop. Specifically, we employ an Extended Kalman Filter (EKF) that integrates per-frame keypoint measurements to estimate 6D object pose, which drives pose-based visual servoing (PBVS) for control. The resulting camera motion, in turn, enhances the tracking of subsequent keypoints, effectively closing the perception-control loop. Additionally, unlike standard PBVS, we propose a probabilistic control law that computes both camera velocity and its associated uncertainty, enabling uncertainty-aware control for safe and reliable operation. We validate our approach on real-world robotic platforms using quantitative metrics and grasping experiments, demonstrating that our method outperforms traditional visual servoing techniques in both accuracy and practical application.

