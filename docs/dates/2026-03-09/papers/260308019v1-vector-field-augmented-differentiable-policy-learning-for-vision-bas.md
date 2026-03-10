---
layout: default
title: Vector Field Augmented Differentiable Policy Learning for Vision-Based Drone Racing
---

# Vector Field Augmented Differentiable Policy Learning for Vision-Based Drone Racing
**arXiv**：[2603.08019v1](https://arxiv.org/abs/2603.08019) · [PDF](https://arxiv.org/pdf/2603.08019.pdf)  
**作者**：Yang Su, Feng Yu, Yu Hu, Xinze Niu, Linzuo Zhang, Fangyu Sun, Danping Zou  

**一句话要点**：提出DiffRacing框架，通过向量场增强可微分策略学习以解决无人机竞速中的障碍规避与高速穿越问题。

**关键词**：无人机竞速, 可微分策略学习, 向量场增强, 障碍规避, 仿真到真实迁移

## 3 点简述
- 核心问题：无人机竞速需高速飞行与可靠避障，但穿越门等目标难以表达为平滑可微分损失。
- 方法要点：集成可微分损失与向量场，提供连续梯度信号，并引入可微分Delta Action模型补偿动力学不匹配。
- 实验或效果：在仿真与真实实验中，DiffRacing表现出高样本效率、快速收敛和鲁棒飞行性能。

## 摘要（原文）

> Autonomous drone racing in complex environments requires agile, high-speed flight while maintaining reliable obstacle avoidance. Differentiable-physics-based policy learning has recently demonstrated high sample efficiency and remarkable performance across various tasks, including agile drone flight and quadruped locomotion. However, applying such methods to drone racing remains difficult, as key objective like gate traversal are inherently hard to express as smooth, differentiable losses. To address these challenges, we propose DiffRacing, a novel vector field-augmented differentiable policy learning framework. DiffRacing integrates differentiable losses and vector fields into the training process to provide continuous and stable gradient signals, balancing obstacle avoidance and high-speed gate traversal. In addition, a differentiable Delta Action Model compensates for dynamics mismatch, enabling efficient sim-to-real transfer without explicit system identification. Extensive simulation and real-world experiments demonstrate that DiffRacing achieves superior sample efficiency, faster convergence, and robust flight performance, thereby demonstrating that vector fields can augment traditional gradient-based policy learning with a task-specific geometric prior.

