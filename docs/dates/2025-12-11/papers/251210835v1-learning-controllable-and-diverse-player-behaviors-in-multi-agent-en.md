---
layout: default
title: Learning Controllable and Diverse Player Behaviors in Multi-Agent Environments
---

# Learning Controllable and Diverse Player Behaviors in Multi-Agent Environments
**arXiv**：[2512.10835v1](https://arxiv.org/abs/2512.10835) · [PDF](https://arxiv.org/pdf/2512.10835.pdf)  
**作者**：Atahan Cilan, Atay Özgövde  

**一句话要点**：提出强化学习框架以在无需人类数据下实现多智能体环境中可控且多样的玩家行为。

**关键词**：强化学习, 多智能体系统, 行为控制, 游戏AI, 可解释AI

## 3 点简述
- 核心问题：现有方法依赖大规模玩家轨迹或缺乏可解释行为参数映射，限制可扩展性和可控性。
- 方法要点：在N维连续空间定义行为，通过目标行为向量输入和距离减少奖励，学习动作对行为统计的影响。
- 实验或效果：在自定义Unity游戏中，相比仅赢基线，产生显著更多行为多样性，并能可靠匹配指定行为向量。

## 摘要（原文）

> This paper introduces a reinforcement learning framework that enables controllable and diverse player behaviors without relying on human gameplay data. Existing approaches often require large-scale player trajectories, train separate models for different player types, or provide no direct mapping between interpretable behavioral parameters and the learned policy, limiting their scalability and controllability. We define player behavior in an N-dimensional continuous space and uniformly sample target behavior vectors from a region that encompasses the subset representing real human styles. During training, each agent receives both its current and target behavior vectors as input, and the reward is based on the normalized reduction in distance between them. This allows the policy to learn how actions influence behavioral statistics, enabling smooth control over attributes such as aggressiveness, mobility, and cooperativeness. A single PPO-based multi-agent policy can reproduce new or unseen play styles without retraining. Experiments conducted in a custom multi-player Unity game show that the proposed framework produces significantly greater behavioral diversity than a win-only baseline and reliably matches specified behavior vectors across diverse targets. The method offers a scalable solution for automated playtesting, game balancing, human-like behavior simulation, and replacing disconnected players in online games.

