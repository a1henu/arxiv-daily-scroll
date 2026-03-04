---
layout: default
title: Learning in Markov Decision Processes with Exogenous Dynamics
---

# Learning in Markov Decision Processes with Exogenous Dynamics
**arXiv**：[2603.02862v1](https://arxiv.org/abs/2603.02862) · [PDF](https://arxiv.org/pdf/2603.02862.pdf)  
**作者**：Davide Maran, Davide Salaorni, Marcello Restelli  

**一句话要点**：提出利用外生动态结构改进强化学习，在马尔可夫决策过程中提升样本效率。

**关键词**：强化学习, 马尔可夫决策过程, 外生动态, 样本效率, 遗憾界, 结构利用

## 3 点简述
- 研究具有外生状态组件的MDPs，其转移独立于智能体动作。
- 利用结构改进学习保证，遗憾界仅依赖外生状态空间大小。
- 实验验证在经典和真实环境中的样本效率显著优于标准方法。

## 摘要（原文）

> Reinforcement learning algorithms are typically designed for generic Markov Decision Processes (MDPs), where any state-action pair can lead to an arbitrary transition distribution. In many practical systems, however, only a subset of the state variables is directly influenced by the agent's actions, while the remaining components evolve according to exogenous dynamics and account for most of the stochasticity. In this work, we study a structured class of MDPs characterized by exogenous state components whose transitions are independent of the agent's actions. We show that exploiting this structure yields significantly improved learning guarantees, with only the size of the exogenous state space appearing in the leading terms of the regret bounds. We further establish a matching lower bound, showing that this dependence is information-theoretically optimal. Finally, we empirically validate our approach across classical toy settings and real-world-inspired environments, demonstrating substantial gains in sample efficiency compared to standard reinforcement learning methods.

