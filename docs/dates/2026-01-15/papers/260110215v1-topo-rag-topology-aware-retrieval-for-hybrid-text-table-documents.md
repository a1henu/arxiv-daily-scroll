---
layout: default
title: Topo-RAG: Topology-aware retrieval for hybrid text-table documents
---

# Topo-RAG: Topology-aware retrieval for hybrid text-table documents
**arXiv**：[2601.10215v1](https://arxiv.org/abs/2601.10215) · [PDF](https://arxiv.org/pdf/2601.10215.pdf)  
**作者**：Alex Dantart, Marco Kóvacs-Navarro  

**一句话要点**：提出Topo-RAG框架以解决企业混合文档检索中线性化方法不足的问题

**关键词**：检索增强生成, 混合文档检索, 表格处理, 拓扑感知, 企业数据集

## 3 点简述
- 核心问题：现有RAG系统将多维表格线性化为文本，无法有效捕捉数据结构，导致检索性能不足。
- 方法要点：采用双架构，文本部分用密集检索器，表格部分用Cell-Aware Late Interaction机制保留空间关系。
- 实验或效果：在SEC-25数据集上，Topo-RAG相比标准线性化方法，混合查询的nDCG@10提升18.4%。

## 摘要（原文）

> In enterprise datasets, documents are rarely pure. They are not just text, nor just numbers; they are a complex amalgam of narrative and structure. Current Retrieval-Augmented Generation (RAG) systems have attempted to address this complexity with a blunt tool: linearization. We convert rich, multidimensional tables into simple Markdown-style text strings, hoping that an embedding model will capture the geometry of a spreadsheet in a single vector. But it has already been shown that this is mathematically insufficient.
>   This work presents Topo-RAG, a framework that challenges the assumption that "everything is text". We propose a dual architecture that respects the topology of the data: we route fluid narrative through traditional dense retrievers, while tabular structures are processed by a Cell-Aware Late Interaction mechanism, preserving their spatial relationships. Evaluated on SEC-25, a synthetic enterprise corpus that mimics real-world complexity, Topo-RAG demonstrates an 18.4% improvement in nDCG@10 on hybrid queries compared to standard linearization approaches. It's not just about searching better; it's about understanding the shape of information.

