---
layout: default
title: ArcAligner: Adaptive Recursive Aligner for Compressed Context Embeddings in RAG
---

# ArcAligner: Adaptive Recursive Aligner for Compressed Context Embeddings in RAG
**arXiv**：[2601.05038v1](https://arxiv.org/abs/2601.05038) · [PDF](https://arxiv.org/pdf/2601.05038.pdf)  
**作者**：Jianbo Li, Yi Jiang, Sendong Zhao, Bairui Hu, Haochun Wang, Bing Qin  

**一句话要点**：提出ArcAligner自适应递归对齐器，以增强RAG中压缩上下文嵌入的利用效率。

**关键词**：检索增强生成, 上下文压缩, 自适应门控, 轻量级模块, 知识密集型问答

## 3 点简述
- 核心问题：RAG中上下文压缩导致LLM理解困难，影响生成准确性。
- 方法要点：集成轻量级自适应门控模块，动态处理复杂信息，保持系统高效。
- 实验或效果：在知识密集型QA基准上优于压缩基线，尤其在多跳和长尾场景。

## 摘要（原文）

> Retrieval-Augmented Generation (RAG) helps LLMs stay accurate, but feeding long documents into a prompt makes the model slow and expensive. This has motivated context compression, ranging from token pruning and summarization to embedding-based compression. While researchers have tried ''compressing'' these documents into smaller summaries or mathematical embeddings, there is a catch: the more you compress the data, the more the LLM struggles to understand it. To address this challenge, we propose ArcAligner (Adaptive recursive context *Aligner*), a lightweight module integrated into the language model layers to help the model better utilize highly compressed context representations for downstream generation. It uses an adaptive ''gating'' system that only adds extra processing power when the information is complex, keeping the system fast. Across knowledge-intensive QA benchmarks, ArcAligner consistently beats compression baselines at comparable compression rates, especially on multi-hop and long-tail settings. The source code is publicly available.

