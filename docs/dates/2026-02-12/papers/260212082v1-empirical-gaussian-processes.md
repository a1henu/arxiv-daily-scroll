---
layout: default
title: Empirical Gaussian Processes
---

# Empirical Gaussian Processes
**arXiv**：[2602.12082v1](https://arxiv.org/abs/2602.12082) · [PDF](https://arxiv.org/pdf/2602.12082.pdf)  
**作者**：Jihao Andreas Lin, Sebastian Ament, Louis C. Tiao, David Eriksson, Maximilian Balandat, Eytan Bakshy  

**一句话要点**：提出经验高斯过程以解决传统核函数选择受限问题，通过数据驱动构建灵活先验。

**关键词**：高斯过程, 经验先验, 核函数学习, 数据驱动建模, EM算法, 时间序列预测

## 3 点简述
- 核心问题：高斯过程依赖手工核函数，需专家知识且假设强，限制模型适应性和性能。
- 方法要点：从历史数据中经验估计均值和协方差函数，构建数据驱动先验，并推导EM算法处理异构数据集。
- 实验或效果：在曲线外推和时间序列预测基准上实现竞争性性能，理论证明模型收敛于真实数据生成过程。

## 摘要（原文）

> Gaussian processes (GPs) are powerful and widely used probabilistic regression models, but their effectiveness in practice is often limited by the choice of kernel function. This kernel function is typically handcrafted from a small set of standard functions, a process that requires expert knowledge, results in limited adaptivity to data, and imposes strong assumptions on the hypothesis space. We study Empirical GPs, a principled framework for constructing flexible, data-driven GP priors that overcome these limitations. Rather than relying on standard parametric kernels, we estimate the mean and covariance functions empirically from a corpus of historical observations, enabling the prior to reflect rich, non-trivial covariance structures present in the data. Theoretically, we show that the resulting model converges to the GP that is closest (in KL-divergence sense) to the real data generating process. Practically, we formulate the problem of learning the GP prior from independent datasets as likelihood estimation and derive an Expectation-Maximization algorithm with closed-form updates, allowing the model handle heterogeneous observation locations across datasets. We demonstrate that Empirical GPs achieve competitive performance on learning curve extrapolation and time series forecasting benchmarks.

