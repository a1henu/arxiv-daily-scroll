---
layout: default
title: Non-Stationary Online Resource Allocation: Learning from a Single Sample
---

# Non-Stationary Online Resource Allocation: Learning from a Single Sample
**arXiv**：[2602.18114v1](https://arxiv.org/abs/2602.18114) · [PDF](https://arxiv.org/pdf/2602.18114.pdf)  
**作者**：Yiding Feng, Jiashuo Jiang, Yige Wang  

**一句话要点**：提出基于分位数的元策略，以单样本处理非平稳在线资源分配问题

**关键词**：在线资源分配, 非平稳环境, 单样本学习, 分位数策略, 多资源约束, 遗憾分析

## 3 点简述
- 研究非平稳需求下的在线资源分配，仅需每期一个历史样本
- 方法包括奖励分布估计、流体松弛优化和动态接受阈值决策
- 在奖励可观测和仅类型样本下分别实现次线性和多对数遗憾

## 摘要（原文）

> We study online resource allocation under non-stationary demand with a minimum offline data requirement. In this problem, a decision-maker must allocate multiple types of resources to sequentially arriving queries over a finite horizon. Each query belongs to a finite set of types with fixed resource consumption and a stochastic reward drawn from an unknown, type-specific distribution. Critically, the environment exhibits arbitrary non-stationarity -- arrival distributions may shift unpredictably-while the algorithm requires only one historical sample per period to operate effectively. We distinguish two settings based on sample informativeness: (i) reward-observed samples containing both query type and reward realization, and (ii) the more challenging type-only samples revealing only query type information.
>   We propose a novel type-dependent quantile-based meta-policy that decouples the problem into modular components: reward distribution estimation, optimization of target service probabilities via fluid relaxation, and real-time decisions through dynamic acceptance thresholds. For reward-observed samples, our static threshold policy achieves $\tilde{O}(\sqrt{T})$ regret. For type-only samples, we first establish that sublinear regret is impossible without additional structure; under a mild minimum-arrival-probability assumption, we design both a partially adaptive policy attaining the same $\tilde{O}({T})$ bound and, more significantly, a fully adaptive resolving policy with careful rounding that achieves the first poly-logarithmic regret guarantee of $O((\log T)^3)$ for non-stationary multi-resource allocation. Our framework advances prior work by operating with minimal offline data (one sample per period), handling arbitrary non-stationarity without variation-budget assumptions, and supporting multiple resource constraints.

