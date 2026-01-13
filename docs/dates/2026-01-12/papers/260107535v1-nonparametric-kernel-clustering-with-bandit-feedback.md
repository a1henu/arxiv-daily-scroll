---
layout: default
title: Nonparametric Kernel Clustering with Bandit Feedback
---

# Nonparametric Kernel Clustering with Bandit Feedback
**arXiv**：[2601.07535v1](https://arxiv.org/abs/2601.07535) · [PDF](https://arxiv.org/pdf/2601.07535.pdf)  
**作者**：Victor Thuot, Sebastian Vogt, Debarghya Ghoshdastidar, Nicolas Verzelen  

**一句话要点**：提出非参数核聚类框架KABC算法，以解决带反馈的聚类问题，适用于真实世界数据集。

**关键词**：带反馈聚类, 非参数方法, 核均值嵌入, 最大均值差异, 自适应算法, 推荐系统

## 3 点简述
- 核心问题：在带反馈的聚类中，现有方法依赖子高斯分布假设，限制了实际应用。
- 方法要点：采用核方法将非参数问题转化为RKHS中的核均值嵌入聚类，引入自适应算法KABC。
- 实验或效果：算法具有理论正确性保证，分析采样预算，适应未知信噪比，实现实例依赖性能。

## 摘要（原文）

> Clustering with bandit feedback refers to the problem of partitioning a set of items, where the clustering algorithm can sequentially query the items to receive noisy observations. The problem is formally posed as the task of partitioning the arms of an N-armed stochastic bandit according to their underlying distributions, grouping two arms together if and only if they share the same distribution, using samples collected sequentially and adaptively. This setting has gained attention in recent years due to its applicability in recommendation systems and crowdsourcing. Existing works on clustering with bandit feedback rely on a strong assumption that the underlying distributions are sub-Gaussian. As a consequence, the existing methods mainly cover settings with linearly-separable clusters, which has little practical relevance. We introduce a framework of ``nonparametric clustering with bandit feedback'', where the underlying arm distributions are not constrained to any parametric, and hence, it is applicable for active clustering of real-world datasets. We adopt a kernel-based approach, which allows us to reformulate the nonparametric problem as the task of clustering the arms according to their kernel mean embeddings in a reproducing kernel Hilbert space (RKHS). Building on this formulation, we introduce the KABC algorithm with theoretical correctness guarantees and analyze its sampling budget. We introduce a notion of signal-to-noise ratio for this problem that depends on the maximum mean discrepancy (MMD) between the arm distributions and on their variance in the RKHS. Our algorithm is adaptive to this unknown quantity: it does not require it as an input yet achieves instance-dependent guarantees.

