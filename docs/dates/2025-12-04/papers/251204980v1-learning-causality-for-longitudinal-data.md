---
layout: default
title: Learning Causality for Longitudinal Data
---

# Learning Causality for Longitudinal Data
**arXiv**：[2512.04980v1](https://arxiv.org/abs/2512.04980) · [PDF](https://arxiv.org/pdf/2512.04980.pdf)  
**作者**：Mouad EL Bouchattaoui  

**一句话要点**：提出CDVAE与增强RNN框架以解决高维时序数据中的因果推断与表示学习问题

**关键词**：因果推断, 时序数据, 变分自编码器, 循环神经网络, 对比预测编码, 表示学习

## 3 点简述
- 核心问题：高维时序数据中因果推断与表示学习，处理未观测异质性和时变混杂
- 方法要点：CDVAE估计个体处理效应，RNN结合CPC捕获长程依赖，几何方法解释潜在原因
- 实验或效果：CDVAE优于基线，增强模型接近Oracle性能，框架实现高效长程反事实回归

## 摘要（原文）

> This thesis develops methods for causal inference and causal representation learning (CRL) in high-dimensional, time-varying data.
>   The first contribution introduces the Causal Dynamic Variational Autoencoder (CDVAE), a model for estimating Individual Treatment Effects (ITEs) by capturing unobserved heterogeneity in treatment response driven by latent risk factors that affect only outcomes. CDVAE comes with theoretical guarantees on valid latent adjustment and generalization bounds for ITE error. Experiments on synthetic and real datasets show that CDVAE outperforms baselines, and that state-of-the-art models greatly improve when augmented with its latent substitutes, approaching oracle performance without access to true adjustment variables.
>   The second contribution proposes an efficient framework for long-term counterfactual regression based on RNNs enhanced with Contrastive Predictive Coding (CPC) and InfoMax. It captures long-range dependencies under time-varying confounding while avoiding the computational cost of transformers, achieving state-of-the-art results and introducing CPC into causal inference.
>   The third contribution advances CRL by addressing how latent causes manifest in observed variables. We introduce a model-agnostic interpretability layer based on the geometry of the decoder Jacobian. A sparse self-expression prior induces modular, possibly overlapping groups of observed features aligned with shared latent influences. We provide recovery guarantees in both disjoint and overlapping settings and show that meaningful latent-to-observed structure can be recovered without anchor features or single-parent assumptions. Scalable Jacobian-based regularization techniques are also developed.

