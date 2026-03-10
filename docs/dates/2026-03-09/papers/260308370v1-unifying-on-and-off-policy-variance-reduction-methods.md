---
layout: default
title: Unifying On- and Off-Policy Variance Reduction Methods
---

# Unifying On- and Off-Policy Variance Reduction Methods
**arXiv**：[2603.08370v1](https://arxiv.org/abs/2603.08370) · [PDF](https://arxiv.org/pdf/2603.08370.pdf)  
**作者**：Olivier Jeunen  

**一句话要点**：统一在线与离线方差减少方法，建立形式等价性以指导实践与研究

**关键词**：方差减少, 在线A/B测试, 离线策略评估, 控制变量, 双重稳健估计, 统计等价性

## 3 点简述
- 核心问题：在线A/B测试与离线策略评估领域隔离，术语和统计工具不统一，阻碍方法互通。
- 方法要点：证明在线差异均值估计器与离线逆倾向评分加最优控制变量估计器数学等价，回归调整方法结构等价于双重稳健估计。
- 实验或效果：统一视角扩展对常用方法的理解，为从业者和研究者提供跨领域指导，促进方法应用。

## 摘要（原文）

> Continuous and efficient experimentation is key to the practical success of user-facing applications on the web, both through online A/B-tests and off-policy evaluation. Despite their shared objective -- estimating the incremental value of a treatment -- these domains often operate in isolation, utilising distinct terminologies and statistical toolkits. This paper bridges that divide by establishing a formal equivalence between their canonical variance reduction methods.
>   We prove that the standard online Difference-in-Means estimator is mathematically identical to an off-policy Inverse Propensity Scoring estimator equipped with an optimal (variance-minimising) additive control variate. Extending this unification, we demonstrate that widespread regression adjustment methods (such as CUPED, CUPAC, and ML-RATE) are structurally equivalent to Doubly Robust estimation. This unified view extends our understanding of commonly used approaches, and can guide practitioners and researchers working on either class of problems.

