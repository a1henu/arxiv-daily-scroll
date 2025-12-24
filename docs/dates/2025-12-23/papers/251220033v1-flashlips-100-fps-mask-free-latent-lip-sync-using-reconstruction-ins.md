---
layout: default
title: FlashLips: 100-FPS Mask-Free Latent Lip-Sync using Reconstruction Instead of Diffusion or GANs
---

# FlashLips: 100-FPS Mask-Free Latent Lip-Sync using Reconstruction Instead of Diffusion or GANs
**arXiv**：[2512.20033v1](https://arxiv.org/abs/2512.20033) · [PDF](https://arxiv.org/pdf/2512.20033.pdf)  
**作者**：Andreas Zinonos, Michał Stypułkowski, Antoni Bigata, Stavros Petridis, Maja Pantic, Nikita Drobyshev  

**一句话要点**：提出FlashLips，一种两阶段、无掩码的唇形同步系统，通过重构而非扩散或GANs实现实时性能。

**关键词**：唇形同步, 实时渲染, 重构损失, 潜在空间编辑, 音频驱动, 流匹配

## 3 点简述
- 核心问题：现有唇形同步模型依赖掩码或复杂生成方法，难以兼顾实时速度与视觉质量。
- 方法要点：第一阶段使用重构损失训练紧凑的潜在空间编辑器，第二阶段基于流匹配训练音频到姿态的Transformer。
- 实验或效果：在单GPU上达到超过100 FPS的实时性能，视觉质量媲美更大规模的最先进模型。

## 摘要（原文）

> We present FlashLips, a two-stage, mask-free lip-sync system that decouples lips control from rendering and achieves real-time performance running at over 100 FPS on a single GPU, while matching the visual quality of larger state-of-the-art models. Stage 1 is a compact, one-step latent-space editor that reconstructs an image using a reference identity, a masked target frame, and a low-dimensional lips-pose vector, trained purely with reconstruction losses - no GANs or diffusion. To remove explicit masks at inference, we use self-supervision: we generate mouth-altered variants of the target image, that serve as pseudo ground truth for fine-tuning, teaching the network to localize edits to the lips while preserving the rest. Stage 2 is an audio-to-pose transformer trained with a flow-matching objective to predict lips-poses vectors from speech. Together, these stages form a simple and stable pipeline that combines deterministic reconstruction with robust audio control, delivering high perceptual quality and faster-than-real-time speed.

