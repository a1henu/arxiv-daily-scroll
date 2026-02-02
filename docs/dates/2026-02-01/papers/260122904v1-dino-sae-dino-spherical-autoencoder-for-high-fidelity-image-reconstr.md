---
layout: default
title: DINO-SAE: DINO Spherical Autoencoder for High-Fidelity Image Reconstruction and Generation
---

# DINO-SAE: DINO Spherical Autoencoder for High-Fidelity Image Reconstruction and Generation
**arXiv**：[2601.22904v1](https://arxiv.org/abs/2601.22904) · [PDF](https://arxiv.org/pdf/2601.22904.pdf)  
**作者**：Hun Chang, Byunghee Cha, Jong Chul Ye  

**一句话要点**：提出DINO-SAE以解决基于预训练视觉基础模型的生成自编码器重建保真度不足问题

**关键词**：自编码器, 图像重建, 生成模型, 对比学习, 黎曼流匹配, 扩散变换器

## 3 点简述
- 核心问题：现有方法因高频细节丢失导致重建保真度受限
- 方法要点：引入分层卷积补丁嵌入模块和余弦相似度对齐目标，增强细节保留
- 实验或效果：在ImageNet-1K上达到0.37 rFID和26.2 dB PSNR，重建质量领先

## 摘要（原文）

> Recent studies have explored using pretrained Vision Foundation Models (VFMs) such as DINO for generative autoencoders, showing strong generative performance. Unfortunately, existing approaches often suffer from limited reconstruction fidelity due to the loss of high-frequency details. In this work, we present the DINO Spherical Autoencoder (DINO-SAE), a framework that bridges semantic representation and pixel-level reconstruction. Our key insight is that semantic information in contrastive representations is primarily encoded in the direction of feature vectors, while forcing strict magnitude matching can hinder the encoder from preserving fine-grained details. To address this, we introduce Hierarchical Convolutional Patch Embedding module that enhances local structure and texture preservation, and Cosine Similarity Alignment objective that enforces semantic consistency while allowing flexible feature magnitudes for detail retention. Furthermore, leveraging the observation that SSL-based foundation model representations intrinsically lie on a hypersphere, we employ Riemannian Flow Matching to train a Diffusion Transformer (DiT) directly on this spherical latent manifold. Experiments on ImageNet-1K demonstrate that our approach achieves state-of-the-art reconstruction quality, reaching 0.37 rFID and 26.2 dB PSNR, while maintaining strong semantic alignment to the pretrained VFM. Notably, our Riemannian Flow Matching-based DiT exhibits efficient convergence, achieving a gFID of 3.47 at 80 epochs.

