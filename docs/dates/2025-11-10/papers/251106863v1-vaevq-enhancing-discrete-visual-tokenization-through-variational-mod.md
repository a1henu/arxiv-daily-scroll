---
layout: default
title: VAEVQ: Enhancing Discrete Visual Tokenization through Variational Modeling
---

# VAEVQ: Enhancing Discrete Visual Tokenization through Variational Modeling
**arXiv**：[2511.06863v1](https://arxiv.org/abs/2511.06863) · [PDF](https://arxiv.org/pdf/2511.06863.pdf)  
**作者**：Sicheng Yang, Xing Hu, Qiang Wu, Dawei Yang  

**一句话要点**：提出VAEVQ以解决向量量化中的潜在空间不平滑和码本利用不足问题

**关键词**：向量量化, 变分自编码器, 离散表示, 码本学习, 生成模型, 潜在空间对齐

## 3 点简述
- 核心问题：向量量化导致潜在空间不平滑、量化前后特征对齐弱，影响生成模型性能
- 方法要点：引入变分潜在量化、表示一致性策略和分布一致性正则化，提升码本利用
- 实验或效果：在基准数据集上优于现有方法，改善重建和生成任务表现

## 摘要（原文）

> Vector quantization (VQ) transforms continuous image features into discrete
> representations, providing compressed, tokenized inputs for generative models.
> However, VQ-based frameworks suffer from several issues, such as non-smooth
> latent spaces, weak alignment between representations before and after
> quantization, and poor coherence between the continuous and discrete domains.
> These issues lead to unstable codeword learning and underutilized codebooks,
> ultimately degrading the performance of both reconstruction and downstream
> generation tasks. To this end, we propose VAEVQ, which comprises three key
> components: (1) Variational Latent Quantization (VLQ), replacing the AE with a
> VAE for quantization to leverage its structured and smooth latent space,
> thereby facilitating more effective codeword activation; (2) Representation
> Coherence Strategy (RCS), adaptively modulating the alignment strength between
> pre- and post-quantization features to enhance consistency and prevent
> overfitting to noise; and (3) Distribution Consistency Regularization (DCR),
> aligning the entire codebook distribution with the continuous latent
> distribution to improve utilization. Extensive experiments on two benchmark
> datasets demonstrate that VAEVQ outperforms state-of-the-art methods.

