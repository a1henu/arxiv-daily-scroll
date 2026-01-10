---
layout: default
title: Multi-Scale Local Speculative Decoding for Image Generation
---

# Multi-Scale Local Speculative Decoding for Image Generation
**arXiv**：[2601.05149v1](https://arxiv.org/abs/2601.05149) · [PDF](https://arxiv.org/pdf/2601.05149.pdf)  
**作者**：Elia Peruzzo, Guillaume Sautière, Amirhossein Habibian  

**一句话要点**：提出多尺度局部推测解码以加速自回归图像生成

**关键词**：图像生成, 推测解码, 多尺度处理, 自回归模型, 加速技术

## 3 点简述
- 自回归图像生成存在序列延迟问题，推测解码受限于令牌级模糊和空间意识缺乏
- 结合多分辨率草稿与空间感知验证，通过低分辨率草稿器和高分辨率目标模型并行验证
- 在MS-COCO上验证，加速达1.7倍，保持语义对齐和感知质量，优于基线方法

## 摘要（原文）

> Autoregressive (AR) models have achieved remarkable success in image synthesis, yet their sequential nature imposes significant latency constraints. Speculative Decoding offers a promising avenue for acceleration, but existing approaches are limited by token-level ambiguity and lack of spatial awareness. In this work, we introduce Multi-Scale Local Speculative Decoding (MuLo-SD), a novel framework that combines multi-resolution drafting with spatially informed verification to accelerate AR image generation. Our method leverages a low-resolution drafter paired with learned up-samplers to propose candidate image tokens, which are then verified in parallel by a high-resolution target model. Crucially, we incorporate a local rejection and resampling mechanism, enabling efficient correction of draft errors by focusing on spatial neighborhoods rather than raster-scan resampling after the first rejection. We demonstrate that MuLo-SD achieves substantial speedups - up to $\mathbf{1.7\times}$ - outperforming strong speculative decoding baselines such as EAGLE-2 and LANTERN in terms of acceleration, while maintaining comparable semantic alignment and perceptual quality. These results are validated using GenEval, DPG-Bench, and FID/HPSv2 on the MS-COCO 5k validation split. Extensive ablations highlight the impact of up-sampling design, probability pooling, and local rejection and resampling with neighborhood expansion. Our approach sets a new state-of-the-art in speculative decoding for image synthesis, bridging the gap between efficiency and fidelity.

