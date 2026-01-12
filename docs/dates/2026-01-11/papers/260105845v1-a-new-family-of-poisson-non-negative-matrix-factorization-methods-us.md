---
layout: default
title: A New Family of Poisson Non-negative Matrix Factorization Methods Using the Shifted Log Link
---

# A New Family of Poisson Non-negative Matrix Factorization Methods Using the Shifted Log Link
**arXiv**：[2601.05845v1](https://arxiv.org/abs/2601.05845) · [PDF](https://arxiv.org/pdf/2601.05845.pdf)  
**作者**：Eric Weine, Peter Carbonetto, Rafael A. Irizarry, Matthew Stephens  

**一句话要点**：提出使用移位对数链接的泊松非负矩阵分解方法，以放宽分解中部分组合的加性假设。

**关键词**：泊松非负矩阵分解, 移位对数链接, 计数数据分解, 最大似然估计, 稀疏数据集优化

## 3 点简述
- 核心问题：现有泊松NMF假设分解部分为加性组合，这在某些场景下可能不自然。
- 方法要点：引入移位对数链接函数，通过调整参数从加性过渡到更乘性组合，并提供最大似然拟合算法。
- 实验或效果：在真实数据集上展示链接函数选择对结果的影响，移位对数链接可提升可解释性。

## 摘要（原文）

> Poisson non-negative matrix factorization (NMF) is a widely used method to find interpretable "parts-based" decompositions of count data. While many variants of Poisson NMF exist, existing methods assume that the "parts" in the decomposition combine additively. This assumption may be natural in some settings, but not in others. Here we introduce Poisson NMF with the shifted-log link function to relax this assumption. The shifted-log link function has a single tuning parameter, and as this parameter varies the model changes from assuming that parts combine additively (i.e., standard Poisson NMF) to assuming that parts combine more multiplicatively. We provide an algorithm to fit this model by maximum likelihood, and also an approximation that substantially reduces computation time for large, sparse datasets (computations scale with the number of non-zero entries in the data matrix). We illustrate these new methods on a variety of real datasets. Our examples show how the choice of link function in Poisson NMF can substantively impact the results, and how in some settings the use of a shifted-log link function may improve interpretability compared with the standard, additive link.

