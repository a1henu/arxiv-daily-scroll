---
layout: default
title: Generative Neural Video Compression via Video Diffusion Prior
---

# Generative Neural Video Compression via Video Diffusion Prior
**arXiv**：[2512.05016v1](https://arxiv.org/abs/2512.05016) · [PDF](https://arxiv.org/pdf/2512.05016.pdf)  
**作者**：Qi Mao, Hao Cheng, Tinghan Yang, Libiao Jin, Siwei Ma  

**一句话要点**：提出GNVC-VD框架，基于视频扩散先验统一压缩与生成，以解决感知视频压缩中的闪烁伪影问题。

**关键词**：生成式神经视频压缩, 视频扩散先验, 时空潜在压缩, 序列级生成细化, 闪烁伪影减少

## 3 点简述
- 现有感知编解码器依赖图像生成先验，缺乏时间建模，导致闪烁伪影。
- 引入统一流匹配潜在细化模块，利用视频扩散Transformer进行序列级去噪，增强时空一致性。
- 实验显示在极低比特率下超越传统和学习编解码器，显著减少闪烁伪影。

## 摘要（原文）

> We present GNVC-VD, the first DiT-based generative neural video compression framework built upon an advanced video generation foundation model, where spatio-temporal latent compression and sequence-level generative refinement are unified within a single codec. Existing perceptual codecs primarily rely on pre-trained image generative priors to restore high-frequency details, but their frame-wise nature lacks temporal modeling and inevitably leads to perceptual flickering. To address this, GNVC-VD introduces a unified flow-matching latent refinement module that leverages a video diffusion transformer to jointly enhance intra- and inter-frame latents through sequence-level denoising, ensuring consistent spatio-temporal details. Instead of denoising from pure Gaussian noise as in video generation, GNVC-VD initializes refinement from decoded spatio-temporal latents and learns a correction term that adapts the diffusion prior to compression-induced degradation. A conditioning adaptor further injects compression-aware cues into intermediate DiT layers, enabling effective artifact removal while maintaining temporal coherence under extreme bitrate constraints. Extensive experiments show that GNVC-VD surpasses both traditional and learned codecs in perceptual quality and significantly reduces the flickering artifacts that persist in prior generative approaches, even below 0.01 bpp, highlighting the promise of integrating video-native generative priors into neural codecs for next-generation perceptual video compression.

