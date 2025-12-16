---
layout: default
title: SACn: Soft Actor-Critic with n-step Returns
---

# SACn: Soft Actor-Critic with n-step Returns
**arXiv**：[2512.13165v1](https://arxiv.org/abs/2512.13165) · [PDF](https://arxiv.org/pdf/2512.13165.pdf)  
**作者**：Jakub Łyskawa, Jakub Lewandowski, Paweł Wawrzyński  

**一句话要点**：提出SACn算法，结合n步回报与稳定重要性采样，解决SAC在离策略强化学习中的偏差问题。

**关键词**：强化学习, 离策略算法, n步回报, 重要性采样, 熵估计, MuJoCo环境

## 3 点简述
- 核心问题：SAC结合n步回报时，因动作分布变化引入偏差，重要性采样可能导致数值不稳定。
- 方法要点：采用数值稳定的重要性采样，简化超参数选择，并引入τ-采样熵估计以降低方差。
- 实验或效果：在MuJoCo模拟环境中验证SACn算法，提升收敛速度与稳定性。

## 摘要（原文）

> Soft Actor-Critic (SAC) is widely used in practical applications and is now one of the most relevant off-policy online model-free reinforcement learning (RL) methods. The technique of n-step returns is known to increase the convergence speed of RL algorithms compared to their 1-step returns-based versions. However, SAC is notoriously difficult to combine with n-step returns, since their usual combination introduces bias in off-policy algorithms due to the changes in action distribution. While this problem is solved by importance sampling, a method for estimating expected values of one distribution using samples from another distribution, importance sampling may result in numerical instability. In this work, we combine SAC with n-step returns in a way that overcomes this issue. We present an approach to applying numerically stable importance sampling with simplified hyperparameter selection. Furthermore, we analyze the entropy estimation approach of Soft Actor-Critic in the context of the n-step maximum entropy framework and formulate the $τ$-sampled entropy estimation to reduce the variance of the learning target. Finally, we formulate the Soft Actor-Critic with n-step returns (SAC$n$) algorithm that we experimentally verify on MuJoCo simulated environments.

