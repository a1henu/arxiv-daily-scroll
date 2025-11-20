---
layout: default
title: Path Planning through Multi-Agent Reinforcement Learning in Dynamic Environments
---

# Path Planning through Multi-Agent Reinforcement Learning in Dynamic Environments
**arXiv**：[2511.15284v1](https://arxiv.org/abs/2511.15284) · [PDF](https://arxiv.org/pdf/2511.15284.pdf)  
**作者**：Jonas De Maeyer, Hossein Yarahmadi, Moharram Challenger  

**一句话要点**：提出基于多智能体强化学习的可扩展路径规划框架，以应对动态环境中的不确定性。

**关键词**：路径规划, 多智能体强化学习, 动态环境, 联邦学习, 可扩展性, 分层分解

## 3 点简述
- 核心问题：动态环境中路径规划需适应变化障碍物，现有方法假设不现实且可扩展性差。
- 方法要点：采用分层环境分解和分布式RL代理，结合局部适应和联邦Q学习聚合策略。
- 实验或效果：联邦变体优于单智能体，接近A* Oracle性能，适应时间短且可扩展性强。

## 摘要（原文）

> Path planning in dynamic environments is a fundamental challenge in intelligent transportation and robotics, where obstacles and conditions change over time, introducing uncertainty and requiring continuous adaptation. While existing approaches often assume complete environmental unpredictability or rely on global planners, these assumptions limit scalability and practical deployment in real-world settings. In this paper, we propose a scalable, region-aware reinforcement learning (RL) framework for path planning in dynamic environments. Our method builds on the observation that environmental changes, although dynamic, are often localized within bounded regions. To exploit this, we introduce a hierarchical decomposition of the environment and deploy distributed RL agents that adapt to changes locally. We further propose a retraining mechanism based on sub-environment success rates to determine when policy updates are necessary. Two training paradigms are explored: single-agent Q-learning and multi-agent federated Q-learning, where local Q-tables are aggregated periodically to accelerate the learning process. Unlike prior work, we evaluate our methods in more realistic settings, where multiple simultaneous obstacle changes and increasing difficulty levels are present. Results show that the federated variants consistently outperform their single-agent counterparts and closely approach the performance of A* Oracle while maintaining shorter adaptation times and robust scalability. Although initial training remains time-consuming in large environments, our decentralized framework eliminates the need for a global planner and lays the groundwork for future improvements using deep RL and flexible environment decomposition.

