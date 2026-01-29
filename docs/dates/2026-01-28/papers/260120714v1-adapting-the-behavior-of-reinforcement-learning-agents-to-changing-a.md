---
layout: default
title: Adapting the Behavior of Reinforcement Learning Agents to Changing Action Spaces and Reward Functions
---

# Adapting the Behavior of Reinforcement Learning Agents to Changing Action Spaces and Reward Functions
**arXiv**：[2601.20714v1](https://arxiv.org/abs/2601.20714) · [PDF](https://arxiv.org/pdf/2601.20714.pdf)  
**作者**：Raul de la Rosa, Ivana Dusparic, Nicolas Cardozo  

**一句话要点**：提出MORPHIN框架，使强化学习代理能自适应非平稳环境中的奖励函数和动作空间变化。

**关键词**：强化学习, 自适应学习, 概念漂移检测, 非平稳环境, Q学习框架, 交通信号控制

## 3 点简述
- 核心问题：强化学习代理在奖励函数变化或动作空间扩展的非平稳环境中表现不佳。
- 方法要点：MORPHIN集成概念漂移检测和动态超参数调整，支持在线适应并防止灾难性遗忘。
- 实验或效果：在Gridworld和交通信号控制模拟中，MORPHIN比标准Q学习收敛更快，学习效率提升达1.7倍。

## 摘要（原文）

> Reinforcement Learning (RL) agents often struggle in real-world applications where environmental conditions are non-stationary, particularly when reward functions shift or the available action space expands. This paper introduces MORPHIN, a self-adaptive Q-learning framework that enables on-the-fly adaptation without full retraining. By integrating concept drift detection with dynamic adjustments to learning and exploration hyperparameters, MORPHIN adapts agents to changes in both the reward function and on-the-fly expansions of the agent's action space, while preserving prior policy knowledge to prevent catastrophic forgetting. We validate our approach using a Gridworld benchmark and a traffic signal control simulation. The results demonstrate that MORPHIN achieves superior convergence speed and continuous adaptation compared to a standard Q-learning baseline, improving learning efficiency by up to 1.7x.

