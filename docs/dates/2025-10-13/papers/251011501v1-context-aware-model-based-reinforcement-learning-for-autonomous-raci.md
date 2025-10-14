---
layout: default
title: Context-Aware Model-Based Reinforcement Learning for Autonomous Racing
---

# Context-Aware Model-Based Reinforcement Learning for Autonomous Racing
**arXiv**：[2510.11501v1](https://arxiv.org/abs/2510.11501) · [PDF](https://arxiv.org/pdf/2510.11501.pdf)  
**作者**：Emran Yasser Moustafa, Ivana Dusparic  

**一句话要点**：提出上下文感知模型强化学习cMask，提升自动驾驶赛车在未知对手行为下的泛化能力。

**关键词**：模型强化学习, 自动驾驶赛车, 上下文感知, 泛化能力, 马尔可夫决策过程

## 3 点简述
- 核心问题：模型强化学习在环境动态变化时泛化能力不足，影响自动驾驶赛车安全。
- 方法要点：使用上下文马尔可夫决策过程参数化对手行为，扩展为上下文感知MBRL算法。
- 实验或效果：cMask在分布内外对手行为下均优于上下文无关及其他上下文感知方法。

## 摘要（原文）

> Autonomous vehicles have shown promising potential to be a groundbreaking
> technology for improving the safety of road users. For these vehicles, as well
> as many other safety-critical robotic technologies, to be deployed in
> real-world applications, we require algorithms that can generalize well to
> unseen scenarios and data. Model-based reinforcement learning algorithms (MBRL)
> have demonstrated state-of-the-art performance and data efficiency across a
> diverse set of domains. However, these algorithms have also shown
> susceptibility to changes in the environment and its transition dynamics.
>   In this work, we explore the performance and generalization capabilities of
> MBRL algorithms for autonomous driving, specifically in the simulated
> autonomous racing environment, Roboracer (formerly F1Tenth). We frame the
> head-to-head racing task as a learning problem using contextual Markov decision
> processes and parameterize the driving behavior of the adversaries using the
> context of the episode, thereby also parameterizing the transition and reward
> dynamics. We benchmark the behavior of MBRL algorithms in this environment and
> propose a novel context-aware extension of the existing literature, cMask. We
> demonstrate that context-aware MBRL algorithms generalize better to
> out-of-distribution adversary behaviors relative to context-free approaches. We
> also demonstrate that cMask displays strong generalization capabilities, as
> well as further performance improvement relative to other context-aware MBRL
> approaches when racing against adversaries with in-distribution behaviors.

