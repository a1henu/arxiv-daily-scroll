---
layout: default
title: Bridging OLAP and RAG: A Multidimensional Approach to the Design of Corpus Partitioning
---

# Bridging OLAP and RAG: A Multidimensional Approach to the Design of Corpus Partitioning
**arXiv**：[2601.03748v1](https://arxiv.org/abs/2601.03748) · [PDF](https://arxiv.org/pdf/2601.03748.pdf)  
**作者**：Dario Maio, Stefano Rizzi  

**一句话要点**：提出维度事实模型以指导大规模RAG系统的多维分区设计

**关键词**：检索增强生成, 多维分区, 维度事实模型, 可解释检索, 大规模文档检索, OLAP建模

## 3 点简述
- 核心问题：当前RAG系统依赖相似性驱动分区，缺乏概念化分区设计，影响可解释性和可控性。
- 方法要点：结合语义聚类和多维分区，引入维度事实模型作为概念框架，支持分层路由和回退策略。
- 实验或效果：未知，本文为立场论文，旨在激发关于可扩展、可解释检索策略的进一步研究。

## 摘要（原文）

> Retrieval-Augmented Generation (RAG) systems are increasingly deployed on large-scale document collections, often comprising millions of documents and tens of millions of text chunks. In industrial-scale retrieval platforms, scalability is typically addressed through horizontal sharding and a combination of Approximate Nearest-Neighbor search, hybrid indexing, and optimized metadata filtering. Although effective from an efficiency perspective, these mechanisms rely on bottom-up, similarity-driven organization and lack a conceptual rationale for corpus partitioning. In this paper, we claim that the design of large-scale RAG systems may benefit from the combination of two orthogonal strategies: semantic clustering, which optimizes locality in embedding space, and multidimensional partitioning, which governs where retrieval should occur based on conceptual dimensions such as time and organizational context. Although such dimensions are already implicitly present in current systems, they are used in an ad hoc and poorly structured manner. We propose the Dimensional Fact Model (DFM) as a conceptual framework to guide the design of multidimensional partitions for RAG corpora. The DFM provides a principled way to reason about facts, dimensions, hierarchies, and granularity in retrieval-oriented settings. This framework naturally supports hierarchical routing and controlled fallback strategies, ensuring that retrieval remains robust even in the presence of incomplete metadata, while transforming the search process from a 'black-box' similarity matching into a governable and deterministic workflow. This work is intended as a position paper; its goal is to bridge the gap between OLAP-style multidimensional modeling and modern RAG architectures, and to stimulate further research on principled, explainable, and governable retrieval strategies at scale.

