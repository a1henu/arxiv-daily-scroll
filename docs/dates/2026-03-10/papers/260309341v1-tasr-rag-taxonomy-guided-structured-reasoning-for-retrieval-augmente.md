---
layout: default
title: TaSR-RAG: Taxonomy-guided Structured Reasoning for Retrieval-Augmented Generation
---

# TaSR-RAG: Taxonomy-guided Structured Reasoning for Retrieval-Augmented Generation
**arXiv**：[2603.09341v1](https://arxiv.org/abs/2603.09341) · [PDF](https://arxiv.org/pdf/2603.09341.pdf)  
**作者**：Jiashuo Sun, Yixuan Xie, Jimeng Shi, Shaowen Wang, Jiawei Han  

**一句话要点**：提出TaSR-RAG框架，通过分类引导的结构化推理解决检索增强生成中的多跳推理问题。

**关键词**：检索增强生成, 结构化推理, 多跳问答, 关系三元组, 分类引导, 证据选择

## 3 点简述
- 核心问题：传统RAG系统依赖非结构化检索和单步生成，导致冗余上下文、低信息密度和多跳推理脆弱。
- 方法要点：将查询和文档表示为关系三元组，使用轻量级分类约束实体语义，通过分解问题和逐步证据选择实现结构化推理。
- 实验或效果：在多个多跳问答基准上，性能优于基线方法达14%，提供更清晰的证据归因和忠实推理轨迹。

## 摘要（原文）

> Retrieval-Augmented Generation (RAG) helps large language models (LLMs) answer knowledge-intensive and time-sensitive questions by conditioning generation on external evidence. However, most RAG systems still retrieve unstructured chunks and rely on one-shot generation, which often yields redundant context, low information density, and brittle multi-hop reasoning. While structured RAG pipelines can improve grounding, they typically require costly and error-prone graph construction or impose rigid entity-centric structures that do not align with the query's reasoning chain.
>   We propose \textsc{TaSR-RAG}, a taxonomy-guided structured reasoning framework for evidence selection. We represent both queries and documents as relational triples, and constrain entity semantics with a lightweight two-level taxonomy to balance generalization and precision. Given a complex question, \textsc{TaSR-RAG} decomposes it into an ordered sequence of triple sub-queries with explicit latent variables, then performs step-wise evidence selection via hybrid triple matching that combines semantic similarity over raw triples with structural consistency over typed triples.
>   By maintaining an explicit entity binding table across steps, \textsc{TaSR-RAG} resolves intermediate variables and reduces entity conflation without explicit graph construction or exhaustive search. Experiments on multiple multi-hop question answering benchmarks show that \textsc{TaSR-RAG} consistently outperforms strong RAG and structured-RAG baselines by up to 14\%, while producing clearer evidence attribution and more faithful reasoning traces.

