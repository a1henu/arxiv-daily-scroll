---
layout: default
title: Perception-Aware Time-Optimal Planning for Quadrotor Waypoint Flight
---

# Perception-Aware Time-Optimal Planning for Quadrotor Waypoint Flight
**arXiv**：[2603.04305v1](https://arxiv.org/abs/2603.04305) · [PDF](https://arxiv.org/pdf/2603.04305.pdf)  
**作者**：Chao Qin, Jiaxu Xing, Rudolf Reiter, Angel Romero, Yifan Lin, Hugh H. -T. Liu, Davide Scaramuzza  

**一句话要点**：提出感知感知时间最优规划框架，解决视觉四旋翼在动态飞行中因感知质量下降导致的闭环失败问题。

**关键词**：四旋翼轨迹规划, 感知约束优化, 时间最优控制, 视觉状态估计, 模型预测跟踪

## 3 点简述
- 核心问题：现有时间最优轨迹规划忽略车辆动力学、环境几何与视觉状态估计的耦合，导致轨迹动态可行但闭环执行失败。
- 方法要点：统一优化框架结合非线性动力学、感知约束（如位置不确定性度量、视场约束）和几何门表示，实现速度与感知可靠性的权衡。
- 实验或效果：实验显示飞行速度达9.8 m/s，平均跟踪误差0.07 m，闭环成功率从55%提升至100%。

## 摘要（原文）

> Agile quadrotor flight pushes the limits of control, actuation, and onboard perception. While time-optimal trajectory planning has been extensively studied, existing approaches typically neglect the tight coupling between vehicle dynamics, environmental geometry, and the visual requirements of onboard state estimation. As a result, trajectories that are dynamically feasible may fail in closed-loop execution due to degraded visual quality. This paper introduces a unified time-optimal trajectory optimization framework for vision-based quadrotors that explicitly incorporates perception constraints alongside full nonlinear dynamics, rotor actuation limits, aerodynamic effects, camera field-of-view constraints, and convex geometric gate representations.
>   The proposed formulation solves minimum-time lap trajectories for arbitrary racetracks with diverse gate shapes and orientations, while remaining numerically robust and computationally efficient. We derive an information-theoretic position uncertainty metric to quantify visual state-estimation quality and integrate it into the planner through three perception objectives: position uncertainty minimization, sequential field-of-view constraints, and look-ahead alignment. This enables systematic exploration of the trade-offs between speed and perceptual reliability.
>   To accurately track the resulting perception-aware trajectories, we develop a model predictive contouring tracking controller that separates lateral and progress errors. Experiments demonstrate real-world flight speeds up to 9.8 m/s with 0.07 m average tracking error, and closed-loop success rates improved from 55% to 100% on a challenging Split-S course. The proposed system provides a scalable benchmark for studying the fundamental limits of perception-aware, time-optimal autonomous flight.

