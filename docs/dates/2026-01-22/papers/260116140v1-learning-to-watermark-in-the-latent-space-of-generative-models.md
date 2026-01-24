---
layout: default
title: Learning to Watermark in the Latent Space of Generative Models
---

# Learning to Watermark in the Latent Space of Generative Models
**arXiv**：[2601.16140v1](https://arxiv.org/abs/2601.16140) · [PDF](https://arxiv.org/pdf/2601.16140.pdf)  
**作者**：Sylvestre-Alvise Rebuffi, Tuan Tran, Valeriu Lacatusu, Pierre Fernandez, Tomáš Souček, Nikola Jovanović, Tom Sander, Hady Elsahar, Alexandre Mourachko  

**一句话要点**：提出DistSeal方法，在生成模型的潜在空间进行水印嵌入，以提升效率与鲁棒性。

**关键词**：潜在空间水印, 生成模型, 蒸馏训练, 扩散模型, 自回归模型, 鲁棒性

## 3 点简述
- 现有像素空间水印方法存在计算开销大和视觉伪影问题。
- DistSeal在潜在空间训练水印模型，可蒸馏至生成模型或解码器实现内嵌水印。
- 实验显示潜在水印在鲁棒性竞争性下，速度提升高达20倍且不可感知性相似。

## 摘要（原文）

> Existing approaches for watermarking AI-generated images often rely on post-hoc methods applied in pixel space, introducing computational overhead and potential visual artifacts. In this work, we explore latent space watermarking and introduce DistSeal, a unified approach for latent watermarking that works across both diffusion and autoregressive models. Our approach works by training post-hoc watermarking models in the latent space of generative models. We demonstrate that these latent watermarkers can be effectively distilled either into the generative model itself or into the latent decoder, enabling in-model watermarking. The resulting latent watermarks achieve competitive robustness while offering similar imperceptibility and up to 20x speedup compared to pixel-space baselines. Our experiments further reveal that distilling latent watermarkers outperforms distilling pixel-space ones, providing a solution that is both more efficient and more robust.

