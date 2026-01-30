---
layout: default
title: Bridging Functional and Representational Similarity via Usable Information
---

# Bridging Functional and Representational Similarity via Usable Information
**arXiv**：[2601.21568v1](https://arxiv.org/abs/2601.21568) · [PDF](https://arxiv.org/pdf/2601.21568.pdf)  
**作者**：Antonio Almudévar, Alfonso Ortega  

**一句话要点**：提出基于可用信息的统一框架，量化表示相似性并连接功能与表示维度。

**关键词**：表示相似性, 可用信息, 功能相似性, 条件互信息, 任务粒度

## 3 点简述
- 核心问题：如何统一量化表示相似性，连接功能与表示维度。
- 方法要点：通过可用信息理论，建立缝合性能与条件互信息的联系，分析双向不对称性。
- 实验或效果：证明表示相似性对功能相似性充分但不必要，建立任务粒度层次。

## 摘要（原文）

> We present a unified framework for quantifying the similarity between representations through the lens of \textit{usable information}, offering a rigorous theoretical and empirical synthesis across three key dimensions. First, addressing functional similarity, we establish a formal link between stitching performance and conditional mutual information. We further reveal that stitching is inherently asymmetric, demonstrating that robust functional comparison necessitates a bidirectional analysis rather than a unidirectional mapping. Second, concerning representational similarity, we prove that reconstruction-based metrics and standard tools (e.g., CKA, RSA) act as estimators of usable information under specific constraints. Crucially, we show that similarity is relative to the capacity of the predictive family: representations that appear distinct to a rigid observer may be identical to a more expressive one. Third, we demonstrate that representational similarity is sufficient but not necessary for functional similarity. We unify these concepts through a task-granularity hierarchy: similarity on a complex task guarantees similarity on any coarser derivative, establishing representational similarity as the limit of maximum granularity: input reconstruction.

