---
layout: default
title: Community Concealment from Unsupervised Graph Learning-Based Clustering
---

# Community Concealment from Unsupervised Graph Learning-Based Clustering
**arXiv**：[2602.12250v1](https://arxiv.org/abs/2602.12250) · [PDF](https://arxiv.org/pdf/2602.12250.pdf)  
**作者**：Dalyapraz Manatova, Pablo Moriano, L. Jean Camp  

**一句话要点**：提出基于图扰动的方法以保护社区隐私，防止无监督图学习聚类暴露敏感群体。

**关键词**：图神经网络, 社区检测, 隐私保护, 图扰动, 无监督学习, 群体隐私

## 3 点简述
- 核心问题：图神经网络在社区检测中可能泄露敏感群体信息，引发群体级隐私风险。
- 方法要点：通过重连边和修改节点特征，降低社区边界连通性和特征相似性，以隐蔽目标社区。
- 实验或效果：在合成和真实网络图中，相比DICE方法，在相同扰动预算下实现中位数相对隐蔽提升约20-45%。

## 摘要（原文）

> Graph neural networks (GNNs) are designed to use attributed graphs to learn representations. Such representations are beneficial in the unsupervised learning of clusters and community detection. Nonetheless, such inference may reveal sensitive groups, clustered systems, or collective behaviors, raising concerns regarding group-level privacy. Community attribution in social and critical infrastructure networks, for example, can expose coordinated asset groups, operational hierarchies, and system dependencies that could be used for profiling or intelligence gathering. We study a defensive setting in which a data publisher (defender) seeks to conceal a community of interest while making limited, utility-aware changes in the network. Our analysis indicates that community concealment is strongly influenced by two quantifiable factors: connectivity at the community boundary and feature similarity between the protected community and adjacent communities. Informed by these findings, we present a perturbation strategy that rewires a set of selected edges and modifies node features to reduce the distinctiveness leveraged by GNN message passing. The proposed method outperforms DICE in our experiments on synthetic benchmarks and real network graphs under identical perturbation budgets. Overall, it achieves median relative concealment improvements of approximately 20-45% across the evaluated settings. These findings demonstrate a mitigation strategy against GNN-based community learning and highlight group-level privacy risks intrinsic to graph learning.

