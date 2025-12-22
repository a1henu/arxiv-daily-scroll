---
layout: default
title: An Empirical Study of Sampling Hyperparameters in Diffusion-Based Super-Resolution
---

# An Empirical Study of Sampling Hyperparameters in Diffusion-Based Super-Resolution
**arXiv**：[2512.17675v1](https://arxiv.org/abs/2512.17675) · [PDF](https://arxiv.org/pdf/2512.17675.pdf)  
**作者**：Yudhistira Arief Wibowo  

**一句话要点**：实证研究扩散模型超分辨率中采样超参数的影响，发现条件步长比扩散步数更重要。

**关键词**：扩散模型, 超分辨率, 条件采样, 超参数调优, 实证研究, FFHQ数据集

## 3 点简述
- 核心问题：扩散模型用于超分辨率时，条件方法引入的超参数需精细调优，影响性能。
- 方法要点：通过消融实验分析条件步长和扩散步数对FFHQ数据集超分辨率性能的影响。
- 实验或效果：实验表明条件步长在[2.0, 3.0]范围内性能最佳，其影响显著大于扩散步数。

## 摘要（原文）

> Diffusion models have shown strong potential for solving inverse problems such as single-image super-resolution, where a high-resolution image is recovered from a low-resolution observation using a pretrained unconditional prior. Conditioning methods, including Diffusion Posterior Sampling (DPS) and Manifold Constrained Gradient (MCG), can substantially improve reconstruction quality, but they introduce additional hyperparameters that require careful tuning. In this work, we conduct an empirical ablation study on FFHQ super-resolution to identify the dominant factors affecting performance when applying conditioning to pretrained diffusion models, and show that the conditioning step size has a significantly greater impact than the diffusion step count, with step sizes in the range of [2.0, 3.0] yielding the best overall performance in our experiments.

