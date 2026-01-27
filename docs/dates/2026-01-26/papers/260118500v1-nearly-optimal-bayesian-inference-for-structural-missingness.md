---
layout: default
title: Nearly Optimal Bayesian Inference for Structural Missingness
---

# Nearly Optimal Bayesian Inference for Structural Missingness
**arXiv**：[2601.18500v1](https://arxiv.org/abs/2601.18500) · [PDF](https://arxiv.org/pdf/2601.18500.pdf)  
**作者**：Chen Liang, Donghua Yang, Yutong Wang, Tianle Zhang, Shenghe Zhou, Zhiyu Liang, Hengtong Zhang, Hongzhi Wang, Ziqi Li, Xiyang Zhang, Zheng Liang, Yifei Li  

**一句话要点**：提出贝叶斯推断框架以解决结构化缺失下的因果循环和分布偏移问题

**关键词**：结构化缺失, 贝叶斯推断, 后验预测分布, MNAR处理, 不确定性传播, 因果模型

## 3 点简述
- 结构化缺失导致因果循环和MNAR分布偏移，传统插值方法存在偏差
- 通过后验预测分布解耦缺失值推断与标签预测，实现不确定性传播
- 在43个分类和15个插值基准上达到SOTA，并提供有限样本近贝叶斯最优性保证

## 摘要（原文）

> Structural missingness breaks 'just impute and train': values can be undefined by causal or logical constraints, and the mask may depend on observed variables, unobserved variables (MNAR), and other missingness indicators. It simultaneously brings (i) a catch-22 situation with causal loop, prediction needs the missing features, yet inferring them depends on the missingness mechanism, (ii) under MNAR, the unseen are different, the missing part can come from a shifted distribution, and (iii) plug-in imputation, a single fill-in can lock in uncertainty and yield overconfident, biased decisions. In the Bayesian view, prediction via the posterior predictive distribution integrates over the full model posterior uncertainty, rather than relying on a single point estimate. This framework decouples (i) learning an in-model missing-value posterior from (ii) label prediction by optimizing the predictive posterior distribution, enabling posterior integration. This decoupling yields an in-model almost-free-lunch: once the posterior is learned, prediction is plug-and-play while preserving uncertainty propagation. It achieves SOTA on 43 classification and 15 imputation benchmarks, with finite-sample near Bayes-optimality guarantees under our SCM prior.

