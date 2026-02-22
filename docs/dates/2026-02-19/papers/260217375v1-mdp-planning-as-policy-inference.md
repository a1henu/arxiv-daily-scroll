---
layout: default
title: MDP Planning as Policy Inference
---

# MDP Planning as Policy Inference
**arXiv**：[2602.17375v1](https://arxiv.org/abs/2602.17375) · [PDF](https://arxiv.org/pdf/2602.17375.pdf)  
**作者**：David Tolpin  

**一句话要点**：将MDP规划建模为策略贝叶斯推断，通过变分序列蒙特卡洛近似后验分布

**关键词**：马尔可夫决策过程, 贝叶斯推断, 变分序列蒙特卡洛, 策略优化, 离散域规划, 不确定性建模

## 3 点简述
- 核心问题：将马尔可夫决策过程规划视为策略的贝叶斯推断，以处理最优行为的不确定性
- 方法要点：使用变分序列蒙特卡洛近似策略后验分布，引入一致性扫描和耦合转移随机性
- 实验或效果：在网格世界、Blackjack等离散域中分析策略分布结构，与Soft Actor-Critic比较行为差异

## 摘要（原文）

> We cast episodic Markov decision process (MDP) planning as Bayesian inference over _policies_. A policy is treated as the latent variable and is assigned an unnormalized probability of optimality that is monotone in its expected return, yielding a posterior distribution whose modes coincide with return-maximizing solutions while posterior dispersion represents uncertainty over optimal behavior. To approximate this posterior in discrete domains, we adapt variational sequential Monte Carlo (VSMC) to inference over deterministic policies under stochastic dynamics, introducing a sweep that enforces policy consistency across revisited states and couples transition randomness across particles to avoid confounding from simulator noise. Acting is performed by posterior predictive sampling, which induces a stochastic control policy through a Thompson-sampling interpretation rather than entropy regularization. Across grid worlds, Blackjack, Triangle Tireworld, and Academic Advising, we analyze the structure of inferred policy distributions and compare the resulting behavior to discrete Soft Actor-Critic, highlighting qualitative and statistical differences that arise from policy-level uncertainty.

