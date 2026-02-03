---
layout: default
title: Breaking the Static Graph: Context-Aware Traversal for Robust Retrieval-Augmented Generation
---

# Breaking the Static Graph: Context-Aware Traversal for Robust Retrieval-Augmented Generation
**arXiv**：[2602.01965v1](https://arxiv.org/abs/2602.01965) · [PDF](https://arxiv.org/pdf/2602.01965.pdf)  
**作者**：Kwun Hang Lau, Fangyuan Zhang, Boyu Ruan, Yingli Zhou, Qintian Guo, Ruiyuan Zhang, Xiaofang Zhou  

**一句话要点**：提出CatRAG框架以解决检索增强生成中静态知识图谱导致的语义漂移问题

**关键词**：检索增强生成, 知识图谱, 随机游走, 多跳推理, 动态图结构, 语义漂移

## 3 点简述
- 核心问题：现有方法依赖静态知识图谱，忽略查询相关边权重，导致随机游走偏向高连接节点，阻碍完整证据链检索。
- 方法要点：CatRAG引入符号锚定、查询感知动态边权重和关键事实段落权重增强，动态调整图结构以引导随机游走。
- 实验或效果：在四个多跳基准测试中，CatRAG在推理完整性方面显著优于基线，有效提升证据路径的完整检索能力。

## 摘要（原文）

> Recent advances in Retrieval-Augmented Generation (RAG) have shifted from simple vector similarity to structure-aware approaches like HippoRAG, which leverage Knowledge Graphs (KGs) and Personalized PageRank (PPR) to capture multi-hop dependencies. However, these methods suffer from a "Static Graph Fallacy": they rely on fixed transition probabilities determined during indexing. This rigidity ignores the query-dependent nature of edge relevance, causing semantic drift where random walks are diverted into high-degree "hub" nodes before reaching critical downstream evidence. Consequently, models often achieve high partial recall but fail to retrieve the complete evidence chain required for multi-hop queries. To address this, we propose CatRAG, Context-Aware Traversal for robust RAG, a framework that builds on the HippoRAG 2 architecture and transforms the static KG into a query-adaptive navigation structure. We introduce a multi-faceted framework to steer the random walk: (1) Symbolic Anchoring, which injects weak entity constraints to regularize the random walk; (2) Query-Aware Dynamic Edge Weighting, which dynamically modulates graph structure, to prune irrelevant paths while amplifying those aligned with the query's intent; and (3) Key-Fact Passage Weight Enhancement, a cost-efficient bias that structurally anchors the random walk to likely evidence. Experiments across four multi-hop benchmarks demonstrate that CatRAG consistently outperforms state of the art baselines. Our analysis reveals that while standard Recall metrics show modest gains, CatRAG achieves substantial improvements in reasoning completeness, the capacity to recover the entire evidence path without gaps. These results reveal that our approach effectively bridges the gap between retrieving partial context and enabling fully grounded reasoning. Resources are available at https://github.com/kwunhang/CatRAG.

