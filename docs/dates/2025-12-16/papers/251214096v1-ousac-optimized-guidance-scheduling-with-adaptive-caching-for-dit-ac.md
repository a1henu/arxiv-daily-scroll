---
layout: default
title: OUSAC: Optimized Guidance Scheduling with Adaptive Caching for DiT Acceleration
---

# OUSAC: Optimized Guidance Scheduling with Adaptive Caching for DiT Acceleration
**arXiv**：[2512.14096v1](https://arxiv.org/abs/2512.14096) · [PDF](https://arxiv.org/pdf/2512.14096.pdf)  
**作者**：Ruitong Sun, Tianze Yang, Wei Niu, Jin Sun  

**一句话要点**：提出OUSAC框架，通过优化引导调度与自适应缓存加速扩散变换器，减少计算成本并保持生成质量。

**关键词**：扩散模型加速, 分类器自由引导优化, 自适应缓存, 进化算法, 计算效率提升

## 3 点简述
- 核心问题：扩散模型因迭代去噪计算昂贵，分类器自由引导加倍计算，现有缓存方法在变引导下失效。
- 方法要点：两阶段优化，阶段1用进化算法联合优化跳过步长与引导尺度，阶段2引入自适应秩分配保持缓存有效性。
- 实验效果：在DiT-XL/2等模型上实现53%计算节省与15%质量提升，显著优于现有加速方法。

## 摘要（原文）

> Diffusion models have emerged as the dominant paradigm for high-quality image generation, yet their computational expense remains substantial due to iterative denoising. Classifier-Free Guidance (CFG) significantly enhances generation quality and controllability but doubles the computation by requiring both conditional and unconditional forward passes at every timestep. We present OUSAC (Optimized gUidance Scheduling with Adaptive Caching), a framework that accelerates diffusion transformers (DiT) through systematic optimization. Our key insight is that variable guidance scales enable sparse computation: adjusting scales at certain timesteps can compensate for skipping CFG at others, enabling both fewer total sampling steps and fewer CFG steps while maintaining quality. However, variable guidance patterns introduce denoising deviations that undermine standard caching methods, which assume constant CFG scales across steps. Moreover, different transformer blocks are affected at different levels under dynamic conditions. This paper develops a two-stage approach leveraging these insights. Stage-1 employs evolutionary algorithms to jointly optimize which timesteps to skip and what guidance scale to use, eliminating up to 82% of unconditional passes. Stage-2 introduces adaptive rank allocation that tailors calibration efforts per transformer block, maintaining caching effectiveness under variable guidance. Experiments demonstrate that OUSAC significantly outperforms state-of-the-art acceleration methods, achieving 53% computational savings with 15% quality improvement on DiT-XL/2 (ImageNet 512x512), 60% savings with 16.1% improvement on PixArt-alpha (MSCOCO), and 5x speedup on FLUX while improving CLIP Score over the 50-step baseline.

