---
layout: default
title: DVI: Disentangling Semantic and Visual Identity for Training-Free Personalized Generation
---

# DVI: Disentangling Semantic and Visual Identity for Training-Free Personalized Generation
**arXiv**：[2512.18964v1](https://arxiv.org/abs/2512.18964) · [PDF](https://arxiv.org/pdf/2512.18964.pdf)  
**作者**：Guandong Li, Yijun Ding  

**一句话要点**：提出DVI框架以解决个性化生成中的语义-视觉不协调问题，实现免训练的身份定制。

**关键词**：个性化生成, 免训练定制, 语义-视觉解耦, VAE潜在空间, 特征调制, 扩散模型

## 3 点简述
- 核心问题：现有免训练身份定制方法忽视视觉上下文，导致面部几何与输入氛围冲突，产生不自然的贴纸效应。
- 方法要点：通过解耦语义和视觉流，利用VAE潜在空间的统计特性，引入参数无关特征调制和动态时间粒度调度器。
- 实验或效果：在IBench评估中优于现有方法，增强视觉一致性和氛围保真度，无需参数微调。

## 摘要（原文）

> Recent tuning-free identity customization methods achieve high facial fidelity but often overlook visual context, such as lighting, skin texture, and environmental tone. This limitation leads to ``Semantic-Visual Dissonance,'' where accurate facial geometry clashes with the input's unique atmosphere, causing an unnatural ``sticker-like'' effect. We propose **DVI (Disentangled Visual-Identity)**, a zero-shot framework that orthogonally disentangles identity into fine-grained semantic and coarse-grained visual streams. Unlike methods relying solely on semantic vectors, DVI exploits the inherent statistical properties of the VAE latent space, utilizing mean and variance as lightweight descriptors for global visual atmosphere. We introduce a **Parameter-Free Feature Modulation** mechanism that adaptively modulates semantic embeddings with these visual statistics, effectively injecting the reference's ``visual soul'' without training. Furthermore, a **Dynamic Temporal Granularity Scheduler** aligns with the diffusion process, prioritizing visual atmosphere in early denoising stages while refining semantic details later. Extensive experiments demonstrate that DVI significantly enhances visual consistency and atmospheric fidelity without parameter fine-tuning, maintaining robust identity preservation and outperforming state-of-the-art methods in IBench evaluations.

