---
layout: default
title: Observability Analysis and Composite Disturbance Filtering for a Bar Tethered to Dual UAVs Subject to Multi-source Disturbances
---

# Observability Analysis and Composite Disturbance Filtering for a Bar Tethered to Dual UAVs Subject to Multi-source Disturbances
**arXiv**：[2512.09377v1](https://arxiv.org/abs/2512.09377) · [PDF](https://arxiv.org/pdf/2512.09377.pdf)  
**作者**：Lidan Xu, Dadong Fan, Junhong Wang, Wenshuo Li, Hao Lu, Jianzhong Qiao  

**一句话要点**：提出基于可观测性分析与复合扰动滤波的双无人机吊挂系统状态估计方法

**关键词**：无人机协同运输, 可观测性分析, 扰动滤波, 扩展卡尔曼滤波, 状态估计

## 3 点简述
- 针对双无人机吊挂系统在多源扰动下仅依赖无人机里程计信息时负载姿态的可观测性问题，通过可观测性秩准则证明系统在不超过两类集总扰动下完全可观测
- 设计基于扰动观测器的误差状态扩展卡尔曼滤波器，在流形上实现系统状态与扰动的联合估计，减少传感器依赖
- 通过仿真与实验验证了仅使用无人机里程计信息即可完全估计系统状态与扰动的可行性

## 摘要（原文）

> Cooperative suspended aerial transportation is highly susceptible to multi-source disturbances such as aerodynamic effects and thrust uncertainties. To achieve precise load manipulation, existing methods often rely on extra sensors to measure cable directions or the payload's pose, which increases the system cost and complexity. A fundamental question remains: is the payload's pose observable under multi-source disturbances using only the drones' odometry information? To answer this question, this work focuses on the two-drone-bar system and proves that the whole system is observable when only two or fewer types of lumped disturbances exist by using the observability rank criterion. To the best of our knowledge, we are the first to present such a conclusion and this result paves the way for more cost-effective and robust systems by minimizing their sensor suites. Next, to validate this analysis, we consider the situation where the disturbances are only exerted on the drones, and develop a composite disturbance filtering scheme. A disturbance observer-based error-state extended Kalman filter is designed for both state and disturbance estimation, which renders improved estimation performance for the whole system evolving on the manifold $(\mathbb{R}^3)^2\times(TS^2)^3$. Our simulation and experimental tests have validated that it is possible to fully estimate the state and disturbance of the system with only odometry information of the drones.

