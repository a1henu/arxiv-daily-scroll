---
layout: default
title: Continuous-time reinforcement learning for optimal switching over multiple regimes
---

# Continuous-time reinforcement learning for optimal switching over multiple regimes
**arXiv**：[2512.04697v1](https://arxiv.org/abs/2512.04697) · [PDF](https://arxiv.org/pdf/2512.04697.pdf)  
**作者**：Yijie Huang, Mengge Li, Xiang Yu, Zhou Zhou  

**一句话要点**：提出连续时间强化学习算法，解决多制度最优切换问题

**关键词**：连续时间强化学习, 最优切换, 熵正则化, HJB方程, 策略迭代, 神经网络算法

## 3 点简述
- 研究多制度最优切换的连续时间强化学习问题
- 基于熵正则化建立HJB方程并分析策略迭代收敛性
- 设计强化学习算法并用神经网络数值验证有效性

## 摘要（原文）

> This paper studies the continuous-time reinforcement learning (RL) for optimal switching problems across multiple regimes. We consider a type of exploratory formulation under entropy regularization where the agent randomizes both the timing of switches and the selection of regimes through the generator matrix of an associated continuous-time finite-state Markov chain. We establish the well-posedness of the associated system of Hamilton-Jacobi-Bellman (HJB) equations and provide a characterization of the optimal policy. The policy improvement and the convergence of the policy iterations are rigorously established by analyzing the system of equations. We also show the convergence of the value function in the exploratory formulation towards the value function in the classical formulation as the temperature parameter vanishes. Finally, a reinforcement learning algorithm is devised and implemented by invoking the policy evaluation based on the martingale characterization. Our numerical examples with the aid of neural networks illustrate the effectiveness of the proposed RL algorithm.

