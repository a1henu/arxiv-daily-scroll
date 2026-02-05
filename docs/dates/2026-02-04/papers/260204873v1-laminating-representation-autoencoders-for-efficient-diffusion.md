---
layout: default
title: Laminating Representation Autoencoders for Efficient Diffusion
---

# Laminating Representation Autoencoders for Efficient Diffusion
**arXiv**：[2602.04873v1](https://arxiv.org/abs/2602.04873) · [PDF](https://arxiv.org/pdf/2602.04873.pdf)  
**作者**：Ramón Calvo-González, François Fleuret  

**一句话要点**：提出FlatDINO变分自编码器以压缩SSL特征，提升扩散模型效率

**关键词**：扩散模型, 特征压缩, 变分自编码器, 计算效率, SSL特征, 图像生成

## 3 点简述
- 核心问题：DINOv2等SSL编码器生成密集补丁特征存在冗余，导致扩散模型计算成本高。
- 方法要点：FlatDINO将SSL特征压缩为32个连续令牌的一维序列，实现序列长度8倍减少和总维度48倍压缩。
- 实验或效果：在ImageNet 256x256上，基于FlatDINO的DiT-XL模型gFID达1.80，前向计算FLOPs减少8倍，训练步骤FLOPs最多减少4.5倍。

## 摘要（原文）

> Recent work has shown that diffusion models can generate high-quality images by operating directly on SSL patch features rather than pixel-space latents. However, the dense patch grids from encoders like DINOv2 contain significant redundancy, making diffusion needlessly expensive. We introduce FlatDINO, a variational autoencoder that compresses this representation into a one-dimensional sequence of just 32 continuous tokens -an 8x reduction in sequence length and 48x compression in total dimensionality. On ImageNet 256x256, a DiT-XL trained on FlatDINO latents achieves a gFID of 1.80 with classifier-free guidance while requiring 8x fewer FLOPs per forward pass and up to 4.5x fewer FLOPs per training step compared to diffusion on uncompressed DINOv2 features. These are preliminary results and this work is in progress.

