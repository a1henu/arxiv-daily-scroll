---
layout: default
title: Kernel Integrated $R^2$: A Measure of Dependence
---

# Kernel Integrated $R^2$: A Measure of Dependence
**arXiv**：[2602.22985v1](https://arxiv.org/abs/2602.22985) · [PDF](https://arxiv.org/pdf/2602.22985.pdf)  
**作者**：Pouya Roudaki, Shakeel Gavioli-Akilagun, Florian Kalinke, Mona Azadkia, Zoltán Szabó  

**一句话要点**：提出核集成R²以测量多变量、函数和结构化数据的统计依赖性

**关键词**：统计依赖性度量, 再生核希尔伯特空间, 条件均值嵌入, K近邻估计, 非参数统计, 依赖性测试

## 3 点简述
- 核心问题：扩展集成R²以处理非标量响应数据，如多变量、函数和结构化数据，同时保持对尾部行为和振荡依赖结构的敏感性。
- 方法要点：结合集成R²的局部归一化原则与再生核希尔伯特空间的灵活性，定义取值在[0,1]的依赖性度量，并开发基于K近邻和条件均值嵌入的估计器。
- 实验或效果：在模拟和真实数据实验中，该度量在非线性和结构化关系场景下，与先进依赖性度量相比表现出竞争力。

## 摘要（原文）

> We introduce kernel integrated $R^2$, a new measure of statistical dependence that combines the local normalization principle of the recently introduced integrated $R^2$ with the flexibility of reproducing kernel Hilbert spaces (RKHSs). The proposed measure extends integrated $R^2$ from scalar responses to responses taking values on general spaces equipped with a characteristic kernel, allowing to measure dependence of multivariate, functional, and structured data, while remaining sensitive to tail behaviour and oscillatory dependence structures. We establish that (i) this new measure takes values in $[0,1]$, (ii) equals zero if and only if independence holds, and (iii) equals one if and only if the response is almost surely a measurable function of the covariates. Two estimators are proposed: a graph-based method using $K$-nearest neighbours and an RKHS-based method built on conditional mean embeddings. We prove consistency and derive convergence rates for the graph-based estimator, showing its adaptation to intrinsic dimensionality. Numerical experiments on simulated data and a real data experiment in the context of dependency testing for media annotations demonstrate competitive power against state-of-the-art dependence measures, particularly in settings involving non-linear and structured relationships.

