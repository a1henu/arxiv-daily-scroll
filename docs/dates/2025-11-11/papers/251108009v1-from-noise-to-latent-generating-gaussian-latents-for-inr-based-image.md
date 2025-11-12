---
layout: default
title: From Noise to Latent: Generating Gaussian Latents for INR-Based Image Compression
---

# From Noise to Latent: Generating Gaussian Latents for INR-Based Image Compression
**arXiv**：[2511.08009v1](https://arxiv.org/abs/2511.08009) · [PDF](https://arxiv.org/pdf/2511.08009.pdf)  
**作者**：Chaoyi Lin, Yaojun Wu, Yue Li, Junru Li, Kai Zhang, Li Zhang  

**一句话要点**：提出从高斯噪声生成隐变量以消除隐码传输的图像压缩方法

**关键词**：图像压缩, 隐式神经表示, 高斯噪声生成, 隐变量预测, 率失真优化

## 3 点简述
- 核心问题：INR图像压缩方法因隐码表达能力不足而性能劣于端到端方法
- 方法要点：使用共享随机种子生成多尺度高斯噪声，通过重参数化预测隐变量
- 实验或效果：在Kodak和CLIC数据集上实现竞争性率失真性能

## 摘要（原文）

> Recent implicit neural representation (INR)-based image compression methods have shown competitive performance by overfitting image-specific latent codes. However, they remain inferior to end-to-end (E2E) compression approaches due to the absence of expressive latent representations. On the other hand, E2E methods rely on transmitting latent codes and requiring complex entropy models, leading to increased decoding complexity. Inspired by the normalization strategy in E2E codecs where latents are transformed into Gaussian noise to demonstrate the removal of spatial redundancy, we explore the inverse direction: generating latents directly from Gaussian noise. In this paper, we propose a novel image compression paradigm that reconstructs image-specific latents from a multi-scale Gaussian noise tensor, deterministically generated using a shared random seed. A Gaussian Parameter Prediction (GPP) module estimates the distribution parameters, enabling one-shot latent generation via reparameterization trick. The predicted latent is then passed through a synthesis network to reconstruct the image. Our method eliminates the need to transmit latent codes while preserving latent-based benefits, achieving competitive rate-distortion performance on Kodak and CLIC dataset. To the best of our knowledge, this is the first work to explore Gaussian latent generation for learned image compression.

