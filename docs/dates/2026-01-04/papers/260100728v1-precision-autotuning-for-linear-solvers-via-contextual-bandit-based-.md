---
layout: default
title: Precision Autotuning for Linear Solvers via Contextual Bandit-Based RL
---

# Precision Autotuning for Linear Solvers via Contextual Bandit-Based RL
**arXiv**：[2601.00728v1](https://arxiv.org/abs/2601.00728) · [PDF](https://arxiv.org/pdf/2601.00728.pdf)  
**作者**：Erin Carson, Xinye Chen  

**一句话要点**：提出基于上下文多臂老虎机强化学习的自适应精度调优框架，用于线性求解器以平衡精度与计算效率。

**关键词**：自适应精度调优, 上下文多臂老虎机, 线性求解器, 强化学习, 混合精度计算, 科学计算

## 3 点简述
- 核心问题：线性求解器精度调优需权衡计算成本与准确性，传统方法缺乏动态适应性。
- 方法要点：将问题建模为上下文多臂老虎机，使用离散化状态空间和增量动作值估计，通过epsilon-greedy策略优化Q表选择精度配置。
- 实验或效果：应用于迭代精化求解线性系统，在未见数据集上验证，能降低计算成本同时保持与双精度基准相当的准确性。

## 摘要（原文）

> We propose a reinforcement learning (RL) framework for adaptive precision tuning of linear solvers, and can be extended to general algorithms. The framework is formulated as a contextual bandit problem and solved using incremental action-value estimation with a discretized state space to select optimal precision configurations for computational steps, balancing precision and computational efficiency. To verify its effectiveness, we apply the framework to iterative refinement for solving linear systems $Ax = b$. In this application, our approach dynamically chooses precisions based on calculated features from the system. In detail, a Q-table maps discretized features (e.g., approximate condition number and matrix norm)to actions (chosen precision configurations for specific steps), optimized via an epsilon-greedy strategy to maximize a multi-objective reward balancing accuracy and computational cost. Empirical results demonstrate effective precision selection, reducing computational cost while maintaining accuracy comparable to double-precision baselines. The framework generalizes to diverse out-of-sample data and offers insight into utilizing RL precision selection for other numerical algorithms, advancing mixed-precision numerical methods in scientific computing. To the best of our knowledge, this is the first work on precision autotuning with RL and verified on unseen datasets.

