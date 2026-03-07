---
layout: default
title: Frequency-Aware Error-Bounded Caching for Accelerating Diffusion Transformers
---

# Frequency-Aware Error-Bounded Caching for Accelerating Diffusion Transformers
**arXiv**：[2603.05315v1](https://arxiv.org/abs/2603.05315) · [PDF](https://arxiv.org/pdf/2603.05315.pdf)  
**作者**：Guandong Li  

**一句话要点**：提出SpectralCache框架以加速扩散变换器推理，通过频率感知和误差有界缓存优化计算效率。

**关键词**：扩散变换器加速, 缓存优化, 频率分解, 误差有界计算, 推理效率

## 3 点简述
- 核心问题：现有缓存方法假设扩散变换器去噪过程均匀，忽略时间、深度和特征维度的非均匀性，导致计算加速受限。
- 方法要点：基于非均匀性观察，设计Timestep-Aware Dynamic Scheduling、Cumulative Error Budgets和Frequency-Decomposed Caching组件，实现训练即插即用的统一缓存框架。
- 实验或效果：在FLUX.1-schnell模型上，SpectralCache实现2.46倍加速，质量指标与基线相近，速度提升16%。

## 摘要（原文）

> Diffusion Transformers (DiTs) have emerged as the dominant architecture for high-quality image and video generation, yet their iterative denoising process incurs substantial computational cost during inference. Existing caching methods accelerate DiTs by reusing intermediate computations across timesteps, but they share a common limitation: treating the denoising process as uniform across time,depth, and feature dimensions. In this work, we identify three orthogonal axes of non-uniformity in DiT denoising: (1) temporal -- sensitivity to caching errors varies dramatically across the denoising trajectory; (2) depth -- consecutive caching decisions lead to cascading approximation errors; and (3) feature -- different components of the hidden state exhibit heterogeneous temporal dynamics. Based on these observations, we propose SpectralCache, a unified caching framework comprising Timestep-Aware Dynamic Scheduling (TADS), Cumulative Error Budgets (CEB), and Frequency-Decomposed Caching (FDC). On FLUX.1-schnell at 512x512 resolution, SpectralCache achieves 2.46x speedup with LPIPS 0.217 and SSIM 0.727, outperforming TeaCache (2.12x, LPIPS 0.215, SSIM 0.734) by 16% in speed while maintaining comparable quality (LPIPS difference < 1%). Our approach is training-free, plug-and-play, and compatible with existing DiT architectures.

