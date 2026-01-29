---
layout: default
title: SemBind: Binding Diffusion Watermarks to Semantics Against Black-Box Forgery Attacks
---

# SemBind: Binding Diffusion Watermarks to Semantics Against Black-Box Forgery Attacks
**arXiv**：[2601.20310v1](https://arxiv.org/abs/2601.20310) · [PDF](https://arxiv.org/pdf/2601.20310.pdf)  
**作者**：Xin Zhang, Zijin Yang, Kejiang Chen, Linfeng Ma, Weiming Zhang, Nenghai Yu  

**一句话要点**：提出SemBind框架，通过语义绑定防御潜在扩散模型水印的黑盒伪造攻击

**关键词**：潜在扩散模型, 水印防御, 黑盒攻击, 语义绑定, 对比学习, 图像溯源

## 3 点简述
- 核心问题：黑盒伪造攻击可将提供商水印嵌入非生成图像，威胁溯源与信任
- 方法要点：利用学习语义掩码器将潜在信号绑定到图像语义，基于对比学习训练
- 实验或效果：在四种主流水印方法中显著降低误接受率，保持图像质量与可控权衡

## 摘要（原文）

> Latent-based watermarks, integrated into the generation process of latent diffusion models (LDMs), simplify detection and attribution of generated images. However, recent black-box forgery attacks, where an attacker needs at least one watermarked image and black-box access to the provider's model, can embed the provider's watermark into images not produced by the provider, posing outsized risk to provenance and trust. We propose SemBind, the first defense framework for latent-based watermarks that resists black-box forgery by binding latent signals to image semantics via a learned semantic masker. Trained with contrastive learning, the masker yields near-invariant codes for the same prompt and near-orthogonal codes across prompts; these codes are reshaped and permuted to modulate the target latent before any standard latent-based watermark. SemBind is generally compatible with existing latent-based watermarking schemes and keeps image quality essentially unchanged, while a simple mask-ratio parameter offers a tunable trade-off between anti-forgery strength and robustness. Across four mainstream latent-based watermark methods, our SemBind-enabled anti-forgery variants markedly reduce false acceptance under black-box forgery while providing a controllable robustness-security balance.

