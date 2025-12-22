---
layout: default
title: Kinematics-Aware Diffusion Policy with Consistent 3D Observation and Action Space for Whole-Arm Robotic Manipulation
---

# Kinematics-Aware Diffusion Policy with Consistent 3D Observation and Action Space for Whole-Arm Robotic Manipulation
**arXiv**：[2512.17568v1](https://arxiv.org/abs/2512.17568) · [PDF](https://arxiv.org/pdf/2512.17568.pdf)  
**作者**：Kangchen Lv, Mingrui Yu, Yongyi Jia, Chenyu Zhang, Xiang Li  

**一句话要点**：提出基于扩散策略的运动学感知模仿学习框架，以解决全臂机器人操作中任务空间与关节空间不对齐问题。

**关键词**：全臂机器人操作, 扩散策略, 运动学感知, 3D点表示, 模仿学习, 空间泛化

## 3 点简述
- 核心问题：全臂操作中关节空间与3D任务空间不对齐，增加策略学习复杂性，难以从有限演示中泛化。
- 方法要点：使用3D点表示机器人状态和动作，与点云观测对齐，并在扩散过程中融入运动学先验以确保动作可行性。
- 实验或效果：仿真和真实实验显示，相比现有方法，该方法在成功率和空间泛化能力上表现更优。

## 摘要（原文）

> Whole-body control of robotic manipulators with awareness of full-arm kinematics is crucial for many manipulation scenarios involving body collision avoidance or body-object interactions, which makes it insufficient to consider only the end-effector poses in policy learning. The typical approach for whole-arm manipulation is to learn actions in the robot's joint space. However, the unalignment between the joint space and actual task space (i.e., 3D space) increases the complexity of policy learning, as generalization in task space requires the policy to intrinsically understand the non-linear arm kinematics, which is difficult to learn from limited demonstrations. To address this issue, this letter proposes a kinematics-aware imitation learning framework with consistent task, observation, and action spaces, all represented in the same 3D space. Specifically, we represent both robot states and actions using a set of 3D points on the arm body, naturally aligned with the 3D point cloud observations. This spatially consistent representation improves the policy's sample efficiency and spatial generalizability while enabling full-body control. Built upon the diffusion policy, we further incorporate kinematics priors into the diffusion processes to guarantee the kinematic feasibility of output actions. The joint angle commands are finally calculated through an optimization-based whole-body inverse kinematics solver for execution. Simulation and real-world experimental results demonstrate higher success rates and stronger spatial generalizability of our approach compared to existing methods in body-aware manipulation policy learning.

