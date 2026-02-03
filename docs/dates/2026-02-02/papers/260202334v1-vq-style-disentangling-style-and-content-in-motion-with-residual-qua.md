---
layout: default
title: VQ-Style: Disentangling Style and Content in Motion with Residual Quantized Representations
---

# VQ-Style: Disentangling Style and Content in Motion with Residual Quantized Representations
**arXiv**：[2602.02334v1](https://arxiv.org/abs/2602.02334) · [PDF](https://arxiv.org/pdf/2602.02334.pdf)  
**作者**：Fatemeh Zargarbashi, Dhruv Agrawal, Jakob Buhmann, Martin Guay, Stelian Coros, Robert W. Sumner  

**一句话要点**：提出基于残差量化表示的方法，以解耦人体运动中的风格与内容，实现风格迁移。

**关键词**：人体运动分析, 风格解耦, 残差量化表示, 风格迁移, 对比学习, 变分自编码器

## 3 点简述
- 核心问题：人体运动数据复杂，风格与内容难以有效解耦，影响风格迁移应用。
- 方法要点：使用残差量化变分自编码器学习层次表示，结合对比学习和信息泄漏损失增强解耦。
- 实验或效果：通过量化代码交换实现无需微调的风格迁移，支持风格移除和运动混合等应用。

## 摘要（原文）

> Human motion data is inherently rich and complex, containing both semantic content and subtle stylistic features that are challenging to model. We propose a novel method for effective disentanglement of the style and content in human motion data to facilitate style transfer. Our approach is guided by the insight that content corresponds to coarse motion attributes while style captures the finer, expressive details. To model this hierarchy, we employ Residual Vector Quantized Variational Autoencoders (RVQ-VAEs) to learn a coarse-to-fine representation of motion. We further enhance the disentanglement by integrating contrastive learning and a novel information leakage loss with codebook learning to organize the content and the style across different codebooks. We harness this disentangled representation using our simple and effective inference-time technique Quantized Code Swapping, which enables motion style transfer without requiring any fine-tuning for unseen styles. Our framework demonstrates strong versatility across multiple inference applications, including style transfer, style removal, and motion blending.

