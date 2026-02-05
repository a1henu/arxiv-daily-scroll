---
layout: default
title: Adaptive 1D Video Diffusion Autoencoder
---

# Adaptive 1D Video Diffusion Autoencoder
**arXiv**：[2602.04220v1](https://arxiv.org/abs/2602.04220) · [PDF](https://arxiv.org/pdf/2602.04220.pdf)  
**作者**：Yao Teng, Minxuan Lin, Xian Liu, Shuai Wang, Xiao Yang, Xihui Liu  

**一句话要点**：提出自适应一维视频扩散自编码器以解决现有视频自编码器在压缩效率、架构灵活性和解码质量方面的限制。

**关键词**：视频自编码器, 自适应压缩, 扩散模型, Transformer架构, 生成建模

## 3 点简述
- 现有视频自编码器存在固定压缩率、CNN架构不灵活和确定性解码器细节恢复差的问题。
- 采用基于查询的视觉Transformer编码器和像素空间扩散Transformer解码器，支持自适应一维编码。
- 在相同压缩比下性能媲美3D-CNN VAE，并支持更高压缩比，通过正则化和微调优化生成建模。

## 摘要（原文）

> Recent video generation models largely rely on video autoencoders that compress pixel-space videos into latent representations. However, existing video autoencoders suffer from three major limitations: (1) fixed-rate compression that wastes tokens on simple videos, (2) inflexible CNN architectures that prevent variable-length latent modeling, and (3) deterministic decoders that struggle to recover appropriate details from compressed latents. To address these issues, we propose One-Dimensional Diffusion Video Autoencoder (One-DVA), a transformer-based framework for adaptive 1D encoding and diffusion-based decoding. The encoder employs query-based vision transformers to extract spatiotemporal features and produce latent representations, while a variable-length dropout mechanism dynamically adjusts the latent length. The decoder is a pixel-space diffusion transformer that reconstructs videos with the latents as input conditions. With a two-stage training strategy, One-DVA achieves performance comparable to 3D-CNN VAEs on reconstruction metrics at identical compression ratios. More importantly, it supports adaptive compression and thus can achieve higher compression ratios. To better support downstream latent generation, we further regularize the One-DVA latent distribution for generative modeling and fine-tune its decoder to mitigate artifacts caused by the generation process.

