---
layout: default
title: Information-directed sampling for bandits: a primer
---

# Information-directed sampling for bandits: a primer
**arXiv**：[2512.20096v1](https://arxiv.org/abs/2512.20096) · [PDF](https://arxiv.org/pdf/2512.20096.pdf)  
**作者**：Annika Hirling, Giorgio Nicoletti, Antonio Celani  

**一句话要点**：提出改进信息导向采样策略，用于两状态伯努利多臂老虎机，平衡探索与利用。

**关键词**：多臂老虎机, 信息导向采样, 探索与利用, 遗憾分析, 统计物理, 强化学习

## 3 点简述
- 核心问题：多臂老虎机中探索与利用的权衡，聚焦两状态伯努利模型。
- 方法要点：扩展信息导向采样至折扣无限时域，引入修正信息度量和调参。
- 实验或效果：对称老虎机中实现有界累积遗憾，单公平硬币场景遗憾对数增长。

## 摘要（原文）

> The Multi-Armed Bandit problem provides a fundamental framework for analyzing the tension between exploration and exploitation in sequential learning. This paper explores Information Directed Sampling (IDS) policies, a class of heuristics that balance immediate regret against information gain. We focus on the tractable environment of two-state Bernoulli bandits as a minimal model to rigorously compare heuristic strategies against the optimal policy. We extend the IDS framework to the discounted infinite-horizon setting by introducing a modified information measure and a tuning parameter to modulate the decision-making behavior. We examine two specific problem classes: symmetric bandits and the scenario involving one fair coin. In the symmetric case we show that IDS achieves bounded cumulative regret, whereas in the one-fair-coin scenario the IDS policy yields a regret that scales logarithmically with the horizon, in agreement with classical asymptotic lower bounds. This work serves as a pedagogical synthesis, aiming to bridge concepts from reinforcement learning and information theory for an audience of statistical physicists.

