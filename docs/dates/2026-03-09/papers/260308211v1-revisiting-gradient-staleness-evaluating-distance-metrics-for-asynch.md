---
layout: default
title: Revisiting Gradient Staleness: Evaluating Distance Metrics for Asynchronous Federated Learning Aggregation
---

# Revisiting Gradient Staleness: Evaluating Distance Metrics for Asynchronous Federated Learning Aggregation
**arXiv**：[2603.08211v1](https://arxiv.org/abs/2603.08211) · [PDF](https://arxiv.org/pdf/2603.08211.pdf)  
**作者**：Patrick Wilhelm, Odej Kao  

**一句话要点**：探索距离度量以改进异步联邦学习中的梯度陈旧性聚合

**关键词**：异步联邦学习, 梯度陈旧性, 距离度量, 模型聚合, 非独立同分布数据, 训练稳定性

## 3 点简述
- 异步联邦学习中，客户端更新延迟导致梯度陈旧性，影响模型收敛和准确性。
- 研究多种距离度量替代欧氏距离，以更精确衡量梯度陈旧性并集成到聚合过程中。
- 在异构客户端和非独立同分布数据下评估不同度量对收敛速度、性能和稳定性的影响。

## 摘要（原文）

> In asynchronous federated learning (FL), client devices send updates to a central server at varying times based on their computational speed, often using stale versions of the global model. This staleness can degrade the convergence and accuracy of the global model. Previous work, such as AsyncFedED, proposed an adaptive aggregation method using Euclidean distance to measure staleness. In this paper, we extend this approach by exploring alternative distance metrics to more accurately capture the effect of gradient staleness. We integrate these metrics into the aggregation process and evaluate their impact on convergence speed, model performance, and training stability under heterogeneous clients and non-IID data settings. Our results demonstrate that certain metrics lead to more robust and efficient asynchronous FL training, offering a stronger foundation for practical deployment.

