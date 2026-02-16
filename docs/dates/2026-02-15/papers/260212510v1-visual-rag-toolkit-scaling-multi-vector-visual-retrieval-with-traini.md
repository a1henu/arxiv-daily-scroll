---
layout: default
title: Visual RAG Toolkit: Scaling Multi-Vector Visual Retrieval with Training-Free Pooling and Multi-Stage Search
---

# Visual RAG Toolkit: Scaling Multi-Vector Visual Retrieval with Training-Free Pooling and Multi-Stage Search
**arXiv**：[2602.12510v1](https://arxiv.org/abs/2602.12510) · [PDF](https://arxiv.org/pdf/2602.12510.pdf)  
**作者**：Ara Yeroyan  

**一句话要点**：提出Visual RAG Toolkit，通过无训练池化和多阶段检索扩展多向量视觉检索效率

**关键词**：多向量视觉检索, 无训练池化, 多阶段检索, 效率优化, 视觉RAG系统, 模型感知压缩

## 3 点简述
- 多向量视觉检索器（如ColPali）精度高但扩展性差，每页产生数千向量导致索引和搜索成本高。
- 采用无训练模型感知池化（如滑动窗口平均）压缩向量，结合多阶段检索减少比较次数，实现高效候选生成和重排序。
- 在ViDoRe v2基准上，两阶段检索保持NDCG和Recall@5/10精度，吞吐量提升约4倍，硬件需求降低。

## 摘要（原文）

> Multi-vector visual retrievers (e.g., ColPali-style late interaction models) deliver strong accuracy, but scale poorly because each page yields thousands of vectors, making indexing and search increasingly expensive. We present Visual RAG Toolkit, a practical system for scaling visual multi-vector retrieval with training-free, model-aware pooling and multi-stage retrieval. Motivated by Matryoshka Embeddings, our method performs static spatial pooling - including a lightweight sliding-window averaging variant - over patch embeddings to produce compact tile-level and global representations for fast candidate generation, followed by exact MaxSim reranking using full multi-vector embeddings.
>   Our design yields a quadratic reduction in vector-to-vector comparisons by reducing stored vectors per page from thousands to dozens, notably without requiring post-training, adapters, or distillation. Across experiments with interaction-style models such as ColPali and ColSmol-500M, we observe that over the limited ViDoRe v2 benchmark corpus 2-stage retrieval typically preserves NDCG and Recall @ 5/10 with minimal degradation, while substantially improving throughput (approximately 4x QPS); with sensitivity mainly at very large k. The toolkit additionally provides robust preprocessing - high resolution PDF to image conversion, optional margin/empty-region cropping and token hygiene (indexing only visual tokens) - and a reproducible evaluation pipeline, enabling rapid exploration of two-, three-, and cascaded retrieval variants. By emphasizing efficiency at common cutoffs (e.g., k <= 10), the toolkit lowers hardware barriers and makes state-of-the-art visual retrieval more accessible in practice.

