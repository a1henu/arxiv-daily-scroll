---
layout: default
title: On the Statistical Optimality of Optimal Decision Trees
---

# On the Statistical Optimality of Optimal Decision Trees
**arXiv**：[2603.05340v1](https://arxiv.org/abs/2603.05340) · [PDF](https://arxiv.org/pdf/2603.05340.pdf)  
**作者**：Zineng Xu, Subhroshekhar Ghosh, Yan Shuo Tan  

**一句话要点**：提出基于经验风险最小化的最优决策树统计理论，涵盖高维回归与分类场景。

**关键词**：决策树, 统计最优性, 经验风险最小化, 高维回归, 分类, Rademacher复杂度

## 3 点简述
- 核心问题：最优决策树在统计性能上缺乏严格理论保证。
- 方法要点：使用经验局部化Rademacher复杂度建立均匀集中框架。
- 实验或效果：推导出最小化最优速率，适用于稀疏、各向异性平滑和空间异质性函数类。

## 摘要（原文）

> While globally optimal empirical risk minimization (ERM) decision trees have become computationally feasible and empirically successful, rigorous theoretical guarantees for their statistical performance remain limited. In this work, we develop a comprehensive statistical theory for ERM trees under random design in both high-dimensional regression and classification. We first establish sharp oracle inequalities that bound the excess risk of the ERM estimator relative to the best possible approximation achievable by any tree with at most $L$ leaves, thereby characterizing the interpretability-accuracy trade-off. We derive these results using a novel uniform concentration framework based on empirically localized Rademacher complexity. Furthermore, we derive minimax optimal rates over a novel function class: the piecewise sparse heterogeneous anisotropic Besov (PSHAB) space. This space explicitly captures three key structural features encountered in practice: sparsity, anisotropic smoothness, and spatial heterogeneity. While our main results are established under sub-Gaussianity, we also provide robust guarantees that hold under heavy-tailed noise settings. Together, these findings provide a principled foundation for the optimality of ERM trees and introduce empirical process tools broadly applicable to other highly adaptive, data-driven procedures.

