---
layout: default
title: Reasoning in Trees: Improving Retrieval-Augmented Generation for Multi-Hop Question Answering
---

# Reasoning in Trees: Improving Retrieval-Augmented Generation for Multi-Hop Question Answering
**arXiv**：[2601.11255v1](https://arxiv.org/abs/2601.11255) · [PDF](https://arxiv.org/pdf/2601.11255.pdf)  
**作者**：Yuling Shi, Maolin Sun, Zijun Liu, Mo Yang, Yixiong Fang, Tianran Sun, Xiaodong Gu  

**一句话要点**：提出RT-RAG框架，通过推理树分解与遍历策略解决多跳问答中的查询分解不准确和错误传播问题。

**关键词**：检索增强生成, 多跳问答, 推理树, 查询分解, 错误传播, 迭代检索

## 3 点简述
- 核心问题：当前迭代方法在多跳问答中因查询分解不准确和错误传播导致推理连贯性差。
- 方法要点：RT-RAG通过结构化实体分析和共识树选择构建推理树，采用自底向上遍历进行查询重写与精炼。
- 实验或效果：在实验中，RT-RAG在F1和EM指标上分别超越现有方法7.0%和6.0%。

## 摘要（原文）

> Retrieval-Augmented Generation (RAG) has demonstrated significant effectiveness in enhancing large language models (LLMs) for complex multi-hop question answering (QA). For multi-hop QA tasks, current iterative approaches predominantly rely on LLMs to self-guide and plan multi-step exploration paths during retrieval, leading to substantial challenges in maintaining reasoning coherence across steps from inaccurate query decomposition and error propagation. To address these issues, we introduce Reasoning Tree Guided RAG (RT-RAG), a novel hierarchical framework for complex multi-hop QA. RT-RAG systematically decomposes multi-hop questions into explicit reasoning trees, minimizing inaccurate decomposition through structured entity analysis and consensus-based tree selection that clearly separates core queries, known entities, and unknown entities. Subsequently, a bottom-up traversal strategy employs iterative query rewriting and refinement to collect high-quality evidence, thereby mitigating error propagation. Comprehensive experiments show that RT-RAG substantially outperforms state-of-the-art methods by 7.0% F1 and 6.0% EM, demonstrating the effectiveness of RT-RAG in complex multi-hop QA.

