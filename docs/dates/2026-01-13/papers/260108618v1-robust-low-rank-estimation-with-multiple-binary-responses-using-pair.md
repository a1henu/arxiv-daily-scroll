---
layout: default
title: Robust low-rank estimation with multiple binary responses using pairwise AUC loss
---

# Robust low-rank estimation with multiple binary responses using pairwise AUC loss
**arXiv**：[2601.08618v1](https://arxiv.org/abs/2601.08618) · [PDF](https://arxiv.org/pdf/2601.08618.pdf)  
**作者**：The Tien Mai  

**一句话要点**：提出基于成对AUC损失的低秩估计框架，以提升多二元响应任务的鲁棒性与排序性能。

**关键词**：多二元响应, 低秩估计, 成对AUC损失, 鲁棒学习, 排序性能

## 3 点简述
- 核心问题：多二元响应任务中，传统方法忽略共享结构且统计效率低，尤其在类不平衡场景。
- 方法要点：通过最小化ROC曲线下面积的代理损失，结合低秩约束系数矩阵，利用投影梯度下降算法优化。
- 实验或效果：模拟研究显示方法在标签切换和数据污染下鲁棒，优于基于似然的方法。

## 摘要（原文）

> Multiple binary responses arise in many modern data-analytic problems. Although fitting separate logistic regressions for each response is computationally attractive, it ignores shared structure and can be statistically inefficient, especially in high-dimensional and class-imbalanced regimes. Low-rank models offer a natural way to encode latent dependence across tasks, but existing methods for binary data are largely likelihood-based and focus on pointwise classification rather than ranking performance. In this work, we propose a unified framework for learning with multiple binary responses that directly targets discrimination by minimizing a surrogate loss for the area under the ROC curve (AUC). The method aggregates pairwise AUC surrogate losses across responses while imposing a low-rank constraint on the coefficient matrix to exploit shared structure. We develop a scalable projected gradient descent algorithm based on truncated singular value decomposition. Exploiting the fact that the pairwise loss depends only on differences of linear predictors, we simplify computation and analysis. We establish non-asymptotic convergence guarantees, showing that under suitable regularity conditions, leading to linear convergence up to the minimax-optimal statistical precision. Extensive simulation studies demonstrate that the proposed method is robust in challenging settings such as label switching and data contamination and consistently outperforms likelihood-based approaches.

