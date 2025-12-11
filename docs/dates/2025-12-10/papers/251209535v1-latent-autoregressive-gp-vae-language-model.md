---
layout: default
title: Latent-Autoregressive GP-VAE Language Model
---

# Latent-Autoregressive GP-VAE Language Model
**arXiv**：[2512.09535v1](https://arxiv.org/abs/2512.09535) · [PDF](https://arxiv.org/pdf/2512.09535.pdf)  
**作者**：Yves Ruffenach  

**一句话要点**：提出基于高斯过程的潜在自回归GP-VAE语言模型，将序列动态转移至潜在空间以支持部分时间结构。

**关键词**：潜在自回归模型, 高斯过程变分自编码器, 语言模型, 序列建模, 非自回归解码, 概率几何

## 3 点简述
- 核心问题：探索语言模型中时间结构是否可由潜在空间的概率几何而非显式神经操作支持。
- 方法要点：集成高斯过程先验和结构化摊销后验，采用正则化ELBO训练协议，实现非自回归解码。
- 实验或效果：在概念验证框架下，模型训练稳定，序列与并行采样变体表现一致。

## 摘要（原文）

> We investigate a fully Latent AutoRegressive scheme based on a Gaussian Process (GP) integrated into a Variational Autoencoder (VAE). In this setting, sequential dynamics are transferred from the observation space to a continuous latent space, while linguistic generation remains parallel through a non-autoregressive decoder. We present a complete methodological formulation, including a causal GP prior, a structured amortized posterior, and a training protocol based on a regularized ELBO. Empirical evaluation, conducted within a deliberately constrained proof-of-concept (POC) framework, shows that the model can be trained stably and that the sequential and parallel sampling variants exhibit consistent behavior. Overall, the results suggest that part of the temporal structure in a language model can be supported by the probabilistic geometry of the latent space rather than by explicit neural operations.

