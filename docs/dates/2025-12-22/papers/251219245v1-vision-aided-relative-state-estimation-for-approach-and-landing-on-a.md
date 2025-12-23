---
layout: default
title: Vision-Aided Relative State Estimation for Approach and Landing on a Moving Platform with Inertial Measurements
---

# Vision-Aided Relative State Estimation for Approach and Landing on a Moving Platform with Inertial Measurements
**arXiv**：[2512.19245v1](https://arxiv.org/abs/2512.19245) · [PDF](https://arxiv.org/pdf/2512.19245.pdf)  
**作者**：Tarek Bouazza, Alessandro Melis, Soulaimane Berkane, Robert Mahony, Tarek Hamel  

**一句话要点**：提出级联观测器，利用视觉和IMU数据估计无人机与移动平台在着陆过程中的相对状态

**关键词**：相对状态估计, 视觉惯性融合, 无人机着陆, 级联观测器, 移动平台

## 3 点简述
- 核心问题：估计无人机与任意3D运动平面平台在接近着陆时的相对位置、姿态和速度
- 方法要点：基于SO(3)互补滤波器和线性Riccati观测器的级联设计，确保收敛性和稳定性
- 实验或效果：通过广泛仿真验证观测器性能，并扩展到平台旋转受限情况

## 摘要（原文）

> This paper tackles the problem of estimating the relative position, orientation, and velocity between a UAV and a planar platform undergoing arbitrary 3D motion during approach and landing. The estimation relies on measurements from Inertial Measurement Units (IMUs) mounted on both systems, assuming there is a suitable communication channel to exchange data, together with visual information provided by an onboard monocular camera, from which the bearing (line-of-sight direction) to the platform's center and the normal vector of its planar surface are extracted. We propose a cascade observer with a complementary filter on SO(3) to reconstruct the relative attitude, followed by a linear Riccati observer for relative position and velocity estimation. Convergence of both observers is established under persistently exciting conditions, and the cascade is shown to be almost globally asymptotically and locally exponentially stable. We further extend the design to the case where the platform's rotation is restricted to its normal axis and show that its measured linear acceleration can be exploited to recover the remaining unobservable rotation angle. A sufficient condition to ensure local exponential convergence in this setting is provided. The performance of the proposed observers is validated through extensive simulations.

