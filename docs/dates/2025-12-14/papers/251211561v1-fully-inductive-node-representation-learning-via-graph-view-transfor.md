---
layout: default
title: Fully Inductive Node Representation Learning via Graph View Transformation
---

# Fully Inductive Node Representation Learning via Graph View Transformation
**arXiv**：[2512.11561v1](https://arxiv.org/abs/2512.11561) · [PDF](https://arxiv.org/pdf/2512.11561.pdf)  
**作者**：Dooho Lee, Myeong Kong, Minho Jeong, Jaemin Yoo  

**一句话要点**：提出图视图变换以实现跨数据集的完全归纳节点表示学习

**关键词**：图神经网络, 完全归纳学习, 节点表示学习, 视图空间, 跨数据集泛化, 图视图变换

## 3 点简述
- 核心问题：图数据特征空间差异大，阻碍预训练模型跨数据集归纳推理
- 方法要点：引入视图空间，设计节点和特征置换等变的图视图变换作为构建块
- 实验或效果：在27个节点分类基准上，超越现有完全归纳模型和个体调优GNN

## 摘要（原文）

> Generalizing a pretrained model to unseen datasets without retraining is an essential step toward a foundation model. However, achieving such cross-dataset, fully inductive inference is difficult in graph-structured data where feature spaces vary widely in both dimensionality and semantics. Any transformation in the feature space can easily violate the inductive applicability to unseen datasets, strictly limiting the design space of a graph model. In this work, we introduce the view space, a novel representational axis in which arbitrary graphs can be naturally encoded in a unified manner. We then propose Graph View Transformation (GVT), a node- and feature-permutation-equivariant mapping in the view space. GVT serves as the building block for Recurrent GVT, a fully inductive model for node representation learning. Pretrained on OGBN-Arxiv and evaluated on 27 node-classification benchmarks, Recurrent GVT outperforms GraphAny, the prior fully inductive graph model, by +8.93% and surpasses 12 individually tuned GNNs by at least +3.30%. These results establish the view space as a principled and effective ground for fully inductive node representation learning.

