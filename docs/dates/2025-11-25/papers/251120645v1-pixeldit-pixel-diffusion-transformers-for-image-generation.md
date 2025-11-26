---
layout: default
title: PixelDiT: Pixel Diffusion Transformers for Image Generation
---

# PixelDiT: Pixel Diffusion Transformers for Image Generation
**arXiv**：[2511.20645v1](https://arxiv.org/abs/2511.20645) · [PDF](https://arxiv.org/pdf/2511.20645.pdf)  
**作者**：Yongsheng Yu, Wei Xiong, Weili Nie, Yichen Sheng, Shiqiu Liu, Jiebo Luo  

**一句话要点**：提出PixelDiT以解决潜在空间扩散模型依赖两阶段流程导致的误差累积问题

**关键词**：像素扩散, Transformer架构, 图像生成, 端到端学习, 文本到图像生成

## 3 点简述
- 核心问题：潜在空间扩散模型依赖两阶段流程，引入有损重建和误差累积
- 方法要点：采用单阶段端到端像素空间扩散，结合补丁级和像素级Transformer设计
- 实验或效果：在ImageNet 256x256上FID达1.61，超越现有像素生成模型

## 摘要（原文）

> Latent-space modeling has been the standard for Diffusion Transformers (DiTs). However, it relies on a two-stage pipeline where the pretrained autoencoder introduces lossy reconstruction, leading to error accumulation while hindering joint optimization. To address these issues, we propose PixelDiT, a single-stage, end-to-end model that eliminates the need for the autoencoder and learns the diffusion process directly in the pixel space. PixelDiT adopts a fully transformer-based architecture shaped by a dual-level design: a patch-level DiT that captures global semantics and a pixel-level DiT that refines texture details, enabling efficient training of a pixel-space diffusion model while preserving fine details. Our analysis reveals that effective pixel-level token modeling is essential to the success of pixel diffusion. PixelDiT achieves 1.61 FID on ImageNet 256x256, surpassing existing pixel generative models by a large margin. We further extend PixelDiT to text-to-image generation and pretrain it at the 1024x1024 resolution in pixel space. It achieves 0.74 on GenEval and 83.5 on DPG-bench, approaching the best latent diffusion models.

