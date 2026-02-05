---
layout: default
title: Beyond Rewards in Reinforcement Learning for Cyber Defence
---

# Beyond Rewards in Reinforcement Learning for Cyber Defence
**arXiv**：[2602.04809v1](https://arxiv.org/abs/2602.04809) · [PDF](https://arxiv.org/pdf/2602.04809.pdf)  
**作者**：Elizabeth Bates, Chris Hicks, Vasilios Mavroudis  

**一句话要点**：评估稀疏奖励在强化学习网络防御中的优势，提出更可靠低风险的策略

**关键词**：强化学习, 网络防御, 奖励函数, 策略评估, 稀疏奖励, 风险控制

## 3 点简述
- 核心问题：密集奖励函数可能导致网络防御强化学习代理偏向次优高风险策略
- 方法要点：通过稀疏与密集奖励函数对比，结合多种网络环境和算法评估策略行为
- 实验或效果：稀疏奖励在目标对齐且频繁可遇时，能提升训练可靠性并降低策略风险

## 摘要（原文）

> Recent years have seen an explosion of interest in autonomous cyber defence agents trained to defend computer networks using deep reinforcement learning. These agents are typically trained in cyber gym environments using dense, highly engineered reward functions which combine many penalties and incentives for a range of (un)desirable states and costly actions. Dense rewards help alleviate the challenge of exploring complex environments but risk biasing agents towards suboptimal and potentially riskier solutions, a critical issue in complex cyber environments. We thoroughly evaluate the impact of reward function structure on learning and policy behavioural characteristics using a variety of sparse and dense reward functions, two well-established cyber gyms, a range of network sizes, and both policy gradient and value-based RL algorithms. Our evaluation is enabled by a novel ground truth evaluation approach which allows directly comparing between different reward functions, illuminating the nuanced inter-relationships between rewards, action space and the risks of suboptimal policies in cyber environments. Our results show that sparse rewards, provided they are goal aligned and can be encountered frequently, uniquely offer both enhanced training reliability and more effective cyber defence agents with lower-risk policies. Surprisingly, sparse rewards can also yield policies that are better aligned with cyber defender goals and make sparing use of costly defensive actions without explicit reward-based numerical penalties.

