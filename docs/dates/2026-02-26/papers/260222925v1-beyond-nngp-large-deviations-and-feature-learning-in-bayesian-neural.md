---
layout: default
title: Beyond NNGP: Large Deviations and Feature Learning in Bayesian Neural Networks
---

# Beyond NNGP: Large Deviations and Feature Learning in Bayesian Neural Networks
**arXiv**：[2602.22925v1](https://arxiv.org/abs/2602.22925) · [PDF](https://arxiv.org/pdf/2602.22925.pdf)  
**作者**：Katerina Papagiannouli, Dario Trevisan, Giuseppe Pio Zitto  

**一句话要点**：提出基于大偏差理论的贝叶斯神经网络分析框架，超越高斯过程极限以研究后验集中和特征学习。

**关键词**：贝叶斯神经网络, 大偏差理论, 后验集中, 特征学习, 高斯过程极限, 变分优化

## 3 点简述
- 研究宽贝叶斯神经网络中罕见但统计主导的波动，这些波动控制后验集中，超越高斯过程极限。
- 利用大偏差理论在预测器层面提供变分目标（率函数），直接定义复杂性和特征学习的新概念。
- 数值实验表明，该方法能准确描述中等规模网络的有限宽度行为，捕捉非高斯尾部、后验变形和数据依赖的核选择效应。

## 摘要（原文）

> We study wide Bayesian neural networks focusing on the rare but statistically dominant fluctuations that govern posterior concentration, beyond Gaussian-process limits. Large-deviation theory provides explicit variational objectives-rate functions-on predictors, providing an emerging notion of complexity and feature learning directly at the functional level. We show that the posterior output rate function is obtained by a joint optimization over predictors and internal kernels, in contrast with fixed-kernel (NNGP) theory. Numerical experiments demonstrate that the resulting predictions accurately describe finite-width behavior for moderately sized networks, capturing non-Gaussian tails, posterior deformation, and data-dependent kernel selection effects.

