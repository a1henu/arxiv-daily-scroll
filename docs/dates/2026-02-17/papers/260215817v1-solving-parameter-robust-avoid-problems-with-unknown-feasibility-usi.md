---
layout: default
title: Solving Parameter-Robust Avoid Problems with Unknown Feasibility using Reinforcement Learning
---

# Solving Parameter-Robust Avoid Problems with Unknown Feasibility using Reinforcement Learning
**arXiv**：[2602.15817v1](https://arxiv.org/abs/2602.15817) · [PDF](https://arxiv.org/pdf/2602.15817.pdf)  
**作者**：Oswin So, Eric Yang Yu, Songyuan Zhang, Matthew Cleaveland, Mitchell Black, Chuchu Fan  

**一句话要点**：提出可行性引导探索方法，以解决参数鲁棒可达性问题中未知可行性的强化学习应用

**关键词**：强化学习, 可达性问题, 参数鲁棒性, 可行性引导探索, 安全策略学习

## 3 点简述
- 核心问题：强化学习与可达性问题存在目标不匹配，导致低概率安全状态性能差。
- 方法要点：同时识别可行初始条件子集并学习策略，解决可达性问题。
- 实验或效果：在MuJoCo和Kinetix模拟器中，覆盖范围比现有最佳方法提高50%以上。

## 摘要（原文）

> Recent advances in deep reinforcement learning (RL) have achieved strong results on high-dimensional control tasks, but applying RL to reachability problems raises a fundamental mismatch: reachability seeks to maximize the set of states from which a system remains safe indefinitely, while RL optimizes expected returns over a user-specified distribution. This mismatch can result in policies that perform poorly on low-probability states that are still within the safe set. A natural alternative is to frame the problem as a robust optimization over a set of initial conditions that specify the initial state, dynamics and safe set, but whether this problem has a solution depends on the feasibility of the specified set, which is unknown a priori. We propose Feasibility-Guided Exploration (FGE), a method that simultaneously identifies a subset of feasible initial conditions under which a safe policy exists, and learns a policy to solve the reachability problem over this set of initial conditions. Empirical results demonstrate that FGE learns policies with over 50% more coverage than the best existing method for challenging initial conditions across tasks in the MuJoCo simulator and the Kinetix simulator with pixel observations.

