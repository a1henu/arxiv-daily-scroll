---
layout: default
title: Sawtooth Sampling for Time Series Denoising Diffusion Implicit Models
---

# Sawtooth Sampling for Time Series Denoising Diffusion Implicit Models
**arXiv**：[2511.21320v1](https://arxiv.org/abs/2511.21320) · [PDF](https://arxiv.org/pdf/2511.21320.pdf)  
**作者**：Heiko Oppel, Andreas Spilz, Michael Munz  

**一句话要点**：提出Sawtooth采样器以加速时间序列去噪扩散隐式模型的采样过程

**关键词**：时间序列生成, 去噪扩散模型, 采样加速, 隐式扩散模型, 分类任务增强

## 3 点简述
- 核心问题：去噪扩散概率模型采样过程计算成本高，影响时间序列数据生成效率
- 方法要点：结合隐式扩散模型与新型Sawtooth采样器，可加速任何预训练扩散模型的反向过程
- 实验或效果：在分类任务中，实现30倍加速并提升生成序列质量

## 摘要（原文）

> Denoising Diffusion Probabilistic Models (DDPMs) can generate synthetic timeseries data to help improve the performance of a classifier, but their sampling process is computationally expensive. We address this by combining implicit diffusion models with a novel Sawtooth Sampler that accelerates the reverse process and can be applied to any pretrained diffusion model. Our approach achieves a 30 times speed-up over the standard baseline while also enhancing the quality of the generated sequences for classification tasks.

