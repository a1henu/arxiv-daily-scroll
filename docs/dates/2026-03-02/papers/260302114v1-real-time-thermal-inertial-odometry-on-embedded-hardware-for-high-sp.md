---
layout: default
title: Real-Time Thermal-Inertial Odometry on Embedded Hardware for High-Speed GPS-Denied Flight
---

# Real-Time Thermal-Inertial Odometry on Embedded Hardware for High-Speed GPS-Denied Flight
**arXiv**：[2603.02114v1](https://arxiv.org/abs/2603.02114) · [PDF](https://arxiv.org/pdf/2603.02114.pdf)  
**作者**：Austin Stone, Mark Petersen, Cammy Peterson  

**一句话要点**：提出实时热惯性里程计系统，用于嵌入式硬件上的高速GPS拒止飞行

**关键词**：热惯性里程计, 嵌入式硬件, GPS拒止导航, 传感器融合, 实时系统, 高速飞行

## 3 点简述
- 核心问题：高速GPS拒止飞行中，热图像因运动模糊和低对比度导致特征跟踪不可靠，气压高度在高空速下误差大。
- 方法要点：融合多传感器于固定滞后因子图，采用热优化前端和深度先验稳定尺度，使用GRU网络建模气压失真动态。
- 实验或效果：在NVIDIA Jetson Xavier NX上实现30 m/s闭环四旋翼飞行，千米轨迹漂移低于2%。

## 摘要（原文）

> We present a real-time monocular thermal-inertial odometry system designed for high-velocity, GPS-denied flight on embedded hardware. The system fuses measurements from a FLIR Boson+ 640 longwave infrared camera, a high-rate IMU, a laser range finder, a barometer, and a magnetometer within a fixed-lag factor graph. To sustain reliable feature tracks under motion blur, low contrast, and rapid viewpoint changes, we employ a lightweight thermal-optimized front-end with multi-stage feature filtering. Laser range finder measurements provide per-feature depth priors that stabilize scale during weakly observable motion. High-rate inertial data is first pre-filtered using a Chebyshev Type II infinite impulse response (IIR) filter and then preintegrated, improving robustness to airframe vibrations during aggressive maneuvers. To address barometric altitude errors induced at high airspeeds, we train an uncertainty-aware gated recurrent unit (GRU) network that models the temporal dynamics of static pressure distortion, outperforming polynomial and multi-layer perceptron (MLP) baselines. Integrated on an NVIDIA Jetson Xavier NX, the complete system supports closed-loop quadrotor flight at 30 m/s with drift under 2% over kilometer-scale trajectories. These contributions expand the operational envelope of thermal-inertial navigation, enabling reliable high-speed flight in visually degraded and GPS-denied environments.

