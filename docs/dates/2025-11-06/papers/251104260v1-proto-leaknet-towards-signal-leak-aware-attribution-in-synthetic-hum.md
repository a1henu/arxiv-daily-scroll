---
layout: default
title: Proto-LeakNet: Towards Signal-Leak Aware Attribution in Synthetic Human Face Imagery
---

# Proto-LeakNet: Towards Signal-Leak Aware Attribution in Synthetic Human Face Imagery
**arXiv**：[2511.04260v1](https://arxiv.org/abs/2511.04260) · [PDF](https://arxiv.org/pdf/2511.04260.pdf)  
**作者**：Claudio Giusti, Luca Guarnera, Sebastiano Battiato  

**一句话要点**：提出Proto-LeakNet以解决合成人脸图像中信号泄漏感知的源归属问题

**关键词**：信号泄漏感知, 源归属, 扩散模型, 潜在空间分析, 可解释AI, 深度伪造取证

## 3 点简述
- 核心问题：扩散模型输出中信号泄漏导致合成图像源归属困难
- 方法要点：在潜在域重模拟扩散，结合注意力编码器和原型头实现可解释归属
- 实验或效果：Macro AUC达98.13%，对未知生成器具有强鲁棒性和可分性

## 摘要（原文）

> The growing sophistication of synthetic image and deepfake generation models
> has turned source attribution and authenticity verification into a critical
> challenge for modern computer vision systems. Recent studies suggest that
> diffusion pipelines unintentionally imprint persistent statistical traces,
> known as signal leaks, within their outputs, particularly in latent
> representations. Building on this observation, we propose Proto-LeakNet, a
> signal-leak-aware and interpretable attribution framework that integrates
> closed-set classification with a density-based open-set evaluation on the
> learned embeddings, enabling analysis of unseen generators without retraining.
> Operating in the latent domain of diffusion models, our method re-simulates
> partial forward diffusion to expose residual generator-specific cues. A
> temporal attention encoder aggregates multi-step latent features, while a
> feature-weighted prototype head structures the embedding space and enables
> transparent attribution. Trained solely on closed data and achieving a Macro
> AUC of 98.13%, Proto-LeakNet learns a latent geometry that remains robust under
> post-processing, surpassing state-of-the-art methods, and achieves strong
> separability between known and unseen generators. These results demonstrate
> that modeling signal-leak bias in latent space enables reliable and
> interpretable AI-image and deepfake forensics. The code for the whole work will
> be available upon submission.

