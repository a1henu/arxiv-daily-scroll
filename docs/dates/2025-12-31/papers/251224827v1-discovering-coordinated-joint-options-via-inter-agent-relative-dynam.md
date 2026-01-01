---
layout: default
title: Discovering Coordinated Joint Options via Inter-Agent Relative Dynamics
---

# Discovering Coordinated Joint Options via Inter-Agent Relative Dynamics
**arXiv**：[2512.24827v1](https://arxiv.org/abs/2512.24827) · [PDF](https://arxiv.org/pdf/2512.24827.pdf)  
**作者**：Raul D. Steleac, Mohan Sridharan, David Abel  

**一句话要点**：提出基于智能体相对动态的联合选项发现方法，以解决多智能体协调行为设计挑战。

**关键词**：多智能体强化学习, 选项发现, 状态抽象, 协调行为, 图拉普拉斯估计

## 3 点简述
- 核心问题：多智能体环境中，状态空间指数增长导致协调行为设计困难，现有方法常牺牲协调性。
- 方法要点：通过联合状态抽象压缩状态空间，利用费马状态和扩散度度量智能体对齐，使用神经图拉普拉斯估计器发现同步模式选项。
- 实验或效果：在多个多智能体场景中评估，相比其他方法，所提选项展现出更强的下游协调能力。

## 摘要（原文）

> Temporally extended actions improve the ability to explore and plan in single-agent settings. In multi-agent settings, the exponential growth of the joint state space with the number of agents makes coordinated behaviours even more valuable. Yet, this same exponential growth renders the design of multi-agent options particularly challenging. Existing multi-agent option discovery methods often sacrifice coordination by producing loosely coupled or fully independent behaviours. Toward addressing these limitations, we describe a novel approach for multi-agent option discovery. Specifically, we propose a joint-state abstraction that compresses the state space while preserving the information necessary to discover strongly coordinated behaviours. Our approach builds on the inductive bias that synchronisation over agent states provides a natural foundation for coordination in the absence of explicit objectives. We first approximate a fictitious state of maximal alignment with the team, the \textit{Fermat} state, and use it to define a measure of \textit{spreadness}, capturing team-level misalignment on each individual state dimension. Building on this representation, we then employ a neural graph Laplacian estimator to derive options that capture state synchronisation patterns between agents. We evaluate the resulting options across multiple scenarios in two multi-agent domains, showing that they yield stronger downstream coordination capabilities compared to alternative option discovery methods.

