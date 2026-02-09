---
layout: default
title: Soft Forward-Backward Representations for Zero-shot Reinforcement Learning with General Utilities
---

# Soft Forward-Backward Representations for Zero-shot Reinforcement Learning with General Utilities
**arXiv**：[2602.06769v1](https://arxiv.org/abs/2602.06769) · [PDF](https://arxiv.org/pdf/2602.06769.pdf)  
**作者**：Marco Bagatella, Thomas Rupf, Georg Martius, Andreas Krause  

**一句话要点**：提出软前向-后向表示方法，以零样本方式解决具有一般效用的强化学习问题。

**关键词**：零样本强化学习, 一般效用优化, 离线数据学习, 最大熵策略, 前向-后向算法, 随机策略族

## 3 点简述
- 核心问题：零样本强化学习扩展到一般效用目标，如分布匹配或纯探索，超越传统加性奖励。
- 方法要点：引入最大熵软前向-后向算法，从离线数据中恢复随机策略族，结合零阶搜索直接优化一般效用。
- 实验或效果：在理论和实验中验证方法保留前向-后向算法优势，并扩展至更广泛的强化学习任务。

## 摘要（原文）

> Recent advancements in zero-shot reinforcement learning (RL) have facilitated the extraction of diverse behaviors from unlabeled, offline data sources. In particular, forward-backward algorithms (FB) can retrieve a family of policies that can approximately solve any standard RL problem (with additive rewards, linear in the occupancy measure), given sufficient capacity. While retaining zero-shot properties, we tackle the greater problem class of RL with general utilities, in which the objective is an arbitrary differentiable function of the occupancy measure. This setting is strictly more expressive, capturing tasks such as distribution matching or pure exploration, which may not be reduced to additive rewards. We show that this additional complexity can be captured by a novel, maximum entropy (soft) variant of the forward-backward algorithm, which recovers a family of stochastic policies from offline data. When coupled with zero-order search over compact policy embeddings, this algorithm can sidestep iterative optimization schemes, and optimizes general utilities directly at test-time. Across both didactic and high-dimensional experiments, we demonstrate that our method retains favorable properties of FB algorithms, while also extending their range to more general RL problems.

