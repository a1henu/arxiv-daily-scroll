---
layout: default
title: T-Retriever: Tree-based Hierarchical Retrieval Augmented Generation for Textual Graphs
---

# T-Retriever: Tree-based Hierarchical Retrieval Augmented Generation for Textual Graphs
**arXiv**：[2601.04945v1](https://arxiv.org/abs/2601.04945) · [PDF](https://arxiv.org/pdf/2601.04945.pdf)  
**作者**：Chunyu Wei, Huaiyu Qin, Siyuan He, Yunhai Wang, Yueguo Chen  

**一句话要点**：提出T-Retriever框架，通过树基层次检索增强生成解决图RAG中层次信息管理问题

**关键词**：检索增强生成, 图推理, 层次检索, 语义结构熵, 自适应压缩, 编码树

## 3 点简述
- 核心问题：现有图RAG方法在层次信息管理中面临压缩配额僵化和忽视语义内容的问题
- 方法要点：采用语义结构引导编码树，结合自适应压缩编码和语义结构熵进行全局优化
- 实验或效果：在多个图推理基准测试中显著优于现有RAG方法，提供更连贯和上下文相关的响应

## 摘要（原文）

> Retrieval-Augmented Generation (RAG) has significantly enhanced Large Language Models' ability to access external knowledge, yet current graph-based RAG approaches face two critical limitations in managing hierarchical information: they impose rigid layer-specific compression quotas that damage local graph structures, and they prioritize topological structure while neglecting semantic content. We introduce T-Retriever, a novel framework that reformulates attributed graph retrieval as tree-based retrieval using a semantic and structure-guided encoding tree. Our approach features two key innovations: (1) Adaptive Compression Encoding, which replaces artificial compression quotas with a global optimization strategy that preserves the graph's natural hierarchical organization, and (2) Semantic-Structural Entropy ($S^2$-Entropy), which jointly optimizes for both structural cohesion and semantic consistency when creating hierarchical partitions. Experiments across diverse graph reasoning benchmarks demonstrate that T-Retriever significantly outperforms state-of-the-art RAG methods, providing more coherent and contextually relevant responses to complex queries.

