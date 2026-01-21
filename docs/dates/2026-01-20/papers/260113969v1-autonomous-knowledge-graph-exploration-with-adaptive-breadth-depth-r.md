---
layout: default
title: Autonomous Knowledge Graph Exploration with Adaptive Breadth-Depth Retrieval
---

# Autonomous Knowledge Graph Exploration with Adaptive Breadth-Depth Retrieval
**arXiv**：[2601.13969v1](https://arxiv.org/abs/2601.13969) · [PDF](https://arxiv.org/pdf/2601.13969.pdf)  
**作者**：Joaquín Polonuer, Lucas Vittor, Iñaki Arango, Ayush Noori, David A. Clifton, Luciano Del Corro, Marinka Zitnik  

**一句话要点**：提出自适应知识图谱检索器ARK，通过全局搜索与邻域探索平衡广度与深度检索。

**关键词**：知识图谱检索, 自适应检索, 多跳遍历, 工具使用, 蒸馏训练, 无训练方法

## 3 点简述
- 核心问题：知识图谱检索需平衡广度搜索与多跳遍历，现有方法易受种子节点选择限制。
- 方法要点：ARK使用两操作工具集，自适应切换全局搜索和邻域探索，无需训练或预设跳数。
- 实验或效果：在STaRK基准上，ARK显著提升Hit@1和MRR，并通过蒸馏提升8B模型性能。

## 摘要（原文）

> Retrieving evidence for language model queries from knowledge graphs requires balancing broad search across the graph with multi-hop traversal to follow relational links. Similarity-based retrievers provide coverage but remain shallow, whereas traversal-based methods rely on selecting seed nodes to start exploration, which can fail when queries span multiple entities and relations. We introduce ARK: Adaptive Retriever of Knowledge, an agentic KG retriever that gives a language model control over this breadth-depth tradeoff using a two-operation toolset: global lexical search over node descriptors and one-hop neighborhood exploration that composes into multi-hop traversal. ARK alternates between breadth-oriented discovery and depth-oriented expansion without depending on a fragile seed selection, a pre-set hop depth, or requiring retrieval training. ARK adapts tool use to queries, using global search for language-heavy queries and neighborhood exploration for relation-heavy queries. On STaRK, ARK reaches 59.1% average Hit@1 and 67.4 average MRR, improving average Hit@1 by up to 31.4% and average MRR by up to 28.0% over retrieval-based and agentic training-free methods. Finally, we distill ARK's tool-use trajectories from a large teacher into an 8B model via label-free imitation, improving Hit@1 by +7.0, +26.6, and +13.5 absolute points over the base 8B model on AMAZON, MAG, and PRIME datasets, respectively, while retaining up to 98.5% of the teacher's Hit@1 rate.

