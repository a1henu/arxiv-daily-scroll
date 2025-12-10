---
layout: default
title: Heuristics for Combinatorial Optimization via Value-based Reinforcement Learning: A Unified Framework and Analysis
---

# Heuristics for Combinatorial Optimization via Value-based Reinforcement Learning: A Unified Framework and Analysis
**arXiv**：[2512.08601v1](https://arxiv.org/abs/2512.08601) · [PDF](https://arxiv.org/pdf/2512.08601.pdf)  
**作者**：Orit Davidovich, Shimrit Shtern, Segev Wasserkrug, Nimrod Megiddo  

**一句话要点**：提出基于值强化学习的统一框架与分析，用于组合优化启发式学习

**关键词**：组合优化, 强化学习, 马尔可夫决策过程, 值函数学习, 最优性间隙, 理论分析

## 3 点简述
- 核心问题：组合优化启发式学习缺乏理论支撑，需统一建模与分析
- 方法要点：将组合优化问题建模为无折扣马尔可夫决策过程，提供收敛条件与最优性间隙保证
- 实验或效果：分析深度Q学习算法的成功与局限，为实际应用提供理论指导

## 摘要（原文）

> Since the 1990s, considerable empirical work has been carried out to train statistical models, such as neural networks (NNs), as learned heuristics for combinatorial optimization (CO) problems. When successful, such an approach eliminates the need for experts to design heuristics per problem type. Due to their structure, many hard CO problems are amenable to treatment through reinforcement learning (RL). Indeed, we find a wealth of literature training NNs using value-based, policy gradient, or actor-critic approaches, with promising results, both in terms of empirical optimality gaps and inference runtimes. Nevertheless, there has been a paucity of theoretical work undergirding the use of RL for CO problems. To this end, we introduce a unified framework to model CO problems through Markov decision processes (MDPs) and solve them using RL techniques. We provide easy-to-test assumptions under which CO problems can be formulated as equivalent undiscounted MDPs that provide optimal solutions to the original CO problems. Moreover, we establish conditions under which value-based RL techniques converge to approximate solutions of the CO problem with a guarantee on the associated optimality gap. Our convergence analysis provides: (1) a sufficient rate of increase in batch size and projected gradient descent steps at each RL iteration; (2) the resulting optimality gap in terms of problem parameters and targeted RL accuracy; and (3) the importance of a choice of state-space embedding. Together, our analysis illuminates the success (and limitations) of the celebrated deep Q-learning algorithm in this problem context.

