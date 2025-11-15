---
layout: default
title: One Small Step in Latent, One Giant Leap for Pixels: Fast Latent Upscale Adapter for Your Diffusion Models
---

# One Small Step in Latent, One Giant Leap for Pixels: Fast Latent Upscale Adapter for Your Diffusion Models
**arXiv**：[2511.10629v1](https://arxiv.org/abs/2511.10629) · [PDF](https://arxiv.org/pdf/2511.10629.pdf)  
**作者**：Aleksandr Razin, Danil Kazantsev, Ilya Makarov  

**一句话要点**：提出潜在上采样适配器以解决扩散模型高分辨率合成效率低的问题

**关键词**：扩散模型, 潜在空间超分辨率, 高效图像合成, 轻量适配器, VAE兼容性

## 3 点简述
- 扩散模型直接高分辨率采样慢，后处理超分引入伪影和延迟
- LUA在潜在空间执行超分，无需修改基础模型，单前向传播实现
- 实验显示解码和上采样时间减少近3倍，保真度接近原生高分辨率

## 摘要（原文）

> Diffusion models struggle to scale beyond their training resolutions, as direct high-resolution sampling is slow and costly, while post-hoc image super-resolution (ISR) introduces artifacts and additional latency by operating after decoding. We present the Latent Upscaler Adapter (LUA), a lightweight module that performs super-resolution directly on the generator's latent code before the final VAE decoding step. LUA integrates as a drop-in component, requiring no modifications to the base model or additional diffusion stages, and enables high-resolution synthesis through a single feed-forward pass in latent space. A shared Swin-style backbone with scale-specific pixel-shuffle heads supports 2x and 4x factors and remains compatible with image-space SR baselines, achieving comparable perceptual quality with nearly 3x lower decoding and upscaling time (adding only +0.42 s for 1024 px generation from 512 px, compared to 1.87 s for pixel-space SR using the same SwinIR architecture). Furthermore, LUA shows strong generalization across the latent spaces of different VAEs, making it easy to deploy without retraining from scratch for each new decoder. Extensive experiments demonstrate that LUA closely matches the fidelity of native high-resolution generation while offering a practical and efficient path to scalable, high-fidelity image synthesis in modern diffusion pipelines.

