---
layout: default
title: FraQAT: Quantization Aware Training with Fractional bits
---

# FraQAT: Quantization Aware Training with Fractional bits
**arXiv**：[2510.14823v1](https://arxiv.org/abs/2510.14823) · [PDF](https://arxiv.org/pdf/2510.14823.pdf)  
**作者**：Luca Morreale, Alberto Gil C. P. Ramos, Malcolm Chadwick, Mehid Noroozi, Ruchika Chavhan, Abhinav Mehrotra, Sourav Bhattacharya  

**一句话要点**：提出分数位量化方法以在移动设备上保持生成模型质量

**关键词**：量化感知训练, 分数位量化, 生成模型, 移动部署, 扩散模型

## 3 点简述
- 核心问题：大模型量化后质量下降，难以部署于内存受限设备
- 方法要点：渐进降低精度至4位，利用分数位优化保持生成质量
- 实验或效果：在多种扩散模型上实现更低FiD，成功部署于三星手机

## 摘要（原文）

> State-of-the-art (SOTA) generative models have demonstrated impressive
> capabilities in image synthesis or text generation, often with a large capacity
> model. However, these large models cannot be deployed on smartphones due to the
> limited availability of on-board memory and computations. Quantization methods
> lower the precision of the model parameters, allowing for efficient
> computations, \eg, in \INT{8}. Although aggressive quantization addresses
> efficiency and memory constraints, preserving the quality of the model remains
> a challenge. To retain quality in previous aggressive quantization, we propose
> a new fractional bits quantization (\short) approach. The novelty is a simple
> yet effective idea: we progressively reduce the model's precision from 32 to 4
> bits per parameter, and exploit the fractional bits during optimization to
> maintain high generation quality. We show that the \short{} yields improved
> quality on a variety of diffusion models, including SD3.5-Medium, Sana,
> \pixart, and FLUX.1-schnell, while achieving $4-7\%$ lower FiD than standard
> QAT. Finally, we deploy and run Sana on a Samsung S25U, which runs on the
> Qualcomm SM8750-AB Snapdragon 8 Elite Hexagon Tensor Processor (HTP).

