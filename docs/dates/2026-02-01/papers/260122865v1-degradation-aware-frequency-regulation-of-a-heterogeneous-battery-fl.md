---
layout: default
title: Degradation-Aware Frequency Regulation of a Heterogeneous Battery Fleet via Reinforcement Learning
---

# Degradation-Aware Frequency Regulation of a Heterogeneous Battery Fleet via Reinforcement Learning
**arXiv**：[2601.22865v1](https://arxiv.org/abs/2601.22865) · [PDF](https://arxiv.org/pdf/2601.22865.pdf)  
**作者**：Tanay Raghunandan Srinivasa, Vivek Deulkar, Jia Bhargava, Mohammad Hajiesmaili, Prashant Shenoy  

**一句话要点**：提出基于强化学习的异构电池组频率调节方法，以最小化循环退化

**关键词**：电池储能系统, 频率调节, 强化学习, 循环退化, 异构电池组, 马尔可夫决策过程

## 3 点简述
- 研究异构电池组实时调度问题，在满足约束下跟踪随机平衡信号，同时最小化长期循环退化。
- 将问题建模为带约束动作空间的马尔可夫决策过程，设计密集代理奖励以对齐长期循环深度减少。
- 使用极端学习机结合线性时序差分学习进行函数逼近，在模拟和真实信号上验证了循环深度和退化指标的降低。

## 摘要（原文）

> Battery energy storage systems are increasingly deployed as fast-responding resources for grid balancing services such as frequency regulation and for mitigating renewable generation uncertainty. However, repeated charging and discharging induces cycling degradation and reduces battery lifetime. This paper studies the real-time scheduling of a heterogeneous battery fleet that collectively tracks a stochastic balancing signal subject to per-battery ramp-rate and capacity constraints, while minimizing long-term cycling degradation.
>   Cycling degradation is fundamentally path-dependent: it is determined by charge-discharge cycles formed by the state-of-charge (SoC) trajectory and is commonly quantified via rainflow cycle counting. This non-Markovian structure makes it difficult to express degradation as an additive per-time-step cost, complicating classical dynamic programming approaches. We address this challenge by formulating the fleet scheduling problem as a Markov decision process (MDP) with constrained action space and designing a dense proxy reward that provides informative feedback at each time step while remaining aligned with long-term cycle-depth reduction.
>   To scale learning to large state-action spaces induced by fine-grained SoC discretization and asymmetric per-battery constraints, we develop a function-approximation reinforcement learning method using an Extreme Learning Machine (ELM) as a random nonlinear feature map combined with linear temporal-difference learning. We evaluate the proposed approach on a toy Markovian signal model and on a Markovian model trained from real-world regulation signal traces obtained from the University of Delaware, and demonstrate consistent reductions in cycle-depth occurrence and degradation metrics compared to baseline scheduling policies.

