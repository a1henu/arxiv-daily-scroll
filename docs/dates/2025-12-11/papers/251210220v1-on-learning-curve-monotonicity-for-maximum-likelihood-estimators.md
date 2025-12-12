---
layout: default
title: On Learning-Curve Monotonicity for Maximum Likelihood Estimators
---

# On Learning-Curve Monotonicity for Maximum Likelihood Estimators
**arXiv**：[2512.10220v1](https://arxiv.org/abs/2512.10220) · [PDF](https://arxiv.org/pdf/2512.10220.pdf)  
**作者**：Mark Sellke, Steven Yin  

**一句话要点**：证明最大似然估计器在学习曲线单调性上的非平凡保证，针对高斯和伽马分布等参数设置。

**关键词**：学习曲线单调性, 最大似然估计器, KL散度, 高斯分布, 伽马分布, 参数估计

## 3 点简述
- 核心问题：学习曲线单调性，即算法性能随数据量增加而单调提升，在最大似然估计器中缺乏理论保证。
- 方法要点：使用GPT-5.2 Pro推导变体，证明高斯向量和伽马变量的前向KL散度单调性，并观察指数家族的反向KL散度单调性。
- 实验或效果：首次为高斯协方差未知等开放问题提供单调性证明，覆盖已知和未知均值情况。

## 摘要（原文）

> The property of learning-curve monotonicity, highlighted in a recent series of work by Loog, Mey and Viering, describes algorithms which only improve in average performance given more data, for any underlying data distribution within a given family. We establish the first nontrivial monotonicity guarantees for the maximum likelihood estimator in a variety of well-specified parametric settings. For sequential prediction with log loss, we show monotonicity (in fact complete monotonicity) of the forward KL divergence for Gaussian vectors with unknown covariance and either known or unknown mean, as well as for Gamma variables with unknown scale parameter. The Gaussian setting was explicitly highlighted as open in the aforementioned works, even in dimension 1. Finally we observe that for reverse KL divergence, a folklore trick yields monotonicity for very general exponential families.
>   All results in this paper were derived by variants of GPT-5.2 Pro. Humans did not provide any proof strategies or intermediate arguments, but only prompted the model to continue developing additional results, and verified and transcribed its proofs.

