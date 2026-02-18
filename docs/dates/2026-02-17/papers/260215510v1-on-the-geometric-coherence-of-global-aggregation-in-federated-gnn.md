---
layout: default
title: On the Geometric Coherence of Global Aggregation in Federated GNN
---

# On the Geometric Coherence of Global Aggregation in Federated GNN
**arXiv**：[2602.15510v1](https://arxiv.org/abs/2602.15510) · [PDF](https://arxiv.org/pdf/2602.15510.pdf)  
**作者**：Chethana Prasad Kabgere, Shylaja SS  

**一句话要点**：提出GGRS框架以解决联邦图神经网络中全局聚合的几何失配问题

**关键词**：联邦学习, 图神经网络, 几何一致性, 全局聚合, 消息传递, 异质图

## 3 点简述
- 核心问题：联邦GNN中客户端图结构异质导致全局聚合破坏消息传递的几何一致性
- 方法要点：GGRS基于几何容许准则在服务器端调节客户端更新，保持变换方向一致性和传播子空间多样性
- 实验或效果：在异质GNN原生和Amazon Co-purchase数据集上验证GGRS能维持全局消息传递一致性

## 摘要（原文）

> Federated Learning (FL) enables distributed training across multiple clients without centralized data sharing, while Graph Neural Networks (GNNs) model relational data through message passing. In federated GNN settings, client graphs often exhibit heterogeneous structural and propagation characteristics. When standard aggregation mechanisms are applied to such heterogeneous updates, the global model may converge numerically while exhibiting degraded relational behavior.Our work identifies a geometric failure mode of global aggregation in Cross- Domain Federated GNNs. Although GNN parameters are numerically represented as vectors, they encode relational transformations that govern the direction, strength, and sensitivity of information flow across graph neighborhoods. Aggregating updates originating from incompatible propagation regimes can therefore introduce destructive interference in this transformation space.This leads to loss of coherence in global message passing. Importantly, this degradation is not necessarily reflected in conventional metrics such as loss or accuracy.To address this issue, we propose GGRS (Global Geometric Reference Structure), a server-side framework that regulates client updates prior to aggregation based on geometric admissibility criteria. GGRS preserves directional consistency of relational transformations as well as maintains diversity of admissible propagation subspaces. It also stabilizes sensitivity to neighborhood interactions, without accessing client data or graph topology. Experiments on heterogeneous GNN-native, Amazon Co-purchase datasets demonstrate that GGRS preserves global message-passing coherence across training rounds by highlighting the necessity of geometry-aware regulation in federated graph learning.

