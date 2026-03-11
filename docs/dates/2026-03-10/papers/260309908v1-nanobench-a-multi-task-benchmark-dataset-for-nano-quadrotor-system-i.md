---
layout: default
title: NanoBench: A Multi-Task Benchmark Dataset for Nano-Quadrotor System Identification, Control, and State Estimation
---

# NanoBench: A Multi-Task Benchmark Dataset for Nano-Quadrotor System Identification, Control, and State Estimation
**arXiv**：[2603.09908v1](https://arxiv.org/abs/2603.09908) · [PDF](https://arxiv.org/pdf/2603.09908.pdf)  
**作者**：Syed Izzat Ullah, Jose Baca  

**一句话要点**：提出NanoBench基准数据集，用于纳米四旋翼系统辨识、控制和状态估计研究。

**关键词**：纳米四旋翼, 系统辨识, 控制器基准, 状态估计, 开源数据集, 多任务评估

## 3 点简述
- 现有基准忽略纳米四旋翼的致动器信号，模型和控制器不适用。
- 提供包含170多条轨迹的多任务数据集，同步高精度地面真值和原始数据。
- 定义标准化评估协议和开源基线，支持系统辨识、控制器和状态估计任务。

## 摘要（原文）

> Existing aerial-robotics benchmarks target vehicles from hundreds of grams to several kilograms and typically expose only high-level state data. They omit the actuator-level signals required to study nano-scale quadrotors, where low-Reynolds number aerodynamics, coreless DC motor nonlinearities, and severe computational constraints invalidate models and controllers developed for larger vehicles. We introduce NanoBench, an open-source multi-task benchmark collected on the commercially available Crazyflie 2.1 nano-quadrotor (takeoff weight 27 g) in a Vicon motion capture arena. The dataset contains over 170 flight trajectories spanning hover, multi-frequency excitation, standard tracking, and aggressive maneuvers across multiple speed regimes. Each trajectory provides synchronized Vicon ground truth, raw IMU data, onboard extended Kalman filter estimates, PID controller internals, and motor PWM commands at 100 Hz, alongside battery telemetry at 10 Hz, aligned with sub-0.5 ms consistency. NanoBench defines standardized evaluation protocols, train/test splits, and open-source baselines for three tasks: nonlinear system identification, closed-loop controller benchmarking, and onboard state estimation assessment. To our knowledge, it is the first public dataset to jointly provide actuator commands, controller internals, and estimator outputs with millimeter-accurate ground truth on a commercially available nano-scale aerial platform.

