---
layout: default
title: Re-Depth Anything: Test-Time Depth Refinement via Self-Supervised Re-lighting
---

# Re-Depth Anything: Test-Time Depth Refinement via Self-Supervised Re-lighting
**arXiv**：[2512.17908v1](https://arxiv.org/abs/2512.17908) · [PDF](https://arxiv.org/pdf/2512.17908.pdf)  
**作者**：Ananta R. Bhattarai, Helge Rhodin  

**一句话要点**：提出Re-Depth Anything，通过自监督重光照在测试时优化单目深度估计以弥合领域差距。

**关键词**：单目深度估计, 测试时优化, 自监督学习, 重光照, 扩散模型, 领域适应

## 3 点简述
- 核心问题：基础模型如Depth Anything V2在远离训练分布的图像上深度估计性能受限。
- 方法要点：融合深度模型与2D扩散模型先验，利用重光照和Score Distillation Sampling进行无标签优化。
- 实验或效果：在多个基准测试中显著提升深度准确性和真实感，优于原模型。

## 摘要（原文）

> Monocular depth estimation remains challenging as recent foundation models, such as Depth Anything V2 (DA-V2), struggle with real-world images that are far from the training distribution. We introduce Re-Depth Anything, a test-time self-supervision framework that bridges this domain gap by fusing DA-V2 with the powerful priors of large-scale 2D diffusion models. Our method performs label-free refinement directly on the input image by re-lighting predicted depth maps and augmenting the input. This re-synthesis method replaces classical photometric reconstruction by leveraging shape from shading (SfS) cues in a new, generative context with Score Distillation Sampling (SDS). To prevent optimization collapse, our framework employs a targeted optimization strategy: rather than optimizing depth directly or fine-tuning the full model, we freeze the encoder and only update intermediate embeddings while also fine-tuning the decoder. Across diverse benchmarks, Re-Depth Anything yields substantial gains in depth accuracy and realism over the DA-V2, showcasing new avenues for self-supervision by augmenting geometric reasoning.

