---
layout: default
title: Airborne Magnetic Anomaly Navigation with Neural-Network-Augmented Online Calibration
---

# Airborne Magnetic Anomaly Navigation with Neural-Network-Augmented Online Calibration
**arXiv**：[2603.08265v1](https://arxiv.org/abs/2603.08265) · [PDF](https://arxiv.org/pdf/2603.08265.pdf)  
**作者**：Antonia Hager, Sven Nebendahl, Alexej Klushyn, Jasper Krauser, Torleiv H. Bryne, Tor Arne Johansen  

**一句话要点**：提出自适应磁异常导航架构，通过在线校准实现冷启动，无需离线训练或校准飞行。

**关键词**：磁异常导航, 在线校准, 扩展卡尔曼滤波, 神经网络, 残差学习, 冷启动能力

## 3 点简述
- 核心问题：磁异常导航需实时补偿飞机动态磁干扰，现有方法依赖离线校准，部署不便。
- 方法要点：结合扩展卡尔曼滤波与神经网络，在线估计物理模型系数和神经网络参数，约束神经网络为残差学习。
- 实验或效果：在MagNav挑战数据集上验证，仅用磁力计特征限制惯性漂移，精度媲美离线训练模型。

## 摘要（原文）

> Airborne Magnetic Anomaly Navigation (MagNav) provides a jamming-resistant and robust alternative to satellite navigation but requires the real-time compensation of the aircraft platform's large and dynamic magnetic interference. State-of-the-art solutions often rely on extensive offline calibration flights or pre-training, creating a logistical barrier to operational deployment. We present a fully adaptive MagNav architecture featuring a "cold-start" capability that identifies and compensates for the aircraft's magnetic signature entirely in-flight. The proposed method utilizes an extended Kalman filter with an augmented state vector that simultaneously estimates the aircraft's kinematic states as well as the coefficients of the physics-based Tolles-Lawson calibration model and the parameters of a Neural Network to model aircraft interferences. The Kalman filter update is mathematically equivalent to an online Natural Gradient descent, integrating superior convergence and data efficiency of state-of-the-art second-order optimization directly into the navigation filter. To enhance operational robustness, the neural network is constrained to a residual learning role, modeling only the nonlinearities uncorrected by the explainable physics-based calibration baseline. Validated on the MagNav Challenge dataset, our framework effectively bounds inertial drift using a magnetometer-only feature set. The results demonstrate navigation accuracy comparable to state-of-the-art models trained offline, without requiring prior calibration flights or dedicated maneuvers.

