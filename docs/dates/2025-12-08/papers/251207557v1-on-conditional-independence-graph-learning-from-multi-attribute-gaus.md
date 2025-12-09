---
layout: default
title: On Conditional Independence Graph Learning From Multi-Attribute Gaussian Dependent Time Series
---

# On Conditional Independence Graph Learning From Multi-Attribute Gaussian Dependent Time Series
**arXiv**：[2512.07557v1](https://arxiv.org/abs/2512.07557) · [PDF](https://arxiv.org/pdf/2512.07557.pdf)  
**作者**：Jitendra K. Tugnait  

**一句话要点**：提出基于频域惩罚似然的多属性高斯时间序列条件独立图学习方法

**关键词**：条件独立图学习, 多属性时间序列, 频域方法, 惩罚似然, 高维统计, 图恢复

## 3 点简述
- 研究多属性高斯时间序列的条件独立图估计问题，扩展单属性模型
- 使用频域惩罚似然方法，结合凸与非凸惩罚函数，建立高维一致性理论
- 通过合成和真实数据实验验证方法，并基于贝叶斯信息准则选择调参

## 摘要（原文）

> Estimation of the conditional independence graph (CIG) of high-dimensional multivariate Gaussian time series from multi-attribute data is considered. Existing methods for graph estimation for such data are based on single-attribute models where one associates a scalar time series with each node. In multi-attribute graphical models, each node represents a random vector or vector time series. In this paper we provide a unified theoretical analysis of multi-attribute graph learning for dependent time series using a penalized log-likelihood objective function formulated in the frequency domain using the discrete Fourier transform of the time-domain data. We consider both convex (sparse-group lasso) and non-convex (log-sum and SCAD group penalties) penalty/regularization functions. We establish sufficient conditions in a high-dimensional setting for consistency (convergence of the inverse power spectral density to true value in the Frobenius norm), local convexity when using non-convex penalties, and graph recovery. We do not impose any incoherence or irrepresentability condition for our convergence results. We also empirically investigate selection of the tuning parameters based on the Bayesian information criterion, and illustrate our approach using numerical examples utilizing both synthetic and real data.

