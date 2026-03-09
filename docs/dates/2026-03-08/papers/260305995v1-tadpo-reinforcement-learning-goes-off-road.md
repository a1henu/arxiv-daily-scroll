---
layout: default
title: TADPO: Reinforcement Learning Goes Off-road
---

# TADPO: Reinforcement Learning Goes Off-road
**arXiv**：[2603.05995v1](https://arxiv.org/abs/2603.05995) · [PDF](https://arxiv.org/pdf/2603.05995.pdf)  
**作者**：Zhouchonghao Wu, Raymond Song, Vedant Mundheda, Luis E. Navarro-Serment, Christof Schoenborn, Jeff Schneider  

**一句话要点**：提出TADPO强化学习方法，解决越野自动驾驶中的长时程规划与控制问题。

**关键词**：越野自动驾驶, 强化学习, 策略梯度, 零样本迁移, 端到端系统

## 3 点简述
- 越野自动驾驶面临未映射多变地形和不确定动态的挑战，需长时程规划与自适应控制。
- TADPO基于PPO扩展，利用离策略轨迹指导与在策略轨迹探索，提升策略学习效率。
- 系统在仿真中验证，并零样本迁移至全尺寸越野车，实现高速越野驾驶。

## 摘要（原文）

> Off-road autonomous driving poses significant challenges such as navigating unmapped, variable terrain with uncertain and diverse dynamics. Addressing these challenges requires effective long-horizon planning and adaptable control. Reinforcement Learning (RL) offers a promising solution by learning control policies directly from interaction. However, because off-road driving is a long-horizon task with low-signal rewards, standard RL methods are challenging to apply in this setting. We introduce TADPO, a novel policy gradient formulation that extends Proximal Policy Optimization (PPO), leveraging off-policy trajectories for teacher guidance and on-policy trajectories for student exploration. Building on this, we develop a vision-based, end-to-end RL system for high-speed off-road driving, capable of navigating extreme slopes and obstacle-rich terrain. We demonstrate our performance in simulation and, importantly, zero-shot sim-to-real transfer on a full-scale off-road vehicle. To our knowledge, this work represents the first deployment of RL-based policies on a full-scale off-road platform.

