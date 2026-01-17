---
layout: default
title: Redundancy-Driven Top-$k$ Functional Dependency Discovery
---

# Redundancy-Driven Top-$k$ Functional Dependency Discovery
**arXiv**：[2601.10130v1](https://arxiv.org/abs/2601.10130) · [PDF](https://arxiv.org/pdf/2601.10130.pdf)  
**作者**：Xiaolong Wan, Xixian Han  

**一句话要点**：提出SDP算法以高效发现基于冗余计数的top-k函数依赖，解决大规模高维数据中FD发现的计算和结果集问题。

**关键词**：函数依赖发现, 冗余计数, 搜索空间剪枝, top-k查询, 数据库约束, 大规模数据处理

## 3 点简述
- 核心问题：传统FD发现算法计算成本高且结果集庞大，难以在大规模高维数据中应用。
- 方法要点：SDP利用冗余计数的单调上界剪枝搜索空间，结合属性排序、分区基数矩阵和全局调度优化。
- 实验或效果：在40多个数据集上验证，SDP比穷举方法更快且内存使用更少。

## 摘要（原文）

> Functional dependencies (FDs) are basic constraints in relational databases and are used for many data management tasks. Most FD discovery algorithms find all valid dependencies, but this causes two problems. First, the computational cost is prohibitive: computational complexity grows quadratically with the number of tuples and exponentially with the number of attributes, making discovery slow on large-scale and high-dimensional data. Second, the result set can be huge, making it hard to identify useful dependencies. We propose SDP (Selective-Discovery-and-Prune), which discovers the top-$k$ FDs ranked by redundancy count. Redundancy count measures how much duplicated information an FD explains and connects directly to storage overhead and update anomalies. SDP uses an upper bound on redundancy to prune the search space. It is proved that this upper bound is monotone: adding attributes refines partitions and thus decreases the bound. Once the bound falls below the top-$k$ threshold, the entire branch can be skipped. We improve SDP with three optimizations: ordering attributes by partition cardinality, using pairwise statistics in a Partition Cardinality Matrix to tighten bounds, and a global scheduler to explore promising branches first. Experiments on over 40 datasets show that SDP is much faster and uses less memory than exhaustive methods.

