---
layout: default
title: Delayed Assignments in Online Non-Centroid Clustering with Stochastic Arrivals
---

# Delayed Assignments in Online Non-Centroid Clustering with Stochastic Arrivals
**arXiv**：[2601.16091v1](https://arxiv.org/abs/2601.16091) · [PDF](https://arxiv.org/pdf/2601.16091.pdf)  
**作者**：Saar Cohen  

**一句话要点**：提出在线非质心聚类延迟分配框架，在随机到达模型中实现常数竞争比

**关键词**：在线聚类, 延迟分配, 随机到达模型, 常数竞争比, 非质心聚类, 距离成本优化

## 3 点简述
- 研究在线非质心聚类问题，允许延迟分配以权衡距离成本和延迟成本
- 针对随机到达模型，设计算法在期望总成本上相对于离线最优解有常数竞争比
- 克服最坏情况到达模型中的强不可能性，为超越最坏情况分析提供希望

## 摘要（原文）

> Clustering is a fundamental problem, aiming to partition a set of elements, like agents or data points, into clusters such that elements in the same cluster are closer to each other than to those in other clusters. In this paper, we present a new framework for studying online non-centroid clustering with delays, where elements, that arrive one at a time as points in a finite metric space, should be assigned to clusters, but assignments need not be immediate. Specifically, upon arrival, each point's location is revealed, and an online algorithm has to irrevocably assign it to an existing cluster or create a new one containing, at this moment, only this point. However, we allow decisions to be postponed at a delay cost, instead of following the more common assumption of immediate decisions upon arrival. This poses a critical challenge: the goal is to minimize both the total distance costs between points in each cluster and the overall delay costs incurred by postponing assignments. In the classic worst-case arrival model, where points arrive in an arbitrary order, no algorithm has a competitive ratio better than sublogarithmic in the number of points. To overcome this strong impossibility, we focus on a stochastic arrival model, where points' locations are drawn independently across time from an unknown and fixed probability distribution over the finite metric space. We offer hope for beyond worst-case adversaries: we devise an algorithm that is constant competitive in the sense that, as the number of points grows, the ratio between the expected overall costs of the output clustering and an optimal offline clustering is bounded by a constant.

