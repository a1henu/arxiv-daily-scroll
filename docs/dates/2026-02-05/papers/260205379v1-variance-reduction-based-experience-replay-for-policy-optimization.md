---
layout: default
title: Variance Reduction Based Experience Replay for Policy Optimization
---

# Variance Reduction Based Experience Replay for Policy Optimization
**arXiv**：[2602.05379v1](https://arxiv.org/abs/2602.05379) · [PDF](https://arxiv.org/pdf/2602.05379.pdf)  
**作者**：Hua Zheng, Wei Xie, M. Ben Feng, Keilung Choy  

**一句话要点**：提出方差缩减经验回放以加速策略优化，通过选择性重用样本降低梯度方差。

**关键词**：强化学习, 经验回放, 策略优化, 方差缩减, 样本效率, 偏差-方差权衡

## 3 点简述
- 核心问题：传统经验回放均匀处理历史数据，未考虑样本对学习的贡献差异。
- 方法要点：VRER框架选择性重用信息性样本，减少策略梯度估计方差，算法无关。
- 实验或效果：PG-VRER在实验中加速策略学习，性能优于先进算法，理论分析揭示偏差-方差权衡。

## 摘要（原文）

> Effective reinforcement learning (RL) for complex stochastic systems requires leveraging historical data collected in previous iterations to accelerate policy optimization. Classical experience replay treats all past observations uniformly and fails to account for their varying contributions to learning. To overcome this limitation, we propose Variance Reduction Experience Replay (VRER), a principled framework that selectively reuses informative samples to reduce variance in policy gradient estimation. VRER is algorithm-agnostic and integrates seamlessly with existing policy optimization methods, forming the basis of our sample-efficient off-policy algorithm, Policy Gradient with VRER (PG-VRER). Motivated by the lack of rigorous theoretical analysis of experience replay, we develop a novel framework that explicitly captures dependencies introduced by Markovian dynamics and behavior-policy interactions. Using this framework, we establish finite-time convergence guarantees for PG-VRER and reveal a fundamental bias-variance trade-off: reusing older experience increases bias but simultaneously reduces gradient variance. Extensive empirical experiments demonstrate that VRER consistently accelerates policy learning and improves performance over state-of-the-art policy optimization algorithms.

