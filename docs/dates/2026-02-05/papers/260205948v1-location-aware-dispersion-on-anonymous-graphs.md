---
layout: default
title: Location-Aware Dispersion on Anonymous Graphs
---

# Location-Aware Dispersion on Anonymous Graphs
**arXiv**：[2602.05948v1](https://arxiv.org/abs/2602.05948) · [PDF](https://arxiv.org/pdf/2602.05948.pdf)  
**作者**：Himani, Supantha Pandit, Gokarna Sharma  

**一句话要点**：提出位置感知分散问题，在匿名图中基于颜色匹配实现机器人分散，扩展经典分散问题。

**关键词**：分布式机器人, 匿名图, 位置感知分散, 确定性算法, 时间内存界限, 颜色匹配

## 3 点简述
- 核心问题：在匿名图中，机器人需移动到同色节点实现分散，引入位置感知约束。
- 方法要点：开发确定性算法，保证时间和内存界限，并给出不可能性和下界分析。
- 实验或效果：算法验证位置感知分散的可行性，但相比经典分散更复杂低效。

## 摘要（原文）

> The well-studied DISPERSION problem is a fundamental coordination problem in distributed robotics, where a set of mobile robots must relocate so that each occupies a distinct node of a network. DISPERSION assumes that a robot can settle at any node as long as no other robot settles on that node. In this work, we introduce LOCATION-AWARE DISPERSION, a novel generalization of DISPERSION that incorporates location awareness: Let $G = (V, E)$ be an anonymous, connected, undirected graph with $n = \|V\|$ nodes, each labeled with a color $\sf{col}(v) \in C = \{c_1, \dots, c_t\}, t\leq n$. A set $R = \{r_1, \dots, r_k\}$ of $k \leq n$ mobile robots is given, where each robot $r_i$ has an associated color $\mathsf{col}(r_i) \in C$. Initially placed arbitrarily on the graph, the goal is to relocate the robots so that each occupies a distinct node of the same color. When $\|C\|=1$, LOCATION-AWARE DISPERSION reduces to DISPERSION. There is a solution to DISPERSION in graphs with any $k\leq n$ without knowing $k,n$.
>   Like DISPERSION, the goal is to solve LOCATION-AWARE DISPERSION minimizing both time and memory requirement at each agent. We develop several deterministic algorithms with guaranteed bounds on both time and memory requirement. We also give an impossibility and a lower bound for any deterministic algorithm for LOCATION-AWARE DISPERSION. To the best of our knowledge, the presented results collectively establish the algorithmic feasibility of LOCATION-AWARE DISPERSION in anonymous networks and also highlight the challenges on getting an efficient solution compared to the solutions for DISPERSION.

