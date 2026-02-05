---
layout: default
title: Training A Foundation Model to Represent Graphs as Vectors
---

# Training A Foundation Model to Represent Graphs as Vectors
**arXiv**：[2602.04244v1](https://arxiv.org/abs/2602.04244) · [PDF](https://arxiv.org/pdf/2602.04244.pdf)  
**作者**：Qi Feng, Jicong Fan  

**一句话要点**：提出图基础模型，通过多图特征对齐和密度最大化均值对齐算法，实现图向量表示以支持下游任务。

**关键词**：图基础模型, 图向量表示, 多图特征对齐, 密度最大化均值对齐, 图神经网络, 少样本学习

## 3 点简述
- 核心问题：训练图基础模型，将任意图表示为向量，保留结构和语义信息，用于图分类和聚类等下游任务。
- 方法要点：采用多图特征对齐方法生成一致节点嵌入，结合密度最大化均值对齐算法增强特征一致性，并设计多层参考分布模块避免池化操作。
- 实验或效果：在少样本图分类和图聚类实验中，模型优于强基线，并提供理论泛化界支持有效性。

## 摘要（原文）

> This paper aims to train a graph foundation model that is able to represent any graph as a vector preserving structural and semantic information useful for downstream graph-level tasks such as graph classification and graph clustering. To learn the features of graphs from diverse domains while maintaining strong generalization ability to new domains, we propose a multi-graph-based feature alignment method, which constructs weighted graphs using the attributes of all nodes in each dataset and then generates consistent node embeddings. To enhance the consistency of the features from different datasets, we propose a density maximization mean alignment algorithm with guaranteed convergence. The original graphs and generated node embeddings are fed into a graph neural network to achieve discriminative graph representations in contrastive learning. More importantly, to enhance the information preservation from node-level representations to the graph-level representation, we construct a multi-layer reference distribution module without using any pooling operation. We also provide a theoretical generalization bound to support the effectiveness of the proposed model. The experimental results of few-shot graph classification and graph clustering show that our model outperforms strong baselines.

