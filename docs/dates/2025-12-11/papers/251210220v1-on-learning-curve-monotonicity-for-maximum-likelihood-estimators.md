---
layout: default
title: On Learning-Curve Monotonicity for Maximum Likelihood Estimators
---

# On Learning-Curve Monotonicity for Maximum Likelihood Estimators
**arXiv**：[2512.10220v1](https://arxiv.org/abs/2512.10220) · [PDF](https://arxiv.org/pdf/2512.10220.pdf)  
**作者**：Mark Sellke, Steven Yin  

**一句话要点**：证明最大似然估计器在多种参数设置下的学习曲线单调性，包括高斯和Gamma分布

**关键词**：学习曲线单调性, 最大似然估计, KL散度, 高斯分布, Gamma分布, 参数估计

## 3 点简述
- 研究学习曲线单调性，即算法随数据增加平均性能提升的性质
- 针对高斯向量和Gamma变量，证明前向KL散度的单调性，解决开放问题
- 使用GPT-5.2 Pro生成所有结果，人类仅验证和转录证明

## 摘要（原文）

> The property of learning-curve monotonicity, highlighted in a recent series of work by Loog, Mey and Viering, describes algorithms which only improve in average performance given more data, for any underlying data distribution within a given family. We establish the first nontrivial monotonicity guarantees for the maximum likelihood estimator in a variety of well-specified parametric settings. For sequential prediction with log loss, we show monotonicity (in fact complete monotonicity) of the forward KL divergence for Gaussian vectors with unknown covariance and either known or unknown mean, as well as for Gamma variables with unknown scale parameter. The Gaussian setting was explicitly highlighted as open in the aforementioned works, even in dimension 1. Finally we observe that for reverse KL divergence, a folklore trick yields monotonicity for very general exponential families.
>   All results in this paper were derived by variants of GPT-5.2 Pro. Humans did not provide any proof strategies or intermediate arguments, but only prompted the model to continue developing additional results, and verified and transcribed its proofs.

