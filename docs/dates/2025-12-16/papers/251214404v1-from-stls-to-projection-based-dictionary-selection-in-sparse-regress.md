---
layout: default
title: From STLS to Projection-based Dictionary Selection in Sparse Regression for System Identification
---

# From STLS to Projection-based Dictionary Selection in Sparse Regression for System Identification
**arXiv**：[2512.14404v1](https://arxiv.org/abs/2512.14404) · [PDF](https://arxiv.org/pdf/2512.14404.pdf)  
**作者**：Hangjun Cho, Fabio V. G. Amaral, Andrei A. Klishin, Cassio M. Oishi, Steven L. Brunton  

**一句话要点**：提出基于投影分数的字典选择方法，以增强稀疏回归在系统辨识中的准确性和可解释性。

**关键词**：稀疏回归, 系统辨识, 字典选择, STLS算法, SINDy框架

## 3 点简述
- 核心问题：稀疏回归中字典选择对系统辨识精度和可解释性的影响。
- 方法要点：分析STLS算法的分数和字典选择策略，提出基于投影分数的指导方法。
- 实验或效果：在常微分和偏微分方程上验证，分数筛选提升辨识准确性和模型可解释性。

## 摘要（原文）

> In this work, we revisit dictionary-based sparse regression, in particular, Sequential Threshold Least Squares (STLS), and propose a score-guided library selection to provide practical guidance for data-driven modeling, with emphasis on SINDy-type algorithms. STLS is an algorithm to solve the $\ell_0$ sparse least-squares problem, which relies on splitting to efficiently solve the least-squares portion while handling the sparse term via proximal methods. It produces coefficient vectors whose components depend on both the projected reconstruction errors, here referred to as the scores, and the mutual coherence of dictionary terms. The first contribution of this work is a theoretical analysis of the score and dictionary-selection strategy. This could be understood in both the original and weak SINDy regime. Second, numerical experiments on ordinary and partial differential equations highlight the effectiveness of score-based screening, improving both accuracy and interpretability in dynamical system identification. These results suggest that integrating score-guided methods to refine the dictionary more accurately may help SINDy users in some cases to enhance their robustness for data-driven discovery of governing equations.

