---
layout: default
title: Learning Transferability: A Two-Stage Reinforcement Learning Approach for Enhancing Quadruped Robots' Performance in U-Shaped Stair Climbing
---

# Learning Transferability: A Two-Stage Reinforcement Learning Approach for Enhancing Quadruped Robots' Performance in U-Shaped Stair Climbing
**arXiv**：[2602.14473v1](https://arxiv.org/abs/2602.14473) · [PDF](https://arxiv.org/pdf/2602.14473.pdf)  
**作者**：Baixiao Huang, Baiyu Huang, Yu Hou  

**一句话要点**：提出两阶段强化学习方法以提升四足机器人在U形楼梯的攀爬性能

**关键词**：四足机器人, 强化学习, 楼梯攀爬, 策略迁移, 端到端学习

## 3 点简述
- 核心问题：四足机器人在不同室内楼梯自主攀爬困难，影响建筑任务完成。
- 方法要点：采用两阶段端到端深度强化学习，先在金字塔楼梯训练，再迁移至U形楼梯。
- 实验或效果：成功实现U形楼梯攀爬，并验证策略在直形、L形和螺旋楼梯的迁移性。

## 摘要（原文）

> Quadruped robots are employed in various scenarios in building construction. However, autonomous stair climbing across different indoor staircases remains a major challenge for robot dogs to complete building construction tasks. In this project, we employed a two-stage end-to-end deep reinforcement learning (RL) approach to optimize a robot's performance on U-shaped stairs. The training robot-dog modality, Unitree Go2, was first trained to climb stairs on Isaac Lab's pyramid-stair terrain, and then to climb a U-shaped indoor staircase using the learned policies. This project explores end-to-end RL methods that enable robot dogs to autonomously climb stairs. The results showed (1) the successful goal reached for robot dogs climbing U-shaped stairs with a stall penalty, and (2) the transferability from the policy trained on U-shaped stairs to deployment on straight, L-shaped, and spiral stair terrains, and transferability from other stair models to deployment on U-shaped terrain.

