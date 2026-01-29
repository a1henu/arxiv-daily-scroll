---
layout: default
title: Hyperparameter Transfer with Mixture-of-Expert Layers
---

# Hyperparameter Transfer with Mixture-of-Expert Layers
**arXiv**：[2601.20205v1](https://arxiv.org/abs/2601.20205) · [PDF](https://arxiv.org/pdf/2601.20205.pdf)  
**作者**：Tianze Jiang, Blake Bordelon, Cengiz Pehlevan, Boris Hanin  

**一句话要点**：提出基于动态平均场理论的参数化方法，以解决混合专家层超参数迁移问题。

**关键词**：混合专家层, 超参数调优, 动态平均场理论, 参数化方法, 模型扩展

## 3 点简述
- 混合专家层引入新参数和架构维度，增加超参数调优复杂性。
- 通过动态平均场理论分析，提出可扩展的模型参数化方案。
- 实验表明，该方法能在不同规模模型间实现可靠的超参数迁移。

## 摘要（原文）

> Mixture-of-Experts (MoE) layers have emerged as an important tool in scaling up modern neural networks by decoupling total trainable parameters from activated parameters in the forward pass for each token. However, sparse MoEs add complexity to training due to (i) new trainable parameters (router weights) that, like all other parameter groups, require hyperparameter (HP) tuning; (ii) new architecture scale dimensions (number of and size of experts) that must be chosen and potentially taken large. To make HP selection cheap and reliable, we propose a new parameterization for transformer models with MoE layers when scaling model width, depth, number of experts, and expert (hidden) size. Our parameterization is justified by a novel dynamical mean-field theory (DMFT) analysis. When varying different model dimensions trained at a fixed token budget, we find empirically that our parameterization enables reliable HP transfer across models from 51M to over 2B total parameters. We further take HPs identified from sweeping small models on a short token horizon to train larger models on longer horizons and report performant model behaviors.

