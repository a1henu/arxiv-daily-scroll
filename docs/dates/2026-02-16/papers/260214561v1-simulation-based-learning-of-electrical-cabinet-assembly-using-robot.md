---
layout: default
title: Simulation-based Learning of Electrical Cabinet Assembly Using Robot Skills
---

# Simulation-based Learning of Electrical Cabinet Assembly Using Robot Skills
**arXiv**：[2602.14561v1](https://arxiv.org/abs/2602.14561) · [PDF](https://arxiv.org/pdf/2602.14561.pdf)  
**作者**：Arik Laemmle, Balázs András Bálint, Philipp Tenbrock, Frank Naegele, David Traunecker, József Váncza, Marco F. Huber  

**一句话要点**：提出基于仿真与机器人技能的深度强化学习方法，以自动化电气柜端子装配任务。

**关键词**：深度强化学习, 机器人技能, 物理仿真, 装配自动化, 域随机化

## 3 点简述
- 核心问题：电气端子装配编程复杂且产品多变，传统方法难以适应。
- 方法要点：结合深度强化学习与参数化机器人技能，在物理仿真中训练策略。
- 实验或效果：仿真与实物实验成功率高达100%，能泛化新端子类型和位置。

## 摘要（原文）

> This paper presents a simulation-driven approach for automating the force-controlled assembly of electrical terminals on DIN-rails, a task traditionally hindered by high programming effort and product variability. The proposed method integrates deep reinforcement learning (DRL) with parameterizable robot skills in a physics-based simulation environment. To realistically model the snap-fit assembly process, we develop and evaluate two types of joining models: analytical models based on beam theory and rigid-body models implemented in the MuJoCo physics engine. These models enable accurate simulation of interaction forces, essential for training DRL agents. The robot skills are structured using the pitasc framework, allowing modular, reusable control strategies. Training is conducted in simulation using Soft Actor-Critic (SAC) and Twin Delayed Deep Deterministic Policy Gradient (TD3) algorithms. Domain randomization is applied to improve robustness. The trained policies are transferred to a physical UR10e robot system without additional tuning. Experimental results demonstrate high success rates (up to 100%) in both simulation and real-world settings, even under significant positional and rotational deviations. The system generalizes well to new terminal types and positions, significantly reducing manual programming effort. This work highlights the potential of combining simulation-based learning with modular robot skills for flexible, scalable automation in small-batch manufacturing. Future work will explore hybrid learning methods, automated environment parameterization, and further refinement of joining models for design integration.

