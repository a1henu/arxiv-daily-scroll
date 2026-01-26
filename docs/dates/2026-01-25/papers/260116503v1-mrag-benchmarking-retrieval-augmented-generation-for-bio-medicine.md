---
layout: default
title: MRAG: Benchmarking Retrieval-Augmented Generation for Bio-medicine
---

# MRAG: Benchmarking Retrieval-Augmented Generation for Bio-medicine
**arXiv**：[2601.16503v1](https://arxiv.org/abs/2601.16503) · [PDF](https://arxiv.org/pdf/2601.16503.pdf)  
**作者**：Wei Zhu  

**一句话要点**：提出MRAG基准以评估生物医学领域的检索增强生成系统

**关键词**：检索增强生成, 生物医学基准, 多语言评估, 工具包开发, 可靠性提升

## 3 点简述
- 核心问题：缺乏医学领域RAG的全面评估基准
- 方法要点：构建涵盖中英文任务的MRAG基准和工具包
- 实验或效果：RAG提升可靠性，但长问题可读性略降

## 摘要（原文）

> While Retrieval-Augmented Generation (RAG) has been swiftly adopted in scientific and clinical QA systems, a comprehensive evaluation benchmark in the medical domain is lacking. To address this gap, we introduce the Medical Retrieval-Augmented Generation (MRAG) benchmark, covering various tasks in English and Chinese languages, and building a corpus with Wikipedia and Pubmed. Additionally, we develop the MRAG-Toolkit, facilitating systematic exploration of different RAG components. Our experiments reveal that: (a) RAG enhances LLM reliability across MRAG tasks. (b) the performance of RAG systems is influenced by retrieval approaches, model sizes, and prompting strategies. (c) While RAG improves usefulness and reasoning quality, LLM responses may become slightly less readable for long-form questions. We will release the MRAG-Bench's dataset and toolkit with CCBY-4.0 license upon acceptance, to facilitate applications from both academia and industry.

