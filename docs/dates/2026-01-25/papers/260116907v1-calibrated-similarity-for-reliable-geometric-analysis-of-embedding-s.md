---
layout: default
title: Calibrated Similarity for Reliable Geometric Analysis of Embedding Spaces
---

# Calibrated Similarity for Reliable Geometric Analysis of Embedding Spaces
**arXiv**：[2601.16907v1](https://arxiv.org/abs/2601.16907) · [PDF](https://arxiv.org/pdf/2601.16907.pdf)  
**作者**：Nicolas Tacheny  

**一句话要点**：提出单调校准方法以解决预训练嵌入空间中余弦相似度绝对值的系统性误校准问题

**关键词**：嵌入空间校准, 余弦相似度, 等渗回归, 几何分析, 单调变换

## 3 点简述
- 预训练嵌入空间中的余弦相似度存在各向异性，导致绝对值集中在高相似度带，限制定量解释性
- 使用基于人类相似度判断的等渗回归构建单调变换，校准绝对值同时保持排序相关性和局部稳定性
- 实验显示校准后达到近完美校准，且基于顺序的几何构造在此变换下保持不变

## 摘要（原文）

> While raw cosine similarity in pretrained embedding spaces exhibits strong rank correlation with human judgments, anisotropy induces systematic miscalibration of absolute values: scores concentrate in a narrow high-similarity band regardless of actual semantic relatedness, limiting interpretability as a quantitative measure. Prior work addresses this by modifying the embedding space (whitening, contrastive fine tuning), but such transformations alter geometric structure and require recomputing all embeddings.
>   Using isotonic regression trained on human similarity judgments, we construct a monotonic transformation that achieves near-perfect calibration while preserving rank correlation and local stability(98% across seven perturbation types). Our contribution is not to replace cosine similarity, but to restore interpretability of its absolute values through monotone calibration, without altering its ranking properties.
>   We characterize isotonic calibration as an order-preserving reparameterization and prove that all order-based constructions (angular ordering, nearest neighbors, threshold graphs and quantile-based decisions) are invariant under this transformation.

