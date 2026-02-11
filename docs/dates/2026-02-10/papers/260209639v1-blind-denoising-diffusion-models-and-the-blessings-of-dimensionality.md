---
layout: default
title: Blind denoising diffusion models and the blessings of dimensionality
---

# Blind denoising diffusion models and the blessings of dimensionality
**arXiv**：[2602.09639v1](https://arxiv.org/abs/2602.09639) · [PDF](https://arxiv.org/pdf/2602.09639.pdf)  
**作者**：Zahra Kadkhodaie, Aram-Alexandre Pooladian, Sinho Chewi, Eero Simoncelli  

**一句话要点**：提出盲去噪扩散模型，利用低内在维度实现高效采样并提升样本质量。

**关键词**：盲去噪扩散模型, 低内在维度, 隐式噪声计划, 样本质量提升, 扩散模型理论分析

## 3 点简述
- 核心问题：传统扩散模型依赖噪声幅度信息，盲去噪模型在训练和采样中不提供此信息。
- 方法要点：基于低内在维度假设，盲去噪模型自动追踪隐式噪声计划，实现多项式步数采样。
- 实验或效果：在合成和图像数据上验证，盲去噪模型准确估计噪声方差，样本质量优于非盲模型。

## 摘要（原文）

> We analyze, theoretically and empirically, the performance of generative diffusion models based on \emph{blind denoisers}, in which the denoiser is not given the noise amplitude in either the training or sampling processes. Assuming that the data distribution has low intrinsic dimensionality, we prove that blind denoising diffusion models (BDDMs), despite not having access to the noise amplitude, \emph{automatically} track a particular \emph{implicit} noise schedule along the reverse process. Our analysis shows that BDDMs can accurately sample from the data distribution in polynomially many steps as a function of the intrinsic dimension. Empirical results corroborate these mathematical findings on both synthetic and image data, demonstrating that the noise variance is accurately estimated from the noisy image. Remarkably, we observe that schedule-free BDDMs produce samples of higher quality compared to their non-blind counterparts. We provide evidence that this performance gain arises because BDDMs correct the mismatch between the true residual noise (of the image) and the noise assumed by the schedule used in non-blind diffusion models.

