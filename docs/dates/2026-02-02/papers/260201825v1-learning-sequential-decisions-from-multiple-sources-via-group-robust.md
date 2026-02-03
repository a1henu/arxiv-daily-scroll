---
layout: default
title: Learning Sequential Decisions from Multiple Sources via Group-Robust Markov Decision Processes
---

# Learning Sequential Decisions from Multiple Sources via Group-Robust Markov Decision Processes
**arXiv**：[2602.01825v1](https://arxiv.org/abs/2602.01825) · [PDF](https://arxiv.org/pdf/2602.01825.pdf)  
**作者**：Mingyuan Xu, Zongqi Xia, Tianxi Cai, Doudou Zhou, Nian Si  

**一句话要点**：提出基于组线性结构分布鲁棒MDP的离线多站点策略学习框架

**关键词**：分布鲁棒马尔可夫决策过程, 多站点学习, 离线强化学习, 特征级不确定性, 悲观值迭代, 聚类扩展

## 3 点简述
- 核心问题：从异构多站点离线数据中学习鲁棒序列决策策略，处理站点间不确定性。
- 方法要点：引入特征级不确定性集，开发悲观值迭代算法，支持聚类扩展以提高样本效率。
- 实验或效果：在鲁棒部分覆盖假设下，证明策略次优性界，提供理论保证。

## 摘要（原文）

> We often collect data from multiple sites (e.g., hospitals) that share common structure but also exhibit heterogeneity. This paper aims to learn robust sequential decision-making policies from such offline, multi-site datasets. To model cross-site uncertainty, we study distributionally robust MDPs with a group-linear structure: all sites share a common feature map, and both the transition kernels and expected reward functions are linear in these shared features. We introduce feature-wise (d-rectangular) uncertainty sets, which preserve tractable robust Bellman recursions while maintaining key cross-site structure. Building on this, we then develop an offline algorithm based on pessimistic value iteration that includes: (i) per-site ridge regression for Bellman targets, (ii) feature-wise worst-case (row-wise minimization) aggregation, and (iii) a data-dependent pessimism penalty computed from the diagonals of the inverse design matrices. We further propose a cluster-level extension that pools similar sites to improve sample efficiency, guided by prior knowledge of site similarity. Under a robust partial coverage assumption, we prove a suboptimality bound for the resulting policy. Overall, our framework addresses multi-site learning with heterogeneous data sources and provides a principled approach to robust planning without relying on strong state-action rectangularity assumptions.

