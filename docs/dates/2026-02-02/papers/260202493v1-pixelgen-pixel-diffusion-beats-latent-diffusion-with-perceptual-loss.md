---
layout: default
title: PixelGen: Pixel Diffusion Beats Latent Diffusion with Perceptual Loss
---

# PixelGen: Pixel Diffusion Beats Latent Diffusion with Perceptual Loss
**arXiv**：[2602.02493v1](https://arxiv.org/abs/2602.02493) · [PDF](https://arxiv.org/pdf/2602.02493.pdf)  
**作者**：Zehong Ma, Ruihan Xu, Shiliang Zhang  

**一句话要点**：提出PixelGen，通过感知损失监督像素扩散，超越潜在扩散模型性能。

**关键词**：像素扩散, 感知损失, 图像生成, 端到端训练, 扩散模型

## 3 点简述
- 核心问题：像素扩散在高维像素空间中优化困难，包含感知无关信号，性能落后于潜在扩散。
- 方法要点：引入LPIPS和DINO感知损失，引导模型学习感知流形，无需VAE或潜在表示。
- 实验或效果：在ImageNet-256上FID达5.11，大规模文本到图像生成GenEval得分0.79，训练仅80轮。

## 摘要（原文）

> Pixel diffusion generates images directly in pixel space in an end-to-end manner, avoiding the artifacts and bottlenecks introduced by VAEs in two-stage latent diffusion. However, it is challenging to optimize high-dimensional pixel manifolds that contain many perceptually irrelevant signals, leaving existing pixel diffusion methods lagging behind latent diffusion models. We propose PixelGen, a simple pixel diffusion framework with perceptual supervision. Instead of modeling the full image manifold, PixelGen introduces two complementary perceptual losses to guide diffusion model towards learning a more meaningful perceptual manifold. An LPIPS loss facilitates learning better local patterns, while a DINO-based perceptual loss strengthens global semantics. With perceptual supervision, PixelGen surpasses strong latent diffusion baselines. It achieves an FID of 5.11 on ImageNet-256 without classifier-free guidance using only 80 training epochs, and demonstrates favorable scaling performance on large-scale text-to-image generation with a GenEval score of 0.79. PixelGen requires no VAEs, no latent representations, and no auxiliary stages, providing a simpler yet more powerful generative paradigm. Codes are publicly available at https://github.com/Zehong-Ma/PixelGen.

