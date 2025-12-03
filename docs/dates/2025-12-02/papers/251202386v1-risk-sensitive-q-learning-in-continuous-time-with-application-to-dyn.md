---
layout: default
title: Risk-Sensitive Q-Learning in Continuous Time with Application to Dynamic Portfolio Selection
---

# Risk-Sensitive Q-Learning in Continuous Time with Application to Dynamic Portfolio Selection
**arXiv**：[2512.02386v1](https://arxiv.org/abs/2512.02386) · [PDF](https://arxiv.org/pdf/2512.02386.pdf)  
**作者**：Chuhan Xie  

**一句话要点**：提出CT-RS-q算法以解决连续时间风险敏感强化学习问题，应用于动态投资组合选择。

**关键词**：风险敏感强化学习, 连续时间控制, 随机微分方程, 优化确定性等价, 动态投资组合选择, 鞅表征

## 3 点简述
- 研究连续时间风险敏感强化学习，环境由可控随机微分方程描述，目标为累积奖励的非线性泛函。
- 证明当泛函为优化确定性等价时，最优策略相对于增强环境是马尔可夫的，并基于鞅表征提出CT-RS-q算法。
- 在动态投资组合选择模拟中验证算法有效性，未知具体性能指标。

## 摘要（原文）

> This paper studies the problem of risk-sensitive reinforcement learning (RSRL) in continuous time, where the environment is characterized by a controllable stochastic differential equation (SDE) and the objective is a potentially nonlinear functional of cumulative rewards. We prove that when the functional is an optimized certainty equivalent (OCE), the optimal policy is Markovian with respect to an augmented environment. We also propose \textit{CT-RS-q}, a risk-sensitive q-learning algorithm based on a novel martingale characterization approach. Finally, we run a simulation study on a dynamic portfolio selection problem and illustrate the effectiveness of our algorithm.

