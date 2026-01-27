---
layout: default
title: Nonlinear multi-study factor analysis
---

# Nonlinear multi-study factor analysis
**arXiv**：[2601.18128v1](https://arxiv.org/abs/2601.18128) · [PDF](https://arxiv.org/pdf/2601.18128.pdf)  
**作者**：Gemma E. Moran, Anandi Krishnan  

**一句话要点**：提出非线性多研究因子分析模型，以识别高维数据中的共享与特定因子。

**关键词**：多研究因子分析, 稀疏变分自编码器, 基因表达数据, 非线性建模, 因子识别

## 3 点简述
- 核心问题：高维多研究数据中，如何区分共享因子与特定因子。
- 方法要点：使用多研究稀疏变分自编码器，实现非线性因子建模与稀疏性约束。
- 实验或效果：在血小板基因表达数据中恢复有意义的因子，并证明因子可识别性。

## 摘要（原文）

> High-dimensional data often exhibit variation that can be captured by lower dimensional factors. For high-dimensional data from multiple studies or environments, one goal is to understand which underlying factors are common to all studies, and which factors are study or environment-specific. As a particular example, we consider platelet gene expression data from patients in different disease groups. In this data, factors correspond to clusters of genes which are co-expressed; we may expect some clusters (or biological pathways) to be active for all diseases, while some clusters are only active for a specific disease. To learn these factors, we consider a nonlinear multi-study factor model, which allows for both shared and specific factors. To fit this model, we propose a multi-study sparse variational autoencoder. The underlying model is sparse in that each observed feature (i.e. each dimension of the data) depends on a small subset of the latent factors. In the genomics example, this means each gene is active in only a few biological processes. Further, the model implicitly induces a penalty on the number of latent factors, which helps separate the shared factors from the group-specific factors. We prove that the latent factors are identified, and demonstrate our method recovers meaningful factors in the platelet gene expression data.

