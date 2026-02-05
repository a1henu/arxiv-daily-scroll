---
layout: default
title: CRoSS: A Continual Robotic Simulation Suite for Scalable Reinforcement Learning with High Task Diversity and Realistic Physics Simulation
---

# CRoSS: A Continual Robotic Simulation Suite for Scalable Reinforcement Learning with High Task Diversity and Realistic Physics Simulation
**arXiv**：[2602.04868v1](https://arxiv.org/abs/2602.04868) · [PDF](https://arxiv.org/pdf/2602.04868.pdf)  
**作者**：Yannick Denker, Alexander Gepperth  

**一句话要点**：提出CRoSS基准套件，用于机器人场景中高物理真实性的持续强化学习研究。

**关键词**：持续强化学习, 机器人模拟, 基准套件, 物理仿真, 可扩展性, 可复现性

## 3 点简述
- 核心问题：持续强化学习需在任务序列中学习而不遗忘先前策略。
- 方法要点：基于Gazebo模拟器，提供两轮差速机器人和七关节机械臂的多样化任务基准。
- 实验或效果：支持容器化部署，报告DQN和策略梯度算法性能，确保可复现性。

## 摘要（原文）

> Continual reinforcement learning (CRL) requires agents to learn from a sequence of tasks without forgetting previously acquired policies. In this work, we introduce a novel benchmark suite for CRL based on realistically simulated robots in the Gazebo simulator. Our Continual Robotic Simulation Suite (CRoSS) benchmarks rely on two robotic platforms: a two-wheeled differential-drive robot with lidar, camera and bumper sensor, and a robotic arm with seven joints. The former represent an agent in line-following and object-pushing scenarios, where variation of visual and structural parameters yields a large number of distinct tasks, whereas the latter is used in two goal-reaching scenarios with high-level cartesian hand position control (modeled after the Continual World benchmark), and low-level control based on joint angles. For the robotic arm benchmarks, we provide additional kinematics-only variants that bypass the need for physical simulation (as long as no sensor readings are required), and which can be run two orders of magnitude faster. CRoSS is designed to be easily extensible and enables controlled studies of continual reinforcement learning in robotic settings with high physical realism, and in particular allow the use of almost arbitrary simulated sensors. To ensure reproducibility and ease of use, we provide a containerized setup (Apptainer) that runs out-of-the-box, and report performances of standard RL algorithms, including Deep Q-Networks (DQN) and policy gradient methods. This highlights the suitability as a scalable and reproducible benchmark for CRL research.

