---
layout: default
title: Neural Algorithmic Reasoning for Approximate $k$-Coloring with Recursive Warm Starts
---

# Neural Algorithmic Reasoning for Approximate $k$-Coloring with Recursive Warm Starts
**arXiv**：[2601.05137v1](https://arxiv.org/abs/2601.05137) · [PDF](https://arxiv.org/pdf/2601.05137.pdf)  
**作者**：Knut Vanderbush, Melanie Weber  

**一句话要点**：提出基于图神经网络的近似k-着色算法，结合递归预热启动提升性能

**关键词**：图神经网络, 近似k-着色, 递归预热启动, 组合优化, 图着色算法, 局部搜索

## 3 点简述
- 研究近似k-着色问题，即用最多k种颜色为图节点着色，最小化同色边数量
- 优化图神经网络方法，引入正交节点特征初始化和基于度的损失函数，并设计递归预热启动策略
- 实验表明，图神经网络在大规模图上表现更优，递归预热启动可独立用于组合优化

## 摘要（原文）

> Node coloring is the task of assigning colors to the nodes of a graph such that no two adjacent nodes have the same color, while using as few colors as possible. It is the most widely studied instance of graph coloring and of central importance in graph theory; major results include the Four Color Theorem and work on the Hadwiger-Nelson Problem. As an abstraction of classical combinatorial optimization tasks, such as scheduling and resource allocation, it is also rich in practical applications. Here, we focus on a relaxed version, approximate $k$-coloring, which is the task of assigning at most $k$ colors to the nodes of a graph such that the number of edges whose vertices have the same color is approximately minimized. While classical approaches leverage mathematical programming or SAT solvers, recent studies have explored the use of machine learning. We follow this route and explore the use of graph neural networks (GNNs) for node coloring. We first present an optimized differentiable algorithm that improves a prior approach by Schuetz et al. with orthogonal node feature initialization and a loss function that penalizes conflicting edges more heavily when their endpoints have higher degree; the latter inspired by the classical result that a graph is $k$-colorable if and only if its $k$-core is $k$-colorable. Next, we introduce a lightweight greedy local search algorithm and show that it may be improved by recursively computing a $(k-1)$-coloring to use as a warm start. We then show that applying such recursive warm starts to the GNN approach leads to further improvements. Numerical experiments on a range of different graph structures show that while the local search algorithms perform best on small inputs, the GNN exhibits superior performance at scale. The recursive warm start may be of independent interest beyond graph coloring for local search methods for combinatorial optimization.

