---
layout: default
title: Trajectory Tracking for Multi-Manipulator Systems in Constrained Environments
---

# Trajectory Tracking for Multi-Manipulator Systems in Constrained Environments
**arXiv**：[2512.14206v1](https://arxiv.org/abs/2512.14206) · [PDF](https://arxiv.org/pdf/2512.14206.pdf)  
**作者**：Mayank Sewlia, Christos K. Verginis, Dimos V. Dimarogonas  

**一句话要点**：提出多速率规划控制框架以解决受限环境中多移动机械臂协同操作轨迹跟踪问题

**关键词**：多移动机械臂系统, 轨迹跟踪, 受限环境, 时空任务规范, 多速率控制, 协同操作

## 3 点简述
- 核心问题：在障碍物密集的受限环境下，多移动机械臂系统需满足时空任务规范，协调运输抓取物体。
- 方法要点：结合离线生成满足STL的对象轨迹和无碰撞基座轨迹，在线进行约束逆运动学和连续时间反馈控制。
- 实验或效果：通过高保真物理仿真，使用三个Franka Emika Panda移动机械臂刚性抓取物体进行评估。

## 摘要（原文）

> We consider the problem of cooperative manipulation by a mobile multi-manipulator system operating in obstacle-cluttered and highly constrained environments under spatio-temporal task specifications. The task requires transporting a grasped object while respecting both continuous robot dynamics and discrete geometric constraints arising from obstacles and narrow passages. To address this hybrid structure, we propose a multi-rate planning and control framework that combines offline generation of an STL-satisfying object trajectory and collision-free base footprints with online constrained inverse kinematics and continuous-time feedback control. The resulting closed-loop system enables coordinated reconfiguration of multiple manipulators while tracking the desired object motion. The approach is evaluated in high-fidelity physics simulations using three Franka Emika Panda mobile manipulators rigidly grasping an object.

