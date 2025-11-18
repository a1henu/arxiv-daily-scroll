---
layout: default
title: Contact-Safe Reinforcement Learning with ProMP Reparameterization and Energy Awareness
---

# Contact-Safe Reinforcement Learning with ProMP Reparameterization and Energy Awareness
**arXiv**：[2511.13459v1](https://arxiv.org/abs/2511.13459) · [PDF](https://arxiv.org/pdf/2511.13459.pdf)  
**作者**：Bingkun Huang, Yuhe Gong, Zewen Yang, Tianyu Ren, Luis Figueredo  

**一句话要点**：提出任务空间能量安全框架，结合PPO与运动基元，解决接触丰富操作中的安全与鲁棒性问题。

**关键词**：强化学习, 机器人操作, 接触安全, 能量感知, 运动基元, 笛卡尔阻抗控制

## 3 点简述
- 核心问题：传统强化学习在机器人任务空间操作中忽视接触安全和能量感知，导致交互不安全。
- 方法要点：结合PPO与运动基元，引入能量感知笛卡尔阻抗控制器，确保安全交互。
- 实验或效果：在多种3D环境表面任务中，优于现有方法，实现高成功率和平滑轨迹。

## 摘要（原文）

> Reinforcement learning (RL) approaches based on Markov Decision Processes (MDPs) are predominantly applied in the robot joint space, often relying on limited task-specific information and partial awareness of the 3D environment. In contrast, episodic RL has demonstrated advantages over traditional MDP-based methods in terms of trajectory consistency, task awareness, and overall performance in complex robotic tasks. Moreover, traditional step-wise and episodic RL methods often neglect the contact-rich information inherent in task-space manipulation, especially considering the contact-safety and robustness. In this work, contact-rich manipulation tasks are tackled using a task-space, energy-safe framework, where reliable and safe task-space trajectories are generated through the combination of Proximal Policy Optimization (PPO) and movement primitives. Furthermore, an energy-aware Cartesian Impedance Controller objective is incorporated within the proposed framework to ensure safe interactions between the robot and the environment. Our experimental results demonstrate that the proposed framework outperforms existing methods in handling tasks on various types of surfaces in 3D environments, achieving high success rates as well as smooth trajectories and energy-safe interactions.

