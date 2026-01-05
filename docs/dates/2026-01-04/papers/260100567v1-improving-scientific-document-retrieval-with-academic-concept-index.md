---
layout: default
title: Improving Scientific Document Retrieval with Academic Concept Index
---

# Improving Scientific Document Retrieval with Academic Concept Index
**arXiv**：[2601.00567v1](https://arxiv.org/abs/2601.00567) · [PDF](https://arxiv.org/pdf/2601.00567.pdf)  
**作者**：Jeyun Lee, Junhyoung Lee, Wonbin Kweon, Bowen Jin, Yu Zhang, Susik Yoon, Dongha Lee, Hwanjo Yu, Jiawei Han, Seongku Kang  

**一句话要点**：提出学术概念索引以改进科学文档检索，通过概念覆盖生成和上下文增强提升性能。

**关键词**：科学文档检索, 学术概念索引, 查询生成, 上下文增强, 大语言模型

## 3 点简述
- 核心问题：科学文档检索因领域特定标注稀缺和词汇不匹配而困难，现有方法忽视学术概念多样性。
- 方法要点：构建学术概念索引，指导概念覆盖查询生成和概念聚焦上下文增强，优化检索过程。
- 实验或效果：实验表明，该方法能生成高质量查询，改善概念对齐，并提升检索性能。

## 摘要（原文）

> Adapting general-domain retrievers to scientific domains is challenging due to the scarcity of large-scale domain-specific relevance annotations and the substantial mismatch in vocabulary and information needs. Recent approaches address these issues through two independent directions that leverage large language models (LLMs): (1) generating synthetic queries for fine-tuning, and (2) generating auxiliary contexts to support relevance matching. However, both directions overlook the diverse academic concepts embedded within scientific documents, often producing redundant or conceptually narrow queries and contexts. To address this limitation, we introduce an academic concept index, which extracts key concepts from papers and organizes them guided by an academic taxonomy. This structured index serves as a foundation for improving both directions. First, we enhance the synthetic query generation with concept coverage-based generation (CCQGen), which adaptively conditions LLMs on uncovered concepts to generate complementary queries with broader concept coverage. Second, we strengthen the context augmentation with concept-focused auxiliary contexts (CCExpand), which leverages a set of document snippets that serve as concise responses to the concept-aware CCQGen queries. Extensive experiments show that incorporating the academic concept index into both query generation and context augmentation leads to higher-quality queries, better conceptual alignment, and improved retrieval performance.

