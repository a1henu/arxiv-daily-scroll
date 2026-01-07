---
layout: default
title: Multi-Distribution Robust Conformal Prediction
---

# Multi-Distribution Robust Conformal Prediction
**arXiv**：[2601.02998v1](https://arxiv.org/abs/2601.02998) · [PDF](https://arxiv.org/pdf/2601.02998.pdf)  
**作者**：Yuqi Yang, Ying Jin  

**一句话要点**：提出多分布鲁棒保形预测框架，确保任意测试分布下的覆盖保证

**关键词**：保形预测, 分布鲁棒性, 多源学习, 公平性, 预测集优化

## 3 点简述
- 研究多源分布下保形预测的均匀覆盖问题，测试数据可来自任意分布或混合
- 提出max-p聚合方案，在有限样本下实现多分布覆盖，并优化效率以减小预测集大小
- 实验显示方法在保持最坏情况覆盖的同时，显著减小集大小，优于单源方法

## 摘要（原文）

> In many fairness and distribution robustness problems, one has access to labeled data from multiple source distributions yet the test data may come from an arbitrary member or a mixture of them. We study the problem of constructing a conformal prediction set that is uniformly valid across multiple, heterogeneous distributions, in the sense that no matter which distribution the test point is from, the coverage of the prediction set is guaranteed to exceed a pre-specified level. We first propose a max-p aggregation scheme that delivers finite-sample, multi-distribution coverage given any conformity scores associated with each distribution. Upon studying several efficiency optimization programs subject to uniform coverage, we prove the optimality and tightness of our aggregation scheme, and propose a general algorithm to learn conformity scores that lead to efficient prediction sets after the aggregation under standard conditions. We discuss how our framework relates to group-wise distributionally robust optimization, sub-population shift, fairness, and multi-source learning. In synthetic and real-data experiments, our method delivers valid worst-case coverage across multiple distributions while greatly reducing the set size compared with naively applying max-p aggregation to single-source conformity scores, and can be comparable in size to single-source prediction sets with popular, standard conformity scores.

