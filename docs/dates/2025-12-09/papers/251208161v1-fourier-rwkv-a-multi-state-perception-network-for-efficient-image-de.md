---
layout: default
title: Fourier-RWKV: A Multi-State Perception Network for Efficient Image Dehazing
---

# Fourier-RWKV: A Multi-State Perception Network for Efficient Image Dehazing
**arXiv**：[2512.08161v1](https://arxiv.org/abs/2512.08161) · [PDF](https://arxiv.org/pdf/2512.08161.pdf)  
**作者**：Lirong Zheng, Yanshan Li, Rui Yu, Kaihao Zhang  

**一句话要点**：提出Fourier-RWKV多状态感知网络，以线性复杂度高效解决非均匀图像去雾问题。

**关键词**：图像去雾, 线性复杂度, 多状态感知, 傅里叶变换, 非均匀雾霾, 高效模型

## 3 点简述
- 核心问题：真实世界非均匀雾霾条件下图像去雾挑战大，Transformer方法计算复杂度高。
- 方法要点：结合空间、频域和语义感知状态，通过DQ-Shift、Fourier Mix和SBM模块实现高效去雾。
- 实验或效果：在多个基准测试中达到先进性能，显著降低计算开销，平衡恢复质量与效率。

## 摘要（原文）

> Image dehazing is crucial for reliable visual perception, yet it remains highly challenging under real-world non-uniform haze conditions. Although Transformer-based methods excel at capturing global context, their quadratic computational complexity hinders real-time deployment. To address this, we propose Fourier Receptance Weighted Key Value (Fourier-RWKV), a novel dehazing framework based on a Multi-State Perception paradigm. The model achieves comprehensive haze degradation modeling with linear complexity by synergistically integrating three distinct perceptual states: (1) Spatial-form Perception, realized through the Deformable Quad-directional Token Shift (DQ-Shift) operation, which dynamically adjusts receptive fields to accommodate local haze variations; (2) Frequency-domain Perception, implemented within the Fourier Mix block, which extends the core WKV attention mechanism of RWKV from the spatial domain to the Fourier domain, preserving the long-range dependencies essential for global haze estimation while mitigating spatial attenuation; (3) Semantic-relation Perception, facilitated by the Semantic Bridge Module (SBM), which utilizes Dynamic Semantic Kernel Fusion (DSK-Fusion) to precisely align encoder-decoder features and suppress artifacts. Extensive experiments on multiple benchmarks demonstrate that Fourier-RWKV delivers state-of-the-art performance across diverse haze scenarios while significantly reducing computational overhead, establishing a favorable trade-off between restoration quality and practical efficiency. Code is available at: https://github.com/Dilizlr/Fourier-RWKV.

