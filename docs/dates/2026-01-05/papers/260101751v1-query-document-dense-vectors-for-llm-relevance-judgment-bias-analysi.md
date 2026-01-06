---
layout: default
title: Query-Document Dense Vectors for LLM Relevance Judgment Bias Analysis
---

# Query-Document Dense Vectors for LLM Relevance Judgment Bias Analysis
**arXiv**：[2601.01751v1](https://arxiv.org/abs/2601.01751) · [PDF](https://arxiv.org/pdf/2601.01751.pdf)  
**作者**：Samaneh Mohtadi, Gianluca Demartini  

**一句话要点**：提出基于查询-文档密集向量和聚类的框架，以分析LLM在信息检索评估中的系统性判断偏差。

**关键词**：信息检索评估, 大语言模型偏差分析, 查询-文档密集向量, 语义聚类, 相关性判断

## 3 点简述
- 核心问题：LLM作为相关性评估者时，是否存在系统性错误，而非仅平均性能差异。
- 方法要点：将查询-文档对嵌入联合语义空间，通过聚类分析揭示人类与LLM标签的分歧模式。
- 实验或效果：在TREC数据集上发现系统性分歧集中于特定语义簇，如定义寻求或模糊查询场景。

## 摘要（原文）

> Large Language Models (LLMs) have been used as relevance assessors for Information Retrieval (IR) evaluation collection creation due to reduced cost and increased scalability as compared to human assessors. While previous research has looked at the reliability of LLMs as compared to human assessors, in this work, we aim to understand if LLMs make systematic mistakes when judging relevance, rather than just understanding how good they are on average. To this aim, we propose a novel representational method for queries and documents that allows us to analyze relevance label distributions and compare LLM and human labels to identify patterns of disagreement and localize systematic areas of disagreement. We introduce a clustering-based framework that embeds query-document (Q-D) pairs into a joint semantic space, treating relevance as a relational property. Experiments on TREC Deep Learning 2019 and 2020 show that systematic disagreement between humans and LLMs is concentrated in specific semantic clusters rather than distributed randomly. Query-level analyses reveal recurring failures, most often in definition-seeking, policy-related, or ambiguous contexts. Queries with large variation in agreement across their clusters emerge as disagreement hotspots, where LLMs tend to under-recall relevant content or over-include irrelevant material. This framework links global diagnostics with localized clustering to uncover hidden weaknesses in LLM judgments, enabling bias-aware and more reliable IR evaluation.

