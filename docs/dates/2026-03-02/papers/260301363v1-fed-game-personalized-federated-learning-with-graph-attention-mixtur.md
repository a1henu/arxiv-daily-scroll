---
layout: default
title: Fed-GAME: Personalized Federated Learning with Graph Attention Mixture-of-Experts For Time-Series Forecasting
---

# Fed-GAME: Personalized Federated Learning with Graph Attention Mixture-of-Experts For Time-Series Forecasting
**arXiv**：[2603.01363v1](https://arxiv.org/abs/2603.01363) · [PDF](https://arxiv.org/pdf/2603.01363.pdf)  
**作者**：Yi Li, Han Liu, Mingfeng Fan, Guo Chen, Chaojie Li, Biplab Sikdar  

**一句话要点**：提出Fed-GAME框架，通过可学习动态隐式图实现个性化联邦学习，用于时间序列预测。

**关键词**：个性化联邦学习, 时间序列预测, 图注意力网络, 混合专家模型, 动态隐式图

## 3 点简述
- 核心问题：现有图联邦学习方法依赖静态拓扑，难以处理客户端异构性。
- 方法要点：基于参数差异的更新协议，结合图注意力混合专家聚合器进行细粒度个性化。
- 实验或效果：在真实电动汽车充电数据集上优于现有个性化联邦学习基线。

## 摘要（原文）

> Federated learning (FL) on graphs shows promise for distributed time-series forecasting. Yet, existing methods rely on static topologies and struggle with client heterogeneity. We propose Fed-GAME, a framework that models personalized aggregation as message passing over a learnable dynamic implicit graph. The core is a decoupled parameter difference-based update protocol, where clients transmit parameter differences between their fine-tuned private model and a shared global model. On the server, these differences are decomposed into two streams: (1) averaged difference used to updating the global model for consensus (2) the selective difference fed into a novel Graph Attention Mixture-of-Experts (GAME) aggregator for fine-grained personalization. In this aggregator, shared experts provide scoring signals while personalized gates adaptively weight selective updates to support personalized aggregation. Experiments on two real-world electric vehicle charging datasets demonstrate that Fed-GAME outperforms state-of-the-art personalized FL baselines.

