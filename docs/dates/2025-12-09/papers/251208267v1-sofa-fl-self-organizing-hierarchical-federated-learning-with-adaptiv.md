---
layout: default
title: SOFA-FL: Self-Organizing Hierarchical Federated Learning with Adaptive Clustered Data Sharing
---

# SOFA-FL: Self-Organizing Hierarchical Federated Learning with Adaptive Clustered Data Sharing
**arXiv**：[2512.08267v1](https://arxiv.org/abs/2512.08267) · [PDF](https://arxiv.org/pdf/2512.08267.pdf)  
**作者**：Yi Ni, Xinkun Wang, Han Zhang  

**一句话要点**：提出SOFA-FL框架以解决联邦学习在动态环境中的数据异构性和网络拓扑僵化问题

**关键词**：联邦学习, 自组织网络, 数据异构性, 动态聚类, 自适应拓扑, 数据共享

## 3 点简述
- 核心问题：联邦学习在动态环境中面临数据异构性和固定网络拓扑的挑战
- 方法要点：通过动态聚类、自组织拓扑演化和自适应数据共享机制实现系统自适应
- 实验或效果：未知，但框架旨在增强客户端关系捕捉和个性化能力

## 摘要（原文）

> Federated Learning (FL) faces significant challenges in evolving environments, particularly regarding data heterogeneity and the rigidity of fixed network topologies. To address these issues, this paper proposes \textbf{SOFA-FL} (Self-Organizing Hierarchical Federated Learning with Adaptive Clustered Data Sharing), a novel framework that enables hierarchical federated systems to self-organize and adapt over time.
>   The framework is built upon three core mechanisms: (1) \textbf{Dynamic Multi-branch Agglomerative Clustering (DMAC)}, which constructs an initial efficient hierarchical structure; (2) \textbf{Self-organizing Hierarchical Adaptive Propagation and Evolution (SHAPE)}, which allows the system to dynamically restructure its topology through atomic operations -- grafting, pruning, consolidation, and purification -- to adapt to changes in data distribution; and (3) \textbf{Adaptive Clustered Data Sharing}, which mitigates data heterogeneity by enabling controlled partial data exchange between clients and cluster nodes.
>   By integrating these mechanisms, SOFA-FL effectively captures dynamic relationships among clients and enhances personalization capabilities without relying on predetermined cluster structures.

