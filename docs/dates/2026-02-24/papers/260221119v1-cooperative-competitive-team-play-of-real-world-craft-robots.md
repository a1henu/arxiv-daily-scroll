---
layout: default
title: Cooperative-Competitive Team Play of Real-World Craft Robots
---

# Cooperative-Competitive Team Play of Real-World Craft Robots
**arXiv**：[2602.21119v1](https://arxiv.org/abs/2602.21119) · [PDF](https://arxiv.org/pdf/2602.21119.pdf)  
**作者**：Rui Zhao, Xihui Li, Yizheng Zhang, Yuzhen Liu, Zhong Zhang, Yufeng Zhang, Cheng Zhou, Zhengyou Zhang, Lei Han  

**一句话要点**：提出OODSI方法以提升多机器人协同竞争策略的仿真到现实迁移性能

**关键词**：多智能体强化学习, 仿真到现实迁移, 机器人协同竞争, 分布式学习框架, OODSI方法

## 3 点简述
- 核心问题：多智能体强化学习在真实机器人集体训练和策略迁移中效率低、仿真与现实差距大
- 方法要点：开发完整机器人系统，包括仿真、分布式学习框架和物理组件，并引入OODSI缓解仿真到现实差距
- 实验或效果：在真实多机器人汽车竞争游戏和协同任务中验证，OODSI将Sim2Real性能提升20%

## 摘要（原文）

> Multi-agent deep Reinforcement Learning (RL) has made significant progress in developing intelligent game-playing agents in recent years. However, the efficient training of collective robots using multi-agent RL and the transfer of learned policies to real-world applications remain open research questions. In this work, we first develop a comprehensive robotic system, including simulation, distributed learning framework, and physical robot components. We then propose and evaluate reinforcement learning techniques designed for efficient training of cooperative and competitive policies on this platform. To address the challenges of multi-agent sim-to-real transfer, we introduce Out of Distribution State Initialization (OODSI) to mitigate the impact of the sim-to-real gap. In the experiments, OODSI improves the Sim2Real performance by 20%. We demonstrate the effectiveness of our approach through experiments with a multi-robot car competitive game and a cooperative task in real-world settings.

