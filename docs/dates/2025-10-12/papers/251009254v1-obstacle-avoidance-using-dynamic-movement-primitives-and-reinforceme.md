---
layout: default
title: Obstacle Avoidance using Dynamic Movement Primitives and Reinforcement Learning
---

# Obstacle Avoidance using Dynamic Movement Primitives and Reinforcement Learning
**arXiv**：[2510.09254v1](https://arxiv.org/abs/2510.09254) · [PDF](https://arxiv.org/pdf/2510.09254.pdf)  
**作者**：Dominik Urbaniak, Alejandro Agostini, Pol Ramon, Jan Rosell, Raúl Suárez, Michael Suppa  

**一句话要点**：提出结合动态运动基元与强化学习的避障方法，从单演示生成平滑3D轨迹

**关键词**：动态运动基元, 强化学习, 避障规划, 轨迹生成, 机器人控制

## 3 点简述
- 核心问题：学习型运动规划需大量数据或昂贵演示，难以快速生成最优轨迹
- 方法要点：用DMP编码演示，强化学习迭代优化，训练网络输出轨迹参数
- 实验或效果：仿真与真实实验验证，优于RRT-Connect，支持多模态轨迹生成

## 摘要（原文）

> Learning-based motion planning can quickly generate near-optimal
> trajectories. However, it often requires either large training datasets or
> costly collection of human demonstrations. This work proposes an alternative
> approach that quickly generates smooth, near-optimal collision-free 3D
> Cartesian trajectories from a single artificial demonstration. The
> demonstration is encoded as a Dynamic Movement Primitive (DMP) and iteratively
> reshaped using policy-based reinforcement learning to create a diverse
> trajectory dataset for varying obstacle configurations. This dataset is used to
> train a neural network that takes as inputs the task parameters describing the
> obstacle dimensions and location, derived automatically from a point cloud, and
> outputs the DMP parameters that generate the trajectory. The approach is
> validated in simulation and real-robot experiments, outperforming a RRT-Connect
> baseline in terms of computation and execution time, as well as trajectory
> length, while supporting multi-modal trajectory generation for different
> obstacle geometries and end-effector dimensions. Videos and the implementation
> code are available at https://github.com/DominikUrbaniak/obst-avoid-dmp-pi2.

