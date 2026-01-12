---
layout: default
title: WaveRNet: Wavelet-Guided Frequency Learning for Multi-Source Domain-Generalized Retinal Vessel Segmentation
---

# WaveRNet: Wavelet-Guided Frequency Learning for Multi-Source Domain-Generalized Retinal Vessel Segmentation
**arXiv**：[2601.05942v1](https://arxiv.org/abs/2601.05942) · [PDF](https://arxiv.org/pdf/2601.05942.pdf)  
**作者**：Chanchan Wang, Yuanfang Wang, Qing Xu, Guanxin Chen  

**一句话要点**：提出WaveRNet，通过小波引导频率学习解决多源域泛化视网膜血管分割问题。

**关键词**：视网膜血管分割, 域泛化, 小波变换, 频率学习, 测试时适应, 多源域

## 3 点简述
- 核心问题：视网膜血管分割面临光照和对比度变化导致的域偏移，现有方法忽略频域信息且丢失细节。
- 方法要点：设计SDM分离低频结构和高频边界，FADF模块进行测试时域选择，HMPR优化上采样以保留细节。
- 实验或效果：在四个公开数据集上采用Leave-One-Domain-Out协议，WaveRNet达到最先进的泛化性能。

## 摘要（原文）

> Domain-generalized retinal vessel segmentation is critical for automated ophthalmic diagnosis, yet faces significant challenges from domain shift induced by non-uniform illumination and varying contrast, compounded by the difficulty of preserving fine vessel structures. While the Segment Anything Model (SAM) exhibits remarkable zero-shot capabilities, existing SAM-based methods rely on simple adapter fine-tuning while overlooking frequency-domain information that encodes domain-invariant features, resulting in degraded generalization under illumination and contrast variations. Furthermore, SAM's direct upsampling inevitably loses fine vessel details. To address these limitations, we propose WaveRNet, a wavelet-guided frequency learning framework for robust multi-source domain-generalized retinal vessel segmentation. Specifically, we devise a Spectral-guided Domain Modulator (SDM) that integrates wavelet decomposition with learnable domain tokens, enabling the separation of illumination-robust low-frequency structures from high-frequency vessel boundaries while facilitating domain-specific feature generation. Furthermore, we introduce a Frequency-Adaptive Domain Fusion (FADF) module that performs intelligent test-time domain selection through wavelet-based frequency similarity and soft-weighted fusion. Finally, we present a Hierarchical Mask-Prompt Refiner (HMPR) that overcomes SAM's upsampling limitation through coarse-to-fine refinement with long-range dependency modeling. Extensive experiments under the Leave-One-Domain-Out protocol on four public retinal datasets demonstrate that WaveRNet achieves state-of-the-art generalization performance. The source code is available at https://github.com/Chanchan-Wang/WaveRNet.

