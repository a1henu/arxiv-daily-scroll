---
layout: default
title: Inverse Contextual Bandits without Rewards: Learning from a Non-Stationary Learner via Suffix Imitation
---

# Inverse Contextual Bandits without Rewards: Learning from a Non-Stationary Learner via Suffix Imitation
**arXiv**：[2603.03778v1](https://arxiv.org/abs/2603.03778) · [PDF](https://arxiv.org/pdf/2603.03778.pdf)  
**作者**：Yuqi Kong, Xiao Zhang, Weiran Shen  

**一句话要点**：提出两阶段后缀模仿框架以解决无奖励逆上下文赌博机中的非平稳数据挑战

**关键词**：逆上下文赌博机, 非平稳学习, 后缀模仿, 无奖励学习, 经验风险最小化, 收敛率分析

## 3 点简述
- 研究逆上下文赌博机问题，观察者无奖励访问，仅从动作数据恢复参数
- 提出两阶段后缀模仿框架，丢弃初始阶段数据，仅用后续模仿阶段进行经验风险最小化
- 理论证明无奖励观察者能达到收敛率O~(1/√N)，匹配有奖励学习者的渐近效率

## 摘要（原文）

> We study the Inverse Contextual Bandit (ICB) problem, in which a learner seeks to optimize a policy while an observer, who cannot access the learner's rewards and only observes actions, aims to recover the underlying problem parameters. During the learning process, the learner's behavior naturally transitions from exploration to exploitation, resulting in non-stationary action data that poses significant challenges for the observer. To address this issue, we propose a simple and effective framework called Two-Phase Suffix Imitation. The framework discards data from an initial burn-in phase and performs empirical risk minimization using only data from a subsequent imitation phase. We derive a predictive decision loss bound that explicitly characterizes the bias-variance trade-off induced by the choice of burn-in length. Despite the severe information deficit, we show that a reward-free observer can achieve a convergence rate of $\tilde O(1/\sqrt{N})$, matching the asymptotic efficiency of a fully reward-aware learner. This result demonstrates that a passive observer can effectively uncover the optimal policy from actions alone, attaining performance comparable to that of the learner itself.

