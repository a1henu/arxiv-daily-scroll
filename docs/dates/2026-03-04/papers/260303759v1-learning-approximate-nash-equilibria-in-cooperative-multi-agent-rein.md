---
layout: default
title: Learning Approximate Nash Equilibria in Cooperative Multi-Agent Reinforcement Learning via Mean-Field Subsampling
---

# Learning Approximate Nash Equilibria in Cooperative Multi-Agent Reinforcement Learning via Mean-Field Subsampling
**arXiv**：[2603.03759v1](https://arxiv.org/abs/2603.03759) · [PDF](https://arxiv.org/pdf/2603.03759.pdf)  
**作者**：Emile Anand, Ishani Karmarkar  

**一句话要点**：提出交替学习框架以解决通信受限多智能体强化学习中的近似纳什均衡问题

**关键词**：多智能体强化学习, 平均场方法, 通信受限, 近似纳什均衡, 子采样学习, 合作博弈

## 3 点简述
- 研究通信受限下全局智能体与大量同质本地智能体的合作马尔可夫博弈
- 提出交替学习框架，结合子采样平均场Q学习和诱导MDP优化
- 理论证明收敛至近似纳什均衡，并在多机器人控制和联邦优化中验证

## 摘要（原文）

> Many large-scale platforms and networked control systems have a centralized decision maker interacting with a massive population of agents under strict observability constraints. Motivated by such applications, we study a cooperative Markov game with a global agent and $n$ homogeneous local agents in a communication-constrained regime, where the global agent only observes a subset of $k$ local agent states per time step. We propose an alternating learning framework $(\texttt{ALTERNATING-MARL})$, where the global agent performs subsampled mean-field $Q$-learning against a fixed local policy, and local agents update by optimizing in an induced MDP. We prove that these approximate best-response dynamics converge to an $\widetilde{O}(1/\sqrt{k})$-approximate Nash Equilibrium, while yielding a separation in the sample complexities between the joint state space and action space. Finally, we validate our results in numerical simulations for multi-robot control and federated optimization.

