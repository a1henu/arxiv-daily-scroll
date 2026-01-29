---
layout: default
title: Exact Graph Learning via Integer Programming
---

# Exact Graph Learning via Integer Programming
**arXiv**：[2601.20589v1](https://arxiv.org/abs/2601.20589) · [PDF](https://arxiv.org/pdf/2601.20589.pdf)  
**作者**：Lucas Kook, Søren Wengel Mogensen  

**一句话要点**：提出基于非参数条件独立性检验和整数规划的精确图学习方法，解决现有方法依赖强假设或无法保证全局最优的问题。

**关键词**：图学习, 整数规划, 非参数方法, 因果发现, 全局优化, R包实现

## 3 点简述
- 核心问题：从数据中推断变量依赖结构，现有方法常依赖强假设或近似求解，导致敏感或非全局最优。
- 方法要点：将图学习问题重构为整数规划问题，利用图形分离准则高效编码，证明可获全局最优解。
- 实验或效果：实现于R包'glip'，支持多种图类型，在模拟和基准数据集上表现优于现有精确方法。

## 摘要（原文）

> Learning the dependence structure among variables in complex systems is a central problem across medical, natural, and social sciences. These structures can be naturally represented by graphs, and the task of inferring such graphs from data is known as graph learning or as causal discovery if the graphs are given a causal interpretation. Existing approaches typically rely on restrictive assumptions about the data-generating process, employ greedy oracle algorithms, or solve approximate formulations of the graph learning problem. As a result, they are either sensitive to violations of central assumptions or fail to guarantee globally optimal solutions. We address these limitations by introducing a nonparametric graph learning framework based on nonparametric conditional independence testing and integer programming. We reformulate the graph learning problem as an integer-programming problem and prove that solving the integer-programming problem provides a globally optimal solution to the original graph learning problem. Our method leverages efficient encodings of graphical separation criteria, enabling the exact recovery of larger graphs than was previously feasible. We provide an implementation in the openly available R package 'glip' which supports learning (acyclic) directed (mixed) graphs and chain graphs. From the resulting output one can compute representations of the corresponding Markov equivalence classes or weak equivalence classes. Empirically, we demonstrate that our approach is faster than other existing exact graph learning procedures for a large fraction of instances and graphs of various sizes. GLIP also achieves state-of-the-art performance on simulated data and benchmark datasets across all aforementioned classes of graphs.

