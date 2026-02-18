---
layout: default
title: Fluoroscopy-Constrained Magnetic Robot Control via Zernike-Based Field Modeling and Nonlinear MPC
---

# Fluoroscopy-Constrained Magnetic Robot Control via Zernike-Based Field Modeling and Nonlinear MPC
**arXiv**：[2602.15357v1](https://arxiv.org/abs/2602.15357) · [PDF](https://arxiv.org/pdf/2602.15357.pdf)  
**作者**：Xinhao Chen, Hongkun Yao, Anuruddha Bhattacharjee, Suraj Raval, Lamar O. Mair, Yancy Diaz-Mercado, Axel Krieger  

**一句话要点**：提出基于Zernike场建模和非线性MPC的控制框架，以解决荧光成像下磁驱动机器人控制难题。

**关键词**：磁驱动机器人, 非线性模型预测控制, Zernike多项式, 荧光成像, 机器人控制, 手术机器人

## 3 点简述
- 核心问题：荧光成像帧率低、噪声大，限制磁驱动机器人临床部署。
- 方法要点：结合非线性模型预测控制、Zernike多项式磁场模型和卡尔曼滤波器。
- 实验或效果：在模拟临床条件下，实现高精度轨迹跟踪，位置误差RMS为1.18毫米。

## 摘要（原文）

> Magnetic actuation enables surgical robots to navigate complex anatomical pathways while reducing tissue trauma and improving surgical precision. However, clinical deployment is limited by the challenges of controlling such systems under fluoroscopic imaging, which provides low frame rate and noisy pose feedback. This paper presents a control framework that remains accurate and stable under such conditions by combining a nonlinear model predictive control (NMPC) framework that directly outputs coil currents, an analytically differentiable magnetic field model based on Zernike polynomials, and a Kalman filter to estimate the robot state. Experimental validation is conducted with two magnetic robots in a 3D-printed fluid workspace and a spine phantom replicating drug delivery in the epidural space. Results show the proposed control method remains highly accurate when feedback is downsampled to 3 Hz with added Gaussian noise (sigma = 2 mm), mimicking clinical fluoroscopy. In the spine phantom experiments, the proposed method successfully executed a drug delivery trajectory with a root mean square (RMS) position error of 1.18 mm while maintaining safe clearance from critical anatomical boundaries.

