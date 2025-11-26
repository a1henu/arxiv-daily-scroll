---
layout: default
title: Reinforcement Learning with $ω$-Regular Objectives and Constraints
---

# Reinforcement Learning with $ω$-Regular Objectives and Constraints
**arXiv**：[2511.19849v1](https://arxiv.org/abs/2511.19849) · [PDF](https://arxiv.org/pdf/2511.19849.pdf)  
**作者**：Dominik Wagner, Leon Witzman, Luke Ong  

**一句话要点**：提出基于线性规划的强化学习算法，以在满足ω-正则约束下最大化目标概率。

**关键词**：强化学习, ω-正则目标, 约束优化, 线性规划, 模型强化学习

## 3 点简述
- 强化学习标量奖励难以表达复杂行为目标，易导致奖励黑客问题。
- 结合ω-正则目标与约束，开发模型强化学习算法，确保安全与优化分离。
- 算法在极限下保证策略满足约束阈值，并转化为约束平均问题。

## 摘要（原文）

> Reinforcement learning (RL) commonly relies on scalar rewards with limited ability to express temporal, conditional, or safety-critical goals, and can lead to reward hacking. Temporal logic expressible via the more general class of $ω$-regular objectives addresses this by precisely specifying rich behavioural properties. Even still, measuring performance by a single scalar (be it reward or satisfaction probability) masks safety-performance trade-offs that arise in settings with a tolerable level of risk.
>   We address both limitations simultaneously by combining $ω$-regular objectives with explicit constraints, allowing safety requirements and optimisation targets to be treated separately. We develop a model-based RL algorithm based on linear programming, which in the limit produces a policy maximising the probability of satisfying an $ω$-regular objective while also adhering to $ω$-regular constraints within specified thresholds. Furthermore, we establish a translation to constrained limit-average problems with optimality-preserving guarantees.

