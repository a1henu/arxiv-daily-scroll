---
layout: default
title: Automated Customization of LLMs for Enterprise Code Repositories Using Semantic Scopes
---

# Automated Customization of LLMs for Enterprise Code Repositories Using Semantic Scopes
**arXiv**：[2602.05780v1](https://arxiv.org/abs/2602.05780) · [PDF](https://arxiv.org/pdf/2602.05780.pdf)  
**作者**：Ulrich Finkler, Irene Manotas, Wei Zhang, Geert Janssen, Octavian Popescu, Shyam Ramji  

**一句话要点**：提出基于语义范围的自动化LLM定制方法，以提升企业私有代码库的代码补全性能。

**关键词**：代码补全, LLM定制, 语义范围, 检索增强生成, 微调, 企业代码库

## 3 点简述
- 核心问题：通用LLM难以生成与未见过私有代码库对齐的代码，影响开发效率。
- 方法要点：通过语义范围机制处理代码库数据，结合RAG和微调策略进行模型定制。
- 实验或效果：定制模型在私有库上表现优于更大规模未定制模型，提升代码精确度。

## 摘要（原文）

> Code completion (CC) is a task frequently used by developers when working in collaboration with LLM-based programming assistants. Despite the increased performance of LLMs on public benchmarks, out of the box LLMs still have a hard time generating code that aligns with a private code repository not previously seen by the model's training data. Customizing code LLMs to a private repository provides a way to improve the model performance. In this paper we present our approach for automated LLM customization based on semantic scopes in the code. We evaluate LLMs on real industry cases with two private enterprise code repositories with two customization strategies: Retrieval-Augmented Generation (RAG) and supervised Fine-Tuning (FT). Our mechanism for ingesting the repository's data and formulating the training data pairs with semantic scopes helps models to learn the underlying patterns specific to the repository, providing more precise code to developers and helping to boost their productivity. The code completions of moderately sized customized models can be significantly better than those of uncustomized models of much larger capacity. We also include an analysis of customization on two public benchmarks and present opportunities for future work.

