---
layout: default
title: Factored Value Functions for Graph-Based Multi-Agent Reinforcement Learning
---

# Factored Value Functions for Graph-Based Multi-Agent Reinforcement Learning
**arXiv**：[2601.11401v1](https://arxiv.org/abs/2601.11401) · [PDF](https://arxiv.org/pdf/2601.11401.pdf)  
**作者**：Ahmed Rashwan, Keith Briggs, Chris Budd, Lisa Kreusser  

**一句话要点**：提出扩散价值函数以解决图多智能体强化学习中的信用分配问题

**关键词**：多智能体强化学习, 图马尔可夫决策过程, 信用分配, 扩散价值函数, 图神经网络, 分布式优化

## 3 点简述
- 核心问题：大规模图多智能体系统中信用分配困难，全局与局部价值函数各有缺陷
- 方法要点：基于影响图扩散奖励，定义扩散价值函数，支持贝尔曼固定点和可扩展估计
- 实验或效果：在消防基准和分布式计算任务中，DA2C方法平均奖励提升达11%

## 摘要（原文）

> Credit assignment is a core challenge in multi-agent reinforcement learning (MARL), especially in large-scale systems with structured, local interactions. Graph-based Markov decision processes (GMDPs) capture such settings via an influence graph, but standard critics are poorly aligned with this structure: global value functions provide weak per-agent learning signals, while existing local constructions can be difficult to estimate and ill-behaved in infinite-horizon settings. We introduce the Diffusion Value Function (DVF), a factored value function for GMDPs that assigns to each agent a value component by diffusing rewards over the influence graph with temporal discounting and spatial attenuation. We show that DVF is well-defined, admits a Bellman fixed point, and decomposes the global discounted value via an averaging property. DVF can be used as a drop-in critic in standard RL algorithms and estimated scalably with graph neural networks. Building on DVF, we propose Diffusion A2C (DA2C) and a sparse message-passing actor, Learned DropEdge GNN (LD-GNN), for learning decentralised algorithms under communication costs. Across the firefighting benchmark and three distributed computation tasks (vector graph colouring and two transmit power optimisation problems), DA2C consistently outperforms local and global critic baselines, improving average reward by up to 11%.

