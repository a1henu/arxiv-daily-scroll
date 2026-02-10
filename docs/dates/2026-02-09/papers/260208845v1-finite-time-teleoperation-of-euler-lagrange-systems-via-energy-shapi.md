---
layout: default
title: Finite-Time Teleoperation of Euler-Lagrange Systems via Energy-Shaping
---

# Finite-Time Teleoperation of Euler-Lagrange Systems via Energy-Shaping
**arXiv**：[2602.08845v1](https://arxiv.org/abs/2602.08845) · [PDF](https://arxiv.org/pdf/2602.08845.pdf)  
**作者**：Lazaro F. Torres, Carlos I. Aldana, Emmanuel Nuño, Emmanuel Cruz-Zavala  

**一句话要点**：提出有限时间控制器以解决非线性欧拉-拉格朗日系统的双边遥操作问题

**关键词**：有限时间控制, 双边遥操作, 欧拉-拉格朗日系统, 能量整形, 非线性控制, 比例加阻尼注入

## 3 点简述
- 核心问题：在无时延条件下，实现非线性欧拉-拉格朗日系统双边遥操作的位置误差和速度全局收敛
- 方法要点：基于能量整形框架，设计连续时间比例加阻尼注入控制器，确保闭环系统具有负度齐次近似
- 实验或效果：通过仿真和实验验证控制器简单有效，在无时延时实现有限时间收敛

## 摘要（原文）

> This paper proposes a family of finite-time controllers for the bilateral teleoperation of fully actuated nonlinear Euler-Lagrange systems. Based on the energy-shaping framework and under the standard assumption of passive interactions with the human and the environment, the controllers ensure that the position error and velocities globally converge to zero in the absence of time delays. In this case, the closed-loop system admits a homogeneous approximation of negative degree, and thus the control objective is achieved in finite-time. The proposed controllers are simple, continuous-time proportional-plus-damping-injection schemes, validated through both simulation and experimental results.

