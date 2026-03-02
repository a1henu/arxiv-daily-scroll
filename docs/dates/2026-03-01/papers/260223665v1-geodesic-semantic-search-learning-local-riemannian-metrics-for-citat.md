---
layout: default
title: Geodesic Semantic Search: Learning Local Riemannian Metrics for Citation Graph Retrieval
---

# Geodesic Semantic Search: Learning Local Riemannian Metrics for Citation Graph Retrieval
**arXiv**：[2602.23665v1](https://arxiv.org/abs/2602.23665) · [PDF](https://arxiv.org/pdf/2602.23665.pdf)  
**作者**：Brandon Yee, Lucas Wang, Kundana Kommini, Krishna Sharma  

**一句话要点**：提出Geodesic Semantic Search，通过局部黎曼度量学习实现引文图的几何感知语义检索。

**关键词**：引文图检索, 黎曼度量学习, 测地距离, 语义搜索, 低秩近似, 路径解释性

## 3 点简述
- 核心问题：标准嵌入检索依赖固定欧氏距离，在引文图中可能忽略局部语义结构。
- 方法要点：为每个节点学习低秩度量张量，构建局部半正定度量，通过测地距离进行多源Dijkstra检索。
- 实验或效果：在169K论文基准上，Recall@20相对提升23%，计算成本降低4倍，保持97%检索质量。

## 摘要（原文）

> We present Geodesic Semantic Search (GSS), a retrieval system that learns node-specific Riemannian metrics on citation graphs to enable geometry-aware semantic search. Unlike standard embedding-based retrieval that relies on fixed Euclidean distances, \gss{} learns a low-rank metric tensor $\mL_i \in \R^{d \times r}$ at each node, inducing a local positive semi-definite metric $\mG_i = \mL_i \mL_i^\top + \eps \mI$. This parameterization guarantees valid metrics while keeping the model tractable. Retrieval proceeds via multi-source Dijkstra on the learned geodesic distances, followed by Maximal Marginal Relevance reranking and path coherence filtering. On citation prediction benchmarks with 169K papers, \gss{} achieves 23\% relative improvement in Recall@20 over SPECTER+FAISS baselines while providing interpretable citation paths. Our hierarchical coarse-to-fine search with k-means pooling reduces computational cost by 4$\times$ compared to flat geodesic search while maintaining 97\% retrieval quality. We provide theoretical analysis of when geodesic distances outperform direct similarity, characterize the approximation quality of low-rank metrics, and validate predictions empirically. Code and trained models are available at https://github.com/YCRG-Labs/geodesic-search.

