---
layout: default
title: Breaking the Circle: An Autonomous Control-Switching Strategy for Stable Orographic Soaring in MAVs
---

# Breaking the Circle: An Autonomous Control-Switching Strategy for Stable Orographic Soaring in MAVs
**arXiv**：[2510.23084v1](https://arxiv.org/abs/2510.23084) · [PDF](https://arxiv.org/pdf/2510.23084.pdf)  
**作者**：Sunyou Hwang, Christophe De Wagter, Bart Remes, Guido de Croon  

**一句话要点**：提出SAOS控制切换策略以解决MAV地形翱翔中的盘旋行为问题

**关键词**：微型飞行器, 地形翱翔, 控制切换, INDI控制器, 能量效率, 飞行稳定性

## 3 点简述
- 核心问题：MAV地形翱翔中纵向与垂直轴控制冲突导致盘旋，增加能耗与发散风险。
- 方法要点：通过选择性控制水平或垂直轴，将系统从欠驱动转为全驱动翱翔。
- 实验或效果：仿真与风洞实验显示SAOS改善位置收敛、减少油门使用并抑制滚转振荡。

## 摘要（原文）

> Orographic soaring can significantly extend the endurance of micro aerial
> vehicles (MAVs), but circling behavior, arising from control conflicts between
> the longitudinal and vertical axes, increases energy consumption and the risk
> of divergence. We propose a control switching method, named SAOS: Switched
> Control for Autonomous Orographic Soaring, which mitigates circling behavior by
> selectively controlling either the horizontal or vertical axis, effectively
> transforming the system from underactuated to fully actuated during soaring.
> Additionally, the angle of attack is incorporated into the INDI controller to
> improve force estimation. Simulations with randomized initial positions and
> wind tunnel experiments on two MAVs demonstrate that the SAOS improves position
> convergence, reduces throttle usage, and mitigates roll oscillations caused by
> pitch-roll coupling. These improvements enhance energy efficiency and flight
> stability in constrained soaring environments.

