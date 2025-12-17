---
layout: default
title: Quadratic Kalman Filter for Elliptical Extended Object Tracking based on Decoupling State Components
---

# Quadratic Kalman Filter for Elliptical Extended Object Tracking based on Decoupling State Components
**arXiv**：[2512.14426v1](https://arxiv.org/abs/2512.14426) · [PDF](https://arxiv.org/pdf/2512.14426.pdf)  
**作者**：Simon Steuernagel, Marcus Baum  

**一句话要点**：提出基于状态分量解耦的二次卡尔曼滤波器，用于椭圆扩展目标跟踪。

**关键词**：扩展目标跟踪, 卡尔曼滤波器, 状态解耦, 椭圆模型, 雷达数据处理

## 3 点简述
- 核心问题：扩展目标跟踪需同时估计目标运动学参数和物理范围，每时间步多测量。
- 方法要点：通过解耦运动学、方向和轴长状态分量，减少近似需求，实现确定性闭式跟踪。
- 实验或效果：算法性能优于现有方法，达到基于采样方法的精度，并在真实雷达数据上验证。

## 摘要（原文）

> Extended object tracking involves estimating both the physical extent and kinematic parameters of a target object, where typically multiple measurements are observed per time step. In this article, we propose a deterministic closed-form elliptical extended object tracker, based on decoupling of the kinematics, orientation, and axis lengths. By disregarding potential correlations between these state components, fewer approximations are required for the individual estimators than for an overall joint solution. The resulting algorithm outperforms existing algorithms, reaching the accuracy of sampling-based procedures. Additionally, a batch-based variant is introduced, yielding highly efficient computation while outperforming all comparable state-of-the-art algorithms. This is validated both by a simulation study using common models from literature, as well as an extensive quantitative evaluation on real automotive radar data.

