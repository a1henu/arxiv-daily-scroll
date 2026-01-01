---
layout: default
title: A New Decomposition Paradigm for Graph-structured Nonlinear Programs via Message Passing
---

# A New Decomposition Paradigm for Graph-structured Nonlinear Programs via Message Passing
**arXiv**：[2512.24676v1](https://arxiv.org/abs/2512.24676) · [PDF](https://arxiv.org/pdf/2512.24676.pdf)  
**作者**：Kuangyu Ding, Marie Maros, Gesualdo Scutari  

**一句话要点**：提出MP-Jacobi框架，通过消息传递和雅可比更新解决图结构非线性规划问题

**关键词**：图结构优化, 消息传递算法, 去中心化计算, 非线性规划, 超图分解

## 3 点简述
- 研究图或超图结构下的有限和型非线性规划问题，决策变量局部交互
- 提出MP-Jacobi框架，结合最小和消息传递与雅可比块更新，实现单跳通信和收敛
- 实验验证理论，在强凸目标下展示线性收敛，优于去中心化梯度基线

## 摘要（原文）

> We study finite-sum nonlinear programs whose decision variables interact locally according to a graph or hypergraph. We propose MP-Jacobi (Message Passing-Jacobi), a graph-compliant decentralized framework that couples min-sum message passing with Jacobi block updates. The (hyper)graph is partitioned into tree clusters. At each iteration, agents update in parallel by solving a cluster subproblem whose objective decomposes into (i) an intra-cluster term evaluated by a single min-sum sweep on the cluster tree (cost-to-go messages) and (ii) inter-cluster couplings handled via a Jacobi correction using neighbors' latest iterates. This design uses only single-hop communication and yields a convergent message-passing method on loopy graphs.
>   For strongly convex objectives we establish global linear convergence and explicit rates that quantify how curvature, coupling strength, and the chosen partition affect scalability and provide guidance for clustering. To mitigate the computation and communication cost of exact message updates, we develop graph-compliant surrogates that preserve convergence while reducing per-iteration complexity. We further extend MP-Jacobi to hypergraphs; in heavily overlapping regimes, a surrogate-based hyperedge-splitting scheme restores finite-time intra-cluster message updates and maintains convergence. Experiments validate the theory and show consistent improvements over decentralized gradient baselines.

