---
layout: default
title: A Clustering-Based Variable Ordering Framework for Relaxed Decision Diagrams for Maximum Weighted Independent Set Problem
---

# A Clustering-Based Variable Ordering Framework for Relaxed Decision Diagrams for Maximum Weighted Independent Set Problem
**arXiv**：[2512.15198v1](https://arxiv.org/abs/2512.15198) · [PDF](https://arxiv.org/pdf/2512.15198.pdf)  
**作者**：Mohsen Nafar, Michael Römer, Lin Xie  

**一句话要点**：提出基于聚类的变量排序框架，以提升最大加权独立集问题中松弛决策图的质量与效率。

**关键词**：松弛决策图, 变量排序, 最大加权独立集问题, 聚类方法, 分支定界算法

## 3 点简述
- 核心问题：松弛决策图的变量排序影响对偶界紧密度，动态排序全局计算开销大。
- 方法要点：先聚类变量再排序，采用Cluster-to-Cluster和Pick-and-Sort策略减少搜索空间。
- 实验或效果：在MWISP基准测试中，该方法有效降低计算成本，优于标准动态排序基线。

## 摘要（原文）

> Efficient exact algorithms for Discrete Optimization (DO) rely heavily on strong primal and dual bounds. Relaxed Decision Diagrams (DDs) provide a versatile mechanism for deriving such dual bounds by compactly over-approximating the solution space through node merging. However, the quality of these relaxed diagrams, i.e. the tightness of the resulting dual bounds, depends critically on the variable ordering and the merging decisions executed during compilation. While dynamic variable ordering heuristics effectively tighten bounds, they often incur computational overhead when evaluated globally across the entire variable set. To mitigate this trade-off, this work introduces a novel clustering-based framework for variable ordering. Instead of applying dynamic ordering heuristics to the full set of unfixed variables, we first partition variables into clusters. We then leverage this structural decomposition to guide the ordering process, significantly reducing the heuristic's search space. Within this framework, we investigate two distinct strategies: Cluster-to-Cluster, which processes clusters sequentially using problem-specific aggregate criteria (such as cumulative vertex weights in the Maximum Weighted Independent Set Problem (MWISP)), and Pick-and-Sort, which iteratively selects and sorts representative variables from each cluster to balance local diversity with heuristic guidance. Later on, developing some theoretical results on the growth of the size of DDs for MWISP we propose two different policies for setting the number of clusters within the proposed framework. We embed these strategies into a DD-based branch-and-bound algorithm and evaluate them on the MWISP. Across benchmark instances, the proposed methodology consistently reduces computational costs compared to standard dynamic variable ordering baseline.

