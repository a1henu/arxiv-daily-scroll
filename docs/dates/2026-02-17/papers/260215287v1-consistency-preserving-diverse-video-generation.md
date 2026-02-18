---
layout: default
title: Consistency-Preserving Diverse Video Generation
---

# Consistency-Preserving Diverse Video Generation
**arXiv**：[2602.15287v1](https://arxiv.org/abs/2602.15287) · [PDF](https://arxiv.org/pdf/2602.15287.pdf)  
**作者**：Xinshuang Liu, Runfa Blark Li, Truong Nguyen  

**一句话要点**：提出联合采样框架以提升文本到视频生成的批次多样性和时间一致性

**关键词**：文本到视频生成, 时间一致性, 批次多样性, 流匹配, 潜在空间模型, 联合采样

## 3 点简述
- 核心问题：文本到视频生成成本高，批次样本少，现有方法提升多样性时损害时间一致性且计算开销大。
- 方法要点：采用联合采样框架，先应用多样性驱动更新，再移除降低时间一致性的组件，使用轻量级潜在空间模型避免视频解码和反向传播。
- 实验或效果：在先进文本到视频流匹配模型上实验，多样性媲美基线，时间一致性和色彩自然性显著提升。

## 摘要（原文）

> Text-to-video generation is expensive, so only a few samples are typically produced per prompt. In this low-sample regime, maximizing the value of each batch requires high cross-video diversity. Recent methods improve diversity for image generation, but for videos they often degrade within-video temporal consistency and require costly backpropagation through a video decoder. We propose a joint-sampling framework for flow-matching video generators that improves batch diversity while preserving temporal consistency. Our approach applies diversity-driven updates and then removes only the components that would decrease a temporal-consistency objective. To avoid image-space gradients, we compute both objectives with lightweight latent-space models, avoiding video decoding and decoder backpropagation. Experiments on a state-of-the-art text-to-video flow-matching model show diversity comparable to strong joint-sampling baselines while substantially improving temporal consistency and color naturalness. Code will be released.

