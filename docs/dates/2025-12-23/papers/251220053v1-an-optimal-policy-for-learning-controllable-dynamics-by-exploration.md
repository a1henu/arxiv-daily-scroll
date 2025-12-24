---
layout: default
title: An Optimal Policy for Learning Controllable Dynamics by Exploration
---

# An Optimal Policy for Learning Controllable Dynamics by Exploration
**arXiv**：[2512.20053v1](https://arxiv.org/abs/2512.20053) · [PDF](https://arxiv.org/pdf/2512.20053.pdf)  
**作者**：Peter N. Loxley  

**一句话要点**：提出一种最优策略，用于在未知环境中通过有限时间探索学习可控马尔可夫链动态。

**关键词**：可控马尔可夫链, 最优探索策略, 动态规划, 信息增益, 非平稳策略

## 3 点简述
- 核心问题：在未知环境中，如何通过探索学习可控马尔可夫链动态，以最大化信息增益。
- 方法要点：给出最优策略的一般形式，基于贪婪选择控制，处理瞬态、吸收态等限制状态。
- 实验或效果：通过六个示例详细分析，使用计数论证和动态规划验证策略最优性。

## 摘要（原文）

> Controllable Markov chains describe the dynamics of sequential decision making tasks and are the central component in optimal control and reinforcement learning. In this work, we give the general form of an optimal policy for learning controllable dynamics in an unknown environment by exploring over a limited time horizon. This policy is simple to implement and efficient to compute, and allows an agent to ``learn by exploring" as it maximizes its information gain in a greedy fashion by selecting controls from a constraint set that changes over time during exploration. We give a simple parameterization for the set of controls, and present an algorithm for finding an optimal policy. The reason for this policy is due to the existence of certain types of states that restrict control of the dynamics; such as transient states, absorbing states, and non-backtracking states. We show why the occurrence of these states makes a non-stationary policy essential for achieving optimal exploration. Six interesting examples of controllable dynamics are treated in detail. Policy optimality is demonstrated using counting arguments, comparing with suboptimal policies, and by making use of a sequential improvement property from dynamic programming.

