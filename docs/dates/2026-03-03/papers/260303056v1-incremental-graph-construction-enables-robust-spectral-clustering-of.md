---
layout: default
title: Incremental Graph Construction Enables Robust Spectral Clustering of Texts
---

# Incremental Graph Construction Enables Robust Spectral Clustering of Texts
**arXiv**：[2603.03056v1](https://arxiv.org/abs/2603.03056) · [PDF](https://arxiv.org/pdf/2603.03056.pdf)  
**作者**：Marko Pranjić, Boshko Koloski, Nada Lavrač, Senja Pollak, Marko Robnik-Šikonja  

**一句话要点**：提出增量图构建方法以解决文本谱聚类中邻域图不连通问题

**关键词**：谱聚类, 文本嵌入, 邻域图构建, 增量学习, 连通性保证, SentenceTransformer

## 3 点简述
- 核心问题：标准k-NN图在稀疏设置下易产生不连通组件，导致谱聚类退化。
- 方法要点：设计增量k-NN图构建，每个新节点连接至k个最近已插入节点，保证图连通性。
- 实验效果：在低k值下优于标准方法，高k值时性能相当，验证于六个文本嵌入数据集。

## 摘要（原文）

> Neighborhood graphs are a critical but often fragile step in spectral clustering of text embeddings. On realistic text datasets, standard $k$-NN graphs can contain many disconnected components at practical sparsity levels (small $k$), making spectral clustering degenerate and sensitive to hyperparameters. We introduce a simple incremental $k$-NN graph construction that preserves connectivity by design: each new node is linked to its $k$ nearest previously inserted nodes, which guarantees a connected graph for any $k$. We provide an inductive proof of connectedness and discuss implications for incremental updates when new documents arrive. We validate the approach on spectral clustering of SentenceTransformer embeddings using Laplacian eigenmaps across six clustering datasets from the Massive Text Embedding Benchmark.Compared to standard $k$-NN graphs, our method outperforms in the low-$k$ regime where disconnected components are prevalent, and matches standard $k$-NN at larger $k$.

