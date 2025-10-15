---
layout: default
title: Advancing End-to-End Pixel Space Generative Modeling via Self-supervised Pre-training
---

# Advancing End-to-End Pixel Space Generative Modeling via Self-supervised Pre-training
**arXiv**：[2510.12586v1](https://arxiv.org/abs/2510.12586) · [PDF](https://arxiv.org/pdf/2510.12586.pdf)  
**作者**：Jiachen Lei, Keli Liu, Julius Berner, Haiming Yu, Hongkai Zheng, Jiahong Wu, Xiangxiang Chu  

**一句话要点**：提出两阶段训练框架以提升像素空间生成模型性能

**关键词**：像素空间生成模型, 自监督预训练, 扩散模型, 一致性模型, 端到端训练, 图像生成

## 3 点简述
- 像素空间生成模型训练困难且性能低于潜在空间模型
- 采用自监督预训练编码器，结合端到端微调解码器
- 在ImageNet上实现高FID分数，超越现有像素空间方法

## 摘要（原文）

> Pixel-space generative models are often more difficult to train and generally
> underperform compared to their latent-space counterparts, leaving a persistent
> performance and efficiency gap. In this paper, we introduce a novel two-stage
> training framework that closes this gap for pixel-space diffusion and
> consistency models. In the first stage, we pre-train encoders to capture
> meaningful semantics from clean images while aligning them with points along
> the same deterministic sampling trajectory, which evolves points from the prior
> to the data distribution. In the second stage, we integrate the encoder with a
> randomly initialized decoder and fine-tune the complete model end-to-end for
> both diffusion and consistency models. Our training framework demonstrates
> strong empirical performance on ImageNet dataset. Specifically, our diffusion
> model reaches an FID of 2.04 on ImageNet-256 and 2.35 on ImageNet-512 with 75
> number of function evaluations (NFE), surpassing prior pixel-space methods by a
> large margin in both generation quality and efficiency while rivaling leading
> VAE-based models at comparable training cost. Furthermore, on ImageNet-256, our
> consistency model achieves an impressive FID of 8.82 in a single sampling step,
> significantly surpassing its latent-space counterpart. To the best of our
> knowledge, this marks the first successful training of a consistency model
> directly on high-resolution images without relying on pre-trained VAEs or
> diffusion models.

