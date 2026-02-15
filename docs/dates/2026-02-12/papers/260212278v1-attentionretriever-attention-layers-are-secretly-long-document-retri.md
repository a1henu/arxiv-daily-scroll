---
layout: default
title: AttentionRetriever: Attention Layers are Secretly Long Document Retrievers
---

# AttentionRetriever: Attention Layers are Secretly Long Document Retrievers
**arXiv**：[2602.12278v1](https://arxiv.org/abs/2602.12278) · [PDF](https://arxiv.org/pdf/2602.12278.pdf)  
**作者**：David Jiahao Fu, Lam Thanh Do, Jiayu Li, Kevin Chen-Chuan Chang  

**一句话要点**：提出AttentionRetriever，利用注意力机制和基于实体的检索解决长文档检索中的上下文感知和范围确定问题。

**关键词**：长文档检索, 注意力机制, 实体检索, 上下文感知, 检索增强生成

## 3 点简述
- 核心问题：现有检索模型不适用于长文档，难以处理上下文感知、因果依赖和检索范围等挑战。
- 方法要点：结合注意力机制和实体检索，构建上下文感知嵌入并确定检索范围。
- 实验或效果：在长文档检索数据集上大幅超越现有模型，同时保持与密集检索模型相当的效率。

## 摘要（原文）

> Retrieval augmented generation (RAG) has been widely adopted to help Large Language Models (LLMs) to process tasks involving long documents. However, existing retrieval models are not designed for long document retrieval and fail to address several key challenges of long document retrieval, including context-awareness, causal dependence, and scope of retrieval. In this paper, we proposed AttentionRetriever, a novel long document retrieval model that leverages attention mechanism and entity-based retrieval to build context-aware embeddings for long document and determine the scope of retrieval. With extensive experiments, we found AttentionRetriever is able to outperform existing retrieval models on long document retrieval datasets by a large margin while remaining as efficient as dense retrieval models.

