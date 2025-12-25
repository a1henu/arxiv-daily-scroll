---
layout: default
title: HiStream: Efficient High-Resolution Video Generation via Redundancy-Eliminated Streaming
---

# HiStream: Efficient High-Resolution Video Generation via Redundancy-Eliminated Streaming
**arXiv**：[2512.21338v1](https://arxiv.org/abs/2512.21338) · [PDF](https://arxiv.org/pdf/2512.21338.pdf)  
**作者**：Haonan Qiu, Shikun Liu, Zijian Zhou, Zhaochong An, Weiming Ren, Zhiheng Liu, Jonas Schult, Sen He, Shoufa Chen, Yuren Cong, Tao Xiang, Ziwei Liu, Juan-Manuel Perez-Rua  

**一句话要点**：提出HiStream框架，通过消除冗余实现高效高分辨率视频生成，解决扩散模型计算瓶颈问题。

**关键词**：高分辨率视频生成, 扩散模型优化, 冗余消除, 自回归框架, 计算效率提升

## 3 点简述
- 核心问题：高分辨率视频生成因扩散模型二次复杂度导致计算瓶颈，实际推理不可行。
- 方法要点：采用空间、时间和时间步压缩，通过缓存特征和分块策略减少冗余。
- 实验或效果：在1080p基准上，HiStream模型实现SOTA视觉质量，加速达76.2倍，HiStream+加速107.5倍。

## 摘要（原文）

> High-resolution video generation, while crucial for digital media and film, is computationally bottlenecked by the quadratic complexity of diffusion models, making practical inference infeasible. To address this, we introduce HiStream, an efficient autoregressive framework that systematically reduces redundancy across three axes: i) Spatial Compression: denoising at low resolution before refining at high resolution with cached features; ii) Temporal Compression: a chunk-by-chunk strategy with a fixed-size anchor cache, ensuring stable inference speed; and iii) Timestep Compression: applying fewer denoising steps to subsequent, cache-conditioned chunks. On 1080p benchmarks, our primary HiStream model (i+ii) achieves state-of-the-art visual quality while demonstrating up to 76.2x faster denoising compared to the Wan2.1 baseline and negligible quality loss. Our faster variant, HiStream+, applies all three optimizations (i+ii+iii), achieving a 107.5x acceleration over the baseline, offering a compelling trade-off between speed and quality, thereby making high-resolution video generation both practical and scalable.

