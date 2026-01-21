---
layout: default
title: Fisher-Informed Parameterwise Aggregation for Federated Learning with Heterogeneous Data
---

# Fisher-Informed Parameterwise Aggregation for Federated Learning with Heterogeneous Data
**arXiv**：[2601.13608v1](https://arxiv.org/abs/2601.13608) · [PDF](https://arxiv.org/pdf/2601.13608.pdf)  
**作者**：Zhipeng Chang, Ting He, Wenrui Hao  

**一句话要点**：提出Fisher信息参数级聚合方法以解决异构数据下联邦学习的客户端漂移问题

**关键词**：联邦学习, 异构数据, Fisher信息矩阵, 参数级聚合, 客户端漂移, 低秩近似

## 3 点简述
- 核心问题：标准联邦学习方法在非独立同分布数据下使用客户端级标量权重，导致参数更新错位和客户端漂移。
- 方法要点：基于Fisher信息矩阵为每个参数分配特定权重，实现参数级缩放，并通过低秩近似保持通信和计算效率。
- 实验或效果：在非线性函数回归、偏微分方程学习和图像分类任务中，FIPA优于基于平均的聚合方法，并能结合先进客户端优化算法提升准确率。

## 摘要（原文）

> Federated learning aggregates model updates from distributed clients, but standard first order methods such as FedAvg apply the same scalar weight to all parameters from each client. Under non-IID data, these uniformly weighted updates can be strongly misaligned across clients, causing client drift and degrading the global model. Here we propose Fisher-Informed Parameterwise Aggregation (FIPA), a second-order aggregation method that replaces client-level scalar weights with parameter-specific Fisher Information Matrix (FIM) weights, enabling true parameter-level scaling that captures how each client's data uniquely influences different parameters. With low-rank approximation, FIPA remains communication- and computation-efficient. Across nonlinear function regression, PDE learning, and image classification, FIPA consistently improves over averaging-based aggregation, and can be effectively combined with state-of-the-art client-side optimization algorithms to further improve image classification accuracy. These results highlight the benefits of FIPA for federated learning under heterogeneous data distributions.

