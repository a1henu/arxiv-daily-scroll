---
layout: default
title: Hierarchical Federated Learning with SignSGD: A Highly Communication-Efficient Approach
---

# Hierarchical Federated Learning with SignSGD: A Highly Communication-Efficient Approach
**arXiv**：[2602.02355v1](https://arxiv.org/abs/2602.02355) · [PDF](https://arxiv.org/pdf/2602.02355.pdf)  
**作者**：Amirreza Kazemi, Seyed Mohammad Azimi-Abarghouyi, Gabor Fodor, Carlo Fischione  

**一句话要点**：提出HierSignSGD框架，以解决分层联邦学习中通信效率低的问题。

**关键词**：分层联邦学习, 符号随机梯度下降, 通信效率, 梯度压缩, 非凸优化, 多数投票聚合

## 3 点简述
- 核心问题：分层联邦学习中，现有SignSGD理论与算法不适用于边缘-云两层聚合，性能影响未知。
- 方法要点：设备发送符号梯度，边缘服务器多数投票聚合，云端定期平均模型，并采用下行量化广播。
- 实验或效果：在异构数据下，HierSignSGD通信成本低，精度接近或优于全精度SGD，且对下行稀疏化鲁棒。

## 摘要（原文）

> Hierarchical federated learning (HFL) has emerged as a key architecture for large-scale wireless and Internet of Things systems, where devices communicate with nearby edge servers before reaching the cloud. In these environments, uplink bandwidth and latency impose strict communication limits, thereby making aggressive gradient compression essential. One-bit methods such as sign-based stochastic gradient descent (SignSGD) offer an attractive solution in flat federated settings, but existing theory and algorithms do not naturally extend to hierarchical settings. In particular, the interaction between majority-vote aggregation at the edge layer and model aggregation at the cloud layer, and its impact on end-to-end performance, remains unknown. To bridge this gap, we propose a highly communication-efficient sign-based HFL framework and develop its corresponding formulation for nonconvex learning, where devices send only signed stochastic gradients, edge servers combine them through majority-vote, and the cloud periodically averages the obtained edge models, while utilizing downlink quantization to broadcast the global model. We introduce the resulting scalable HFL algorithm, HierSignSGD, and provide the convergence analysis for SignSGD in a hierarchical setting. Our core technical contribution is a characterization of how biased sign compression, two-level aggregation intervals, and inter-cluster heterogeneity collectively affect convergence. Numerical experiments under homogeneous and heterogeneous data splits show that HierSignSGD, despite employing extreme compression, achieves accuracy comparable to or better than full-precision stochastic gradient descent while reducing communication cost in the process, and remains robust under aggressive downlink sparsification.

