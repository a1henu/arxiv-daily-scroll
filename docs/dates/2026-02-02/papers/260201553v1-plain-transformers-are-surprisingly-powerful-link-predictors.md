---
layout: default
title: Plain Transformers are Surprisingly Powerful Link Predictors
---

# Plain Transformers are Surprisingly Powerful Link Predictors
**arXiv**：[2602.01553v1](https://arxiv.org/abs/2602.01553) · [PDF](https://arxiv.org/pdf/2602.01553.pdf)  
**作者**：Quang Truong, Yu Song, Donald Loveland, Mingxuan Ju, Tong Zhao, Neil Shah, Jiliang Tang  

**一句话要点**：提出PENCIL，一种基于普通Transformer的链接预测方法，以解决图机器学习中复杂依赖建模的挑战。

**关键词**：链接预测, 图Transformer, 子图采样, 注意力机制, 可扩展性, 参数效率

## 3 点简述
- 核心问题：链接预测需捕获复杂拓扑依赖，现有方法如GNN依赖启发式或内存密集型嵌入，难以泛化或扩展到大规模图。
- 方法要点：PENCIL使用仅编码器的普通Transformer，通过注意力机制处理采样子图，替代手工先验，保持可扩展性和硬件效率。
- 实验或效果：PENCIL在实验中超越启发式GNN，参数效率高，即使无节点特征也能在多样基准上保持竞争力。

## 摘要（原文）

> Link prediction is a core challenge in graph machine learning, demanding models that capture rich and complex topological dependencies. While Graph Neural Networks (GNNs) are the standard solution, state-of-the-art pipelines often rely on explicit structural heuristics or memory-intensive node embeddings -- approaches that struggle to generalize or scale to massive graphs. Emerging Graph Transformers (GTs) offer a potential alternative but often incur significant overhead due to complex structural encodings, hindering their applications to large-scale link prediction. We challenge these sophisticated paradigms with PENCIL, an encoder-only plain Transformer that replaces hand-crafted priors with attention over sampled local subgraphs, retaining the scalability and hardware efficiency of standard Transformers. Through experimental and theoretical analysis, we show that PENCIL extracts richer structural signals than GNNs, implicitly generalizing a broad class of heuristics and subgraph-based expressivity. Empirically, PENCIL outperforms heuristic-informed GNNs and is far more parameter-efficient than ID-embedding--based alternatives, while remaining competitive across diverse benchmarks -- even without node features. Our results challenge the prevailing reliance on complex engineering techniques, demonstrating that simple design choices are potentially sufficient to achieve the same capabilities.

