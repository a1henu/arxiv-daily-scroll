---
layout: default
title: K-VARK: Kernelized Variance-Aware Residual Kalman Filter for Sensorless Force Estimation in Collaborative Robots
---

# K-VARK: Kernelized Variance-Aware Residual Kalman Filter for Sensorless Force Estimation in Collaborative Robots
**arXiv**：[2512.13009v1](https://arxiv.org/abs/2512.13009) · [PDF](https://arxiv.org/pdf/2512.13009.pdf)  
**作者**：Oğuzhan Akbıyık, Naseem Alhousani, Fares J. Abu-Dakka  

**一句话要点**：提出K-VARK核化方差感知残差卡尔曼滤波器，用于协作机器人无传感器力估计。

**关键词**：无传感器力估计, 卡尔曼滤波器, 核化方法, 方差感知, 协作机器人, 残差建模

## 3 点简述
- 核心问题：无传感器力估计因建模误差和复杂残差动力学而困难。
- 方法要点：集成核化概率模型到自适应卡尔曼滤波器，捕捉残差力矩的均值和异方差方差。
- 实验或效果：在6自由度协作机械臂上验证，RMSE降低超20%，适用于抛光和装配任务。

## 摘要（原文）

> Reliable estimation of contact forces is crucial for ensuring safe and precise interaction of robots with unstructured environments. However, accurate sensorless force estimation remains challenging due to inherent modeling errors and complex residual dynamics and friction. To address this challenge, in this paper, we propose K-VARK (Kernelized Variance-Aware Residual Kalman filter), a novel approach that integrates a kernelized, probabilistic model of joint residual torques into an adaptive Kalman filter framework. Through Kernelized Movement Primitives trained on optimized excitation trajectories, K-VARK captures both the predictive mean and input-dependent heteroscedastic variance of residual torques, reflecting data variability and distance-to-training effects. These statistics inform a variance-aware virtual measurement update by augmenting the measurement noise covariance, while the process noise covariance adapts online via variational Bayesian optimization to handle dynamic disturbances. Experimental validation on a 6-DoF collaborative manipulator demonstrates that K-VARK achieves over 20% reduction in RMSE compared to state-of-the-art sensorless force estimation methods, yielding robust and accurate external force/torque estimation suitable for advanced tasks such as polishing and assembly.

