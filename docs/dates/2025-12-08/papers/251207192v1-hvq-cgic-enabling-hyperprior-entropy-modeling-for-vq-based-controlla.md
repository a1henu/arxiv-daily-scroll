---
layout: default
title: HVQ-CGIC: Enabling Hyperprior Entropy Modeling for VQ-Based Controllable Generative Image Compression
---

# HVQ-CGIC: Enabling Hyperprior Entropy Modeling for VQ-Based Controllable Generative Image Compression
**arXiv**：[2512.07192v1](https://arxiv.org/abs/2512.07192) · [PDF](https://arxiv.org/pdf/2512.07192.pdf)  
**作者**：Niu Yi, Xu Tianyi, Ma Mingming, Wang Xinkun  

**一句话要点**：提出基于VQ超先验的可控生成图像压缩框架，以解决VQ索引熵建模的非自适应问题。

**关键词**：生成图像压缩, 向量量化, 超先验熵建模, 率失真控制, VQGAN压缩

## 3 点简述
- 核心问题：VQ生成压缩中索引熵模型使用静态全局分布，无法适应图像内容，限制比特率潜力。
- 方法要点：引入超先验到VQ索引熵模型，通过新颖损失设计实现率失真平衡与控制。
- 实验或效果：在Kodak数据集上，相比SOTA方法，以61.3%更少比特实现相同LPIPS。

## 摘要（原文）

> Generative learned image compression methods using Vector Quantization (VQ) have recently shown impressive potential in balancing distortion and perceptual quality. However, these methods typically estimate the entropy of VQ indices using a static, global probability distribution, which fails to adapt to the specific content of each image. This non-adaptive approach leads to untapped bitrate potential and challenges in achieving flexible rate control. To address this challenge, we introduce a Controllable Generative Image Compression framework based on a VQ Hyperprior, termed HVQ-CGIC. HVQ-CGIC rigorously derives the mathematical foundation for introducing a hyperprior to the VQ indices entropy model. Based on this foundation, through novel loss design, to our knowledge, this framework is the first to introduce RD balance and control into vector quantization-based Generative Image Compression. Cooperating with a lightweight hyper-prior estimation network, HVQ-CGIC achieves a significant advantage in rate-distortion (RD) performance compared to current state-of-the-art (SOTA) generative compression methods. On the Kodak dataset, we achieve the same LPIPS as Control-GIC, CDC and HiFiC with an average of 61.3% fewer bits. We posit that HVQ-CGIC has the potential to become a foundational component for VQGAN-based image compression, analogous to the integral role of the HyperPrior framework in neural image compression.

