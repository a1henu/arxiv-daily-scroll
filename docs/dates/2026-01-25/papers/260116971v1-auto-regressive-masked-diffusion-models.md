---
layout: default
title: Auto-Regressive Masked Diffusion Models
---

# Auto-Regressive Masked Diffusion Models
**arXiv**：[2601.16971v1](https://arxiv.org/abs/2601.16971) · [PDF](https://arxiv.org/pdf/2601.16971.pdf)  
**作者**：Mahdi Karami, Ali Ghodsi  

**一句话要点**：提出自回归掩码扩散模型以统一训练效率与并行生成能力

**关键词**：自回归模型, 掩码扩散模型, 并行文本生成, 因果架构, 训练效率, 语言建模

## 3 点简述
- 掩码扩散模型在语言建模中性能落后于自回归模型且训练迭代多
- 将掩码扩散重构为块级因果模型，实现单次并行前向计算所有条件概率
- 实验显示在标准基准上达到最优性能，显著减少训练步骤并加速推理

## 摘要（原文）

> Masked diffusion models (MDMs) have emerged as a promising approach for language modeling, yet they face a performance gap compared to autoregressive models (ARMs) and require more training iterations. In this work, we present the Auto-Regressive Masked Diffusion (ARMD) model, an architecture designed to close this gap by unifying the training efficiency of autoregressive models with the parallel generation capabilities of diffusion-based models. Our key insight is to reframe the masked diffusion process as a block-wise causal model. This perspective allows us to design a strictly causal, permutation-equivariant architecture that computes all conditional probabilities across multiple denoising steps in a single, parallel forward pass. The resulting architecture supports efficient, autoregressive-style decoding and a progressive permutation training scheme, allowing the model to learn both canonical left-to-right and random token orderings. Leveraging this flexibility, we introduce a novel strided parallel generation strategy that accelerates inference by generating tokens in parallel streams while maintaining global coherence. Empirical results demonstrate that ARMD achieves state-of-the-art performance on standard language modeling benchmarks, outperforming established diffusion baselines while requiring significantly fewer training steps. Furthermore, it establishes a new benchmark for parallel text generation, effectively bridging the performance gap between parallel and sequential decoding.

