---
layout: default
title: Beyond NNGP: Large Deviations and Feature Learning in Bayesian Neural Networks
---

# Beyond NNGP: Large Deviations and Feature Learning in Bayesian Neural Networks
**arXiv**：[2602.22925v1](https://arxiv.org/abs/2602.22925) · [PDF](https://arxiv.org/pdf/2602.22925.pdf)  
**作者**：Katerina Papagiannouli, Dario Trevisan, Giuseppe Pio Zitto  

**一句话要点**：提出基于大偏差理论的变分目标，以超越高斯过程极限，研究贝叶斯神经网络的后验集中与特征学习。

**关键词**：贝叶斯神经网络, 大偏差理论, 后验集中, 特征学习, 变分优化, 核选择

## 3 点简述
- 核心问题：研究宽贝叶斯神经网络中控制后验集中的罕见但统计主导的波动，超越高斯过程极限。
- 方法要点：利用大偏差理论在预测器上定义变分目标（率函数），通过联合优化预测器和内部核实现特征学习。
- 实验或效果：数值实验表明，该方法能准确描述中等规模网络的有限宽度行为，捕捉非高斯尾部、后验变形和数据依赖核选择效应。

## 摘要（原文）

> We study wide Bayesian neural networks focusing on the rare but statistically dominant fluctuations that govern posterior concentration, beyond Gaussian-process limits. Large-deviation theory provides explicit variational objectives-rate functions-on predictors, providing an emerging notion of complexity and feature learning directly at the functional level. We show that the posterior output rate function is obtained by a joint optimization over predictors and internal kernels, in contrast with fixed-kernel (NNGP) theory. Numerical experiments demonstrate that the resulting predictions accurately describe finite-width behavior for moderately sized networks, capturing non-Gaussian tails, posterior deformation, and data-dependent kernel selection effects.

