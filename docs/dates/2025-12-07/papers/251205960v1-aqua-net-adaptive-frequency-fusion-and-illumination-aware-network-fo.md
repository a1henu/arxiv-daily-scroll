---
layout: default
title: AQUA-Net: Adaptive Frequency Fusion and Illumination Aware Network for Underwater Image Enhancement
---

# AQUA-Net: Adaptive Frequency Fusion and Illumination Aware Network for Underwater Image Enhancement
**arXiv**：[2512.05960v1](https://arxiv.org/abs/2512.05960) · [PDF](https://arxiv.org/pdf/2512.05960.pdf)  
**作者**：Munsif Ali, Najmul Hassan, Lucia Ventura, Davide Di Bari, Simonepietro Canese  

**一句话要点**：提出AQUA-Net以解决水下图像增强中的颜色失真、低对比度和实时部署问题。

**关键词**：水下图像增强, 频率融合, 光照感知, 深度学习模型, 实时应用, 数据集构建

## 3 点简述
- 水下图像因光吸收和散射导致颜色失真、低对比度和雾状外观。
- AQUA-Net集成残差编码解码器，在频率和光照域操作，通过频率融合和光照感知恢复细节。
- 实验表明模型在多个数据集上性能与SOTA相当，参数更少，泛化能力强。

## 摘要（原文）

> Underwater images often suffer from severe color distortion, low contrast, and a hazy appearance due to wavelength-dependent light absorption and scattering. Simultaneously, existing deep learning models exhibit high computational complexity, which limits their practical deployment for real-time underwater applications. To address these challenges, this paper presents a novel underwater image enhancement model, called Adaptive Frequency Fusion and Illumination Aware Network (AQUA-Net). It integrates a residual encoder decoder with dual auxiliary branches, which operate in the frequency and illumination domains. The frequency fusion encoder enriches spatial representations with frequency cues from the Fourier domain and preserves fine textures and structural details. Inspired by Retinex, the illumination-aware decoder performs adaptive exposure correction through a learned illumination map that separates reflectance from lighting effects. This joint spatial, frequency, and illumination design enables the model to restore color balance, visual contrast, and perceptual realism under diverse underwater conditions. Additionally, we present a high-resolution, real-world underwater video-derived dataset from the Mediterranean Sea, which captures challenging deep-sea conditions with realistic visual degradations to enable robust evaluation and development of deep learning models. Extensive experiments on multiple benchmark datasets show that AQUA-Net performs on par with SOTA in both qualitative and quantitative evaluations while using less number of parameters. Ablation studies further confirm that the frequency and illumination branches provide complementary contributions that improve visibility and color representation. Overall, the proposed model shows strong generalization capability and robustness, and it provides an effective solution for real-world underwater imaging applications.

