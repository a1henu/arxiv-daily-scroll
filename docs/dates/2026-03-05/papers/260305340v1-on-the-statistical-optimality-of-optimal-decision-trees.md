---
layout: default
title: On the Statistical Optimality of Optimal Decision Trees
---

# On the Statistical Optimality of Optimal Decision Trees
**arXiv**：[2603.05340v1](https://arxiv.org/abs/2603.05340) · [PDF](https://arxiv.org/pdf/2603.05340.pdf)  
**作者**：Zineng Xu, Subhroshekhar Ghosh, Yan Shuo Tan  

**一句话要点**：提出基于经验风险最小化的最优决策树统计理论，涵盖高维回归与分类场景。

**关键词**：最优决策树, 统计理论, 经验风险最小化, oracle不等式, PSHAB空间, 鲁棒性分析

## 3 点简述
- 核心问题：全局最优经验风险最小化决策树缺乏统计性能的严格理论保证。
- 方法要点：使用基于经验局部化Rademacher复杂度的新框架，建立尖锐的oracle不等式。
- 实验或效果：推导出在PSHAB函数类上的极小极大最优速率，并提供鲁棒性保证。

## 摘要（原文）

> While globally optimal empirical risk minimization (ERM) decision trees have become computationally feasible and empirically successful, rigorous theoretical guarantees for their statistical performance remain limited. In this work, we develop a comprehensive statistical theory for ERM trees under random design in both high-dimensional regression and classification. We first establish sharp oracle inequalities that bound the excess risk of the ERM estimator relative to the best possible approximation achievable by any tree with at most $L$ leaves, thereby characterizing the interpretability-accuracy trade-off. We derive these results using a novel uniform concentration framework based on empirically localized Rademacher complexity. Furthermore, we derive minimax optimal rates over a novel function class: the piecewise sparse heterogeneous anisotropic Besov (PSHAB) space. This space explicitly captures three key structural features encountered in practice: sparsity, anisotropic smoothness, and spatial heterogeneity. While our main results are established under sub-Gaussianity, we also provide robust guarantees that hold under heavy-tailed noise settings. Together, these findings provide a principled foundation for the optimality of ERM trees and introduce empirical process tools broadly applicable to other highly adaptive, data-driven procedures.

