---
layout: default
title: Learning Causal Structure of Time Series using Best Order Score Search
---

# Learning Causal Structure of Time Series using Best Order Score Search
**arXiv**：[2603.05370v1](https://arxiv.org/abs/2603.05370) · [PDF](https://arxiv.org/pdf/2603.05370.pdf)  
**作者**：Irene Gema Castillo Mansilla, Urmi Ninad  

**一句话要点**：提出TS-BOSS方法以解决时间序列因果结构学习中的挑战

**关键词**：时间序列因果发现, 动态贝叶斯网络, 排列搜索, 因果结构学习, 高自相关场景

## 3 点简述
- 核心问题：时间序列因果发现因时间依赖性面临挑战，需扩展静态方法。
- 方法要点：基于BOSS扩展，使用排列搜索和动态贝叶斯网络，利用grow-shrink树缓存计算。
- 实验或效果：在合成数据上，高自相关场景下优于标准约束方法，实现高召回率。

## 摘要（原文）

> Causal structure learning from observational data is central to many scientific and policy domains, but the time series setting common to many disciplines poses several challenges due to temporal dependence. In this paper we focus on score-based causal discovery for multivariate time series and introduce TS-BOSS, a time series extension of the recently proposed Best Order Score Search (BOSS) (Andrews et al. 2023). TS-BOSS performs a permutation-based search over dynamic Bayesian network structures while leveraging grow-shrink trees to cache intermediate score computations, preserving the scalability and strong empirical performance of BOSS in the static setting. We provide theoretical guarantees establishing the soundness of TS-BOSS under suitable assumptions, and we present an intermediate result that extends classical subgraph minimality results for permutation-based methods to the dynamic (time series) setting. Our experiments on synthetic data show that TS-BOSS is especially effective in high auto-correlation regimes, where it consistently achieves higher adjacency recall at comparable precision than standard constraint-based methods. Overall, TS-BOSS offers a high-performing, scalable approach for time series causal discovery and our results provide a principled bridge for extending sparsity-based, permutation-driven causal learning theory to dynamic settings.

