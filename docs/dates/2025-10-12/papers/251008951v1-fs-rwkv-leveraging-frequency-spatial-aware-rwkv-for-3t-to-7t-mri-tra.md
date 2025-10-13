---
layout: default
title: FS-RWKV: Leveraging Frequency Spatial-Aware RWKV for 3T-to-7T MRI Translation
---

# FS-RWKV: Leveraging Frequency Spatial-Aware RWKV for 3T-to-7T MRI Translation
**arXiv**：[2510.08951v1](https://arxiv.org/abs/2510.08951) · [PDF](https://arxiv.org/pdf/2510.08951.pdf)  
**作者**：Yingtie Lei, Zimeng Li, Chi-Man Pun, Yupeng Liu, Xuhang Chen  
**一句话要点**：提出FS-RWKV框架，利用频率空间感知RWKV实现3T到7T MRI图像翻译。

**关键词**：医学图像合成, MRI图像翻译, RWKV架构, 频率空间感知, 解剖结构保真

## 3 点简述
- 核心问题：7T MRI设备稀缺，需从3T图像合成高分辨率图像以提升临床可及性。
- 方法要点：引入FSO-Shift和SFEB模块，增强全局上下文和结构保真度。
- 实验或效果：在UNC和BNU数据集上优于多种基线，提升解剖保真度和感知质量。

## 摘要（原文）

> Ultra-high-field 7T MRI offers enhanced spatial resolution and tissue
> contrast that enables the detection of subtle pathological changes in
> neurological disorders. However, the limited availability of 7T scanners
> restricts widespread clinical adoption due to substantial infrastructure costs
> and technical demands. Computational approaches for synthesizing 7T-quality
> images from accessible 3T acquisitions present a viable solution to this
> accessibility challenge. Existing CNN approaches suffer from limited spatial
> coverage, while Transformer models demand excessive computational overhead.
> RWKV architectures offer an efficient alternative for global feature modeling
> in medical image synthesis, combining linear computational complexity with
> strong long-range dependency capture. Building on this foundation, we propose
> Frequency Spatial-RWKV (FS-RWKV), an RWKV-based framework for 3T-to-7T MRI
> translation. To better address the challenges of anatomical detail preservation
> and global tissue contrast recovery, FS-RWKV incorporates two key modules: (1)
> Frequency-Spatial Omnidirectional Shift (FSO-Shift), which performs discrete
> wavelet decomposition followed by omnidirectional spatial shifting on the
> low-frequency branch to enhance global contextual representation while
> preserving high-frequency anatomical details; and (2) Structural Fidelity
> Enhancement Block (SFEB), a module that adaptively reinforces anatomical
> structure through frequency-aware feature fusion. Comprehensive experiments on
> UNC and BNU datasets demonstrate that FS-RWKV consistently outperforms existing
> CNN-, Transformer-, GAN-, and RWKV-based baselines across both T1w and T2w
> modalities, achieving superior anatomical fidelity and perceptual quality.

