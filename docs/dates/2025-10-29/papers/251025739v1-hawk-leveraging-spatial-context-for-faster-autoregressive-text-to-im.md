---
layout: default
title: Hawk: Leveraging Spatial Context for Faster Autoregressive Text-to-Image Generation
---

# Hawk: Leveraging Spatial Context for Faster Autoregressive Text-to-Image Generation
**arXiv**：[2510.25739v1](https://arxiv.org/abs/2510.25739) · [PDF](https://arxiv.org/pdf/2510.25739.pdf)  
**作者**：Zhi-Kai Chen, Jun-Peng Jiang, Han-Jia Ye, De-Chuan Zhan  

**一句话要点**：提出Hawk方法，利用图像空间结构加速自回归文本到图像生成

**关键词**：自回归图像生成, 推测解码, 空间上下文建模, 文本到图像, 加速推理

## 3 点简述
- 自回归图像生成模型推理慢，因序列解码和大采样空间导致对齐困难
- Hawk利用图像二维空间结构，指导草稿模型更准确预测局部依赖
- 实验显示在多个基准上实现1.71倍加速，保持图像保真度和多样性

## 摘要（原文）

> Autoregressive (AR) image generation models are capable of producing
> high-fidelity images but often suffer from slow inference due to their
> inherently sequential, token-by-token decoding process. Speculative decoding,
> which employs a lightweight draft model to approximate the output of a larger
> AR model, has shown promise in accelerating text generation without
> compromising quality. However, its application to image generation remains
> largely underexplored. The challenges stem from a significantly larger sampling
> space, which complicates the alignment between the draft and target model
> outputs, coupled with the inadequate use of the two-dimensional spatial
> structure inherent in images, thereby limiting the modeling of local
> dependencies. To overcome these challenges, we introduce Hawk, a new approach
> that harnesses the spatial structure of images to guide the speculative model
> toward more accurate and efficient predictions. Experimental results on
> multiple text-to-image benchmarks demonstrate a 1.71x speedup over standard AR
> models, while preserving both image fidelity and diversity.

