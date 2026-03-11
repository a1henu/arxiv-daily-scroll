---
layout: default
title: From Representation to Clusters: A Contrastive Learning Approach for Attributed Hypergraph Clustering
---

# From Representation to Clusters: A Contrastive Learning Approach for Attributed Hypergraph Clustering
**arXiv**：[2603.09370v1](https://arxiv.org/abs/2603.09370) · [PDF](https://arxiv.org/pdf/2603.09370.pdf)  
**作者**：Li Ni, Shuaikang Zeng, Lin Mu, Longlong Lin  

**一句话要点**：提出CAHC方法以解决属性超图聚类中对比学习缺乏直接聚类监督的问题

**关键词**：属性超图聚类, 对比学习, 端到端学习, 节点嵌入, 聚类监督

## 3 点简述
- 核心问题：现有对比学习方法先学节点嵌入再聚类，缺乏直接聚类监督，可能引入无关信息
- 方法要点：CAHC通过节点级和超边级对比学习生成嵌入，并联合嵌入与聚类优化，实现端到端聚类
- 实验或效果：在八个数据集上实验显示，CAHC优于基线方法

## 摘要（原文）

> Contrastive learning has demonstrated strong performance in attributed hypergraph clustering. Typically, existing methods based on contrastive learning first learn node embeddings and then apply clustering algorithms, such as k-means, to these embeddings to obtain the clustering results.However, these methods lack direct clustering supervision, risking the inclusion of clustering-irrelevant information in the learned graph.To this end, we propose a Contrastive learning approach for Attributed Hypergraph Clustering (CAHC), an end-to-end method that simultaneously learns node embeddings and obtains clustering results. CAHC consists of two main steps: representation learning and cluster assignment learning. The former employs a novel contrastive learning approach that incorporates both node-level and hyperedge-level objectives to generate node embeddings.The latter joint embedding and clustering optimization to refine these embeddings by clustering-oriented guidance and obtains clustering results simultaneously.Extensive experimental results demonstrate that CAHC outperforms baselines on eight datasets.

