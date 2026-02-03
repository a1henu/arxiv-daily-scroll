---
layout: default
title: Observation-dependent Bayesian active learning via input-warped Gaussian processes
---

# Observation-dependent Bayesian active learning via input-warped Gaussian processes
**arXiv**：[2602.01898v1](https://arxiv.org/abs/2602.01898) · [PDF](https://arxiv.org/pdf/2602.01898.pdf)  
**作者**：Sanna Jarl, Maria Bånkestad, Jonathan J. S. Scragg, Jens Sjölund  

**一句话要点**：提出输入扭曲高斯过程以增强贝叶斯主动学习的观测依赖性

**关键词**：贝叶斯主动学习, 高斯过程, 输入扭曲, 观测依赖性, 样本效率, 非平稳性

## 3 点简述
- 核心问题：高斯过程后验方差仅依赖超参数，导致探索对实际观测不敏感。
- 方法要点：通过单调重参数化扭曲输入空间，使设计策略能根据观测变异性调整区域扩展或压缩。
- 实验或效果：在主动学习基准测试中提高样本效率，尤其在非平稳性挑战传统方法的场景中表现更佳。

## 摘要（原文）

> Bayesian active learning relies on the precise quantification of predictive uncertainty to explore unknown function landscapes. While Gaussian process surrogates are the standard for such tasks, an underappreciated fact is that their posterior variance depends on the observed outputs only through the hyperparameters, rendering exploration largely insensitive to the actual measurements. We propose to inject observation-dependent feedback by warping the input space with a learned, monotone reparameterization. This mechanism allows the design policy to expand or compress regions of the input space in response to observed variability, thereby shaping the behavior of variance-based acquisition functions. We demonstrate that while such warps can be trained via marginal likelihood, a novel self-supervised objective yields substantially better performance. Our approach improves sample efficiency across a range of active learning benchmarks, particularly in regimes where non-stationarity challenges traditional methods.

