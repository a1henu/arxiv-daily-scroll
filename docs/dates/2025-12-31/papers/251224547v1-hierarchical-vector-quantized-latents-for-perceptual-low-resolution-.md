---
layout: default
title: Hierarchical Vector-Quantized Latents for Perceptual Low-Resolution Video Compression
---

# Hierarchical Vector-Quantized Latents for Perceptual Low-Resolution Video Compression
**arXiv**：[2512.24547v1](https://arxiv.org/abs/2512.24547) · [PDF](https://arxiv.org/pdf/2512.24547.pdf)  
**作者**：Manikanta Kotthapalli, Banafsheh Rekabdar  

**一句话要点**：提出多尺度向量量化变分自编码器，用于低分辨率视频的感知压缩，适用于带宽敏感场景。

**关键词**：视频压缩, 向量量化变分自编码器, 分层潜在表示, 感知损失, 边缘计算, 低分辨率视频

## 3 点简述
- 视频流量激增对带宽和存储提出高需求，传统编解码器缺乏深度学习集成支持。
- 扩展VQ-VAE-2至时空域，构建轻量级分层潜在结构，结合感知损失提升重建质量。
- 在UCF101数据集上测试，PSNR达25.96 dB，SSIM为0.8375，优于基线模型。

## 摘要（原文）

> The exponential growth of video traffic has placed increasing demands on bandwidth and storage infrastructure, particularly for content delivery networks (CDNs) and edge devices. While traditional video codecs like H.264 and HEVC achieve high compression ratios, they are designed primarily for pixel-domain reconstruction and lack native support for machine learning-centric latent representations, limiting their integration into deep learning pipelines. In this work, we present a Multi-Scale Vector Quantized Variational Autoencoder (MS-VQ-VAE) designed to generate compact, high-fidelity latent representations of low-resolution video, suitable for efficient storage, transmission, and client-side decoding. Our architecture extends the VQ-VAE-2 framework to a spatiotemporal setting, introducing a two-level hierarchical latent structure built with 3D residual convolutions. The model is lightweight (approximately 18.5M parameters) and optimized for 64x64 resolution video clips, making it appropriate for deployment on edge devices with constrained compute and memory resources. To improve perceptual reconstruction quality, we incorporate a perceptual loss derived from a pre-trained VGG16 network. Trained on the UCF101 dataset using 2-second video clips (32 frames at 16 FPS), on the test set we achieve 25.96 dB PSNR and 0.8375 SSIM. On validation, our model improves over the single-scale baseline by 1.41 dB PSNR and 0.0248 SSIM. The proposed framework is well-suited for scalable video compression in bandwidth-sensitive scenarios, including real-time streaming, mobile video analytics, and CDN-level storage optimization.

