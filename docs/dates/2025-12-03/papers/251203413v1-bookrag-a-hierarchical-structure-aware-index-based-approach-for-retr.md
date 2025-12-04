---
layout: default
title: BookRAG: A Hierarchical Structure-aware Index-based Approach for Retrieval-Augmented Generation on Complex Documents
---

# BookRAG: A Hierarchical Structure-aware Index-based Approach for Retrieval-Augmented Generation on Complex Documents
**arXiv**：[2512.03413v1](https://arxiv.org/abs/2512.03413) · [PDF](https://arxiv.org/pdf/2512.03413.pdf)  
**作者**：Shu Wang, Yingli Zhou, Yixiang Fang  

**一句话要点**：提出BookRAG，一种基于层次结构感知索引的方法，以解决复杂文档问答任务中检索增强生成的性能问题。

**关键词**：检索增强生成, 层次结构感知, 复杂文档问答, 索引构建, 信息觅食理论, 实体关系图

## 3 点简述
- 核心问题：现有RAG方法忽视文档的层次结构，导致在书籍等复杂文档上问答性能不佳。
- 方法要点：构建BookIndex索引，提取文档层次树和实体关系图，并基于信息觅食理论设计代理查询方法。
- 实验或效果：在三个基准测试中实现最先进性能，显著提升检索召回率和问答准确性，同时保持高效性。

## 摘要（原文）

> As an effective method to boost the performance of Large Language Models (LLMs) on the question answering (QA) task, Retrieval-Augmented Generation (RAG), which queries highly relevant information from external complex documents, has attracted tremendous attention from both industry and academia. Existing RAG approaches often focus on general documents, and they overlook the fact that many real-world documents (such as books, booklets, handbooks, etc.) have a hierarchical structure, which organizes their content from different granularity levels, leading to poor performance for the QA task. To address these limitations, we introduce BookRAG, a novel RAG approach targeted for documents with a hierarchical structure, which exploits logical hierarchies and traces entity relations to query the highly relevant information. Specifically, we build a novel index structure, called BookIndex, by extracting a hierarchical tree from the document, which serves as the role of its table of contents, using a graph to capture the intricate relationships between entities, and mapping entities to tree nodes. Leveraging the BookIndex, we then propose an agent-based query method inspired by the Information Foraging Theory, which dynamically classifies queries and employs a tailored retrieval workflow. Extensive experiments on three widely adopted benchmarks demonstrate that BookRAG achieves state-of-the-art performance, significantly outperforming baselines in both retrieval recall and QA accuracy while maintaining competitive efficiency.

