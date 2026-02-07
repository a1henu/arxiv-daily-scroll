---
layout: default
title: Semantic Search over 9 Million Mathematical Theorems
---

# Semantic Search over 9 Million Mathematical Theorems
**arXiv**：[2602.05216v1](https://arxiv.org/abs/2602.05216) · [PDF](https://arxiv.org/pdf/2602.05216.pdf)  
**作者**：Luke Alexander, Eric Leonen, Sophie Szeto, Artemii Remizov, Ignacio Tejeda, Giovanni Inchiostro, Vasily Ilin  

**一句话要点**：提出基于语义检索的方法，在920万定理语料上实现高效数学定理搜索，解决现有工具检索粒度粗的问题。

**关键词**：语义检索, 数学定理搜索, 大规模语料库, 自然语言处理, 嵌入模型, 评估基准

## 3 点简述
- 核心问题：现有数学搜索工具通常返回整篇论文，难以定位特定定理、引理或命题，尤其在研究级数学语料中。
- 方法要点：从arXiv等来源提取920万定理语句，构建统一语料库，使用自然语言描述作为检索表示，系统分析表示上下文、语言模型、嵌入模型和提示策略对检索质量的影响。
- 实验或效果：在专业数学家编写的查询评估集上，相比基线方法，显著提升了定理级和论文级检索效果，证明语义定理搜索在网页规模下可行且有效。

## 摘要（原文）

> Searching for mathematical results remains difficult: most existing tools retrieve entire papers, while mathematicians and theorem-proving agents often seek a specific theorem, lemma, or proposition that answers a query. While semantic search has seen rapid progress, its behavior on large, highly technical corpora such as research-level mathematical theorems remains poorly understood. In this work, we introduce and study semantic theorem retrieval at scale over a unified corpus of $9.2$ million theorem statements extracted from arXiv and seven other sources, representing the largest publicly available corpus of human-authored, research-level theorems. We represent each theorem with a short natural-language description as a retrieval representation and systematically analyze how representation context, language model choice, embedding model, and prompting strategy affect retrieval quality. On a curated evaluation set of theorem-search queries written by professional mathematicians, our approach substantially improves both theorem-level and paper-level retrieval compared to existing baselines, demonstrating that semantic theorem search is feasible and effective at web scale. The theorem search tool is available at \href{https://huggingface.co/spaces/uw-math-ai/theorem-search}{this link}, and the dataset is available at \href{https://huggingface.co/datasets/uw-math-ai/TheoremSearch}{this link}.

