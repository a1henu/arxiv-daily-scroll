---
layout: default
title: Reward Learning through Ranking Mean Squared Error
---

# Reward Learning through Ranking Mean Squared Error
**arXiv**：[2601.09236v1](https://arxiv.org/abs/2601.09236) · [PDF](https://arxiv.org/pdf/2601.09236.pdf)  
**作者**：Chaitanya Kharyal, Calarina Muslimani, Matthew E. Taylor  

**一句话要点**：提出基于排序均方误差的奖励学习方法R4，用于从人类评分中学习强化学习奖励函数。

**关键词**：奖励学习, 强化学习, 人类反馈, 排序均方误差, 机器人控制

## 3 点简述
- 核心问题：强化学习中奖励设计困难，需从人类反馈学习奖励函数。
- 方法要点：使用排序均方误差损失，将评分作为序数目标，通过可微分排序优化。
- 实验或效果：在机器人运动基准测试中，R4匹配或优于现有方法，反馈需求更少。

## 摘要（原文）

> Reward design remains a significant bottleneck in applying reinforcement learning (RL) to real-world problems. A popular alternative is reward learning, where reward functions are inferred from human feedback rather than manually specified. Recent work has proposed learning reward functions from human feedback in the form of ratings, rather than traditional binary preferences, enabling richer and potentially less cognitively demanding supervision. Building on this paradigm, we introduce a new rating-based RL method, Ranked Return Regression for RL (R4). At its core, R4 employs a novel ranking mean squared error (rMSE) loss, which treats teacher-provided ratings as ordinal targets. Our approach learns from a dataset of trajectory-rating pairs, where each trajectory is labeled with a discrete rating (e.g., "bad," "neutral," "good"). At each training step, we sample a set of trajectories, predict their returns, and rank them using a differentiable sorting operator (soft ranks). We then optimize a mean squared error loss between the resulting soft ranks and the teacher's ratings. Unlike prior rating-based approaches, R4 offers formal guarantees: its solution set is provably minimal and complete under mild assumptions. Empirically, using simulated human feedback, we demonstrate that R4 consistently matches or outperforms existing rating and preference-based RL methods on robotic locomotion benchmarks from OpenAI Gym and the DeepMind Control Suite, while requiring significantly less feedback.

