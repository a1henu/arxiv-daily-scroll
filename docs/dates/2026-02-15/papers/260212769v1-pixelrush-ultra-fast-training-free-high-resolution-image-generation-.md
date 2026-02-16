---
layout: default
title: PixelRush: Ultra-Fast, Training-Free High-Resolution Image Generation via One-step Diffusion
---

# PixelRush: Ultra-Fast, Training-Free High-Resolution Image Generation via One-step Diffusion
**arXiv**：[2602.12769v1](https://arxiv.org/abs/2602.12769) · [PDF](https://arxiv.org/pdf/2602.12769.pdf)  
**作者**：Hong-Phuc Lai, Phong Nguyen, Anh Tran  

**一句话要点**：提出PixelRush框架，实现无需训练的高分辨率图像快速生成

**关键词**：高分辨率图像生成, 扩散模型, 免训练方法, 补丁推理, 快速生成

## 3 点简述
- 核心问题：预训练扩散模型受限于原生分辨率，现有免训练方法计算开销大，生成4K图像耗时超5分钟
- 方法要点：基于补丁推理，消除多轮反演和再生，结合低步数去噪、无缝混合策略和噪声注入机制
- 实验或效果：生成4K图像约20秒，速度提升10至35倍，保持高视觉保真度

## 摘要（原文）

> Pre-trained diffusion models excel at generating high-quality images but remain inherently limited by their native training resolution. Recent training-free approaches have attempted to overcome this constraint by introducing interventions during the denoising process; however, these methods incur substantial computational overhead, often requiring more than five minutes to produce a single 4K image. In this paper, we present PixelRush, the first tuning-free framework for practical high-resolution text-to-image generation. Our method builds upon the established patch-based inference paradigm but eliminates the need for multiple inversion and regeneration cycles. Instead, PixelRush enables efficient patch-based denoising within a low-step regime. To address artifacts introduced by patch blending in few-step generation, we propose a seamless blending strategy. Furthermore, we mitigate over-smoothing effects through a noise injection mechanism. PixelRush delivers exceptional efficiency, generating 4K images in approximately 20 seconds representing a 10$\times$ to 35$\times$ speedup over state-of-the-art methods while maintaining superior visual fidelity. Extensive experiments validate both the performance gains and the quality of outputs achieved by our approach.

