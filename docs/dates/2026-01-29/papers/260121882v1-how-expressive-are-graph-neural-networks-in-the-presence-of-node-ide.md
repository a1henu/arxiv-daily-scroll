---
layout: default
title: How Expressive Are Graph Neural Networks in the Presence of Node Identifiers?
---

# How Expressive Are Graph Neural Networks in the Presence of Node Identifiers?
**arXiv**：[2601.21882v1](https://arxiv.org/abs/2601.21882) · [PDF](https://arxiv.org/pdf/2601.21882.pdf)  
**作者**：Arie Soeteman, Michael Benedikt, Martin Grohe, Balder ten Cate  

**一句话要点**：研究图神经网络在节点标识符存在时的表达能力，基于键不变性概念分析其表达极限。

**关键词**：图神经网络, 表达能力, 节点标识符, 键不变性, 聚合操作

## 3 点简述
- 核心问题：图神经网络在具有唯一节点标识符的图上，能表达哪些仅依赖图结构的节点查询。
- 方法要点：引入键不变表达能力概念，类比有限模型理论中的顺序不变可定义性，分析不同聚合类型的GNN。
- 实验或效果：针对局部最大或求和聚合的GNN类，提供了表达能力的具体答案。

## 摘要（原文）

> Graph neural networks (GNNs) are a widely used class of machine learning models for graph-structured data, based on local aggregation over neighbors. GNNs have close connections to logic. In particular, their expressive power is linked to that of modal logics and bounded-variable logics with counting. In many practical scenarios, graphs processed by GNNs have node features that act as unique identifiers. In this work, we study how such identifiers affect the expressive power of GNNs. We initiate a study of the key-invariant expressive power of GNNs, inspired by the notion of order-invariant definability in finite model theory: which node queries that depend only on the underlying graph structure can GNNs express on graphs with unique node identifiers? We provide answers for various classes of GNNs with local max- or sum-aggregation.

