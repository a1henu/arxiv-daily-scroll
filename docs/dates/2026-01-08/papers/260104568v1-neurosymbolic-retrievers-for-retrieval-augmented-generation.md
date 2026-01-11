---
layout: default
title: Neurosymbolic Retrievers for Retrieval-augmented Generation
---

# Neurosymbolic Retrievers for Retrieval-augmented Generation
**arXiv**：[2601.04568v1](https://arxiv.org/abs/2601.04568) · [PDF](https://arxiv.org/pdf/2601.04568.pdf)  
**作者**：Yash Saxena, Manas Gaur  

**一句话要点**：提出神经符号检索增强生成框架，以提升检索过程的可解释性和性能

**关键词**：检索增强生成, 神经符号系统, 知识图谱, 可解释性, 文档检索, 心理健康评估

## 3 点简述
- 核心问题：传统RAG系统内部推理不透明，影响可解释性和调试
- 方法要点：集成知识图谱的符号推理与神经检索，包括MAR、KG-Path和Process Knowledge-infused方法
- 实验或效果：初步实验在心理健康风险评估任务中显示透明度和性能提升

## 摘要（原文）

> Retrieval Augmented Generation (RAG) has made significant strides in overcoming key limitations of large language models, such as hallucination, lack of contextual grounding, and issues with transparency. However, traditional RAG systems consist of three interconnected neural components - the retriever, re-ranker, and generator - whose internal reasoning processes remain opaque. This lack of transparency complicates interpretability, hinders debugging efforts, and erodes trust, especially in high-stakes domains where clear decision-making is essential. To address these challenges, we introduce the concept of Neurosymbolic RAG, which integrates symbolic reasoning using a knowledge graph with neural retrieval techniques. This new framework aims to answer two primary questions: (a) Can retrievers provide a clear and interpretable basis for document selection? (b) Can symbolic knowledge enhance the clarity of the retrieval process? We propose three methods to improve this integration. First is MAR (Knowledge Modulation Aligned Retrieval) that employs modulation networks to refine query embeddings using interpretable symbolic features, thereby making document matching more explicit. Second, KG-Path RAG enhances queries by traversing knowledge graphs to improve overall retrieval quality and interpretability. Lastly, Process Knowledge-infused RAG utilizes domain-specific tools to reorder retrieved content based on validated workflows. Preliminary results from mental health risk assessment tasks indicate that this neurosymbolic approach enhances both transparency and overall performance

