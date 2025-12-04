---
layout: default
title: Multimodal Control of Manipulators: Coupling Kinematics and Vision for Self-Driving Laboratory Operations
---

# Multimodal Control of Manipulators: Coupling Kinematics and Vision for Self-Driving Laboratory Operations
**arXiv**：[2512.03630v1](https://arxiv.org/abs/2512.03630) · [PDF](https://arxiv.org/pdf/2512.03630.pdf)  
**作者**：Shifa Sulaiman, Amarnath H, Simon Bogh, Naresh Marturi  

**一句话要点**：提出基于雅可比方法的三种运动规划方案，用于冗余机械臂与夹爪的自驾实验室操作

**关键词**：运动规划, 雅可比方法, 冗余机械臂, 螺旋理论, RRT*算法, 仿真分析

## 3 点简述
- 核心问题：为冗余机械臂与耦合夹爪规划从初始到最终位姿的运动轨迹和关节解
- 方法要点：使用RRT*算法规划轨迹，基于螺旋理论求解正向运动学，并比较三种雅可比逆解方法
- 实验或效果：通过仿真分析轨迹平滑度、误差及关节运动特性，评估不同方法的优劣

## 摘要（原文）

> Motion planning schemes are used for planning motions of a manipulator from an initial pose to a final pose during a task execution. A motion planning scheme generally comprises of a trajectory planning method and an inverse kinematic solver to determine trajectories and joints solutions respectively. In this paper, 3 motion planning schemes developed based on Jacobian methods are implemented to traverse a redundant manipulator with a coupled finger gripper through given trajectories. RRT* algorithm is used for planning trajectories and screw theory based forward kinematic equations are solved for determining joint solutions of the manipulator and gripper. Inverse solutions are computed separately using 3 Jacobian based methods such as Jacobian Transpose (JT), Pseudo Inverse (PI), and Damped Least Square (DLS) methods. Space Jacobian and manipulability measurements of the manipulator and gripper are obtained using screw theory formulations. Smoothness and RMSE error of generated trajectories and velocity continuity, acceleration profile, jerk, and snap values of joint motions are analysed for determining an efficient motion planning method for a given task. Advantages and disadvantages of the proposed motion planning schemes mentioned above are analysed using simulation studies to determine a suitable inverse solution technique for the tasks.

