---
layout: default
title: Semantic Search over 9 Million Mathematical Theorems
---

# Semantic Search over 9 Million Mathematical Theorems
**arXiv**：[2602.05216v1](https://arxiv.org/abs/2602.05216) · [PDF](https://arxiv.org/pdf/2602.05216.pdf)  
**作者**：Luke Alexander, Eric Leonen, Sophie Szeto, Artemii Remizov, Ignacio Tejeda, Giovanni Inchiostro, Vasily Ilin  

**一句话要点**：提出语义定理检索方法，在920万定理语料上解决数学定理搜索难题。

**关键词**：语义定理检索, 数学定理语料, 自然语言表示, 检索质量分析, 定理搜索工具

## 3 点简述
- 核心问题：现有工具检索整篇论文，难以定位特定定理，数学定理语义搜索在大型技术语料中效果未知。
- 方法要点：从arXiv等源提取920万定理，用自然语言描述表示定理，系统分析表示上下文、模型选择等对检索质量的影响。
- 实验或效果：在数学家编写的查询集上，相比基线显著提升定理级和论文级检索效果，证明语义定理搜索可行且有效。

## 摘要（原文）

> Searching for mathematical results remains difficult: most existing tools retrieve entire papers, while mathematicians and theorem-proving agents often seek a specific theorem, lemma, or proposition that answers a query. While semantic search has seen rapid progress, its behavior on large, highly technical corpora such as research-level mathematical theorems remains poorly understood. In this work, we introduce and study semantic theorem retrieval at scale over a unified corpus of $9.2$ million theorem statements extracted from arXiv and seven other sources, representing the largest publicly available corpus of human-authored, research-level theorems. We represent each theorem with a short natural-language description as a retrieval representation and systematically analyze how representation context, language model choice, embedding model, and prompting strategy affect retrieval quality. On a curated evaluation set of theorem-search queries written by professional mathematicians, our approach substantially improves both theorem-level and paper-level retrieval compared to existing baselines, demonstrating that semantic theorem search is feasible and effective at web scale. The theorem search tool is available at \href{https://huggingface.co/spaces/uw-math-ai/theorem-search}{this link}, and the dataset is available at \href{https://huggingface.co/datasets/uw-math-ai/TheoremSearch}{this link}.

