---
layout: default
title: Repurposing Video Diffusion Transformers for Robust Point Tracking
---

# Repurposing Video Diffusion Transformers for Robust Point Tracking
**arXiv**：[2512.20606v1](https://arxiv.org/abs/2512.20606) · [PDF](https://arxiv.org/pdf/2512.20606.pdf)  
**作者**：Soowon Son, Honggyu An, Chaehyun Kim, Hyunah Ko, Jisu Nam, Dahyun Chung, Siyoon Jin, Jung Yi, Jaewon Min, Junhwa Hur, Seungryong Kim  

**一句话要点**：提出DiTracker，通过适配视频扩散变换器实现鲁棒点跟踪

**关键词**：点跟踪, 视频扩散变换器, 注意力匹配, 轻量调优, 鲁棒匹配

## 3 点简述
- 现有点跟踪方法依赖浅层卷积网络，缺乏时序一致性，在挑战性条件下匹配不可靠。
- 发现预训练视频扩散变换器具有强点跟踪能力，通过查询-键注意力匹配、轻量LoRA调优和成本融合进行适配。
- 在ITTO基准上达到最优性能，在TAP-Vid基准上匹配或超越现有模型，验证了视频扩散变换器特征的有效性。

## 摘要（原文）

> Point tracking aims to localize corresponding points across video frames, serving as a fundamental task for 4D reconstruction, robotics, and video editing. Existing methods commonly rely on shallow convolutional backbones such as ResNet that process frames independently, lacking temporal coherence and producing unreliable matching costs under challenging conditions. Through systematic analysis, we find that video Diffusion Transformers (DiTs), pre-trained on large-scale real-world videos with spatio-temporal attention, inherently exhibit strong point tracking capability and robustly handle dynamic motions and frequent occlusions. We propose DiTracker, which adapts video DiTs through: (1) query-key attention matching, (2) lightweight LoRA tuning, and (3) cost fusion with a ResNet backbone. Despite training with 8 times smaller batch size, DiTracker achieves state-of-the-art performance on challenging ITTO benchmark and matches or outperforms state-of-the-art models on TAP-Vid benchmarks. Our work validates video DiT features as an effective and efficient foundation for point tracking.

