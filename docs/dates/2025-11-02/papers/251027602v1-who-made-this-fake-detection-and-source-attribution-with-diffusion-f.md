---
layout: default
title: Who Made This? Fake Detection and Source Attribution with Diffusion Features
---

# Who Made This? Fake Detection and Source Attribution with Diffusion Features
**arXiv**：[2510.27602v1](https://arxiv.org/abs/2510.27602) · [PDF](https://arxiv.org/pdf/2510.27602.pdf)  
**作者**：Simone Bonechi, Paolo Andreini, Barbara Toniella Corradini  

**一句话要点**：提出FRIDA框架，利用扩散特征进行假图像检测和来源归属

**关键词**：假图像检测, 扩散模型, 来源归属, 跨生成器泛化, k近邻分类

## 3 点简述
- 生成扩散模型使假图像难以区分，引发真实性和版权问题
- 使用预训练扩散模型内部激活，结合k近邻分类器实现跨生成器检测
- 实验显示扩散特征编码生成器模式，无需微调即达先进性能

## 摘要（原文）

> The rapid progress of generative diffusion models has enabled the creation of
> synthetic images that are increasingly difficult to distinguish from real ones,
> raising concerns about authenticity, copyright, and misinformation. Existing
> supervised detectors often struggle to generalize across unseen generators,
> requiring extensive labeled data and frequent retraining. We introduce FRIDA
> (Fake-image Recognition and source Identification via Diffusion-features
> Analysis), a lightweight framework that leverages internal activations from a
> pre-trained diffusion model for deepfake detection and source generator
> attribution. A k-nearest-neighbor classifier applied to diffusion features
> achieves state-of-the-art cross-generator performance without fine-tuning,
> while a compact neural model enables accurate source attribution. These results
> show that diffusion representations inherently encode generator-specific
> patterns, providing a simple and interpretable foundation for synthetic image
> forensics.

