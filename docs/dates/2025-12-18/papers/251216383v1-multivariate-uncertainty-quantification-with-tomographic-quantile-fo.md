---
layout: default
title: Multivariate Uncertainty Quantification with Tomographic Quantile Forests
---

# Multivariate Uncertainty Quantification with Tomographic Quantile Forests
**arXiv**：[2512.16383v1](https://arxiv.org/abs/2512.16383) · [PDF](https://arxiv.org/pdf/2512.16383.pdf)  
**作者**：Takuya Kanazawa  

**一句话要点**：提出Tomographic Quantile Forests以解决多变量目标条件分布的非参数估计问题

**关键词**：不确定性量化, 多变量回归, 条件分位数, 非参数估计, 树模型, Wasserstein距离

## 3 点简述
- 核心问题：多变量目标的条件分布非参数估计在不确定性量化中具有挑战性
- 方法要点：通过单模型学习方向投影的条件分位数，并聚合重构分布，避免凸性限制
- 实验或效果：在合成和真实数据集上评估，并开源代码

## 摘要（原文）

> Quantifying predictive uncertainty is essential for safe and trustworthy real-world AI deployment. Yet, fully nonparametric estimation of conditional distributions remains challenging for multivariate targets. We propose Tomographic Quantile Forests (TQF), a nonparametric, uncertainty-aware, tree-based regression model for multivariate targets. TQF learns conditional quantiles of directional projections $\mathbf{n}^{\top}\mathbf{y}$ as functions of the input $\mathbf{x}$ and the unit direction $\mathbf{n}$. At inference, it aggregates quantiles across many directions and reconstructs the multivariate conditional distribution by minimizing the sliced Wasserstein distance via an efficient alternating scheme with convex subproblems. Unlike classical directional-quantile approaches that typically produce only convex quantile regions and require training separate models for different directions, TQF covers all directions with a single model without imposing convexity restrictions. We evaluate TQF on synthetic and real-world datasets, and release the source code on GitHub.

