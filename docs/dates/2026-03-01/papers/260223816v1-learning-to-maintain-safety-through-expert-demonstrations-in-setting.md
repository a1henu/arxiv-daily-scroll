---
layout: default
title: Learning to maintain safety through expert demonstrations in settings with unknown constraints: A Q-learning perspective
---

# Learning to maintain safety through expert demonstrations in settings with unknown constraints: A Q-learning perspective
**arXiv**：[2602.23816v1](https://arxiv.org/abs/2602.23816) · [PDF](https://arxiv.org/pdf/2602.23816.pdf)  
**作者**：George Papadopoulos, George A. Vouros  

**一句话要点**：提出SafeQIL算法，在未知约束MDP中通过专家演示学习安全策略，平衡奖励与安全性。

**关键词**：安全强化学习, 逆约束学习, Q学习, 专家演示, 未知约束MDP

## 3 点简述
- 核心问题：在奖励可观测但约束未知、成本不可观测的MDP中，基于专家演示学习安全策略。
- 方法要点：通过Q值量化状态-动作对的“承诺”，结合任务奖励与安全评估，实现安全Q学习。
- 实验或效果：在基准任务上比较现有算法，展示SafeQIL在安全性和性能上的优势。

## 摘要（原文）

> Given a set of trajectories demonstrating the execution of a task safely in a constrained MDP with observable rewards but with unknown constraints and non-observable costs, we aim to find a policy that maximizes the likelihood of demonstrated trajectories trading the balance between being conservative and increasing significantly the likelihood of high-rewarding trajectories but with potentially unsafe steps. Having these objectives, we aim towards learning a policy that maximizes the probability of the most $promising$ trajectories with respect to the demonstrations. In so doing, we formulate the ``promise" of individual state-action pairs in terms of $Q$ values, which depend on task-specific rewards as well as on the assessment of states' safety, mixing expectations in terms of rewards and safety. This entails a safe Q-learning perspective of the inverse learning problem under constraints: The devised Safe $Q$ Inverse Constrained Reinforcement Learning (SafeQIL) algorithm is compared to state-of-the art inverse constraint reinforcement learning algorithms to a set of challenging benchmark tasks, showing its merits.

