---
layout: default
title: Unified Latents (UL): How to train your latents
---

# Unified Latents (UL): How to train your latents
**arXiv**：[2602.17270v1](https://arxiv.org/abs/2602.17270) · [PDF](https://arxiv.org/pdf/2602.17270.pdf)  
**作者**：Jonathan Heek, Emiel Hoogeboom, Thomas Mensink, Tim Salimans  

**一句话要点**：提出统一潜变量框架，通过扩散先验和模型联合正则化潜表示，提升图像和视频生成效率与质量。

**关键词**：潜变量学习, 扩散模型, 图像生成, 视频生成, 正则化训练, 计算效率

## 3 点简述
- 核心问题：如何高效学习潜表示，平衡重建质量与计算成本。
- 方法要点：将编码器输出噪声链接到先验最小噪声水平，简化训练目标并约束潜比特率。
- 实验或效果：在ImageNet-512上FID达1.4，Kinetics-600上FVD达1.3，训练FLOPs低于Stable Diffusion潜变量模型。

## 摘要（原文）

> We present Unified Latents (UL), a framework for learning latent representations that are jointly regularized by a diffusion prior and decoded by a diffusion model. By linking the encoder's output noise to the prior's minimum noise level, we obtain a simple training objective that provides a tight upper bound on the latent bitrate. On ImageNet-512, our approach achieves competitive FID of 1.4, with high reconstruction quality (PSNR) while requiring fewer training FLOPs than models trained on Stable Diffusion latents. On Kinetics-600, we set a new state-of-the-art FVD of 1.3.

