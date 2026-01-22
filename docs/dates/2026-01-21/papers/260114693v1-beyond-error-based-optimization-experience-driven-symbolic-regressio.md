---
layout: default
title: Beyond Error-Based Optimization: Experience-Driven Symbolic Regression with Goal-Conditioned Reinforcement Learning
---

# Beyond Error-Based Optimization: Experience-Driven Symbolic Regression with Goal-Conditioned Reinforcement Learning
**arXiv**：[2601.14693v1](https://arxiv.org/abs/2601.14693) · [PDF](https://arxiv.org/pdf/2601.14693.pdf)  
**作者**：Jianwen Sun, Xinrui Li, Fuqing Li, Xiaoxuan Shen  

**一句话要点**：提出EGRL-SR框架，利用目标条件强化学习解决符号回归中误差导向搜索的模糊性问题

**关键词**：符号回归, 目标条件强化学习, 经验驱动搜索, 结构导向奖励, 探索策略, 动作价值网络

## 3 点简述
- 核心问题：传统符号回归方法依赖拟合误差，导致结构相似但误差相近的表达式搜索方向模糊，阻碍收敛到真实函数
- 方法要点：将符号回归建模为目标条件强化学习问题，结合历史轨迹优化动作价值网络，设计结构导向奖励函数和探索策略
- 实验或效果：在公开基准测试中，EGRL-SR在恢复率和鲁棒性上优于现有方法，能更高效恢复复杂表达式

## 摘要（原文）

> Symbolic Regression aims to automatically identify compact and interpretable mathematical expressions that model the functional relationship between input and output variables. Most existing search-based symbolic regression methods typically rely on the fitting error to inform the search process. However, in the vast expression space, numerous candidate expressions may exhibit similar error values while differing substantially in structure, leading to ambiguous search directions and hindering convergence to the underlying true function. To address this challenge, we propose a novel framework named EGRL-SR (Experience-driven Goal-conditioned Reinforcement Learning for Symbolic Regression). In contrast to traditional error-driven approaches, EGRL-SR introduces a new perspective: leveraging precise historical trajectories and optimizing the action-value network to proactively guide the search process, thereby achieving a more robust expression search. Specifically, we formulate symbolic regression as a goal-conditioned reinforcement learning problem and incorporate hindsight experience replay, allowing the action-value network to generalize common mapping patterns from diverse input-output pairs. Moreover, we design an all-point satisfaction binary reward function that encourages the action-value network to focus on structural patterns rather than low-error expressions, and concurrently propose a structure-guided heuristic exploration strategy to enhance search diversity and space coverage. Experiments on public benchmarks show that EGRL-SR consistently outperforms state-of-the-art methods in recovery rate and robustness, and can recover more complex expressions under the same search budget. Ablation results validate that the action-value network effectively guides the search, with both the reward function and the exploration strategy playing critical roles.

