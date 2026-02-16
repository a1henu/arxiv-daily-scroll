---
layout: default
title: A Regularization-Sharpness Tradeoff for Linear Interpolators
---

# A Regularization-Sharpness Tradeoff for Linear Interpolators
**arXiv**：[2602.12680v1](https://arxiv.org/abs/2602.12680) · [PDF](https://arxiv.org/pdf/2602.12680.pdf)  
**作者**：Qingyi Hu, Liam Hodgkinson  

**一句话要点**：提出正则化-锐度权衡框架，用于过参数化线性回归中的ℓ^p惩罚插值器选择。

**关键词**：过参数化线性回归, 正则化-锐度权衡, ℓ^p惩罚, 插值信息准则, 最小范数插值器

## 3 点简述
- 核心问题：过参数化设置下经典偏差-方差权衡失效，需新权衡解释最小范数插值器性能。
- 方法要点：基于插值信息准则，将选择惩罚分解为正则化项和几何锐度项，建立类似偏差-方差的权衡。
- 实验或效果：在真实数据集上验证理论，正则化-锐度项能区分高性能与低性能线性插值器。

## 摘要（原文）

> The rule of thumb regarding the relationship between the bias-variance tradeoff and model size plays a key role in classical machine learning, but is now well-known to break down in the overparameterized setting as per the double descent curve. In particular, minimum-norm interpolating estimators can perform well, suggesting the need for new tradeoff in these settings. Accordingly, we propose a regularization-sharpness tradeoff for overparameterized linear regression with an $\ell^p$ penalty. Inspired by the interpolating information criterion, our framework decomposes the selection penalty into a regularization term (quantifying the alignment of the regularizer and the interpolator) and a geometric sharpness term on the interpolating manifold (quantifying the effect of local perturbations), yielding a tradeoff analogous to bias-variance. Building on prior analyses that established this information criterion for ridge regularizers, this work first provides a general expression of the interpolating information criterion for $\ell^p$ regularizers where $p \ge 2$. Subsequently, we extend this to the LASSO interpolator with $\ell^1$ regularizer, which induces stronger sparsity. Empirical results on real-world datasets with random Fourier features and polynomials validate our theory, demonstrating how the tradeoff terms can distinguish performant linear interpolators from weaker ones.

