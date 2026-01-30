---
layout: default
title: Expected Return Causes Outcome-Level Mode Collapse in Reinforcement Learning and How to Fix It with Inverse Probability Scaling
---

# Expected Return Causes Outcome-Level Mode Collapse in Reinforcement Learning and How to Fix It with Inverse Probability Scaling
**arXiv**：[2601.21669v1](https://arxiv.org/abs/2601.21669) · [PDF](https://arxiv.org/pdf/2601.21669.pdf)  
**作者**：Abhijeet Sinha, Sundari Elango, Dianbo Liu  

**一句话要点**：提出逆概率缩放以解决强化学习中期望回报导致的结果级模式崩溃问题

**关键词**：强化学习, 模式崩溃, 期望回报, 逆概率缩放, 多模态优化, 策略优化

## 3 点简述
- 核心问题：期望回报最大化目标在理论上导致结果级模式崩溃，与探索策略无关
- 方法要点：通过逆概率缩放修正学习信号，消除结果频率放大，实现奖励比例分布
- 实验或效果：在推理和分子生成任务中，IPS-GRPO减少模式崩溃并匹配或超越基线性能

## 摘要（原文）

> Many reinforcement learning (RL) problems admit multiple terminal solutions of comparable quality, where the goal is not to identify a single optimum but to represent a diverse set of high-quality outcomes. Nevertheless, policies trained by standard expected return maximization routinely collapse onto a small subset of outcomes, a phenomenon commonly attributed to insufficient exploration or weak regularization. We show that this explanation is incomplete: outcome level mode collapse is a structural consequence of the expected-return objective itself. Under idealized learning dynamics, the log-probability ratio between any two outcomes evolves linearly in their reward difference, implying exponential ratio divergence and inevitable collapse independent of the exploration strategy, entropy regularization, or optimization algorithm. We identify the source of this pathology as the probability multiplier inside the expectation and propose a minimal correction: inverse probability scaling, which removes outcome-frequency amplification from the learning signal, fundamentally changes the learning dynamics, and provably yields reward-proportional terminal distributions, preventing collapse in multimodal settings. We instantiate this principle in Group Relative Policy Optimization (GRPO) as a drop-in modification, IPS-GRPO, requiring no auxiliary models or architectural changes. Across different reasoning and molecular generation tasks, IPS-GRPO consistently reduces outcome-level mode collapse while matching or exceeding baseline performance, suggesting that correcting the objective rather than adding exploration heuristics is key to reliable multimodal policy optimization.

