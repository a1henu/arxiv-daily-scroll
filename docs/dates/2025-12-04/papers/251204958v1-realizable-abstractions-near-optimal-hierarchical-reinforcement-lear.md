---
layout: default
title: Realizable Abstractions: Near-Optimal Hierarchical Reinforcement Learning
---

# Realizable Abstractions: Near-Optimal Hierarchical Reinforcement Learning
**arXiv**：[2512.04958v1](https://arxiv.org/abs/2512.04958) · [PDF](https://arxiv.org/pdf/2512.04958.pdf)  
**作者**：Roberto Cipollone, Luca Iocchi, Matteo Leonetti  

**一句话要点**：提出可实现的抽象以解决分层强化学习中抽象表达力不足和缺乏效率保证的问题。

**关键词**：分层强化学习, 马尔可夫决策过程, 可实现的抽象, 选项组合, 近似最优策略, RARL算法

## 3 点简述
- 核心问题：现有分层强化学习中的马尔可夫决策过程抽象表达力有限或缺乏形式化效率保证。
- 方法要点：定义可实现的抽象关系，通过选项组合将抽象策略转换为近似最优的低层策略。
- 实验或效果：提出RARL算法，具有概率近似正确性、多项式样本收敛性和对抽象不精确的鲁棒性。

## 摘要（原文）

> The main focus of Hierarchical Reinforcement Learning (HRL) is studying how large Markov Decision Processes (MDPs) can be more efficiently solved when addressed in a modular way, by combining partial solutions computed for smaller subtasks. Despite their very intuitive role for learning, most notions of MDP abstractions proposed in the HRL literature have limited expressive power or do not possess formal efficiency guarantees. This work addresses these fundamental issues by defining Realizable Abstractions, a new relation between generic low-level MDPs and their associated high-level decision processes. The notion we propose avoids non-Markovianity issues and has desirable near-optimality guarantees. Indeed, we show that any abstract policy for Realizable Abstractions can be translated into near-optimal policies for the low-level MDP, through a suitable composition of options. As demonstrated in the paper, these options can be expressed as solutions of specific constrained MDPs. Based on these findings, we propose RARL, a new HRL algorithm that returns compositional and near-optimal low-level policies, taking advantage of the Realizable Abstraction given in the input. We show that RARL is Probably Approximately Correct, it converges in a polynomial number of samples, and it is robust to inaccuracies in the abstraction.

