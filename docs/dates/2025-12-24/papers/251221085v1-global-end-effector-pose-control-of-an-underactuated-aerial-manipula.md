---
layout: default
title: Global End-Effector Pose Control of an Underactuated Aerial Manipulator via Reinforcement Learning
---

# Global End-Effector Pose Control of an Underactuated Aerial Manipulator via Reinforcement Learning
**arXiv**：[2512.21085v1](https://arxiv.org/abs/2512.21085) · [PDF](https://arxiv.org/pdf/2512.21085.pdf)  
**作者**：Shlok Deshmukh, Javier Alonso-Mora, Sihao Sun  

**一句话要点**：提出基于强化学习的控制策略，实现欠驱动空中机械臂的六自由度末端位姿精确控制。

**关键词**：空中机械臂, 强化学习控制, 欠驱动系统, 六自由度控制, 轻量化设计

## 3 点简述
- 核心问题：轻量化2自由度机械臂因欠驱动和外部扰动，难以实现稳定六自由度末端位姿控制。
- 方法要点：使用PPO算法训练代理，生成前馈命令，结合INDI姿态控制器和PID关节控制器进行跟踪。
- 实验或效果：飞行实验显示厘米级位置精度和度级方向精度，在外部力扰动下表现鲁棒。

## 摘要（原文）

> Aerial manipulators, which combine robotic arms with multi-rotor drones, face strict constraints on arm weight and mechanical complexity. In this work, we study a lightweight 2-degree-of-freedom (DoF) arm mounted on a quadrotor via a differential mechanism, capable of full six-DoF end-effector pose control. While the minimal design enables simplicity and reduced payload, it also introduces challenges such as underactuation and sensitivity to external disturbances, including manipulation of heavy loads and pushing tasks. To address these, we employ reinforcement learning, training a Proximal Policy Optimization (PPO) agent in simulation to generate feedforward commands for quadrotor acceleration and body rates, along with joint angle targets. These commands are tracked by an incremental nonlinear dynamic inversion (INDI) attitude controller and a PID joint controller, respectively. Flight experiments demonstrate centimeter-level position accuracy and degree-level orientation precision, with robust performance under external force disturbances. The results highlight the potential of learning-based control strategies for enabling contact-rich aerial manipulation using simple, lightweight platforms.

