---
layout: default
title: Autonomous Planning In-space Assembly Reinforcement-learning free-flYer (APIARY) International Space Station Astrobee Testing
---

# Autonomous Planning In-space Assembly Reinforcement-learning free-flYer (APIARY) International Space Station Astrobee Testing
**arXiv**：[2512.03729v1](https://arxiv.org/abs/2512.03729) · [PDF](https://arxiv.org/pdf/2512.03729.pdf)  
**作者**：Samantha Chapin, Kenneth Stewart, Roxana Leontie, Carl Glen Henshaw  

**一句话要点**：提出基于强化学习的自主规划方法，在国际空间站零重力环境下控制自由飞行机器人Astrobee。

**关键词**：强化学习控制, 自由飞行机器人, 零重力环境, 国际空间站, 近端策略优化, 自主规划

## 3 点简述
- 核心问题：在空间零重力环境中实现自由飞行机器人的自主控制，以提升机器人自主性。
- 方法要点：使用演员-评论家近端策略优化网络，在模拟环境中训练6自由度鲁棒控制策略。
- 实验或效果：在国际空间站上首次实现强化学习控制自由飞行器，验证了快速部署定制行为的能力。

## 摘要（原文）

> The US Naval Research Laboratory's (NRL's) Autonomous Planning In-space Assembly Reinforcement-learning free-flYer (APIARY) experiment pioneers the use of reinforcement learning (RL) for control of free-flying robots in the zero-gravity (zero-G) environment of space. On Tuesday, May 27th 2025 the APIARY team conducted the first ever, to our knowledge, RL control of a free-flyer in space using the NASA Astrobee robot on-board the International Space Station (ISS). A robust 6-degrees of freedom (DOF) control policy was trained using an actor-critic Proximal Policy Optimization (PPO) network within the NVIDIA Isaac Lab simulation environment, randomizing over goal poses and mass distributions to enhance robustness. This paper details the simulation testing, ground testing, and flight validation of this experiment. This on-orbit demonstration validates the transformative potential of RL for improving robotic autonomy, enabling rapid development and deployment (in minutes to hours) of tailored behaviors for space exploration, logistics, and real-time mission needs.

