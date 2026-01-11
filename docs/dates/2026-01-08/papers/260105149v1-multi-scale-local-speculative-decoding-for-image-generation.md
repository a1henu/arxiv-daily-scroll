---
layout: default
title: Multi-Scale Local Speculative Decoding for Image Generation
---

# Multi-Scale Local Speculative Decoding for Image Generation
**arXiv**：[2601.05149v1](https://arxiv.org/abs/2601.05149) · [PDF](https://arxiv.org/pdf/2601.05149.pdf)  
**作者**：Elia Peruzzo, Guillaume Sautière, Amirhossein Habibian  

**一句话要点**：提出多尺度局部推测解码以加速自回归图像生成

**关键词**：图像生成, 推测解码, 多尺度建模, 局部重采样, 自回归模型加速

## 3 点简述
- 自回归图像生成存在延迟高问题，推测解码受限于令牌级模糊和空间意识缺乏
- 结合多分辨率草稿与空间感知验证，通过局部拒绝和重采样机制高效修正错误
- 在MS-COCO验证集上实现1.7倍加速，保持语义对齐和感知质量，超越基线方法

## 摘要（原文）

> Autoregressive (AR) models have achieved remarkable success in image synthesis, yet their sequential nature imposes significant latency constraints. Speculative Decoding offers a promising avenue for acceleration, but existing approaches are limited by token-level ambiguity and lack of spatial awareness. In this work, we introduce Multi-Scale Local Speculative Decoding (MuLo-SD), a novel framework that combines multi-resolution drafting with spatially informed verification to accelerate AR image generation. Our method leverages a low-resolution drafter paired with learned up-samplers to propose candidate image tokens, which are then verified in parallel by a high-resolution target model. Crucially, we incorporate a local rejection and resampling mechanism, enabling efficient correction of draft errors by focusing on spatial neighborhoods rather than raster-scan resampling after the first rejection. We demonstrate that MuLo-SD achieves substantial speedups - up to $\mathbf{1.7\times}$ - outperforming strong speculative decoding baselines such as EAGLE-2 and LANTERN in terms of acceleration, while maintaining comparable semantic alignment and perceptual quality. These results are validated using GenEval, DPG-Bench, and FID/HPSv2 on the MS-COCO 5k validation split. Extensive ablations highlight the impact of up-sampling design, probability pooling, and local rejection and resampling with neighborhood expansion. Our approach sets a new state-of-the-art in speculative decoding for image synthesis, bridging the gap between efficiency and fidelity.

