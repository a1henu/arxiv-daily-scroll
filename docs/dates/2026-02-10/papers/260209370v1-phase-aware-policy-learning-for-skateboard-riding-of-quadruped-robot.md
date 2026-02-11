---
layout: default
title: Phase-Aware Policy Learning for Skateboard Riding of Quadruped Robots via Feature-wise Linear Modulation
---

# Phase-Aware Policy Learning for Skateboard Riding of Quadruped Robots via Feature-wise Linear Modulation
**arXiv**：[2602.09370v1](https://arxiv.org/abs/2602.09370) · [PDF](https://arxiv.org/pdf/2602.09370.pdf)  
**作者**：Minsung Yoon, Jeil Jeong, Sung-Eui Yoon  

**一句话要点**：提出相位感知策略学习框架，通过特征线性调制解决四足机器人滑板骑行的多模态控制问题。

**关键词**：四足机器人, 滑板骑行, 强化学习, 相位感知控制, 特征线性调制, 多模态策略

## 3 点简述
- 核心问题：滑板骑行涉及感知驱动交互和不同阶段的模态控制，对策略学习构成挑战。
- 方法要点：集成相位条件特征线性调制层到强化学习网络，实现统一策略捕获相位依赖行为。
- 实验或效果：仿真验证命令跟踪精度，比较运动效率，并展示现实世界可转移性。

## 摘要（原文）

> Skateboards offer a compact and efficient means of transportation as a type of personal mobility device. However, controlling them with legged robots poses several challenges for policy learning due to perception-driven interactions and multi-modal control objectives across distinct skateboarding phases. To address these challenges, we introduce Phase-Aware Policy Learning (PAPL), a reinforcement-learning framework tailored for skateboarding with quadruped robots. PAPL leverages the cyclic nature of skateboarding by integrating phase-conditioned Feature-wise Linear Modulation layers into actor and critic networks, enabling a unified policy that captures phase-dependent behaviors while sharing robot-specific knowledge across phases. Our evaluations in simulation validate command-tracking accuracy and conduct ablation studies quantifying each component's contribution. We also compare locomotion efficiency against leg and wheel-leg baselines and show real-world transferability.

