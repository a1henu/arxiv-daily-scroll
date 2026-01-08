---
layout: default
title: A Theoretical and Empirical Taxonomy of Imbalance in Binary Classification
---

# A Theoretical and Empirical Taxonomy of Imbalance in Binary Classification
**arXiv**：[2601.04149v1](https://arxiv.org/abs/2601.04149) · [PDF](https://arxiv.org/pdf/2601.04149.pdf)  
**作者**：Rose Yvette Bandolo Essomba, Ernest Fokoué  

**一句话要点**：提出基于三元组(η,κ,Δ)的理论框架，统一分析二分类中类别不平衡导致的性能退化。

**关键词**：类别不平衡, 二分类, 理论框架, 贝叶斯误差, 性能退化, 高维数据

## 3 点简述
- 核心问题：类别不平衡显著降低分类性能，但缺乏统一理论分析。
- 方法要点：从高斯贝叶斯分类器出发，推导闭式贝叶斯误差，定义不平衡系数η、样本-维度比κ和内在可分性Δ。
- 实验或效果：在基因组数据上验证，经验退化与理论预测一致，预测了四种退化机制。

## 摘要（原文）

> Class imbalance significantly degrades classification performance, yet its effects are rarely analyzed from a unified theoretical perspective. We propose a principled framework based on three fundamental scales: the imbalance coefficient $η$, the sample--dimension ratio $κ$, and the intrinsic separability $Δ$. Starting from the Gaussian Bayes classifier, we derive closed-form Bayes errors and show how imbalance shifts the discriminant boundary, yielding a deterioration slope that predicts four regimes: Normal, Mild, Extreme, and Catastrophic. Using a balanced high-dimensional genomic dataset, we vary only $η$ while keeping $κ$ and $Δ$ fixed. Across parametric and non-parametric models, empirical degradation closely follows theoretical predictions: minority Recall collapses once $\log(η)$ exceeds $Δ\sqrtκ$, Precision increases asymmetrically, and F1-score and PR-AUC decline in line with the predicted regimes. These results show that the triplet $(η,κ,Δ)$ provides a model-agnostic, geometrically grounded explanation of imbalance-induced deterioration.

