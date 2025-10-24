---
layout: default
title: SpectraMorph: Structured Latent Learning for Self-Supervised Hyperspectral Super-Resolution
---

# SpectraMorph: Structured Latent Learning for Self-Supervised Hyperspectral Super-Resolution
**arXiv**：[2510.20814v1](https://arxiv.org/abs/2510.20814) · [PDF](https://arxiv.org/pdf/2510.20814.pdf)  
**作者**：Ritik Shah, Marco F Duarte  

**一句话要点**：提出SpectraMorph框架，通过结构化潜空间和自监督学习解决高光谱图像超分辨率问题。

**关键词**：高光谱超分辨率, 自监督学习, 结构化潜空间, 解混瓶颈, 图像融合, 物理引导模型

## 3 点简述
- 高光谱传感器空间分辨率低，导致边界模糊和混合像素问题。
- 采用物理引导的自监督方法，通过解混瓶颈和线性混合重建光谱。
- 实验显示在合成和真实数据集上优于无监督基线，并接近监督方法性能。

## 摘要（原文）

> Hyperspectral sensors capture dense spectra per pixel but suffer from low
> spatial resolution, causing blurred boundaries and mixed-pixel effects.
> Co-registered companion sensors such as multispectral, RGB, or panchromatic
> cameras provide high-resolution spatial detail, motivating hyperspectral
> super-resolution through the fusion of hyperspectral and multispectral images
> (HSI-MSI). Existing deep learning based methods achieve strong performance but
> rely on opaque regressors that lack interpretability and often fail when the
> MSI has very few bands. We propose SpectraMorph, a physics-guided
> self-supervised fusion framework with a structured latent space. Instead of
> direct regression, SpectraMorph enforces an unmixing bottleneck: endmember
> signatures are extracted from the low-resolution HSI, and a compact multilayer
> perceptron predicts abundance-like maps from the MSI. Spectra are reconstructed
> by linear mixing, with training performed in a self-supervised manner via the
> MSI sensor's spectral response function. SpectraMorph produces interpretable
> intermediates, trains in under a minute, and remains robust even with a
> single-band (pan-chromatic) MSI. Experiments on synthetic and real-world
> datasets show SpectraMorph consistently outperforming state-of-the-art
> unsupervised/self-supervised baselines while remaining very competitive against
> supervised baselines.

