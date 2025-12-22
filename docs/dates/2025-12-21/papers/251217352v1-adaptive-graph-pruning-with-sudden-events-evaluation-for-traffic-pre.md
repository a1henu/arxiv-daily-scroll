---
layout: default
title: Adaptive Graph Pruning with Sudden-Events Evaluation for Traffic Prediction using Online Semi-Decentralized ST-GNNs
---

# Adaptive Graph Pruning with Sudden-Events Evaluation for Traffic Prediction using Online Semi-Decentralized ST-GNNs
**arXiv**：[2512.17352v1](https://arxiv.org/abs/2512.17352) · [PDF](https://arxiv.org/pdf/2512.17352.pdf)  
**作者**：Ivan Kralj, Lodovico Giaretta, Gordan Ježić, Ivana Podnar Žarko, Šarūnas Girdzijauskas  

**一句话要点**：提出自适应图剪枝算法与SEPA指标，以降低在线半去中心化ST-GNN的通信开销并提升对交通突发事件的预测能力。

**关键词**：时空图神经网络, 自适应图剪枝, 在线半去中心化学习, 交通预测, 突发交通事件评估, 通信优化

## 3 点简述
- 核心问题：在线半去中心化ST-GNN部署中，相邻边缘节点间重复传输重叠特征导致通信开销过高。
- 方法要点：设计自适应图剪枝算法，动态过滤冗余邻居特征，并引入SEPA指标评估对交通突发事件的响应能力。
- 实验效果：在多个在线半去中心化设置中，算法显著降低通信成本，同时保持预测准确性，SEPA指标能有效揭示空间连通性价值。

## 摘要（原文）

> Spatio-Temporal Graph Neural Networks (ST-GNNs) are well-suited for processing high-frequency data streams from geographically distributed sensors in smart mobility systems. However, their deployment at the edge across distributed compute nodes (cloudlets) createssubstantial communication overhead due to repeated transmission of overlapping node features between neighbouring cloudlets. To address this, we propose an adaptive pruning algorithm that dynamically filters redundant neighbour features while preserving the most informative spatial context for prediction. The algorithm adjusts pruning rates based on recent model performance, allowing each cloudlet to focus on regions experiencing traffic changes without compromising accuracy. Additionally, we introduce the Sudden Event Prediction Accuracy (SEPA), a novel event-focused metric designed to measure responsiveness to traffic slowdowns and recoveries, which are often missed by standard error metrics. We evaluate our approach in an online semi-decentralized setting with traditional FL, server-free FL, and Gossip Learning on two large-scale traffic datasets, PeMS-BAY and PeMSD7-M, across short-, mid-, and long-term prediction horizons. Experiments show that, in contrast to standard metrics, SEPA exposes the true value of spatial connectivity in predicting dynamic and irregular traffic. Our adaptive pruning algorithm maintains prediction accuracy while significantly lowering communication cost in all online semi-decentralized settings, demonstrating that communication can be reduced without compromising responsiveness to critical traffic events.

