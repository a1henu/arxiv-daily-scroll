---
layout: default
title: Feature-Centric Unsupervised Node Representation Learning Without Homophily Assumption
---

# Feature-Centric Unsupervised Node Representation Learning Without Homophily Assumption
**arXiv**：[2512.15112v1](https://arxiv.org/abs/2512.15112) · [PDF](https://arxiv.org/pdf/2512.15112.pdf)  
**作者**：Sunwoo Kim, Soo Yong Lee, Kyungho Kim, Hyunjin Hwang, Jaemin Yoo, Kijung Shin  

**一句话要点**：提出FUEL以在无监督节点表示学习中自适应调整图卷积使用程度，适用于非同配图场景。

**关键词**：无监督节点表示学习, 图卷积自适应, 非同配图, 特征聚类, 嵌入优化, 下游任务性能

## 3 点简述
- 核心问题：图卷积过度依赖在同配性低图中可能导致节点嵌入相似度不当，影响表示质量。
- 方法要点：基于节点特征识别聚类作为类代理，通过增强类内相似性和类间可分性自适应学习图卷积使用程度。
- 实验或效果：在14个基准数据集上对比15种基线方法，FUEL在下游任务中实现最先进性能，适用于不同同配性水平图。

## 摘要（原文）

> Unsupervised node representation learning aims to obtain meaningful node embeddings without relying on node labels. To achieve this, graph convolution, which aggregates information from neighboring nodes, is commonly employed to encode node features and graph topology. However, excessive reliance on graph convolution can be suboptimal-especially in non-homophilic graphs-since it may yield unduly similar embeddings for nodes that differ in their features or topological properties. As a result, adjusting the degree of graph convolution usage has been actively explored in supervised learning settings, whereas such approaches remain underexplored in unsupervised scenarios. To tackle this, we propose FUEL, which adaptively learns the adequate degree of graph convolution usage by aiming to enhance intra-class similarity and inter-class separability in the embedding space. Since classes are unknown, FUEL leverages node features to identify node clusters and treats these clusters as proxies for classes. Through extensive experiments using 15 baseline methods and 14 benchmark datasets, we demonstrate the effectiveness of FUEL in downstream tasks, achieving state-of-the-art performance across graphs with diverse levels of homophily.

