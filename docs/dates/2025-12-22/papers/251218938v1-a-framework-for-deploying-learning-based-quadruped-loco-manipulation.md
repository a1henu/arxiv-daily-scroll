---
layout: default
title: A Framework for Deploying Learning-based Quadruped Loco-Manipulation
---

# A Framework for Deploying Learning-based Quadruped Loco-Manipulation
**arXiv**：[2512.18938v1](https://arxiv.org/abs/2512.18938) · [PDF](https://arxiv.org/pdf/2512.18938.pdf)  
**作者**：Yadong Liu, Jianwei Liu, He Liang, Dimitrios Kanoulas  

**一句话要点**：提出开源框架以部署基于强化学习的四足机器人移动操作控制器

**关键词**：四足机器人, 移动操作, 强化学习, 仿真到现实转移, 开源框架, 全身控制

## 3 点简述
- 核心问题：四足移动操作机器人控制困难，仿真到现实转移不可靠，现有框架多为专有且难以复现。
- 方法要点：通过ROS统一仿真到仿真和仿真到现实转移，在Isaac Gym训练策略，扩展至MuJoCo，并部署到物理硬件。
- 实验或效果：仿真实验揭示接触模型差异影响策略行为，真实世界试验显示全身协调控制提升操作范围和性能。

## 摘要（原文）

> Quadruped mobile manipulators offer strong potential for agile loco-manipulation but remain difficult to control and transfer reliably from simulation to reality. Reinforcement learning (RL) shows promise for whole-body control, yet most frameworks are proprietary and hard to reproduce on real hardware. We present an open pipeline for training, benchmarking, and deploying RL-based controllers on the Unitree B1 quadruped with a Z1 arm. The framework unifies sim-to-sim and sim-to-real transfer through ROS, re-implementing a policy trained in Isaac Gym, extending it to MuJoCo via a hardware abstraction layer, and deploying the same controller on physical hardware. Sim-to-sim experiments expose discrepancies between Isaac Gym and MuJoCo contact models that influence policy behavior, while real-world teleoperated object-picking trials show that coordinated whole-body control extends reach and improves manipulation over floating-base baselines. The pipeline provides a transparent, reproducible foundation for developing and analyzing RL-based loco-manipulation controllers and will be released open source to support future research.

