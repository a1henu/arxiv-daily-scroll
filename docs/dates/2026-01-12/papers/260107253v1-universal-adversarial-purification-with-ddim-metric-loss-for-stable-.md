---
layout: default
title: Universal Adversarial Purification with DDIM Metric Loss for Stable Diffusion
---

# Universal Adversarial Purification with DDIM Metric Loss for Stable Diffusion
**arXiv**：[2601.07253v1](https://arxiv.org/abs/2601.07253) · [PDF](https://arxiv.org/pdf/2601.07253.pdf)  
**作者**：Li Zheng, Liangbin Xie, Jiantao Zhou, He YiMin  

**一句话要点**：提出UDAP框架，通过DDIM度量损失优化净化过程，以防御针对Stable Diffusion的对抗攻击。

**关键词**：对抗净化, Stable Diffusion, DDIM度量损失, 动态优化策略, 图像生成安全

## 3 点简述
- 核心问题：现有净化方法未针对Stable Diffusion的对抗攻击，如VAE编码器或UNet去噪器攻击。
- 方法要点：利用DDIM反转中干净与对抗图像的重建差异，最小化DDIM度量损失以去除对抗噪声。
- 实验或效果：UDAP对多种对抗方法（如PID、Anti-DreamBooth）有效，并跨SD版本和文本提示泛化。

## 摘要（原文）

> Stable Diffusion (SD) often produces degraded outputs when the training dataset contains adversarial noise. Adversarial purification offers a promising solution by removing adversarial noise from contaminated data. However, existing purification methods are primarily designed for classification tasks and fail to address SD-specific adversarial strategies, such as attacks targeting the VAE encoder, UNet denoiser, or both. To address the gap in SD security, we propose Universal Diffusion Adversarial Purification (UDAP), a novel framework tailored for defending adversarial attacks targeting SD models. UDAP leverages the distinct reconstruction behaviors of clean and adversarial images during Denoising Diffusion Implicit Models (DDIM) inversion to optimize the purification process. By minimizing the DDIM metric loss, UDAP can effectively remove adversarial noise. Additionally, we introduce a dynamic epoch adjustment strategy that adapts optimization iterations based on reconstruction errors, significantly improving efficiency without sacrificing purification quality. Experiments demonstrate UDAP's robustness against diverse adversarial methods, including PID (VAE-targeted), Anti-DreamBooth (UNet-targeted), MIST (hybrid), and robustness-enhanced variants like Anti-Diffusion (Anti-DF) and MetaCloak. UDAP also generalizes well across SD versions and text prompts, showcasing its practical applicability in real-world scenarios.

