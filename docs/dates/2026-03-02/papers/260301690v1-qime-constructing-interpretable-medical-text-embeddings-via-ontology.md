---
layout: default
title: QIME: Constructing Interpretable Medical Text Embeddings via Ontology-Grounded Questions
---

# QIME: Constructing Interpretable Medical Text Embeddings via Ontology-Grounded Questions
**arXiv**：[2603.01690v1](https://arxiv.org/abs/2603.01690) · [PDF](https://arxiv.org/pdf/2603.01690.pdf)  
**作者**：Yixuan Tang, Zhenghong Lin, Yandong Sun, Anthony K. H. Tung  

**一句话要点**：提出QIME框架，通过本体基础问题构建可解释的医学文本嵌入，以增强临床决策支持。

**关键词**：医学文本嵌入, 可解释性, 本体基础, 临床决策支持, 免训练嵌入

## 3 点简述
- 核心问题：现有医学文本嵌入方法缺乏可解释性，影响临床决策应用。
- 方法要点：基于本体概念签名生成原子性问题，每个维度对应临床是/否问题，支持免训练嵌入构建。
- 实验或效果：在生物医学语义相似性、聚类和检索基准上超越先前方法，接近黑盒编码器性能。

## 摘要（原文）

> While dense biomedical embeddings achieve strong performance, their black-box nature limits their utility in clinical decision-making. Recent question-based interpretable embeddings represent text as binary answers to natural-language questions, but these approaches often rely on heuristic or surface-level contrastive signals and overlook specialized domain knowledge. We propose QIME, an ontology-grounded framework for constructing interpretable medical text embeddings in which each dimension corresponds to a clinically meaningful yes/no question. By conditioning on cluster-specific medical concept signatures, QIME generates semantically atomic questions that capture fine-grained distinctions in biomedical text. Furthermore, QIME supports a training-free embedding construction strategy that eliminates per-question classifier training while further improving performance. Experiments across biomedical semantic similarity, clustering, and retrieval benchmarks show that QIME consistently outperforms prior interpretable embedding methods and substantially narrows the gap to strong black-box biomedical encoders, while providing concise and clinically informative explanations.

