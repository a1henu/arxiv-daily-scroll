---
layout: default
title: UPath: Universal Planner Across Topological Heterogeneity For Grid-Based Pathfinding
---

# UPath: Universal Planner Across Topological Heterogeneity For Grid-Based Pathfinding
**arXiv**：[2602.23789v1](https://arxiv.org/abs/2602.23789) · [PDF](https://arxiv.org/pdf/2602.23789.pdf)  
**作者**：Aleksandr Ananikian, Daniil Drozdov, Konstantin Yakovlev  

**一句话要点**：提出通用启发式预测器UPath，用于网格路径规划，以解决跨分布泛化问题。

**关键词**：网格路径规划, 启发式学习, 跨分布泛化, 深度学习, A*算法, 通用求解器

## 3 点简述
- 核心问题：现有学习型启发式方法在训练与测试分布不同时性能下降，限制通用求解器应用。
- 方法要点：设计通用启发式预测器，通过深度学习一次训练，能泛化到未见任务，考虑障碍物位置与形状。
- 实验或效果：在完全不同于训练的任务上，将A*计算量减半至2.2倍，平均解成本在最优解3%以内。

## 摘要（原文）

> The performance of search algorithms for grid-based pathfinding, e.g. A*, critically depends on the heuristic function that is used to focus the search. Recent studies have shown that informed heuristics that take the positions/shapes of the obstacles into account can be approximated with the deep neural networks. Unfortunately, the existing learning-based approaches mostly rely on the assumption that training and test grid maps are drawn from the same distribution (e.g., city maps, indoor maps, etc.) and perform poorly on out-of-distribution tasks. This naturally limits their application in practice when often a universal solver is needed that is capable of efficiently handling any problem instance. In this work, we close this gap by designing an universal heuristic predictor: a model trained once, but capable of generalizing across a full spectrum of unseen tasks. Our extensive empirical evaluation shows that the suggested approach halves the computational effort of A* by up to a factor of 2.2, while still providing solutions within 3% of the optimal cost on average altogether on the tasks that are completely different from the ones used for training $\unicode{x2013}$ a milestone reached for the first time by a learnable solver.

