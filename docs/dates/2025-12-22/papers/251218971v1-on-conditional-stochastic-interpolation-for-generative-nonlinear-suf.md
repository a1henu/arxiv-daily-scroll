---
layout: default
title: On Conditional Stochastic Interpolation for Generative Nonlinear Sufficient Dimension Reduction
---

# On Conditional Stochastic Interpolation for Generative Nonlinear Sufficient Dimension Reduction
**arXiv**：[2512.18971v1](https://arxiv.org/abs/2512.18971) · [PDF](https://arxiv.org/pdf/2512.18971.pdf)  
**作者**：Shuntuo Xu, Zhou Yu, Jian Huang  

**一句话要点**：提出GenSDR方法，利用生成模型解决非线性充分降维中低维结构识别问题

**关键词**：非线性充分降维, 生成模型, 条件分布学习, 样本一致性, 非欧响应处理

## 3 点简述
- 核心问题：非线性充分降维中低维充分结构的识别缺乏理论保证
- 方法要点：基于生成模型，在总体和样本层面完全恢复中心σ-场信息
- 实验或效果：数值结果展示优异性能，扩展至非欧响应场景

## 摘要（原文）

> Identifying low-dimensional sufficient structures in nonlinear sufficient dimension reduction (SDR) has long been a fundamental yet challenging problem. Most existing methods lack theoretical guarantees of exhaustiveness in identifying lower dimensional structures, either at the population level or at the sample level. We tackle this issue by proposing a new method, generative sufficient dimension reduction (GenSDR), which leverages modern generative models. We show that GenSDR is able to fully recover the information contained in the central $σ$-field at both the population and sample levels. In particular, at the sample level, we establish a consistency property for the GenSDR estimator from the perspective of conditional distributions, capitalizing on the distributional learning capabilities of deep generative models. Moreover, by incorporating an ensemble technique, we extend GenSDR to accommodate scenarios with non-Euclidean responses, thereby substantially broadening its applicability. Extensive numerical results demonstrate the outstanding empirical performance of GenSDR and highlight its strong potential for addressing a wide range of complex, real-world tasks.

