---
layout: default
title: Community Concealment from Unsupervised Graph Learning-Based Clustering
---

# Community Concealment from Unsupervised Graph Learning-Based Clustering
**arXiv**：[2602.12250v1](https://arxiv.org/abs/2602.12250) · [PDF](https://arxiv.org/pdf/2602.12250.pdf)  
**作者**：Dalyapraz Manatova, Pablo Moriano, L. Jean Camp  

**一句话要点**：提出基于图神经网络扰动的社区隐藏方法，以保护群体隐私

**关键词**：图神经网络, 社区隐藏, 群体隐私, 图扰动, 无监督学习, 社区检测

## 3 点简述
- 研究图神经网络社区检测中的群体隐私风险，关注社区隐藏问题
- 分析社区边界连通性和特征相似性对隐藏效果的影响，设计边重连和节点特征修改策略
- 在合成和真实网络实验中，该方法在相同扰动预算下优于DICE，中位相对隐藏改进约20-45%

## 摘要（原文）

> Graph neural networks (GNNs) are designed to use attributed graphs to learn representations. Such representations are beneficial in the unsupervised learning of clusters and community detection. Nonetheless, such inference may reveal sensitive groups, clustered systems, or collective behaviors, raising concerns regarding group-level privacy. Community attribution in social and critical infrastructure networks, for example, can expose coordinated asset groups, operational hierarchies, and system dependencies that could be used for profiling or intelligence gathering. We study a defensive setting in which a data publisher (defender) seeks to conceal a community of interest while making limited, utility-aware changes in the network. Our analysis indicates that community concealment is strongly influenced by two quantifiable factors: connectivity at the community boundary and feature similarity between the protected community and adjacent communities. Informed by these findings, we present a perturbation strategy that rewires a set of selected edges and modifies node features to reduce the distinctiveness leveraged by GNN message passing. The proposed method outperforms DICE in our experiments on synthetic benchmarks and real network graphs under identical perturbation budgets. Overall, it achieves median relative concealment improvements of approximately 20-45% across the evaluated settings. These findings demonstrate a mitigation strategy against GNN-based community learning and highlight group-level privacy risks intrinsic to graph learning.

