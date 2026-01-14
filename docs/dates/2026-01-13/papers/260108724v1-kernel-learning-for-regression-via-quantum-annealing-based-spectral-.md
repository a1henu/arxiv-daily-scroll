---
layout: default
title: Kernel Learning for Regression via Quantum Annealing Based Spectral Sampling
---

# Kernel Learning for Regression via Quantum Annealing Based Spectral Sampling
**arXiv**：[2601.08724v1](https://arxiv.org/abs/2601.08724) · [PDF](https://arxiv.org/pdf/2601.08724.pdf)  
**作者**：Yasushi Hasegawa, Masayuki Ohzeki  

**一句话要点**：提出基于量子退火的谱采样核学习方法，用于回归任务以提升性能。

**关键词**：量子退火, 核学习, 随机傅里叶特征, 受限玻尔兹曼机, 回归分析, Nadaraya-Watson回归

## 3 点简述
- 核心问题：量子退火在有限温度和噪声下输出近似吉布斯-玻尔兹曼分布的样本，如何有效用于核学习。
- 方法要点：利用受限玻尔兹曼机建模谱分布，通过量子退火采样离散频率并映射为随机傅里叶特征，构建数据自适应核。
- 实验或效果：在多个基准回归数据集上，训练损失降低，核矩阵结构变化，R²和RMSE优于基线高斯核方法。

## 摘要（原文）

> While quantum annealing (QA) has been developed for combinatorial optimization, practical QA devices operate at finite temperature and under noise, and their outputs can be regarded as stochastic samples close to a Gibbs--Boltzmann distribution. In this study, we propose a QA-in-the-loop kernel learning framework that integrates QA not merely as a substitute for Markov-chain Monte Carlo sampling but as a component that directly determines the learned kernel for regression. Based on Bochner's theorem, a shift-invariant kernel is represented as an expectation over a spectral distribution, and random Fourier features (RFF) approximate the kernel by sampling frequencies. We model the spectral distribution with a (multi-layer) restricted Boltzmann machine (RBM), generate discrete RBM samples using QA, and map them to continuous frequencies via a Gaussian--Bernoulli transformation. Using the resulting RFF, we construct a data-adaptive kernel and perform Nadaraya--Watson (NW) regression. Because the RFF approximation based on $\cos(\bmω^{\top}Δ\bm{x})$ can yield small negative values and cancellation across neighbors, the Nadaraya--Watson denominator $\sum_j k_{ij}$ may become close to zero. We therefore employ nonnegative squared-kernel weights $w_{ij}=k(\bm{x}_i,\bm{x}_j)^2$, which also enhances the contrast of kernel weights. The kernel parameters are trained by minimizing the leave-one-out NW mean squared error, and we additionally evaluate local linear regression with the same squared-kernel weights at inference. Experiments on multiple benchmark regression datasets demonstrate a decrease in training loss, accompanied by structural changes in the kernel matrix, and show that the learned kernel tends to improve $R^2$ and RMSE over the baseline Gaussian-kernel NW. Increasing the number of random features at inference further enhances accuracy.

