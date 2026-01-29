---
layout: default
title: Bias-Reduced Estimation of Finite Mixtures: An Application to Latent Group Structures in Panel Data
---

# Bias-Reduced Estimation of Finite Mixtures: An Application to Latent Group Structures in Panel Data
**arXiv**：[2601.20197v1](https://arxiv.org/abs/2601.20197) · [PDF](https://arxiv.org/pdf/2601.20197.pdf)  
**作者**：Raphaël Langevin  

**一句话要点**：提出基于分类-混合似然函数的估计方法以减少有限混合模型参数估计的偏差

**关键词**：有限混合模型, 参数估计偏差, 分类-混合似然, 面板数据, 渐近效率

## 3 点简述
- 核心问题：有限混合模型的最大似然估计在有限样本下存在显著偏差，尤其在组分重叠时
- 方法要点：使用一致分类器最大化分类-混合似然函数，降低偏差并实现渐近效率
- 实验或效果：模拟显示新方法在偏差和均方误差上优于标准MLE，实证应用减少预测误差约17.6%

## 摘要（原文）

> Finite mixture models are widely used in econometric analyses to capture unobserved heterogeneity. This paper shows that maximum likelihood estimation of finite mixtures of parametric densities can suffer from substantial finite-sample bias in all parameters under mild regularity conditions. The bias arises from the influence of outliers in component densities with unbounded or large support and increases with the degree of overlap among mixture components. I show that maximizing the classification-mixture likelihood function, equipped with a consistent classifier, yields parameter estimates that are less biased than those obtained by standard maximum likelihood estimation (MLE). I then derive the asymptotic distribution of the resulting estimator and provide conditions under which oracle efficiency is achieved. Monte Carlo simulations show that conventional mixture MLE exhibits pronounced finite-sample bias, which diminishes as the sample size or the statistical distance between component densities tends to infinity. The simulations further show that the proposed estimation strategy generally outperforms standard MLE in finite samples in terms of both bias and mean squared errors under relatively weak assumptions. An empirical application to latent group panel structures using health administrative data shows that the proposed approach reduces out-of-sample prediction error by approximately 17.6% relative to the best results obtained from standard MLE procedures.

