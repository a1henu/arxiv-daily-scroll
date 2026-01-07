---
layout: default
title: Making Infeasible Tasks Feasible: Planning to Reconfigure Disconnected 3D Environments with Movable Objects
---

# Making Infeasible Tasks Feasible: Planning to Reconfigure Disconnected 3D Environments with Movable Objects
**arXiv**：[2601.02645v1](https://arxiv.org/abs/2601.02645) · [PDF](https://arxiv.org/pdf/2601.02645.pdf)  
**作者**：Samarth Kalluraya, Yiannis Kantaros  

**一句话要点**：提出BRiDGE规划器以解决3D环境中因物理断开导致目标不可达的导航问题

**关键词**：3D环境规划, 可移动物体导航, 采样规划, 机器人交互, 物理断开连接

## 3 点简述
- 核心问题：3D环境中目标区域因高度差或分离而不可达，需通过移动物体创建连接
- 方法要点：开发基于采样的BRiDGE规划器，增量构建配置树，指定物体移动顺序和位置
- 实验或效果：方法具有概率完备性，通过数值和硬件实验验证有效性

## 摘要（原文）

> Several planners have been developed to compute dynamically feasible, collision-free robot paths from an initial to a goal configuration. A key assumption in these works is that the goal region is reachable; an assumption that often fails in practice when environments are disconnected. Motivated by this limitation, we consider known 3D environments comprising objects, also called blocks, that form distinct navigable support surfaces (planes), and that are either non-movable (e.g., tables) or movable (e.g., boxes). These surfaces may be mutually disconnected due to height differences, holes, or lateral separations. Our focus is on tasks where the robot must reach a goal region residing on an elevated plane that is unreachable. Rather than declaring such tasks infeasible, an effective strategy is to enable the robot to interact with the environment, rearranging movable objects to create new traversable connections; a problem known as Navigation Among Movable Objects (NAMO). Existing NAMO planners typically address 2D environments, where obstacles are pushed aside to clear a path. These methods cannot directly handle the considered 3D setting; in such cases, obstacles must be placed strategically to bridge these physical disconnections. We address this challenge by developing BRiDGE (Block-based Reconfiguration in Disconnected 3D Geometric Environments), a sampling-based planner that incrementally builds trees over robot and object configurations to compute feasible plans specifying which objects to move, where to place them, and in what order, while accounting for a limited number of movable objects. To accelerate planning, we introduce non-uniform sampling strategies. We show that our method is probabilistically complete and we provide extensive numerical and hardware experiments validating its effectiveness.

