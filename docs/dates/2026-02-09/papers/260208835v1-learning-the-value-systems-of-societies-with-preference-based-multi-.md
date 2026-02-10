---
layout: default
title: Learning the Value Systems of Societies with Preference-based Multi-objective Reinforcement Learning
---

# Learning the Value Systems of Societies with Preference-based Multi-objective Reinforcement Learning
**arXiv**：[2602.08835v1](https://arxiv.org/abs/2602.08835) · [PDF](https://arxiv.org/pdf/2602.08835.pdf)  
**作者**：Andrés Holgado-Sánchez, Peter Vamplew, Richard Dazeley, Sascha Ossowski, Holger Billhardt  

**一句话要点**：提出基于聚类和偏好多目标强化学习的算法，以学习社会代理的价值对齐模型和价值系统。

**关键词**：价值对齐, 多目标强化学习, 社会代理, 聚类分析, 偏好学习

## 3 点简述
- 核心问题：价值感知AI需适应不同用户的价值系统，但现有方法存在特征设计依赖或缺乏可解释性。
- 方法要点：在MDP中联合学习社会衍生的价值对齐模型和代表用户群体的价值系统，每个集群包含价值系统和近似帕累托最优策略。
- 实验或效果：在两个MDP上评估，与先进PbMORL算法和基线比较，验证方法有效性。

## 摘要（原文）

> Value-aware AI should recognise human values and adapt to the value systems (value-based preferences) of different users. This requires operationalization of values, which can be prone to misspecification. The social nature of values demands their representation to adhere to multiple users while value systems are diverse, yet exhibit patterns among groups. In sequential decision making, efforts have been made towards personalization for different goals or values from demonstrations of diverse agents. However, these approaches demand manually designed features or lack value-based interpretability and/or adaptability to diverse user preferences.
>   We propose algorithms for learning models of value alignment and value systems for a society of agents in Markov Decision Processes (MDPs), based on clustering and preference-based multi-objective reinforcement learning (PbMORL). We jointly learn socially-derived value alignment models (groundings) and a set of value systems that concisely represent different groups of users (clusters) in a society. Each cluster consists of a value system representing the value-based preferences of its members and an approximately Pareto-optimal policy that reflects behaviours aligned with this value system. We evaluate our method against a state-of-the-art PbMORL algorithm and baselines on two MDPs with human values.

