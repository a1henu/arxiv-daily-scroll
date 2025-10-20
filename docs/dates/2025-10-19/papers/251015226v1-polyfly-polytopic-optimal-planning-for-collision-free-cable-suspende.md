---
layout: default
title: PolyFly: Polytopic Optimal Planning for Collision-Free Cable-Suspended Aerial Payload Transportation
---

# PolyFly: Polytopic Optimal Planning for Collision-Free Cable-Suspended Aerial Payload Transportation
**arXiv**：[2510.15226v1](https://arxiv.org/abs/2510.15226) · [PDF](https://arxiv.org/pdf/2510.15226.pdf)  
**作者**：Mrunal Sarvaiya, Guanrui Li, Giuseppe Loianno  

**一句话要点**：提出PolyFly优化规划器，用于悬吊式空中载荷在约束环境中的无碰撞快速运输

**关键词**：空中载荷运输, 多面体规划, 最优控制, 障碍物避让, 四旋翼机器人

## 3 点简述
- 现有方法几何过近似导致保守机动和飞行时间增加
- 采用多面体建模环境和机器人组件，结合姿态感知优化控制
- 在模拟和真实四旋翼实验中，轨迹更快且可靠

## 摘要（原文）

> Aerial transportation robots using suspended cables have emerged as versatile
> platforms for disaster response and rescue operations. To maximize the
> capabilities of these systems, robots need to aggressively fly through tightly
> constrained environments, such as dense forests and structurally unsafe
> buildings, while minimizing flight time and avoiding obstacles. Existing
> methods geometrically over-approximate the vehicle and obstacles, leading to
> conservative maneuvers and increased flight times. We eliminate these
> restrictions by proposing PolyFly, an optimal global planner which considers a
> non-conservative representation for aerial transportation by modeling each
> physical component of the environment, and the robot (quadrotor, cable and
> payload), as independent polytopes. We further increase the model accuracy by
> incorporating the attitude of the physical components by constructing
> orientation-aware polytopes. The resulting optimal control problem is
> efficiently solved by converting the polytope constraints into smooth
> differentiable constraints via duality theory. We compare our method against
> the existing state-of-the-art approach in eight maze-like environments and show
> that PolyFly produces faster trajectories in each scenario. We also
> experimentally validate our proposed approach on a real quadrotor with a
> suspended payload, demonstrating the practical reliability and accuracy of our
> method.

