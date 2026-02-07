---
layout: default
title: Bayesian Neighborhood Adaptation for Graph Neural Networks
---

# Bayesian Neighborhood Adaptation for Graph Neural Networks
**arXiv**：[2602.05358v1](https://arxiv.org/abs/2602.05358) · [PDF](https://arxiv.org/pdf/2602.05358.pdf)  
**作者**：Paribesh Regmi, Rui Li, Kishan K C  

**一句话要点**：提出贝叶斯邻域自适应方法，以优化图神经网络在异质和同质图上的邻域范围选择。

**关键词**：图神经网络, 贝叶斯推断, 邻域自适应, 节点分类, 异质图

## 3 点简述
- 核心问题：图神经网络中邻域范围选择对性能至关重要，传统两阶段方法耗时且易偏置。
- 方法要点：将消息传递建模为随机过程，使用贝叶斯框架同时推断最优邻域范围和优化网络参数。
- 实验或效果：在基准数据集上验证，兼容先进图神经网络变体，节点分类任务表现竞争或更优，预测校准良好。

## 摘要（原文）

> The neighborhood scope (i.e., number of hops) where graph neural networks (GNNs) aggregate information to characterize a node's statistical property is critical to GNNs' performance. Two-stage approaches, training and validating GNNs for every pre-specified neighborhood scope to search for the best setting, is a time-consuming task and tends to be biased due to the search space design. How to adaptively determine proper neighborhood scopes for the aggregation process for both homophilic and heterophilic graphs remains largely unexplored. We thus propose to model the GNNs' message-passing behavior on a graph as a stochastic process by treating the number of hops as a beta process. This Bayesian framework allows us to infer the most plausible neighborhood scope for message aggregation simultaneously with the optimization of GNN parameters. Our theoretical analysis shows that the scope inference improves the expressivity of a GNN. Experiments on benchmark homophilic and heterophilic datasets show that the proposed method is compatible with state-of-the-art GNN variants, achieving competitive or superior performance on the node classification task, and providing well-calibrated predictions.

