---
layout: default
title: Generative Latent Coding for Ultra-Low Bitrate Image Compression
---

# Generative Latent Coding for Ultra-Low Bitrate Image Compression
**arXiv**：[2512.20194v1](https://arxiv.org/abs/2512.20194) · [PDF](https://arxiv.org/pdf/2512.20194.pdf)  
**作者**：Zhaoyang Jia, Jiahao Li, Bin Li, Houqiang Li, Yan Lu  

**一句话要点**：提出生成式潜在编码架构，在超低比特率下实现高真实感与高保真图像压缩。

**关键词**：图像压缩, 生成式模型, 潜在空间编码, 超低比特率, 感知对齐

## 3 点简述
- 核心问题：传统像素空间编码在低比特率下难以兼顾高真实感与高保真，失真与人类感知不匹配。
- 方法要点：在生成式VQ-VAE的潜在空间进行变换编码，利用其稀疏性、语义丰富性和感知对齐优势。
- 实验或效果：在自然图像上低于0.04 bpp、人脸图像上低于0.01 bpp保持高视觉质量，CLIC2020测试集比特节省45%。

## 摘要（原文）

> Most existing image compression approaches perform transform coding in the pixel space to reduce its spatial redundancy. However, they encounter difficulties in achieving both high-realism and high-fidelity at low bitrate, as the pixel-space distortion may not align with human perception. To address this issue, we introduce a Generative Latent Coding (GLC) architecture, which performs transform coding in the latent space of a generative vector-quantized variational auto-encoder (VQ-VAE), instead of in the pixel space. The generative latent space is characterized by greater sparsity, richer semantic and better alignment with human perception, rendering it advantageous for achieving high-realism and high-fidelity compression. Additionally, we introduce a categorical hyper module to reduce the bit cost of hyper-information, and a code-prediction-based supervision to enhance the semantic consistency. Experiments demonstrate that our GLC maintains high visual quality with less than 0.04 bpp on natural images and less than 0.01 bpp on facial images. On the CLIC2020 test set, we achieve the same FID as MS-ILLM with 45% fewer bits. Furthermore, the powerful generative latent space enables various applications built on our GLC pipeline, such as image restoration and style transfer. The code is available at https://github.com/jzyustc/GLC.

