---
layout: default
title: Dual Preintegration for Relative State Estimation
---

# Dual Preintegration for Relative State Estimation
**arXiv**：[2511.21189v1](https://arxiv.org/abs/2511.21189) · [PDF](https://arxiv.org/pdf/2511.21189.pdf)  
**作者**：Ruican Xia, Hailong Pei  

**一句话要点**：提出双预积分方法以提升VR控制器跟踪中的相对状态估计精度

**关键词**：相对状态估计, IMU预积分, 虚拟现实跟踪, 运动学约束, 非线性旋转, 状态估计精度

## 3 点简述
- 核心问题：相对状态估计在非线性旋转下精度下降，线性化误差导致漂移和不一致。
- 方法要点：基于IMU预积分理论，引入双平台预积分作为运动学约束，支持高效重线性化。
- 实验或效果：仿真和真实实验显示，该方法在精度和鲁棒性上优于现有先进算法。

## 摘要（原文）

> Relative State Estimation perform mutually localization between two mobile agents undergoing six-degree-of-freedom motion. Based on the principle of circular motion, the estimation accuracy is sensitive to nonlinear rotations of the reference platform, particularly under large inter-platform distances. This phenomenon is even obvious for linearized kinematics, because cumulative linearization errors significantly degrade precision. In virtual reality (VR) applications, this manifests as substantial positional errors in 6-DoF controller tracking during rapid rotations of the head-mounted display. The linearization errors introduce drift in the estimate and render the estimator inconsistent. In the field of odometry, IMU preintegration is proposed as a kinematic observation to enable efficient relinearization, thus mitigate linearized error. Building on this theory, we propose dual preintegration, a novel observation integrating IMU preintegration from both platforms. This method serves as kinematic constraints for consecutive relative state and supports efficient relinearization. We also perform observability analysis of the state and analytically formulate the accordingly null space. Algorithm evaluation encompasses both simulations and real-world experiments. Multiple nonlinear rotations on the reference platform are simulated to compare the precision of the proposed method with that of other state-of-the-art (SOTA) algorithms. The field test compares the proposed method and SOTA algorithms in the application of VR controller tracking from the perspectives of bias observability, nonlinear rotation, and background texture. The results demonstrate that the proposed method is more precise and robust than the SOTA algorithms.

