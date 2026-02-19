---
layout: default
title: Sensor Query Schedule and Sensor Noise Covariances for Accuracy-constrained Trajectory Estimation
---

# Sensor Query Schedule and Sensor Noise Covariances for Accuracy-constrained Trajectory Estimation
**arXiv**：[2602.16598v1](https://arxiv.org/abs/2602.16598) · [PDF](https://arxiv.org/pdf/2602.16598.pdf)  
**作者**：Abhishek Goudar, Angela P. Schoellig  

**一句话要点**：提出传感器查询调度与噪声协方差估计方法，以在成本约束下实现移动机器人轨迹估计的特定精度要求。

**关键词**：轨迹估计, 传感器调度, 噪声协方差, 半定规划, 移动机器人, 精度约束

## 3 点简述
- 核心问题：在成本和资源限制下，如何确定传感器参数（如测量速率和噪声协方差）以满足轨迹估计的特定精度需求。
- 方法要点：将传感器参数估计问题建模为半定规划，利用现成求解器计算最优调度或协方差。
- 实验或效果：通过仿真和真实实验验证，所提方法能实现目标精度，并识别不可行场景。

## 摘要（原文）

> Trajectory estimation involves determining the trajectory of a mobile robot by combining prior knowledge about its dynamic model with noisy observations of its state obtained using sensors. The accuracy of such a procedure is dictated by the system model fidelity and the sensor parameters, such as the accuracy of the sensor (as represented by its noise covariance) and the rate at which it can generate observations, referred to as the sensor query schedule. Intuitively, high-rate measurements from accurate sensors lead to accurate trajectory estimation. However, cost and resource constraints limit the sensor accuracy and its measurement rate. Our work's novel contribution is the estimation of sensor schedules and sensor covariances necessary to achieve a specific estimation accuracy. Concretely, we focus on estimating: (i) the rate or schedule with which a sensor of known covariance must generate measurements to achieve specific estimation accuracy, and alternatively, (ii) the sensor covariance necessary to achieve specific estimation accuracy for a given sensor update rate. We formulate the problem of estimating these sensor parameters as semidefinite programs, which can be solved by off-the-shelf solvers. We validate our approach in simulation and real experiments by showing that the sensor schedules and the sensor covariances calculated using our proposed method achieve the desired trajectory estimation accuracy. Our method also identifies scenarios where certain estimation accuracy is unachievable with the given system and sensor characteristics.

