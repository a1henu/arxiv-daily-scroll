---
layout: default
title: Legal RAG Bench: an end-to-end benchmark for legal RAG
---

# Legal RAG Bench: an end-to-end benchmark for legal RAG
**arXiv**：[2603.01710v1](https://arxiv.org/abs/2603.01710) · [PDF](https://arxiv.org/pdf/2603.01710.pdf)  
**作者**：Abdur-Rahman Butler, Umar Butler  

**一句话要点**：提出Legal RAG Bench以评估法律RAG系统的端到端性能

**关键词**：法律RAG基准, 端到端评估, 检索增强生成, 错误分解框架, 嵌入模型评估

## 3 点简述
- 核心问题：缺乏评估法律RAG系统端到端性能的基准和方法
- 方法要点：基于维多利亚刑事指控书的4,876个段落和100个复杂问题构建基准，采用全因子设计和分层错误分解框架
- 实验或效果：评估嵌入模型和LLM，发现检索是性能主要驱动因素，Kanon 2 Embedder提升正确性17.5点

## 摘要（原文）

> We introduce Legal RAG Bench, a benchmark and evaluation methodology for assessing the end-to-end performance of legal RAG systems. As a benchmark, Legal RAG Bench consists of 4,876 passages from the Victorian Criminal Charge Book alongside 100 complex, hand-crafted questions demanding expert knowledge of criminal law and procedure. Both long-form answers and supporting passages are provided. As an evaluation methodology, Legal RAG Bench leverages a full factorial design and novel hierarchical error decomposition framework, enabling apples-to-apples comparisons of the contributions of retrieval and reasoning models in RAG. We evaluate three state-of-the-art embedding models (Isaacus' Kanon 2 Embedder, Google's Gemini Embedding 001, and OpenAI's Text Embedding 3 Large) and two frontier LLMs (Gemini 3.1 Pro and GPT-5.2), finding that information retrieval is the primary driver of legal RAG performance, with LLMs exerting a more moderate effect on correctness and groundedness. Kanon 2 Embedder, in particular, had the largest positive impact on performance, improving average correctness by 17.5 points, groundedness by 4.5 points, and retrieval accuracy by 34 points. We observe that many errors attributed to hallucinations in legal RAG systems are in fact triggered by retrieval failures, concluding that retrieval sets the ceiling for the performance of many modern legal RAG systems. We document why and how we built Legal RAG Bench alongside the results of our evaluations. We also openly release our code and data to assist with reproduction of our findings.

