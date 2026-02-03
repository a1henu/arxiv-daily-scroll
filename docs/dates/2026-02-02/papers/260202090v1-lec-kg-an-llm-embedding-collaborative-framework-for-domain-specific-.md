---
layout: default
title: LEC-KG: An LLM-Embedding Collaborative Framework for Domain-Specific Knowledge Graph Construction -- A Case Study on SDGs
---

# LEC-KG: An LLM-Embedding Collaborative Framework for Domain-Specific Knowledge Graph Construction -- A Case Study on SDGs
**arXiv**：[2602.02090v1](https://arxiv.org/abs/2602.02090) · [PDF](https://arxiv.org/pdf/2602.02090.pdf)  
**作者**：Yikai Zeng, Yingchao Piao, Jianhui Li  

**一句话要点**：提出LEC-KG框架，通过LLM与知识图谱嵌入协同，从非结构化文本构建领域知识图谱。

**关键词**：知识图谱构建, 大语言模型, 知识图谱嵌入, 关系提取, 可持续目标, 迭代协同

## 3 点简述
- 核心问题：领域知识图谱构建面临实体异质性、长尾关系分布和模式缺失的挑战。
- 方法要点：采用分层关系提取、证据引导反馈和语义初始化，实现LLM与KGE的迭代协同。
- 实验或效果：在中文SDG报告上验证，显著提升低频关系提取效果，可靠生成已验证三元组。

## 摘要（原文）

> Constructing domain-specific knowledge graphs from unstructured text remains challenging due to heterogeneous entity mentions, long-tail relation distributions, and the absence of standardized schemas. We present LEC-KG, a bidirectional collaborative framework that integrates the semantic understanding of Large Language Models (LLMs) with the structural reasoning of Knowledge Graph Embeddings (KGE). Our approach features three key components: (1) hierarchical coarse-to-fine relation extraction that mitigates long-tail bias, (2) evidence-guided Chain-of-Thought feedback that grounds structural suggestions in source text, and (3) semantic initialization that enables structural validation for unseen entities. The two modules enhance each other iteratively-KGE provides structure-aware feedback to refine LLM extractions, while validated triples progressively improve KGE representations. We evaluate LEC-KG on Chinese Sustainable Development Goal (SDG) reports, demonstrating substantial improvements over LLM baselines, particularly on low-frequency relations. Through iterative refinement, our framework reliably transforms unstructured policy text into validated knowledge graph triples.

