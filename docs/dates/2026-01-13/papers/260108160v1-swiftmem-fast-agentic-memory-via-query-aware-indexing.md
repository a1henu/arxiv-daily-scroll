---
layout: default
title: SwiftMem: Fast Agentic Memory via Query-aware Indexing
---

# SwiftMem: Fast Agentic Memory via Query-aware Indexing
**arXiv**：[2601.08160v1](https://arxiv.org/abs/2601.08160) · [PDF](https://arxiv.org/pdf/2601.08160.pdf)  
**作者**：Anxin Tian, Yiming Li, Xing Li, Hui-Ling Zhen, Lei Chen, Xianzhi Yu, Zhenhua Dong, Mingxuan Yuan  

**一句话要点**：提出SwiftMem以解决代理记忆系统中检索延迟瓶颈，实现快速查询感知索引。

**关键词**：代理记忆系统, 查询感知索引, 次线性检索, 时间索引, 语义DAG-Tag索引, 嵌入-标签协同整合

## 3 点简述
- 核心问题：现有代理记忆系统采用暴力检索，导致存储增长时延迟严重，阻碍实时交互。
- 方法要点：通过时间和语义维度索引实现次线性检索，包括时间索引和语义DAG-Tag索引，并引入嵌入-标签协同整合机制优化存储。
- 实验或效果：在LoCoMo和LongMemEval基准测试中，搜索速度比先进基线快47倍，同时保持准确度。

## 摘要（原文）

> Agentic memory systems have become critical for enabling LLM agents to maintain long-term context and retrieve relevant information efficiently. However, existing memory frameworks suffer from a fundamental limitation: they perform exhaustive retrieval across the entire storage layer regardless of query characteristics. This brute-force approach creates severe latency bottlenecks as memory grows, hindering real-time agent interactions. We propose SwiftMem, a query-aware agentic memory system that achieves sub-linear retrieval through specialized indexing over temporal and semantic dimensions. Our temporal index enables logarithmic-time range queries for time-sensitive retrieval, while the semantic DAG-Tag index maps queries to relevant topics through hierarchical tag structures. To address memory fragmentation during growth, we introduce an embedding-tag co-consolidation mechanism that reorganizes storage based on semantic clusters to improve cache locality. Experiments on LoCoMo and LongMemEval benchmarks demonstrate that SwiftMem achieves 47$\times$ faster search compared to state-of-the-art baselines while maintaining competitive accuracy, enabling practical deployment of memory-augmented LLM agents.

