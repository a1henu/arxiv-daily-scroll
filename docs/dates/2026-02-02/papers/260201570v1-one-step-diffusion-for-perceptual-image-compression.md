---
layout: default
title: One-Step Diffusion for Perceptual Image Compression
---

# One-Step Diffusion for Perceptual Image Compression
**arXiv**：[2602.01570v1](https://arxiv.org/abs/2602.01570) · [PDF](https://arxiv.org/pdf/2602.01570.pdf)  
**作者**：Yiwen Jia, Hao Wei, Yanhui Zhou, Chenyang Ge  

**一句话要点**：提出单步扩散图像压缩方法以解决推理延迟问题

**关键词**：图像压缩, 扩散模型, 单步推理, 感知质量, 特征判别器

## 3 点简述
- 基于扩散的图像压缩方法存在高推理延迟和计算开销问题
- 引入单步扩散过程，显著提升推理速度，并使用特征判别器增强感知质量
- 实验显示压缩性能相当，推理速度比现有方法快46倍

## 摘要（原文）

> Diffusion-based image compression methods have achieved notable progress, delivering high perceptual quality at low bitrates. However, their practical deployment is hindered by significant inference latency and heavy computational overhead, primarily due to the large number of denoising steps required during decoding. To address this problem, we propose a diffusion-based image compression method that requires only a single-step diffusion process, significantly improving inference speed. To enhance the perceptual quality of reconstructed images, we introduce a discriminator that operates on compact feature representations instead of raw pixels, leveraging the fact that features better capture high-level texture and structural details. Experimental results show that our method delivers comparable compression performance while offering a 46$\times$ faster inference speed compared to recent diffusion-based approaches. The source code and models are available at https://github.com/cheesejiang/OSDiff.

