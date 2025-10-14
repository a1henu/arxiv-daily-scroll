---
layout: default
title: Diffusion Transformers with Representation Autoencoders
---

# Diffusion Transformers with Representation Autoencoders
**arXiv**：[2510.11690v1](https://arxiv.org/abs/2510.11690) · [PDF](https://arxiv.org/pdf/2510.11690.pdf)  
**作者**：Boyang Zheng, Nanye Ma, Shengbang Tong, Saining Xie  

**一句话要点**：提出表示自编码器以改进扩散变换器的潜在生成建模

**关键词**：扩散变换器, 表示自编码器, 潜在生成建模, 图像生成, 自监督学习

## 3 点简述
- 核心问题：传统VAE编码器在扩散变换器中存在架构过时、潜在空间低维和表示弱的问题。
- 方法要点：用预训练表示编码器（如DINO）与解码器构建表示自编码器，提供高质量重构和语义丰富潜在空间。
- 实验或效果：在ImageNet上实现低FID分数，如1.51（无引导），并实现更快收敛。

## 摘要（原文）

> Latent generative modeling, where a pretrained autoencoder maps pixels into a
> latent space for the diffusion process, has become the standard strategy for
> Diffusion Transformers (DiT); however, the autoencoder component has barely
> evolved. Most DiTs continue to rely on the original VAE encoder, which
> introduces several limitations: outdated backbones that compromise
> architectural simplicity, low-dimensional latent spaces that restrict
> information capacity, and weak representations that result from purely
> reconstruction-based training and ultimately limit generative quality. In this
> work, we explore replacing the VAE with pretrained representation encoders
> (e.g., DINO, SigLIP, MAE) paired with trained decoders, forming what we term
> Representation Autoencoders (RAEs). These models provide both high-quality
> reconstructions and semantically rich latent spaces, while allowing for a
> scalable transformer-based architecture. Since these latent spaces are
> typically high-dimensional, a key challenge is enabling diffusion transformers
> to operate effectively within them. We analyze the sources of this difficulty,
> propose theoretically motivated solutions, and validate them empirically. Our
> approach achieves faster convergence without auxiliary representation alignment
> losses. Using a DiT variant equipped with a lightweight, wide DDT head, we
> achieve strong image generation results on ImageNet: 1.51 FID at 256x256 (no
> guidance) and 1.13 at both 256x256 and 512x512 (with guidance). RAE offers
> clear advantages and should be the new default for diffusion transformer
> training.

