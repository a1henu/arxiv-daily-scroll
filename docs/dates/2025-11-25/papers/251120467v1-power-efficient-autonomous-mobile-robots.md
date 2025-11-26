---
layout: default
title: Power-Efficient Autonomous Mobile Robots
---

# Power-Efficient Autonomous Mobile Robots
**arXiv**：[2511.20467v1](https://arxiv.org/abs/2511.20467) · [PDF](https://arxiv.org/pdf/2511.20467.pdf)  
**作者**：Liangkai Liu, Weisong Shi, Kang G. Shin  

**一句话要点**：提出pNav系统以优化自主移动机器人的能效

**关键词**：自主移动机器人, 能效优化, 功耗预测, 软硬件协调, 实时建模, ROS导航栈

## 3 点简述
- 核心问题：AMR能效受系统功耗变异性、环境感知导航局部性和软硬件协调挑战影响
- 方法要点：集成毫秒级功耗预测、实时建模导航局部性、动态协调软硬件配置
- 实验或效果：功耗预测准确率>96%，功耗降低38.1%，不影响导航精度与安全

## 摘要（原文）

> This paper presents pNav, a novel power-management system that significantly enhances the power/energy-efficiency of Autonomous Mobile Robots (AMRs) by jointly optimizing their physical/mechanical and cyber subsystems. By profiling AMRs' power consumption, we identify three challenges in achieving CPS (cyber-physical system) power-efficiency that involve both cyber (C) and physical (P) subsystems: (1) variabilities of system power consumption breakdown, (2) environment-aware navigation locality, and (3) coordination of C and P subsystems. pNav takes a multi-faceted approach to achieve power-efficiency of AMRs. First, it integrates millisecond-level power consumption prediction for both C and P subsystems. Second, it includes novel real-time modeling and monitoring of spatial and temporal navigation localities for AMRs. Third, it supports dynamic coordination of AMR software (navigation, detection) and hardware (motors, DVFS driver) configurations. pNav is prototyped using the Robot Operating System (ROS) Navigation Stack, 2D LiDAR, and camera. Our in-depth evaluation with a real robot and Gazebo environments demonstrates a >96% accuracy in predicting power consumption and a 38.1% reduction in power consumption without compromising navigation accuracy and safety.

