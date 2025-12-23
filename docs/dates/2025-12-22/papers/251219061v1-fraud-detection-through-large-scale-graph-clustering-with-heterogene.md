---
layout: default
title: Fraud Detection Through Large-Scale Graph Clustering with Heterogeneous Link Transformation
---

# Fraud Detection Through Large-Scale Graph Clustering with Heterogeneous Link Transformation
**arXiv**：[2512.19061v1](https://arxiv.org/abs/2512.19061) · [PDF](https://arxiv.org/pdf/2512.19061.pdf)  
**作者**：Chi Liu  

**一句话要点**：提出基于异构链接转换的大规模图聚类框架以解决协同欺诈检测问题

**关键词**：欺诈检测, 图聚类, 异构链接, 网络嵌入, 密度聚类

## 3 点简述
- 核心问题：协同欺诈形成复杂网络结构，传统方法覆盖有限或聚类效果差
- 方法要点：区分硬链接和软链接，通过图转换合并硬链接组件并重建加权软链接图
- 实验或效果：在真实支付数据上实现节点大幅减少、检测覆盖翻倍并保持高精度

## 摘要（原文）

> Collaborative fraud, where multiple fraudulent accounts coordinate to exploit online payment systems, poses significant challenges due to the formation of complex network structures. Traditional detection methods that rely solely on high-confidence identity links suffer from limited coverage, while approaches using all available linkages often result in fragmented graphs with reduced clustering effectiveness. In this paper, we propose a novel graph-based fraud detection framework that addresses the challenge of large-scale heterogeneous graph clustering through a principled link transformation approach. Our method distinguishes between \emph{hard links} (high-confidence identity relationships such as phone numbers, credit cards, and national IDs) and \emph{soft links} (behavioral associations including device fingerprints, cookies, and IP addresses). We introduce a graph transformation technique that first identifies connected components via hard links, merges them into super-nodes, and then reconstructs a weighted soft-link graph amenable to efficient embedding and clustering. The transformed graph is processed using LINE (Large-scale Information Network Embedding) for representation learning, followed by HDBSCAN (Hierarchical Density-Based Spatial Clustering of Applications with Noise) for density-based cluster discovery. Experiments on a real-world payment platform dataset demonstrate that our approach achieves significant graph size reduction (from 25 million to 7.7 million nodes), doubles the detection coverage compared to hard-link-only baselines, and maintains high precision across identified fraud clusters. Our framework provides a scalable and practical solution for industrial-scale fraud detection systems.

