---
layout: default
title: SentGraph: Hierarchical Sentence Graph for Multi-hop Retrieval-Augmented Question Answering
---

# SentGraph: Hierarchical Sentence Graph for Multi-hop Retrieval-Augmented Question Answering
**arXiv**：[2601.03014v1](https://arxiv.org/abs/2601.03014) · [PDF](https://arxiv.org/pdf/2601.03014.pdf)  
**作者**：Junli Liang, Pengfei Zhou, Wangqiu Zhou, Wenjie Qing, Qi Zhao, Ziwen Wang, Qi Song, Xiangyang Li  

**一句话要点**：提出SentGraph，基于句子级图结构解决多跳问答中检索增强生成的证据链不完整问题。

**关键词**：多跳问答, 检索增强生成, 句子级图, 修辞结构理论, 证据链建模

## 3 点简述
- 核心问题：传统检索增强生成在多跳问答中因块级检索导致证据不相关、逻辑不连贯，影响推理准确性。
- 方法要点：离线构建分层句子图，利用修辞结构理论区分核心与卫星句子，并通过跨文档实体桥组织主题子图。
- 实验或效果：在四个多跳问答基准测试中验证有效性，证明句子级逻辑依赖建模对多跳推理的重要性。

## 摘要（原文）

> Traditional Retrieval-Augmented Generation (RAG) effectively supports single-hop question answering with large language models but faces significant limitations in multi-hop question answering tasks, which require combining evidence from multiple documents. Existing chunk-based retrieval often provides irrelevant and logically incoherent context, leading to incomplete evidence chains and incorrect reasoning during answer generation. To address these challenges, we propose SentGraph, a sentence-level graph-based RAG framework that explicitly models fine-grained logical relationships between sentences for multi-hop question answering. Specifically, we construct a hierarchical sentence graph offline by first adapting Rhetorical Structure Theory to distinguish nucleus and satellite sentences, and then organizing them into topic-level subgraphs with cross-document entity bridges. During online retrieval, SentGraph performs graph-guided evidence selection and path expansion to retrieve fine-grained sentence-level evidence. Extensive experiments on four multi-hop question answering benchmarks demonstrate the effectiveness of SentGraph, validating the importance of explicitly modeling sentence-level logical dependencies for multi-hop reasoning.

