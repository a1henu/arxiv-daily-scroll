---
layout: default
title: Leveraging Non-linear Dimension Reduction and Random Walk Co-occurrence for Node Embedding
---

# Leveraging Non-linear Dimension Reduction and Random Walk Co-occurrence for Node Embedding
**arXiv**：[2602.24069v1](https://arxiv.org/abs/2602.24069) · [PDF](https://arxiv.org/pdf/2602.24069.pdf)  
**作者**：Ryan DeWolfe  

**一句话要点**：提出COVE高维节点嵌入方法，结合非线性降维提升聚类和链接预测性能。

**关键词**：节点嵌入, 非线性降维, 随机游走, 社区检测, 链接预测

## 3 点简述
- 核心问题：传统节点嵌入受低维限制，影响表达能力和可解释性。
- 方法要点：基于随机游走共现相似性，构建高维嵌入COVE，并利用UMAP降维。
- 实验或效果：COVE结合UMAP和HDBSCAN在社区检测中表现与Louvain算法相当。

## 摘要（原文）

> Leveraging non-linear dimension reduction techniques, we remove the low dimension constraint from node embedding and propose COVE, an explainable high dimensional embedding that, when reduced to low dimension with UMAP, slightly increases performance on clustering and link prediction tasks. The embedding is inspired by neural embedding methods that use co-occurrence on a random walk as an indication of similarity, and is closely related to a diffusion process. Extending on recent community detection benchmarks, we find that a COVE UMAP HDBSCAN pipeline performs similarly to the popular Louvain algorithm.

