---
layout: default
title: Constraint- and Score-Based Nonlinear Granger Causality Discovery with Kernels
---

# Constraint- and Score-Based Nonlinear Granger Causality Discovery with Kernels
**arXiv**：[2601.09579v1](https://arxiv.org/abs/2601.09579) · [PDF](https://arxiv.org/pdf/2601.09579.pdf)  
**作者**：Fiona Murphy, Alessio Benavoli  

**一句话要点**：提出基于核主成分回归的统一框架与高斯过程评分模型，以改进时间序列非线性因果发现

**关键词**：非线性因果发现, 核方法, 格兰杰因果, 高斯过程, 时间序列分析, 核主成分回归

## 3 点简述
- 核心问题：如何有效识别时间序列变量间的非线性因果关系，统一现有核方法。
- 方法要点：理论统一两种核格兰杰因果方法于核主成分回归框架，并引入高斯过程评分模型。
- 实验或效果：新方法在非线性因果发现中表现优于现有先进方法，并提出了基于格兰杰因果的同期因果识别算法。

## 摘要（原文）

> Kernel-based methods are used in the context of Granger Causality to enable the identification of nonlinear causal relationships between time series variables. In this paper, we show that two state of the art kernel-based Granger Causality (GC) approaches can be theoretically unified under the framework of Kernel Principal Component Regression (KPCR), and introduce a method based on this unification, demonstrating that this approach can improve causal identification. Additionally, we introduce a Gaussian Process score-based model with Smooth Information Criterion penalisation on the marginal likelihood, and demonstrate improved performance over existing state of the art time-series nonlinear causal discovery methods. Furthermore, we propose a contemporaneous causal identification algorithm, fully based on GC, using the proposed score-based $GP_{SIC}$ method, and compare its performance to a state of the art contemporaneous time series causal discovery algorithm.

