---
layout: default
title: SALAD-Pan: Sensor-Agnostic Latent Adaptive Diffusion for Pan-Sharpening
---

# SALAD-Pan: Sensor-Agnostic Latent Adaptive Diffusion for Pan-Sharpening
**arXiv**：[2602.04473v1](https://arxiv.org/abs/2602.04473) · [PDF](https://arxiv.org/pdf/2602.04473.pdf)  
**作者**：Junjie Li, Congyang Ou, Haokui Zhang, Guoting Wei, Shengqin Jiang, Ying Li, Chunhua Shen  

**一句话要点**：提出SALAD-Pan，一种传感器无关的潜在空间扩散方法，用于高效全色锐化

**关键词**：全色锐化, 扩散模型, 潜在空间编码, 传感器无关, 跨光谱注意力, 零样本学习

## 3 点简述
- 现有扩散模型在全色锐化中面临像素空间扩散的高延迟和传感器特定限制问题
- SALAD-Pan通过单通道VAE编码、交互控制结构和跨光谱注意力模块实现高效高精度融合
- 实验表明，该方法在多个数据集上优于现有方法，推理速度提升2-3倍，并具有零样本跨传感器能力

## 摘要（原文）

> Recently, diffusion models bring novel insights for Pan-sharpening and notably boost fusion precision. However, most existing models perform diffusion in the pixel space and train distinct models for different multispectral (MS) imagery, suffering from high latency and sensor-specific limitations. In this paper, we present SALAD-Pan, a sensor-agnostic latent space diffusion method for efficient pansharpening. Specifically, SALAD-Pan trains a band-wise single-channel VAE to encode high-resolution multispectral (HRMS) into compact latent representations, supporting MS images with various channel counts and establishing a basis for acceleration. Then spectral physical properties, along with PAN and MS images, are injected into the diffusion backbone through unidirectional and bidirectional interactive control structures respectively, achieving high-precision fusion in the diffusion process. Finally, a lightweight cross-spectral attention module is added to the central layer of diffusion model, reinforcing spectral connections to boost spectral consistency and further elevate fusion precision. Experimental results on GaoFen-2, QuickBird, and WorldView-3 demonstrate that SALAD-Pan outperforms state-of-the-art diffusion-based methods across all three datasets, attains a 2-3x inference speedup, and exhibits robust zero-shot (cross-sensor) capability.

