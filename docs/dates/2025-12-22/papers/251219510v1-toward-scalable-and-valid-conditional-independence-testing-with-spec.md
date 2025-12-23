---
layout: default
title: Toward Scalable and Valid Conditional Independence Testing with Spectral Representations
---

# Toward Scalable and Valid Conditional Independence Testing with Spectral Representations
**arXiv**：[2512.19510v1](https://arxiv.org/abs/2512.19510) · [PDF](https://arxiv.org/pdf/2512.19510.pdf)  
**作者**：Alek Frohlich, Vladimir Kostic, Karim Lounici, Daniel Perazzo, Massimiliano Pontil  

**一句话要点**：提出基于谱表示的条件独立性测试方法，以提升可扩展性和有效性

**关键词**：条件独立性测试, 谱表示学习, 偏协方差算子, 可扩展性, 因果推断

## 3 点简述
- 核心问题：条件独立性测试在无额外假设时不可测，现有方法受限于结构条件或可扩展性差
- 方法要点：利用偏协方差算子的奇异值分解构建表示，设计类似HSIC的统计量，并引入双层对比算法学习表示
- 实验或效果：理论分析链接表示学习误差与测试性能，初步实验显示该方法提供可扩展且统计基础扎实的路径

## 摘要（原文）

> Conditional independence (CI) is central to causal inference, feature selection, and graphical modeling, yet it is untestable in many settings without additional assumptions. Existing CI tests often rely on restrictive structural conditions, limiting their validity on real-world data. Kernel methods using the partial covariance operator offer a more principled approach but suffer from limited adaptivity, slow convergence, and poor scalability. In this work, we explore whether representation learning can help address these limitations. Specifically, we focus on representations derived from the singular value decomposition of the partial covariance operator and use them to construct a simple test statistic, reminiscent of the Hilbert-Schmidt Independence Criterion (HSIC). We also introduce a practical bi-level contrastive algorithm to learn these representations. Our theory links representation learning error to test performance and establishes asymptotic validity and power guarantees. Preliminary experiments suggest that this approach offers a practical and statistically grounded path toward scalable CI testing, bridging kernel-based theory with modern representation learning.

