---
layout: default
title: Comprehensive Comparison of RAG Methods Across Multi-Domain Conversational QA
---

# Comprehensive Comparison of RAG Methods Across Multi-Domain Conversational QA
**arXiv**：[2602.09552v1](https://arxiv.org/abs/2602.09552) · [PDF](https://arxiv.org/pdf/2602.09552.pdf)  
**作者**：Klejda Alushi, Jan Strich, Chris Biemann, Martin Semmann  

**一句话要点**：系统比较多领域对话问答中检索增强生成方法，揭示简单策略优于复杂技术

**关键词**：检索增强生成, 多轮对话问答, 检索策略比较, 跨领域评估, 对话历史处理

## 3 点简述
- 核心问题：缺乏多轮对话问答中RAG方法的系统比较，对话历史等使检索复杂化
- 方法要点：在八个多领域数据集上统一评估基础与高级RAG方法，分析检索与生成质量
- 实验效果：重排序、混合BM25等简单方法稳定优于基础RAG，部分高级技术甚至低于无RAG基线

## 摘要（原文）

> Conversational question answering increasingly relies on retrieval-augmented generation (RAG) to ground large language models (LLMs) in external knowledge. Yet, most existing studies evaluate RAG methods in isolation and primarily focus on single-turn settings. This paper addresses the lack of a systematic comparison of RAG methods for multi-turn conversational QA, where dialogue history, coreference, and shifting user intent substantially complicate retrieval. We present a comprehensive empirical study of vanilla and advanced RAG methods across eight diverse conversational QA datasets spanning multiple domains. Using a unified experimental setup, we evaluate retrieval quality and answer generation using generator and retrieval metrics, and analyze how performance evolves across conversation turns. Our results show that robust yet straightforward methods, such as reranking, hybrid BM25, and HyDE, consistently outperform vanilla RAG. In contrast, several advanced techniques fail to yield gains and can even degrade performance below the No-RAG baseline. We further demonstrate that dataset characteristics and dialogue length strongly influence retrieval effectiveness, explaining why no single RAG strategy dominates across settings. Overall, our findings indicate that effective conversational RAG depends less on method complexity than on alignment between the retrieval strategy and the dataset structure. We publish the code used.\footnote{\href{https://github.com/Klejda-A/exp-rag.git}{GitHub Repository}}

