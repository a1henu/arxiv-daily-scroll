---
layout: default
title: Learning Sim-to-Real Humanoid Locomotion in 15 Minutes
---

# Learning Sim-to-Real Humanoid Locomotion in 15 Minutes
**arXiv**：[2512.01996v1](https://arxiv.org/abs/2512.01996) · [PDF](https://arxiv.org/pdf/2512.01996.pdf)  
**作者**：Younggyo Seo, Carmelo Sferrazza, Juyue Chen, Guanya Shi, Rocky Duan, Pieter Abbeel  

**一句话要点**：提出基于FastSAC和FastTD3的简单配方，在15分钟内实现人形机器人快速仿真到真实环境的强化学习训练。

**关键词**：人形机器人控制, 仿真到真实学习, 强化学习, 大规模并行仿真, 领域随机化

## 3 点简述
- 核心问题：人形机器人仿真到真实环境的强化学习训练因高维度和领域随机化而困难，难以快速可靠。
- 方法要点：使用大规模并行仿真和精心调优的离策略RL算法，结合简约奖励函数，稳定训练过程。
- 实验或效果：在Unitree G1和Booster T1机器人上实现快速端到端学习，包括强领域随机化下的运动控制和全身人体运动跟踪。

## 摘要（原文）

> Massively parallel simulation has reduced reinforcement learning (RL) training time for robots from days to minutes. However, achieving fast and reliable sim-to-real RL for humanoid control remains difficult due to the challenges introduced by factors such as high dimensionality and domain randomization. In this work, we introduce a simple and practical recipe based on off-policy RL algorithms, i.e., FastSAC and FastTD3, that enables rapid training of humanoid locomotion policies in just 15 minutes with a single RTX 4090 GPU. Our simple recipe stabilizes off-policy RL algorithms at massive scale with thousands of parallel environments through carefully tuned design choices and minimalist reward functions. We demonstrate rapid end-to-end learning of humanoid locomotion controllers on Unitree G1 and Booster T1 robots under strong domain randomization, e.g., randomized dynamics, rough terrain, and push perturbations, as well as fast training of whole-body human-motion tracking policies. We provide videos and open-source implementation at: https://younggyo.me/fastsac-humanoid.

