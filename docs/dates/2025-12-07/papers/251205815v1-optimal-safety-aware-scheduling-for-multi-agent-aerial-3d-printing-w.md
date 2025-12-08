---
layout: default
title: Optimal Safety-Aware Scheduling for Multi-Agent Aerial 3D Printing with Utility Maximization under Dependency Constraints
---

# Optimal Safety-Aware Scheduling for Multi-Agent Aerial 3D Printing with Utility Maximization under Dependency Constraints
**arXiv**：[2512.05815v1](https://arxiv.org/abs/2512.05815) · [PDF](https://arxiv.org/pdf/2512.05815.pdf)  
**作者**：Marios-Nektarios Stamatopoulos, Shridhar Velhal, Avijit Banerjee, George Nikolakopoulos  

**一句话要点**：提出多无人机协同空中3D打印的安全感知调度框架，以最大化效用并处理依赖约束。

**关键词**：多无人机协同, 空中3D打印, 安全感知调度, 优化问题, 任务依赖, 效用最大化

## 3 点简述
- 核心问题：多无人机协同空中3D打印中，任务依赖、安全冲突和资源限制下的优化调度问题。
- 方法要点：基于优化问题生成任务分配与调度，动态调整任务起始时间和位置，并引入重要性优先级加速计算。
- 实验或效果：通过Gazebo仿真评估框架有效性，在材料和电池约束下实现无冲突并行执行。

## 摘要（原文）

> This article presents a novel coordination and task-planning framework to enable the simultaneous conflict-free collaboration of multiple unmanned aerial vehicles (UAVs) for aerial 3D printing. The proposed framework formulates an optimization problem that takes a construction mission divided into sub-tasks and a team of autonomous UAVs, along with limited volume and battery. It generates an optimal mission plan comprising task assignments and scheduling while accounting for task dependencies arising from the geometric and structural requirements of the 3D design, inter-UAV safety constraints, material usage, and total flight time of each UAV. The potential conflicts occurring during the simultaneous operation of the UAVs are addressed at a segment level by dynamically selecting the starting time and location of each task to guarantee collision-free parallel execution. An importance prioritization is proposed to accelerate the computation by guiding the solution toward more important tasks. Additionally, a utility maximization formulation is proposed to dynamically determine the optimal number of UAVs required for a given mission, balancing the trade-off between minimizing makespan and the deployment of excess agents. The proposed framework's effectiveness is evaluated through a Gazebo-based simulation setup, where agents are coordinated by a mission control module allocating the printing tasks based on the generated optimal scheduling plan while remaining within the material and battery constraints of each UAV.

