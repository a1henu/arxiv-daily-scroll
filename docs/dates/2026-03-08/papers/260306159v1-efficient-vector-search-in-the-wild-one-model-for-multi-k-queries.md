---
layout: default
title: Efficient Vector Search in the Wild: One Model for Multi-K Queries
---

# Efficient Vector Search in the Wild: One Model for Multi-K Queries
**arXiv**：[2603.06159v1](https://arxiv.org/abs/2603.06159) · [PDF](https://arxiv.org/pdf/2603.06159.pdf)  
**作者**：Yifan Peng, Jiafei Fan, Xingda Wei, Sijie Shen, Rong Chen, Jianning Wang, Xiaojian Luo, Wenyuan Yu, Jingren Zhou, Haibo Chen  

**一句话要点**：提出OMEGA方法以解决多K值向量查询中学习型搜索的泛化问题

**关键词**：向量搜索, 学习型索引, 多K值查询, 动态精炼, 预处理优化

## 3 点简述
- 当前学习型top-K搜索模型无法泛化到多K值查询，导致精度和性能下降
- OMEGA基于K=1训练的基础模型，通过动态精炼和统计特性优化，支持多K值查询
- 实验显示OMEGA在预处理时间减少的同时，实现了更低的平均延迟和相同召回率

## 摘要（原文）

> Learned top-K search is a promising approach for serving vector queries with both high accuracy and performance. However, current models trained for a specific K value fail to generalize to real-world multi-K queries: they suffer from accuracy degradation (for larger Ks) and performance loss (for smaller Ks). Training the model to generalize on different Ks requires orders of magnitude more preprocessing time and is not suitable for serving vector queries in the wild. We present OMEGA, a K-generalizable learned top-K search method that simultaneously achieves high accuracy, high performance, and low preprocessing cost for multi-K vector queries. The key idea is that a base model properly trained on K=1 with our trajectory-based features can be used to accurately predict larger Ks with a dynamic refinement procedure and smaller Ks with minimal performance loss. To make our refinements efficient, we further leverage the statistical properties of top-K searches to reduce excessive model invocations. Extensive evaluations on multiple public and production datasets show that, under the same preprocessing budgets, OMEGA achieves 6-33% lower average latency compared to state-of-the-art learned search methods, while all systems achieve the same recall target. With only 16-30% of the preprocessing time, OMEGA attains 1.01-1.28x of the optimal average latency of these baselines.

