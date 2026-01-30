---
layout: default
title: Generative Recall, Dense Reranking: Learning Multi-View Semantic IDs for Efficient Text-to-Video Retrieval
---

# Generative Recall, Dense Reranking: Learning Multi-View Semantic IDs for Efficient Text-to-Video Retrieval
**arXiv**：[2601.21193v1](https://arxiv.org/abs/2601.21193) · [PDF](https://arxiv.org/pdf/2601.21193.pdf)  
**作者**：Zecheng Zhao, Zhi Chen, Zi Huang, Shazia Sadiq, Tong Chen  

**一句话要点**：提出GRDR方法，通过多视图语义ID提升文本到视频检索的召回质量与效率。

**关键词**：文本到视频检索, 生成式检索, 多视图语义ID, 两阶段检索, 高效检索

## 3 点简述
- 核心问题：生成式检索作为召回模型存在语义模糊和跨模态对齐不足，影响两阶段检索性能。
- 方法要点：设计查询引导的多视图分词器，为视频分配多个语义ID，并联合训练以桥接文本与视频语义。
- 实验或效果：在基准测试中匹配密集检索器精度，索引存储减少一个数量级，全库检索加速达300倍。

## 摘要（原文）

> Text-to-Video Retrieval (TVR) is essential in video platforms. Dense retrieval with dual-modality encoders leads in accuracy, but its computation and storage scale poorly with corpus size. Thus, real-time large-scale applications adopt two-stage retrieval, where a fast recall model gathers a small candidate pool, which is reranked by an advanced dense retriever. Due to hugely reduced candidates, the reranking model can use any off-the-shelf dense retriever without hurting efficiency, meaning the recall model bounds two-stage TVR performance. Recently, generative retrieval (GR) replaces dense video embeddings with discrete semantic IDs and retrieves by decoding text queries into ID tokens. GR offers near-constant inference and storage complexity, and its semantic IDs capture high-level video features via quantization, making it ideal for quickly eliminating irrelevant candidates during recall. However, as a recall model in two-stage TVR, GR suffers from (i) semantic ambiguity, where each video satisfies diverse queries but is forced into one semantic ID; and (ii) cross-modal misalignment, as semantic IDs are solely derived from visual features without text supervision. We propose Generative Recall and Dense Reranking (GRDR), designing a novel GR method to uplift recalled candidate quality. GRDR assigns multiple semantic IDs to each video using a query-guided multi-view tokenizer exposing diverse semantic access paths, and jointly trains the tokenizer and generative retriever via a shared codebook to cast semantic IDs as the semantic bridge between texts and videos. At inference, trie-constrained decoding generates a compact candidate set reranked by a dense model for fine-grained matching. Experiments on TVR benchmarks show GRDR matches strong dense retrievers in accuracy while reducing index storage by an order of magnitude and accelerating up to 300$\times$ in full-corpus retrieval.

