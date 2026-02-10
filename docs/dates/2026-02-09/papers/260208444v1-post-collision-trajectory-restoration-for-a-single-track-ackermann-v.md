---
layout: default
title: Post-Collision Trajectory Restoration for a Single-track Ackermann Vehicle using Heuristic Steering and Tractive Force Functions
---

# Post-Collision Trajectory Restoration for a Single-track Ackermann Vehicle using Heuristic Steering and Tractive Force Functions
**arXiv**：[2602.08444v1](https://arxiv.org/abs/2602.08444) · [PDF](https://arxiv.org/pdf/2602.08444.pdf)  
**作者**：Samsaptak Ghosh, M. Felix Orlando, Sohom Chakrabarty  

**一句话要点**：提出启发式恢复控制律，用于单轨阿克曼车辆碰撞后轨迹恢复，考虑速度变化和非线性耦合。

**关键词**：碰撞后轨迹恢复, 单轨阿克曼车辆, 启发式控制, 非线性耦合, 仿真评估

## 3 点简述
- 核心问题：碰撞后车辆因侧向运动和偏航瞬态偏离路径，需恢复轨迹。
- 方法要点：设计联合控制转向和牵引力的启发式律，考虑时变速度和非线性耦合项。
- 实验或效果：在MATLAB仿真中评估，在代表性初始条件下展示一致恢复行为。

## 摘要（原文）

> Post-collision trajectory restoration is a safety-critical capability for autonomous vehicles, as impact-induced lateral motion and yaw transients can rapidly drive the vehicle away from the intended path. This paper proposes a structured heuristic recovery control law that jointly commands steering and tractive force for a generalized single-track Ackermann vehicle model. The formulation explicitly accounts for time-varying longitudinal velocity in the lateral-yaw dynamics and retains nonlinear steering-coupled interaction terms that are commonly simplified in the literature. Unlike approaches that assume constant longitudinal speed, the proposed design targets the transient post-impact regime where speed variations and nonlinear coupling significantly influence recovery. The method is evaluated in simulation on the proposed generalized single-track model and a standard 3DOF single-track reference model in MATLAB, demonstrating consistent post-collision restoration behaviour across representative initial post-impact conditions.

