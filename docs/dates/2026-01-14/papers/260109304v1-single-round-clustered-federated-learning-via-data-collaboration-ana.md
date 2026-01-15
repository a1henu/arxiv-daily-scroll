---
layout: default
title: Single-Round Clustered Federated Learning via Data Collaboration Analysis for Non-IID Data
---

# Single-Round Clustered Federated Learning via Data Collaboration Analysis for Non-IID Data
**arXiv**：[2601.09304v1](https://arxiv.org/abs/2601.09304) · [PDF](https://arxiv.org/pdf/2601.09304.pdf)  
**作者**：Sota Sugawara, Yuji Kawamata, Akihiro Toyoda, Tomoru Nakayama, Yukihiko Okada  

**一句话要点**：提出基于数据协作的单轮聚类联邦学习框架，以解决非独立同分布数据下通信轮次受限问题。

**关键词**：聚类联邦学习, 非独立同分布数据, 单轮通信, 数据协作分析, 标签分布相似性, 层次聚类

## 3 点简述
- 核心问题：传统聚类联邦学习依赖多轮通信进行聚类估计和模型更新，在通信轮次受限时实用性不足。
- 方法要点：通过标签分布的总变差距离量化客户端相似性，使用层次聚类估计聚类，并通过数据协作分析完成聚类内学习。
- 实验或效果：在多个开放数据集上，该框架在单轮通信下达到与多轮基线相当的准确率，适用于通信受限场景。

## 摘要（原文）

> Federated Learning (FL) enables distributed learning across multiple clients without sharing raw data. When statistical heterogeneity across clients is severe, Clustered Federated Learning (CFL) can improve performance by grouping similar clients and training cluster-wise models. However, most CFL approaches rely on multiple communication rounds for cluster estimation and model updates, which limits their practicality under tight constraints on communication rounds. We propose Data Collaboration-based Clustered Federated Learning (DC-CFL), a single-round framework that completes both client clustering and cluster-wise learning, using only the information shared in DC analysis. DC-CFL quantifies inter-client similarity via total variation distance between label distributions, estimates clusters using hierarchical clustering, and performs cluster-wise learning via DC analysis. Experiments on multiple open datasets under representative non-IID conditions show that DC-CFL achieves accuracy comparable to multi-round baselines while requiring only one communication round. These results indicate that DC-CFL is a practical alternative for collaborative AI model development when multiple communication rounds are impractical.

