---
layout: default
title: DRESS: A Continuous Framework for Structural Graph Refinement
---

# DRESS: A Continuous Framework for Structural Graph Refinement
**arXiv**：[2602.20833v1](https://arxiv.org/abs/2602.20833) · [PDF](https://arxiv.org/pdf/2602.20833.pdf)  
**作者**：Eduar Castrillo Velilla  

**一句话要点**：提出DRESS框架以解决高维WL测试计算成本高的问题，实现可扩展的图结构细化。

**关键词**：图同构测试, 结构细化, 连续动力系统, 计算可扩展性, 强正则图

## 3 点简述
- 核心问题：WL层次结构在3-WL及以上需O(n^4)计算，难以应用于大规模图。
- 方法要点：从Original-DRESS扩展到Motif-DRESS和Generalized-DRESS，引入Delta-DRESS连接重构猜想。
- 实验或效果：在基准图上经验性超越1-WL和3-WL，区分强正则图等复杂结构。

## 摘要（原文）

> The Weisfeiler-Lehman (WL) hierarchy is a cornerstone framework for graph isomorphism testing and structural analysis. However, scaling beyond 1-WL to 3-WL and higher requires tensor-based operations that scale as O(n^3) or O(n^4), making them computationally prohibitive for large graphs. In this paper, we start from the Original-DRESS equation (Castrillo, Leon, and Gomez, 2018)--a parameter-free, continuous dynamical system on edges--and show that it distinguishes the prism graph from K_{3,3}, a pair that 1-WL provably cannot separate. We then generalize it to Motif-DRESS, which replaces triangle neighborhoods with arbitrary structural motifs and converges to a unique fixed point under three sufficient conditions, and further to Generalized-DRESS, an abstract template parameterized by the choice of neighborhood operator, aggregation function and norm. Finally, we introduce Delta-DRESS, which runs DRESS on each node-deleted subgraph G\{v}, connecting the framework to the Kelly-Ulam reconstruction conjecture. Both Motif-DRESS and Delta-DRESS empirically distinguish Strongly Regular Graphs (SRGs)--such as the Rook and Shrikhande graphs--that confound 3-WL. Our results establish the DRESS family as a highly scalable framework that empirically surpasses both 1-WL and 3-WL on well-known benchmark graphs, without the prohibitive O(n^4) computational cost.

