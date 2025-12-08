---
layout: default
title: ArtistMus: A Globally Diverse, Artist-Centric Benchmark for Retrieval-Augmented Music Question Answering
---

# ArtistMus: A Globally Diverse, Artist-Centric Benchmark for Retrieval-Augmented Music Question Answering
**arXiv**：[2512.05430v1](https://arxiv.org/abs/2512.05430) · [PDF](https://arxiv.org/pdf/2512.05430.pdf)  
**作者**：Daeyong Kwon, SeungHeon Doh, Juhan Nam  

**一句话要点**：提出ArtistMus基准和MusWikiDB数据库，以解决音乐问答中检索增强生成评估不足的问题。

**关键词**：音乐问答, 检索增强生成, 艺术家元数据, 向量数据库, 基准评估, 音乐信息检索

## 3 点简述
- 核心问题：大语言模型在音乐推理中因预训练数据稀疏而受限，缺乏基于艺术家元数据的问答资源。
- 方法要点：构建包含144K维基页面的MusWikiDB向量数据库和500位艺术家的ArtistMus基准，支持检索增强生成评估。
- 实验或效果：检索增强生成显著提升事实准确性，开源模型改进达+56.8个百分点，并优于通用维基语料库。

## 摘要（原文）

> Recent advances in large language models (LLMs) have transformed open-domain question answering, yet their effectiveness in music-related reasoning remains limited due to sparse music knowledge in pretraining data. While music information retrieval and computational musicology have explored structured and multimodal understanding, few resources support factual and contextual music question answering (MQA) grounded in artist metadata or historical context. We introduce MusWikiDB, a vector database of 3.2M passages from 144K music-related Wikipedia pages, and ArtistMus, a benchmark of 1,000 questions on 500 diverse artists with metadata such as genre, debut year, and topic. These resources enable systematic evaluation of retrieval-augmented generation (RAG) for MQA. Experiments show that RAG markedly improves factual accuracy; open-source models gain up to +56.8 percentage points (for example, Qwen3 8B improves from 35.0 to 91.8), approaching proprietary model performance. RAG-style fine-tuning further boosts both factual recall and contextual reasoning, improving results on both in-domain and out-of-domain benchmarks. MusWikiDB also yields approximately 6 percentage points higher accuracy and 40% faster retrieval than a general-purpose Wikipedia corpus. We release MusWikiDB and ArtistMus to advance research in music information retrieval and domain-specific question answering, establishing a foundation for retrieval-augmented reasoning in culturally rich domains such as music.

