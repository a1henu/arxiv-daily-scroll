---
layout: default
title: AFFMAE: Scalable and Efficient Vision Pretraining for Desktop Graphics Cards
---

# AFFMAE: Scalable and Efficient Vision Pretraining for Desktop Graphics Cards
**arXiv**：[2602.16249v1](https://arxiv.org/abs/2602.16249) · [PDF](https://arxiv.org/pdf/2602.16249.pdf)  
**作者**：David Smerkous, Zian Wang, Behzad Najafian  

**一句话要点**：提出AFFMAE以解决高分辨率视觉预训练在桌面显卡上的计算效率问题

**关键词**：自监督预训练, 掩码自编码器, 分层架构, 计算效率, 高分辨率视觉, 桌面显卡训练

## 3 点简述
- 核心问题：高分辨率自监督预训练通常依赖服务器级硬件，限制了研究实验室开发领域基础模型。
- 方法要点：基于自适应非网格令牌合并，构建掩码友好的分层预训练框架，丢弃掩码令牌并动态合并可见令牌。
- 实验或效果：在电子显微镜分割任务中，匹配ViT-MAE性能，减少FLOPs达7倍，内存减半，单RTX 5090训练更快。

## 摘要（原文）

> Self-supervised pretraining has transformed computer vision by enabling data-efficient fine-tuning, yet high-resolution training typically requires server-scale infrastructure, limiting in-domain foundation model development for many research laboratories. Masked Autoencoders (MAE) reduce computation by encoding only visible tokens, but combining MAE with hierarchical downsampling architectures remains structurally challenging due to dense grid priors and mask-aware design compromises. We introduce AFFMAE, a masking-friendly hierarchical pretraining framework built on adaptive, off-grid token merging. By discarding masked tokens and performing dynamic merging exclusively over visible tokens, AFFMAE removes dense-grid assumptions while preserving hierarchical scalability. We developed numerically stable mixed-precision Flash-style cluster attention kernels, and mitigate sparse-stage representation collapse via deep supervision. On high-resolution electron microscopy segmentation, AFFMAE matches ViT-MAE performance at equal parameter count while reducing FLOPs by up to 7x, halving memory usage, and achieving faster training on a single RTX 5090. Code available at https://github.com/najafian-lab/affmae.

