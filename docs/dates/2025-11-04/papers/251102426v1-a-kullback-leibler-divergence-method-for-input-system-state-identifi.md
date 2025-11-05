---
layout: default
title: A Kullback-Leibler divergence method for input-system-state identification
---

# A Kullback-Leibler divergence method for input-system-state identification
**arXiv**：[2511.02426v1](https://arxiv.org/abs/2511.02426) · [PDF](https://arxiv.org/pdf/2511.02426.pdf)  
**作者**：Marios Impraimakis  

**一句话要点**：提出基于Kullback-Leibler散度的方法，在Kalman滤波框架中选择最可信的输入-参数-状态估计

**关键词**：Kullback-Leibler散度, Kalman滤波, 系统识别, 参数估计, 不确定性量化

## 3 点简述
- 核心问题：不同初始参数集导致估计结果不确定性，影响系统识别准确性。
- 方法要点：使用KL散度比较先验与后验分布，选择散度最小的估计作为最优结果。
- 实验或效果：在线性、非线性和信息有限应用中，方法能选择性能更好的识别。

## 摘要（原文）

> The capability of a novel Kullback-Leibler divergence method is examined
> herein within the Kalman filter framework to select the input-parameter-state
> estimation execution with the most plausible results. This identification
> suffers from the uncertainty related to obtaining different results from
> different initial parameter set guesses, and the examined approach uses the
> information gained from the data in going from the prior to the posterior
> distribution to address the issue. Firstly, the Kalman filter is performed for
> a number of different initial parameter sets providing the system
> input-parameter-state estimation. Secondly, the resulting posterior
> distributions are compared simultaneously to the initial prior distributions
> using the Kullback-Leibler divergence. Finally, the identification with the
> least Kullback-Leibler divergence is selected as the one with the most
> plausible results. Importantly, the method is shown to select the better
> performed identification in linear, nonlinear, and limited information
> applications, providing a powerful tool for system monitoring.

