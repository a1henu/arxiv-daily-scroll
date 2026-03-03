---
layout: default
title: Phase-Type Variational Autoencoders for Heavy-Tailed Data
---

# Phase-Type Variational Autoencoders for Heavy-Tailed Data
**arXiv**：[2603.01800v1](https://arxiv.org/abs/2603.01800) · [PDF](https://arxiv.org/pdf/2603.01800.pdf)  
**作者**：Abdelhakim Ziani, András Horváth, Paolo Ballarini  

**一句话要点**：提出相位型变分自编码器以解决重尾数据建模问题

**关键词**：变分自编码器, 重尾分布, 相位型分布, 连续时间马尔可夫链, 生成建模, 尾部依赖

## 3 点简述
- 标准变分自编码器使用简单解码器分布，无法有效捕捉重尾行为
- PH-VAE采用相位型分布作为解码器，通过连续时间马尔可夫链吸收时间灵活适应尾部
- 实验表明PH-VAE在合成和真实数据上优于高斯、学生t和极值分布解码器

## 摘要（原文）

> Heavy-tailed distributions are ubiquitous in real-world data, where rare but extreme events dominate risk and variability. However, standard Variational Autoencoders (VAEs) employ simple decoder distributions (e.g., Gaussian) that fail to capture heavy-tailed behavior, while existing heavy-tail-aware extensions remain restricted to predefined parametric families whose tail behavior is fixed a priori.
>   We propose the Phase-Type Variational Autoencoder (PH-VAE), whose decoder distribution is a latent-conditioned Phase-Type (PH) distribution defined as the absorption time of a continuous-time Markov chain (CTMC). This formulation composes multiple exponential time scales, yielding a flexible and analytically tractable decoder that adapts its tail behavior directly from the observed data. Experiments on synthetic and real-world benchmarks demonstrate that PH-VAE accurately recovers diverse heavy-tailed distributions, significantly outperforming Gaussian, Student-t, and extreme-value-based VAE decoders in modeling tail behavior and extreme quantiles. In multivariate settings, PH-VAE captures realistic cross-dimensional tail dependence through its shared latent representation. To our knowledge, this is the first work to integrate Phase-Type distributions into deep generative modeling, bridging applied probability and representation learning.

