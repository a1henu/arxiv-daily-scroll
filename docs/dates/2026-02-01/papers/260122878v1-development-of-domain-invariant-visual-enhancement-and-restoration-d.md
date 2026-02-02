---
layout: default
title: Development of Domain-Invariant Visual Enhancement and Restoration (DIVER) Approach for Underwater Images
---

# Development of Domain-Invariant Visual Enhancement and Restoration (DIVER) Approach for Underwater Images
**arXiv**：[2601.22878v1](https://arxiv.org/abs/2601.22878) · [PDF](https://arxiv.org/pdf/2601.22878.pdf)  
**作者**：Rajini Makam, Sharanya Patil, Dhatri Shankari T M, Suresh Sundaram, Narasimhan Sundararajan  

**一句话要点**：提出DIVER框架，通过无监督域不变方法增强和恢复水下图像

**关键词**：水下图像增强, 无监督学习, 物理引导建模, 域不变性, 机器人视觉

## 3 点简述
- 水下图像因波长相关衰减、散射和光照不均而严重退化，问题随水域类型和深度变化
- DIVER整合经验校正与物理引导建模，包括自适应亮度增强、光谱归一化和光学校正模块
- 在八个多样化数据集上评估，DIVER在UCIQE指标上优于SOTA方法至少9%，并提升机器人感知性能

## 摘要（原文）

> Underwater images suffer severe degradation due to wavelength-dependent attenuation, scattering, and illumination non-uniformity that vary across water types and depths. We propose an unsupervised Domain-Invariant Visual Enhancement and Restoration (DIVER) framework that integrates empirical correction with physics-guided modeling for robust underwater image enhancement. DIVER first applies either IlluminateNet for adaptive luminance enhancement or a Spectral Equalization Filter for spectral normalization. An Adaptive Optical Correction Module then refines hue and contrast using channel-adaptive filtering, while Hydro-OpticNet employs physics-constrained learning to compensate for backscatter and wavelength-dependent attenuation. The parameters of IlluminateNet and Hydro-OpticNet are optimized via unsupervised learning using a composite loss function. DIVER is evaluated on eight diverse datasets covering shallow, deep, and highly turbid environments, including both naturally low-light and artificially illuminated scenes, using reference and non-reference metrics. While state-of-the-art methods such as WaterNet, UDNet, and Phaseformer perform reasonably in shallow water, their performance degrades in deep, unevenly illuminated, or artificially lit conditions. In contrast, DIVER consistently achieves best or near-best performance across all datasets, demonstrating strong domain-invariant capability. DIVER yields at least a 9% improvement over SOTA methods in UCIQE. On the low-light SeaThru dataset, where color-palette references enable direct evaluation of color restoration, DIVER achieves at least a 4.9% reduction in GPMAE compared to existing methods. Beyond visual quality, DIVER also improves robotic perception by enhancing ORB-based keypoint repeatability and matching performance, confirming its robustness across diverse underwater environments.

