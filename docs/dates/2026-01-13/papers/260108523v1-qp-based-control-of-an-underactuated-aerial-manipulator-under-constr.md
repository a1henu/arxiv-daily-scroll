---
layout: default
title: QP-Based Control of an Underactuated Aerial Manipulator under Constraints
---

# QP-Based Control of an Underactuated Aerial Manipulator under Constraints
**arXiv**：[2601.08523v1](https://arxiv.org/abs/2601.08523) · [PDF](https://arxiv.org/pdf/2601.08523.pdf)  
**作者**：Nesserine Laribi, Mohammed Rida Mokhtari, Abdelaziz Benallegue, Abdelhafid El-Hadri, Mehdi Benallegue  

**一句话要点**：提出基于二次规划的约束感知控制框架，用于欠驱动空中机械臂的精确末端轨迹跟踪。

**关键词**：欠驱动空中机械臂, 二次规划控制, 约束感知控制, 轨迹跟踪, 被动性积分, 高保真仿真

## 3 点简述
- 核心问题：欠驱动空中机械臂在安全与可行性约束下的精确末端轨迹跟踪控制。
- 方法要点：将控制问题建模为二次规划，结合被动性积分增强鲁棒性，确保动态一致性与约束满足。
- 实验或效果：通过高保真仿真验证，在扰动和不确定性下实现准确跟踪、平滑控制与可靠约束满足。

## 摘要（原文）

> This paper presents a constraint-aware control framework for underactuated aerial manipulators, enabling accurate end-effector trajectory tracking while explicitly accounting for safety and feasibility constraints. The control problem is formulated as a quadratic program that computes dynamically consistent generalized accelerations subject to underactuation, actuator bounds, and system constraints. To enhance robustness against disturbances, modeling uncertainties, and steady-state errors, a passivity-based integral action is incorporated at the torque level without compromising feasibility. The effectiveness of the proposed approach is demonstrated through high-fidelity physics-based simulations, which include parameter perturbations, viscous joint friction, and realistic sensing and state-estimation effects. This demonstrates accurate tracking, smooth control inputs, and reliable constraint satisfaction under realistic operating conditions.

