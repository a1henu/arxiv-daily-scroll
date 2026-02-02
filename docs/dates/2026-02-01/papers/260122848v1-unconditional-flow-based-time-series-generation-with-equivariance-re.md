---
layout: default
title: Unconditional flow-based time series generation with equivariance-regularised latent spaces
---

# Unconditional flow-based time series generation with equivariance-regularised latent spaces
**arXiv**：[2601.22848v1](https://arxiv.org/abs/2601.22848) · [PDF](https://arxiv.org/pdf/2601.22848.pdf)  
**作者**：Camilo Carvajal Reyes, Felipe Tobar  

**一句话要点**：提出基于等变性正则化潜在空间的流匹配框架，以提升时间序列生成质量与效率。

**关键词**：时间序列生成, 流匹配模型, 等变性正则化, 潜在空间优化, 快速采样

## 3 点简述
- 核心问题：现有流模型在时间序列生成中，潜在空间设计缺乏等变性，影响生成效果。
- 方法要点：通过等变性损失正则化预训练自编码器，强制变换信号与重建的一致性。
- 实验或效果：在多个真实数据集上，生成质量优于扩散基线，采样速度大幅提升。

## 摘要（原文）

> Flow-based models have proven successful for time-series generation, particularly when defined in lower-dimensional latent spaces that enable efficient sampling. However, how to design latent representations with desirable equivariance properties for time-series generative modelling remains underexplored. In this work, we propose a latent flow-matching framework in which equivariance is explicitly encouraged through a simple regularisation of a pre-trained autoencoder. Specifically, we introduce an equivariance loss that enforces consistency between transformed signals and their reconstructions, and use it to fine-tune latent spaces with respect to basic time-series transformations such as translation and amplitude scaling. We show that these equivariance-regularised latent spaces improve generation quality while preserving the computational advantages of latent flow models. Experiments on multiple real-world datasets demonstrate that our approach consistently outperforms existing diffusion-based baselines in standard time-series generation metrics, while achieving orders-of-magnitude faster sampling. These results highlight the practical benefits of incorporating geometric inductive biases into latent generative models for time series.

