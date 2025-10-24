---
layout: default
title: A Parameter-Linear Formulation of the Optimal Path Following Problem for Robotic Manipulator
---

# A Parameter-Linear Formulation of the Optimal Path Following Problem for Robotic Manipulator
**arXiv**：[2510.20496v1](https://arxiv.org/abs/2510.20496) · [PDF](https://arxiv.org/pdf/2510.20496.pdf)  
**作者**：Tobias Marauli, Hubert Gattringer, Andreas Mueller  

**一句话要点**：提出最大化路径速度方法以解决机器人时间最优路径跟随的计算挑战

**关键词**：机器人路径跟随, 时间最优控制, 轨迹规划, 数值优化, 路径参数化

## 3 点简述
- 核心问题：时间最优路径跟随中，路径参数化导致零速度奇点，计算复杂且轨迹不平滑。
- 方法要点：通过最大化路径速度，避免奇点，实现高效数值轨迹规划。
- 实验或效果：离散化后优化问题线性化，计算效率高，轨迹平滑。

## 摘要（原文）

> In this paper the computational challenges of time-optimal path following are
> addressed. The standard approach is to minimize the travel time, which
> inevitably leads to singularities at zero path speed, when reformulating the
> optimization problem in terms of a path parameter. Thus, smooth trajectory
> generation while maintaining a low computational effort is quite challenging,
> since the singularities have to be taken into account. To this end, a different
> approach is presented in this paper. This approach is based on maximizing the
> path speed along a prescribed path. Furthermore, the approach is capable of
> planning smooth trajectories numerically efficient. Moreover, the discrete
> reformulation of the underlying problem is linear in optimization variables.

