---
layout: default
title: Rethinking Garment Conditioning in Diffusion-based Virtual Try-On
---

# Rethinking Garment Conditioning in Diffusion-based Virtual Try-On
**arXiv**：[2511.18775v1](https://arxiv.org/abs/2511.18775) · [PDF](https://arxiv.org/pdf/2511.18775.pdf)  
**作者**：Kihyun Na, Jinyoung Choi, Injung Kim  

**一句话要点**：提出Re-CatVTON以解决扩散式虚拟试衣中计算效率与性能的平衡问题

**关键词**：虚拟试衣, 扩散模型, 单UNet架构, 计算效率优化, 分类器自由引导

## 3 点简述
- 核心问题：双UNet扩散模型在虚拟试衣中计算和内存开销大，影响效率。
- 方法要点：基于假设开发单UNet模型，改进分类器自由引导和直接注入真实服装潜在。
- 实验或效果：性能优于CatVTON，计算内存需求低于Leffa，FID等指标提升。

## 摘要（原文）

> Virtual Try-On (VTON) is the task of synthesizing an image of a person wearing a target garment, conditioned on a person image and a garment image. While diffusion-based VTON models featuring a Dual UNet architecture demonstrate superior fidelity compared to single UNet models, they incur substantial computational and memory overhead due to their heavy structure. In this study, through visualization analysis and theoretical analysis, we derived three hypotheses regarding the learning of context features to condition the denoising process. Based on these hypotheses, we developed Re-CatVTON, an efficient single UNet model that achieves high performance. We further enhance the model by introducing a modified classifier-free guidance strategy tailored for VTON's spatial concatenation conditioning, and by directly injecting the ground-truth garment latent derived from the clean garment latent to prevent the accumulation of prediction error. The proposed Re-CatVTON significantly improves performance compared to its predecessor (CatVTON) and requires less computation and memory than the high-performance Dual UNet model, Leffa. Our results demonstrate improved FID, KID, and LPIPS scores, with only a marginal decrease in SSIM, establishing a new efficiency-performance trade-off for single UNet VTON models.

