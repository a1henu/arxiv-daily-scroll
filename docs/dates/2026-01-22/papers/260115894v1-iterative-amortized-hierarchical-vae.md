---
layout: default
title: Iterative Amortized Hierarchical VAE
---

# Iterative Amortized Hierarchical VAE
**arXiv**：[2601.15894v1](https://arxiv.org/abs/2601.15894) · [PDF](https://arxiv.org/pdf/2601.15894.pdf)  
**作者**：Simon W. Penninga, Ruud J. G. van Sloun  

**一句话要点**：提出迭代摊销分层变分自编码器，结合摊销推理与迭代优化以加速逆问题求解。

**关键词**：变分自编码器, 摊销推理, 迭代优化, 逆问题求解, 实时应用

## 3 点简述
- 核心问题：传统分层变分自编码器在迭代推理时速度慢，影响实时应用。
- 方法要点：采用混合推理方案，先摊销初始猜测，再基于解码器梯度迭代精炼，并在变换域设计线性可分离解码器。
- 实验或效果：实现35倍加速，在去模糊和去噪等逆问题中重建质量优于传统方法。

## 摘要（原文）

> In this paper we propose the Iterative Amortized Hierarchical Variational Autoencoder (IA-HVAE), which expands on amortized inference with a hybrid scheme containing an initial amortized guess and iterative refinement with decoder gradients. We achieve this by creating a linearly separable decoder in a transform domain (e.g. Fourier space), enabling real-time applications with very high model depths. The architectural change leads to a 35x speed-up for iterative inference with respect to the traditional HVAE. We show that our hybrid approach outperforms fully amortized and fully iterative equivalents in accuracy and speed respectively. Moreover, the IAHVAE shows improved reconstruction quality over a vanilla HVAE in inverse problems such as deblurring and denoising.

