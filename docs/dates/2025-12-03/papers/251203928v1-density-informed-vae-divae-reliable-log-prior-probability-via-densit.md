---
layout: default
title: Density-Informed VAE (DiVAE): Reliable Log-Prior Probability via Density Alignment Regularization
---

# Density-Informed VAE (DiVAE): Reliable Log-Prior Probability via Density Alignment Regularization
**arXiv**：[2512.03928v1](https://arxiv.org/abs/2512.03928) · [PDF](https://arxiv.org/pdf/2512.03928.pdf)  
**作者**：Michele Alessi, Alessio Ansuini, Alex Rodriguez  

**一句话要点**：提出DiVAE以通过密度对齐正则化提升VAE先验概率的可靠性

**关键词**：变分自编码器, 密度对齐, 正则化方法, 先验学习, 异常检测, 不确定性校准

## 3 点简述
- 标准VAE忽略数据空间密度结构，导致先验与数据不匹配
- DiVAE通过数据驱动正则化对齐先验与估计密度，优化后验分配
- 在合成和MNIST数据集上改善对齐、覆盖和OOD不确定性校准

## 摘要（原文）

> We introduce Density-Informed VAE (DiVAE), a lightweight, data-driven regularizer that aligns the VAE log-prior probability $\log p_Z(z)$ with a log-density estimated from data. Standard VAEs match latents to a simple prior, overlooking density structure in the data-space. DiVAE encourages the encoder to allocate posterior mass in proportion to data-space density and, when the prior is learnable, nudges the prior toward high-density regions. This is realized by adding a robust, precision-weighted penalty to the ELBO, incurring negligible computational overhead. On synthetic datasets, DiVAE (i) improves distributional alignment of latent log-densities to its ground truth counterpart, (ii) improves prior coverage, and (iii) yields better OOD uncertainty calibration. On MNIST, DiVAE improves alignment of the prior with external estimates of the density, providing better interpretability, and improves OOD detection for learnable priors.

