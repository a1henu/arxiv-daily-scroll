---
layout: default
title: Perception-based Image Denoising via Generative Compression
---

# Perception-based Image Denoising via Generative Compression
**arXiv**：[2602.11553v1](https://arxiv.org/abs/2602.11553) · [PDF](https://arxiv.org/pdf/2602.11553.pdf)  
**作者**：Nam Nguyen, Thinh Nguyen, Bella Bose  

**一句话要点**：提出基于生成压缩的感知图像去噪框架，通过熵编码潜在表示和生成解码器提升去噪的感知质量。

**关键词**：图像去噪, 生成压缩, 感知质量, 条件WGAN, 扩散模型, 熵编码

## 3 点简述
- 核心问题：传统失真驱动去噪方法在强噪声和分布偏移下易产生过度平滑结果，难以保持结构细节和感知真实性。
- 方法要点：引入条件WGAN和扩散模型两种互补实现，利用LPIPS损失和Wasserstein距离等感知度量指导生成解码器恢复真实纹理。
- 实验或效果：在合成和真实噪声基准测试中，该方法在保持竞争性失真性能的同时，实现了感知质量的持续提升。

## 摘要（原文）

> Image denoising aims to remove noise while preserving structural details and perceptual realism, yet distortion-driven methods often produce over-smoothed reconstructions, especially under strong noise and distribution shift. This paper proposes a generative compression framework for perception-based denoising, where restoration is achieved by reconstructing from entropy-coded latent representations that enforce low-complexity structure, while generative decoders recover realistic textures via perceptual measures such as learned perceptual image patch similarity (LPIPS) loss and Wasserstein distance. Two complementary instantiations are introduced: (i) a conditional Wasserstein GAN (WGAN)-based compression denoiser that explicitly controls the rate-distortion-perception (RDP) trade-off, and (ii) a conditional diffusion-based reconstruction strategy that performs iterative denoising guided by compressed latents. We further establish non-asymptotic guarantees for the compression-based maximum-likelihood denoiser under additive Gaussian noise, including bounds on reconstruction error and decoding error probability. Experiments on synthetic and real-noise benchmarks demonstrate consistent perceptual improvements while maintaining competitive distortion performance.

