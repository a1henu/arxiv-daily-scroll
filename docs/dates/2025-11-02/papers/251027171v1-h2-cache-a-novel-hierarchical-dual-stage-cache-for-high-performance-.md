---
layout: default
title: H2-Cache: A Novel Hierarchical Dual-Stage Cache for High-Performance Acceleration of Generative Diffusion Models
---

# H2-Cache: A Novel Hierarchical Dual-Stage Cache for High-Performance Acceleration of Generative Diffusion Models
**arXiv**：[2510.27171v1](https://arxiv.org/abs/2510.27171) · [PDF](https://arxiv.org/pdf/2510.27171.pdf)  
**作者**：Mingyu Sung, Il-Min Kim, Sangseok Yun, Jae-Mo Kang  

**一句话要点**：提出H2-Cache分层双阶段缓存以解决扩散模型推理速度与质量权衡问题

**关键词**：扩散模型, 缓存加速, 图像生成, 去噪过程, 分层缓存, 相似性估计

## 3 点简述
- 扩散模型迭代去噪计算成本高，现有缓存方法在速度与保真度间存在权衡
- H2-Cache基于去噪过程结构定义与细节精炼分离，采用双阈值系统选择性缓存
- 实验显示在Flux架构上加速达5.08倍，图像质量接近基线，优于现有方法

## 摘要（原文）

> Diffusion models have emerged as state-of-the-art in image generation, but
> their practical deployment is hindered by the significant computational cost of
> their iterative denoising process. While existing caching techniques can
> accelerate inference, they often create a challenging trade-off between speed
> and fidelity, suffering from quality degradation and high computational
> overhead. To address these limitations, we introduce H2-Cache, a novel
> hierarchical caching mechanism designed for modern generative diffusion model
> architectures. Our method is founded on the key insight that the denoising
> process can be functionally separated into a structure-defining stage and a
> detail-refining stage. H2-cache leverages this by employing a dual-threshold
> system, using independent thresholds to selectively cache each stage. To ensure
> the efficiency of our dual-check approach, we introduce pooled feature
> summarization (PFS), a lightweight technique for robust and fast similarity
> estimation. Extensive experiments on the Flux architecture demonstrate that
> H2-cache achieves significant acceleration (up to 5.08x) while maintaining
> image quality nearly identical to the baseline, quantitatively and
> qualitatively outperforming existing caching methods. Our work presents a
> robust and practical solution that effectively resolves the speed-quality
> dilemma, significantly lowering the barrier for the real-world application of
> high-fidelity diffusion models. Source code is available at
> https://github.com/Bluear7878/H2-cache-A-Hierarchical-Dual-Stage-Cache.

