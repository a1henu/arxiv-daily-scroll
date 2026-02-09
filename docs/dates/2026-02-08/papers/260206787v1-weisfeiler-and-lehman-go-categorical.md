---
layout: default
title: Weisfeiler and Lehman Go Categorical
---

# Weisfeiler and Lehman Go Categorical
**arXiv**：[2602.06787v1](https://arxiv.org/abs/2602.06787) · [PDF](https://arxiv.org/pdf/2602.06787.pdf)  
**作者**：Seongjin Choi, Gahee Kim, Se-Young Yun  

**一句话要点**：提出范畴Weisfeiler-Lehman框架以系统化超图神经网络设计

**关键词**：超图神经网络, 范畴论, Weisfeiler-Lehman测试, 函子映射, 分级偏序集, 图同构网络

## 3 点简述
- 核心问题：超图神经网络设计缺乏统一框架，现有方法表达力有限
- 方法要点：引入范畴论将提升映射形式化为函子，从超图范畴到分级偏序集范畴
- 实验或效果：理论证明模型表达力超越标准超图Weisfeiler-Lehman测试，实验验证性能提升

## 摘要（原文）

> While lifting map has significantly enhanced the expressivity of graph neural networks, extending this paradigm to hypergraphs remains fragmented. To address this, we introduce the categorical Weisfeiler-Lehman framework, which formalizes lifting as a functorial mapping from an arbitrary data category to the unifying category of graded posets. When applied to hypergraphs, this perspective allows us to systematically derive Hypergraph Isomorphism Networks, a family of neural architectures where the message passing topology is strictly determined by the choice of functor. We introduce two distinct functors from the category of hypergraphs: an incidence functor and a symmetric simplicial complex functor. While the incidence architecture structurally mirrors standard bipartite schemes, our functorial derivation enforces a richer information flow over the resulting poset, capturing complex intersection geometries often missed by existing methods. We theoretically characterize the expressivity of these models, proving that both the incidence-based and symmetric simplicial approaches subsume the expressive power of the standard Hypergraph Weisfeiler-Lehman test. Extensive experiments on real-world benchmarks validate these theoretical findings.

