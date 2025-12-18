---
layout: default
title: Generative Preprocessing for Image Compression with Pre-trained Diffusion Models
---

# Generative Preprocessing for Image Compression with Pre-trained Diffusion Models
**arXiv**：[2512.15270v1](https://arxiv.org/abs/2512.15270) · [PDF](https://arxiv.org/pdf/2512.15270.pdf)  
**作者**：Mengxi Guo, Shijie Zhao, Junlin Li, Li Zhang  

**一句话要点**：提出基于预训练扩散模型的生成预处理方法，以优化图像压缩的率-感知性能。

**关键词**：图像压缩, 扩散模型, 率-感知优化, 模型蒸馏, 预处理技术

## 3 点简述
- 核心问题：现有压缩预处理方法受限于像素级保真度，缺乏率-感知优化。
- 方法要点：通过蒸馏和微调预训练扩散模型，构建两阶段框架，集成标准编解码器。
- 实验或效果：在Kodak数据集上实现高达30.13%的BD-rate降低，提升主观视觉质量。

## 摘要（原文）

> Preprocessing is a well-established technique for optimizing compression, yet existing methods are predominantly Rate-Distortion (R-D) optimized and constrained by pixel-level fidelity. This work pioneers a shift towards Rate-Perception (R-P) optimization by, for the first time, adapting a large-scale pre-trained diffusion model for compression preprocessing. We propose a two-stage framework: first, we distill the multi-step Stable Diffusion 2.1 into a compact, one-step image-to-image model using Consistent Score Identity Distillation (CiD). Second, we perform a parameter-efficient fine-tuning of the distilled model's attention modules, guided by a Rate-Perception loss and a differentiable codec surrogate. Our method seamlessly integrates with standard codecs without any modification and leverages the model's powerful generative priors to enhance texture and mitigate artifacts. Experiments show substantial R-P gains, achieving up to a 30.13% BD-rate reduction in DISTS on the Kodak dataset and delivering superior subjective visual quality.

