---
layout: default
title: Hyperparameter Optimization of Constraint Programming Solvers
---

# Hyperparameter Optimization of Constraint Programming Solvers
**arXiv**：[2601.11389v1](https://arxiv.org/abs/2601.11389) · [PDF](https://arxiv.org/pdf/2601.11389.pdf)  
**作者**：Hedieh Haddad, Thibault Falque, Pierre Talbot, Pascal Bouvry  

**一句话要点**：提出探针求解算法以优化约束编程求解器的超参数配置

**关键词**：超参数优化, 约束编程, 贝叶斯优化, 求解器调优, CPMpy库

## 3 点简述
- 约束编程求解器性能高度依赖超参数选择，手动调优困难耗时
- 算法分两阶段：探针阶段探索超参数，求解阶段应用最优配置
- 实验显示贝叶斯优化在多数实例中优于默认配置和汉明距离搜索

## 摘要（原文）

> The performance of constraint programming solvers is highly sensitive to the choice of their hyperparameters. Manually finding the best solver configuration is a difficult, time-consuming task that typically requires expert knowledge. In this paper, we introduce probe and solve algorithm, a novel two-phase framework for automated hyperparameter optimization integrated into the CPMpy library. This approach partitions the available time budget into two phases: a probing phase that explores different sets of hyperparameters using configurable hyperparameter optimization methods, followed by a solving phase where the best configuration found is used to tackle the problem within the remaining time.
>   We implement and compare two hyperparameter optimization methods within the probe and solve algorithm: Bayesian optimization and Hamming distance search. We evaluate the algorithm on two different constraint programming solvers, ACE and Choco, across 114 combinatorial problem instances, comparing their performance against the solver's default configurations.
>   Results show that using Bayesian optimization, the algorithm outperforms the solver's default configurations, improving solution quality for ACE in 25.4% of instances and matching the default performance in 57.9%, and for Choco, achieving superior results in 38.6% of instances. It also consistently surpasses Hamming distance search within the same framework, confirming the advantage of model-based exploration over simple local search. Overall, the probe and solve algorithm offers a practical, resource-aware approach for tuning constraint solvers that yields robust improvements across diverse problem types.

