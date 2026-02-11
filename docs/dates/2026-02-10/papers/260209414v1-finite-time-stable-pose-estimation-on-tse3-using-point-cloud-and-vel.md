---
layout: default
title: Finite-time Stable Pose Estimation on TSE(3) using Point Cloud and Velocity Sensors
---

# Finite-time Stable Pose Estimation on TSE(3) using Point Cloud and Velocity Sensors
**arXiv**：[2602.09414v1](https://arxiv.org/abs/2602.09414) · [PDF](https://arxiv.org/pdf/2602.09414.pdf)  
**作者**：Nazanin S. Hashkavaei, Abhijit Dongare, Neon Srinivasu, Amit K. Sanyal  

**一句话要点**：提出有限时间稳定姿态估计器，用于三维刚体运动，基于点云和速度传感器测量。

**关键词**：姿态估计, 有限时间稳定, 李群SE(3), 点云处理, 传感器融合, 自主车辆

## 3 点简述
- 核心问题：在SE(3)上设计无奇异性和解绕现象的刚体姿态和速度估计器。
- 方法要点：通过李群切丛上的李雅普诺夫分析，实现有限时间稳定和抗有界噪声。
- 实验或效果：数值模拟和实验验证了优于双四元数扩展卡尔曼滤波和变分姿态估计器的性能。

## 摘要（原文）

> This work presents a finite-time stable pose estimator (FTS-PE) for rigid bodies undergoing rotational and translational motion in three dimensions, using measurements from onboard sensors that provide position vectors to inertially-fixed points and body velocities. The FTS-PE is a full-state observer for the pose (position and orientation) and velocities and is obtained through a Lyapunov analysis that shows its stability in finite time and its robustness to bounded measurement noise. Further, this observer is designed directly on the state space, the tangent bundle of the Lie group of rigid body motions, SE(3), without using local coordinates or (dual) quaternion representations. Therefore, it can estimate arbitrary rigid body motions without encountering singularities or the unwinding phenomenon and be readily applied to autonomous vehicles. A version of this observer that does not need translational velocity measurements and uses only point clouds and angular velocity measurements from rate gyros, is also obtained. It is discretized using the framework of geometric mechanics for numerical and experimental implementations. The numerical simulations compare the FTS-PE with a dual-quaternion extended Kalman filter and our previously developed variational pose estimator (VPE). The experimental results are obtained using point cloud images and rate gyro measurements obtained from a Zed 2i stereo depth camera sensor. These results validate the stability and robustness of the FTS-PE.

