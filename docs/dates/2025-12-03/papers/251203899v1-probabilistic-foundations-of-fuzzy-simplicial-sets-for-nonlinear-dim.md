---
layout: default
title: Probabilistic Foundations of Fuzzy Simplicial Sets for Nonlinear Dimensionality Reduction
---

# Probabilistic Foundations of Fuzzy Simplicial Sets for Nonlinear Dimensionality Reduction
**arXiv**：[2512.03899v1](https://arxiv.org/abs/2512.03899) · [PDF](https://arxiv.org/pdf/2512.03899.pdf)  
**作者**：Janis Keck, Lukas Silvester Barth, Fatemeh, Fahimi, Parvaneh Joharinad, Jürgen Jost  

**一句话要点**：提出概率框架解释模糊单纯集，为非线性降维提供统一理论基础。

**关键词**：模糊单纯集, 非线性降维, 概率模型, UMAP, 单纯集理论, 生成模型

## 3 点简述
- 核心问题：模糊单纯集缺乏概率解释，脱离降维常用理论框架。
- 方法要点：将模糊单纯集建模为单纯集上概率测度的边际，连接生成模型与布尔运算。
- 实验或效果：框架可推导新嵌入方法，例如基于Čech过滤和三元采样的UMAP推广。

## 摘要（原文）

> Fuzzy simplicial sets have become an object of interest in dimensionality reduction and manifold learning, most prominently through their role in UMAP. However, their definition through tools from algebraic topology without a clear probabilistic interpretation detaches them from commonly used theoretical frameworks in those areas. In this work we introduce a framework that explains fuzzy simplicial sets as marginals of probability measures on simplicial sets. In particular, this perspective shows that the fuzzy weights of UMAP arise from a generative model that samples Vietoris-Rips filtrations at random scales, yielding cumulative distribution functions of pairwise distances. More generally, the framework connects fuzzy simplicial sets to probabilistic models on the face poset, clarifies the relation between Kullback-Leibler divergence and fuzzy cross-entropy in this setting, and recovers standard t-norms and t-conorms via Boolean operations on the underlying simplicial sets. We then show how new embedding methods may be derived from this framework and illustrate this on an example where we generalize UMAP using Čech filtrations with triplet sampling. In summary, this probabilistic viewpoint provides a unified probabilistic theoretical foundation for fuzzy simplicial sets, clarifies the role of UMAP within this framework, and enables the systematic derivation of new dimensionality reduction methods.

