---
layout: default
title: Beyond State-Wise Mirror Descent: Offline Policy Optimization with Parameteric Policies
---

# Beyond State-Wise Mirror Descent: Offline Policy Optimization with Parameteric Policies
**arXiv**：[2602.23811v1](https://arxiv.org/abs/2602.23811) · [PDF](https://arxiv.org/pdf/2602.23811.pdf)  
**作者**：Xiang Li, Nan Jiang, Yuheng Zhang  

**一句话要点**：提出基于自然策略梯度的离线强化学习理论框架，以解决参数化策略在大动作空间下的优化问题。

**关键词**：离线强化学习, 参数化策略, 自然策略梯度, 镜像下降, 理论分析

## 3 点简述
- 核心问题：离线强化学习中，现有算法难以处理大或连续动作空间及独立参数化策略。
- 方法要点：将镜像下降与自然策略梯度结合，分析上下文耦合，扩展理论保证至参数化策略类。
- 实验或效果：未知，但理论分析揭示了离线强化学习与模仿学习的统一性。

## 摘要（原文）

> We investigate the theoretical aspects of offline reinforcement learning (RL) under general function approximation. While prior works (e.g., Xie et al., 2021) have established the theoretical foundations of learning a good policy from offline data via pessimism, existing algorithms that are computationally tractable (often in an oracle-efficient sense), such as PSPI, only apply to finite and small action spaces. Moreover, these algorithms rely on state-wise mirror descent and require actors to be implicitly induced from the critic functions, failing to accommodate standalone policy parameterization which is ubiquitous in practice. In this work, we address these limitations and extend the theoretical guarantees to parameterized policy classes over large or continuous action spaces. When extending mirror descent to parameterized policies, we identify contextual coupling as the core difficulty, and show how connecting mirror descent to natural policy gradient leads to novel analyses, guarantees, and algorithmic insights, including a surprising unification between offline RL and imitation learning.

