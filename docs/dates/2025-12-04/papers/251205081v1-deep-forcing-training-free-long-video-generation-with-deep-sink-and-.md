---
layout: default
title: Deep Forcing: Training-Free Long Video Generation with Deep Sink and Participative Compression
---

# Deep Forcing: Training-Free Long Video Generation with Deep Sink and Participative Compression
**arXiv**：[2512.05081v1](https://arxiv.org/abs/2512.05081) · [PDF](https://arxiv.org/pdf/2512.05081.pdf)  
**作者**：Jung Yi, Wooseok Jang, Paul Hyunbin Cho, Jisu Nam, Heeji Yoon, Seungryong Kim  

**一句话要点**：提出Deep Forcing，通过深度汇与参与式压缩实现无需训练的长视频生成，解决自回归视频扩散中的时间重复、漂移和运动减速问题。

**关键词**：长视频生成, 自回归视频扩散, 注意力机制, KV缓存管理, 训练免费方法, 实时生成

## 3 点简述
- 核心问题：自回归视频扩散在长视频生成中存在时间重复、漂移和运动减速，现有方法如StreamingLLM式注意力汇导致保真度下降和运动停滞。
- 方法要点：Deep Forcing包含深度汇（分配滑动窗口一半给持久汇令牌并重新对齐时间RoPE相位）和参与式压缩（基于重要性修剪KV缓存，保留活跃参与令牌）。
- 实验或效果：实现超过12倍外推（如5秒训练生成60秒以上视频），图像质量优于LongLive，美学质量优于RollingForcing，保持实时生成，动态程度显著提升。

## 摘要（原文）

> Recent advances in autoregressive video diffusion have enabled real-time frame streaming, yet existing solutions still suffer from temporal repetition, drift, and motion deceleration. We find that naively applying StreamingLLM-style attention sinks to video diffusion leads to fidelity degradation and motion stagnation. To overcome this, we introduce Deep Forcing, which consists of two training-free mechanisms that address this without any fine-tuning. Specifically, 1) Deep Sink dedicates half of the sliding window to persistent sink tokens and re-aligns their temporal RoPE phase to the current timeline, stabilizing global context during long rollouts. 2) Participative Compression performs importance-aware KV cache pruning that preserves only tokens actively participating in recent attention while safely discarding redundant and degraded history, minimizing error accumulation under out-of-distribution length generation. Together, these components enable over 12x extrapolation (e.g. 5s-trained to 60s+ generation) with better imaging quality than LongLive, better aesthetic quality than RollingForcing, almost maintaining overall consistency, and substantial gains in dynamic degree, all while maintaining real-time generation. Our results demonstrate that training-free KV-cache management can match or exceed training-based approaches for autoregressively streaming long-video generation.

