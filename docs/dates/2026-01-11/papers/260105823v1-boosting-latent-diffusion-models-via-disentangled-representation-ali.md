---
layout: default
title: Boosting Latent Diffusion Models via Disentangled Representation Alignment
---

# Boosting Latent Diffusion Models via Disentangled Representation Alignment
**arXiv**：[2601.05823v1](https://arxiv.org/abs/2601.05823) · [PDF](https://arxiv.org/pdf/2601.05823.pdf)  
**作者**：John Page, Xuesong Niu, Kai Wu, Kun Gai  

**一句话要点**：提出语义解耦VAE以优化潜在扩散模型，通过解耦表示对齐提升图像生成性能。

**关键词**：潜在扩散模型, 语义解耦, 表示对齐, 变分自编码器, 图像生成, 视觉基础模型

## 3 点简述
- 核心问题：现有方法使用相同对齐目标忽略VAE与LDM表示需求差异，VAE需语义解耦。
- 方法要点：设计语义解耦VAE，通过非线性映射网络对齐预训练视觉基础模型的语义层次。
- 实验或效果：在ImageNet 256x256上，训练速度加快，FID达1.21（使用分类器自由引导）和1.75（未使用）。

## 摘要（原文）

> Latent Diffusion Models (LDMs) generate high-quality images by operating in a compressed latent space, typically obtained through image tokenizers such as Variational Autoencoders (VAEs). In pursuit of a generation-friendly VAE, recent studies have explored leveraging Vision Foundation Models (VFMs) as representation alignment targets for VAEs, mirroring the approach commonly adopted for LDMs. Although this yields certain performance gains, using the same alignment target for both VAEs and LDMs overlooks their fundamentally different representational requirements. We advocate that while LDMs benefit from latents retaining high-level semantic concepts, VAEs should excel in semantic disentanglement, enabling encoding of attribute-level information in a structured way. To address this, we propose the Semantic disentangled VAE (Send-VAE), explicitly optimized for disentangled representation learning through aligning its latent space with the semantic hierarchy of pre-trained VFMs. Our approach employs a non-linear mapper network to transform VAE latents, aligning them with VFMs to bridge the gap between attribute-level disentanglement and high-level semantics, facilitating effective guidance for VAE learning. We evaluate semantic disentanglement via linear probing on attribute prediction tasks, showing strong correlation with improved generation performance. Finally, using Send-VAE, we train flow-based transformers SiTs; experiments show Send-VAE significantly speeds up training and achieves a state-of-the-art FID of 1.21 and 1.75 with and without classifier-free guidance on ImageNet 256x256.

