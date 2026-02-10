---
layout: default
title: Welfarist Formulations for Diverse Similarity Search
---

# Welfarist Formulations for Diverse Similarity Search
**arXiv**：[2602.08742v1](https://arxiv.org/abs/2602.08742) · [PDF](https://arxiv.org/pdf/2602.08742.pdf)  
**作者**：Siddharth Barman, Nirjhar Das, Shivam Gupta, Kirankumar Shiragur  

**一句话要点**：提出基于福利函数的多样化相似性搜索方法，以平衡检索中的相关性与多样性。

**关键词**：最近邻搜索, 多样性检索, 福利函数, 纳什社会福利, 近似算法, 检索增强生成

## 3 点简述
- 核心问题：在最近邻搜索中，传统方法难以自适应平衡相关性与多样性，影响推荐系统等应用效果。
- 方法要点：引入数学经济学中的福利函数，特别是纳什社会福利，以查询依赖方式优化目标函数。
- 实验或效果：算法可基于标准近似最近邻方法实现，实验显示在保持高相关性的同时显著提升多样性。

## 摘要（原文）

> Nearest Neighbor Search (NNS) is a fundamental problem in data structures with wide-ranging applications, such as web search, recommendation systems, and, more recently, retrieval-augmented generations (RAG). In such recent applications, in addition to the relevance (similarity) of the returned neighbors, diversity among the neighbors is a central requirement. In this paper, we develop principled welfare-based formulations in NNS for realizing diversity across attributes. Our formulations are based on welfare functions -- from mathematical economics -- that satisfy central diversity (fairness) and relevance (economic efficiency) axioms. With a particular focus on Nash social welfare, we note that our welfare-based formulations provide objective functions that adaptively balance relevance and diversity in a query-dependent manner. Notably, such a balance was not present in the prior constraint-based approach, which forced a fixed level of diversity and optimized for relevance. In addition, our formulation provides a parametric way to control the trade-off between relevance and diversity, providing practitioners with flexibility to tailor search results to task-specific requirements. We develop efficient nearest neighbor algorithms with provable guarantees for the welfare-based objectives. Notably, our algorithm can be applied on top of any standard ANN method (i.e., use standard ANN method as a subroutine) to efficiently find neighbors that approximately maximize our welfare-based objectives. Experimental results demonstrate that our approach is practical and substantially improves diversity while maintaining high relevance of the retrieved neighbors.

