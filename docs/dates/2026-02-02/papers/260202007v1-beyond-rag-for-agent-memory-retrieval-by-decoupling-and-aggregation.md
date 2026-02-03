---
layout: default
title: Beyond RAG for Agent Memory: Retrieval by Decoupling and Aggregation
---

# Beyond RAG for Agent Memory: Retrieval by Decoupling and Aggregation
**arXiv**：[2602.02007v1](https://arxiv.org/abs/2602.02007) · [PDF](https://arxiv.org/pdf/2602.02007.pdf)  
**作者**：Zhanghao Hu, Qinglin Zhu, Hanqi Yan, Yulan He, Lin Gui  

**一句话要点**：提出xMemory以解决智能体记忆检索中的冗余和依赖缺失问题

**关键词**：智能体记忆, 检索增强生成, 语义解耦, 层次检索, 记忆管理

## 3 点简述
- 核心问题：标准RAG在智能体记忆场景下因检索冗余和依赖缺失导致推理错误
- 方法要点：通过解耦-聚合构建语义层次结构，指导记忆分割与合并以驱动检索
- 实验或效果：在LoCoMo和PerLTQA数据集上提升答案质量和令牌效率

## 摘要（原文）

> Agent memory systems often adopt the standard Retrieval-Augmented Generation (RAG) pipeline, yet its underlying assumptions differ in this setting. RAG targets large, heterogeneous corpora where retrieved passages are diverse, whereas agent memory is a bounded, coherent dialogue stream with highly correlated spans that are often duplicates. Under this shift, fixed top-$k$ similarity retrieval tends to return redundant context, and post-hoc pruning can delete temporally linked prerequisites needed for correct reasoning. We argue retrieval should move beyond similarity matching and instead operate over latent components, following decoupling to aggregation: disentangle memories into semantic components, organise them into a hierarchy, and use this structure to drive retrieval. We propose xMemory, which builds a hierarchy of intact units and maintains a searchable yet faithful high-level node organisation via a sparsity--semantics objective that guides memory split and merge. At inference, xMemory retrieves top-down, selecting a compact, diverse set of themes and semantics for multi-fact queries, and expanding to episodes and raw messages only when it reduces the reader's uncertainty. Experiments on LoCoMo and PerLTQA across the three latest LLMs show consistent gains in answer quality and token efficiency.

