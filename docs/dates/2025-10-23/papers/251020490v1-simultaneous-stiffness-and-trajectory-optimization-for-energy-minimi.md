---
layout: default
title: Simultaneous Stiffness and Trajectory Optimization for Energy Minimization of Pick-and-Place Tasks of SEA-Actuated Parallel Kinematic Manipulators
---

# Simultaneous Stiffness and Trajectory Optimization for Energy Minimization of Pick-and-Place Tasks of SEA-Actuated Parallel Kinematic Manipulators
**arXiv**：[2510.20490v1](https://arxiv.org/abs/2510.20490) · [PDF](https://arxiv.org/pdf/2510.20490.pdf)  
**作者**：Thomas Kordik, Hubert Gattringer, Andreas Mueller  

**一句话要点**：提出同时优化刚度和轨迹的方法，以最小化SEA驱动并联机器人在拾取-放置任务中的能耗。

**关键词**：并联机器人, 能量优化, 系列弹性驱动器, 最优控制, 拾取-放置任务

## 3 点简述
- 核心问题：拾取-放置任务中并联机器人能耗高，需优化能量效率。
- 方法要点：推导动态模型，同时优化操作轨迹和SEA刚度以激发本征运动。
- 实验或效果：在冗余驱动机器人上验证，结果证实能耗降低。

## 摘要（原文）

> A major field of industrial robot applications deals with repetitive tasks
> that alternate between operating points. For these so-called pick-and-place
> operations, parallel kinematic manipulators (PKM) are frequently employed.
> These tasks tend to automatically run for a long period of time and therefore
> minimizing energy consumption is always of interest. Recent research addresses
> this topic by the use of elastic elements and particularly series elastic
> actuators (SEA). This paper explores the possibilities of minimizing energy
> consumption of SEA actuated PKM performing pick-and-place tasks. The basic idea
> is to excite eigenmotions that result from the actuator springs and exploit
> their oscillating characteristics. To this end, a prescribed cyclic
> pick-and-place operation is analyzed and a dynamic model of SEA driven PKM is
> derived. Subsequently, an energy minimizing optimal control problem is
> formulated where operating trajectories as well as SEA stiffnesses are
> optimized simultaneously. Here, optimizing the actuator stiffness does not
> account for variable stiffness actuators. It serves as a tool for the design
> and dimensioning process. The hypothesis on energy reduction is tested on two
> (parallel) robot applications where redundant actuation is also addressed. The
> results confirm the validity of this approach.

