---
layout: default
title: A$^{2}$V-SLP: Alignment-Aware Variational Modeling for Disentangled Sign Language Production
---

# A$^{2}$V-SLP: Alignment-Aware Variational Modeling for Disentangled Sign Language Production
**arXiv**：[2602.11861v1](https://arxiv.org/abs/2602.11861) · [PDF](https://arxiv.org/pdf/2602.11861.pdf)  
**作者**：Sümeyye Meryem Taşyürek, Enis Mücahid İskender, Hacer Yalim Keles  

**一句话要点**：提出A²V-SLP框架，通过变分建模和对齐机制改进手语生成中的解耦表示与运动真实性。

**关键词**：手语生成, 变分自编码器, 解耦表示, 非自回归Transformer, 对齐机制, 运动真实性

## 3 点简述
- 核心问题：手语生成中确定性潜在表示可能导致解耦崩溃，影响运动真实性和对齐。
- 方法要点：使用变分自编码器学习发音器级分布，结合非自回归Transformer和gloss注意力机制。
- 实验或效果：在无gloss设置下，实现最先进的回译性能和提升的运动真实性。

## 摘要（原文）

> Building upon recent structural disentanglement frameworks for sign language production, we propose A$^{2}$V-SLP, an alignment-aware variational framework that learns articulator-wise disentangled latent distributions rather than deterministic embeddings. A disentangled Variational Autoencoder (VAE) encodes ground-truth sign pose sequences and extracts articulator-specific mean and variance vectors, which are used as distributional supervision for training a non-autoregressive Transformer. Given text embeddings, the Transformer predicts both latent means and log-variances, while the VAE decoder reconstructs the final sign pose sequences through stochastic sampling at the decoding stage. This formulation maintains articulator-level representations by avoiding deterministic latent collapse through distributional latent modeling. In addition, we integrate a gloss attention mechanism to strengthen alignment between linguistic input and articulated motion. Experimental results show consistent gains over deterministic latent regression, achieving state-of-the-art back-translation performance and improved motion realism in a fully gloss-free setting.

