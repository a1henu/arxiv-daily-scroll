---
layout: default
title: Selecting Offline Reinforcement Learning Algorithms for Stochastic Network Control
---

# Selecting Offline Reinforcement Learning Algorithms for Stochastic Network Control
**arXiv**：[2603.03932v1](https://arxiv.org/abs/2603.03932) · [PDF](https://arxiv.org/pdf/2603.03932.pdf)  
**作者**：Nicolas Helson, Pegah Alizadeh, Anastasios Giovanidis  

**一句话要点**：评估离线强化学习算法在随机网络控制中的性能，为AI驱动网络提供选择指南

**关键词**：离线强化学习, 随机网络控制, 无线网络, 算法评估, AI驱动网络

## 3 点简述
- 核心问题：离线强化学习在无线网络随机动态下的行为理解不足，如衰落和噪声影响
- 方法要点：比较基于贝尔曼、序列和混合的离线RL方法，使用开放随机电信环境进行实验
- 实验或效果：保守Q学习在随机性下表现更稳健，序列方法在数据充足时可能更优

## 摘要（原文）

> Offline Reinforcement Learning (RL) is a promising approach for next-generation wireless networks, where online exploration is unsafe and large amounts of operational data can be reused across the model lifecycle. However, the behavior of offline RL algorithms under genuinely stochastic dynamics -- inherent to wireless systems due to fading, noise, and traffic mobility -- remains insufficiently understood. We address this gap by evaluating Bellman-based (Conservative Q-Learning), sequence-based (Decision Transformers), and hybrid (Critic-Guided Decision Transformers) offline RL methods in an open-access stochastic telecom environment (mobile-env). Our results show that Conservative Q-Learning consistently produces more robust policies across different sources of stochasticity, making it a reliable default choice in lifecycle-driven AI management frameworks. Sequence-based methods remain competitive and can outperform Bellman-based approaches when sufficient high-return trajectories are available. These findings provide practical guidance for offline RL algorithm selection in AI-driven network control pipelines, such as O-RAN and future 6G functions, where robustness and data availability are key operational constraints.

