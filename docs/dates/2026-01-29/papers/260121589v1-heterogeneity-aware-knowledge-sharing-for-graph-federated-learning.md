---
layout: default
title: Heterogeneity-Aware Knowledge Sharing for Graph Federated Learning
---

# Heterogeneity-Aware Knowledge Sharing for Graph Federated Learning
**arXiv**：[2601.21589v1](https://arxiv.org/abs/2601.21589) · [PDF](https://arxiv.org/pdf/2601.21589.pdf)  
**作者**：Wentao Yu, Sheng Wan, Shuo Chen, Bo Han, Chen Gong  

**一句话要点**：提出FedSSA方法以解决图联邦学习中的节点特征和结构异质性问题

**关键词**：图联邦学习, 异质性处理, 语义对齐, 结构对齐, 谱图神经网络, 知识共享

## 3 点简述
- 核心问题：图联邦学习面临节点特征和结构拓扑的异质性挑战，影响模型性能。
- 方法要点：通过语义和结构对齐，分别使用变分模型推断类分布和谱能量度量聚类，实现知识共享。
- 实验或效果：在多个同质和异质图数据集上，FedSSA优于11种先进方法，验证其有效性。

## 摘要（原文）

> Graph Federated Learning (GFL) enables distributed graph representation learning while protecting the privacy of graph data. However, GFL suffers from heterogeneity arising from diverse node features and structural topologies across multiple clients. To address both types of heterogeneity, we propose a novel graph Federated learning method via Semantic and Structural Alignment (FedSSA), which shares the knowledge of both node features and structural topologies. For node feature heterogeneity, we propose a novel variational model to infer class-wise node distributions, so that we can cluster clients based on inferred distributions and construct cluster-level representative distributions. We then minimize the divergence between local and cluster-level distributions to facilitate semantic knowledge sharing. For structural heterogeneity, we employ spectral Graph Neural Networks (GNNs) and propose a spectral energy measure to characterize structural information, so that we can cluster clients based on spectral energy and build cluster-level spectral GNNs. We then align the spectral characteristics of local spectral GNNs with those of cluster-level spectral GNNs to enable structural knowledge sharing. Experiments on six homophilic and five heterophilic graph datasets under both non-overlapping and overlapping partitioning settings demonstrate that FedSSA consistently outperforms eleven state-of-the-art methods.

