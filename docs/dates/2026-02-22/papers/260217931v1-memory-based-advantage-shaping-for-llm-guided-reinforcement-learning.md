---
layout: default
title: Memory-Based Advantage Shaping for LLM-Guided Reinforcement Learning
---

# Memory-Based Advantage Shaping for LLM-Guided Reinforcement Learning
**arXiv**：[2602.17931v1](https://arxiv.org/abs/2602.17931) · [PDF](https://arxiv.org/pdf/2602.17931.pdf)  
**作者**：Narjes Nourzad, Carlee Joe-Wong  

**一句话要点**：提出基于记忆的优势塑形方法，以稀疏奖励环境中的LLM引导强化学习。

**关键词**：强化学习, 大语言模型引导, 优势塑形, 记忆图, 稀疏奖励, 样本效率

## 3 点简述
- 核心问题：稀疏或延迟奖励导致强化学习样本复杂度高，LLM引导存在可扩展性和可靠性问题。
- 方法要点：构建记忆图编码子目标和轨迹，推导效用函数塑形优势函数，减少在线LLM查询依赖。
- 实验或效果：基准环境中样本效率提升，早期学习加速，最终回报与频繁LLM交互方法相当。

## 摘要（原文）

> In environments with sparse or delayed rewards, reinforcement learning (RL) incurs high sample complexity due to the large number of interactions needed for learning. This limitation has motivated the use of large language models (LLMs) for subgoal discovery and trajectory guidance. While LLMs can support exploration, frequent reliance on LLM calls raises concerns about scalability and reliability. We address these challenges by constructing a memory graph that encodes subgoals and trajectories from both LLM guidance and the agent's own successful rollouts. From this graph, we derive a utility function that evaluates how closely the agent's trajectories align with prior successful strategies. This utility shapes the advantage function, providing the critic with additional guidance without altering the reward. Our method relies primarily on offline input and only occasional online queries, avoiding dependence on continuous LLM supervision. Preliminary experiments in benchmark environments show improved sample efficiency and faster early learning compared to baseline RL methods, with final returns comparable to methods that require frequent LLM interaction.

