---
layout: default
title: Graphon Mean-Field Subsampling for Cooperative Heterogeneous Multi-Agent Reinforcement Learning
---

# Graphon Mean-Field Subsampling for Cooperative Heterogeneous Multi-Agent Reinforcement Learning
**arXiv**：[2602.16196v1](https://arxiv.org/abs/2602.16196) · [PDF](https://arxiv.org/pdf/2602.16196.pdf)  
**作者**：Emile Anand, Richard Hoffmann, Sarah Liaw, Adam Wierman  

**一句话要点**：提出图子均值场子采样框架以解决异构多智能体强化学习中的可扩展性问题

**关键词**：多智能体强化学习, 图子理论, 均值场方法, 异构交互, 子采样, 可扩展性

## 3 点简述
- 核心问题：大规模异构智能体交互导致计算复杂度高，现有方法难以兼顾异质性和可扩展性
- 方法要点：通过基于交互强度的子采样近似图子加权均值场，降低样本复杂度至多项式级别
- 实验或效果：在机器人协调仿真中验证了框架能实现接近最优的性能，理论分析显示最优性差距为O(1/√κ)

## 摘要（原文）

> Coordinating large populations of interacting agents is a central challenge in multi-agent reinforcement learning (MARL), where the size of the joint state-action space scales exponentially with the number of agents. Mean-field methods alleviate this burden by aggregating agent interactions, but these approaches assume homogeneous interactions. Recent graphon-based frameworks capture heterogeneity, but are computationally expensive as the number of agents grows. Therefore, we introduce $\texttt{GMFS}$, a $\textbf{G}$raphon $\textbf{M}$ean-$\textbf{F}$ield $\textbf{S}$ubsampling framework for scalable cooperative MARL with heterogeneous agent interactions. By subsampling $κ$ agents according to interaction strength, we approximate the graphon-weighted mean-field and learn a policy with sample complexity $\mathrm{poly}(κ)$ and optimality gap $O(1/\sqrtκ)$. We verify our theory with numerical simulations in robotic coordination, showing that $\texttt{GMFS}$ achieves near-optimal performance.

