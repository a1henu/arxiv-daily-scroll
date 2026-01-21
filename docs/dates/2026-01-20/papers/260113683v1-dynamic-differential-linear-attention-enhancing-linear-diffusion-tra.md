---
layout: default
title: Dynamic Differential Linear Attention: Enhancing Linear Diffusion Transformer for High-Quality Image Generation
---

# Dynamic Differential Linear Attention: Enhancing Linear Diffusion Transformer for High-Quality Image Generation
**arXiv**：[2601.13683v1](https://arxiv.org/abs/2601.13683) · [PDF](https://arxiv.org/pdf/2601.13683.pdf)  
**作者**：Boyuan Cao, Xingbo Yao, Chenhui Wang, Jiaxin Ye, Yujie Wei, Hongming Shan  

**一句话要点**：提出动态差分线性注意力以增强线性扩散变换器，提升高质量图像生成性能

**关键词**：图像生成, 扩散变换器, 线性注意力, 动态注意力机制, 高质量生成

## 3 点简述
- 核心问题：线性扩散变换器因注意力权重过平滑导致生成质量下降
- 方法要点：通过动态投影、动态测量核和令牌差分算子改进线性注意力机制
- 实验或效果：DyDi-LiT在多项指标上优于当前最先进模型，展现实用潜力

## 摘要（原文）

> Diffusion transformers (DiTs) have emerged as a powerful architecture for high-fidelity image generation, yet the quadratic cost of self-attention poses a major scalability bottleneck. To address this, linear attention mechanisms have been adopted to reduce computational cost; unfortunately, the resulting linear diffusion transformers (LiTs) models often come at the expense of generative performance, frequently producing over-smoothed attention weights that limit expressiveness. In this work, we introduce Dynamic Differential Linear Attention (DyDiLA), a novel linear attention formulation that enhances the effectiveness of LiTs by mitigating the oversmoothing issue and improving generation quality. Specifically, the novelty of DyDiLA lies in three key designs: (i) dynamic projection module, which facilitates the decoupling of token representations by learning with dynamically assigned knowledge; (ii) dynamic measure kernel, which provides a better similarity measurement to capture fine-grained semantic distinctions between tokens by dynamically assigning kernel functions for token processing; and (iii) token differential operator, which enables more robust query-to-key retrieval by calculating the differences between the tokens and their corresponding information redundancy produced by dynamic measure kernel. To capitalize on DyDiLA, we introduce a refined LiT, termed DyDi-LiT, that systematically incorporates our advancements. Extensive experiments show that DyDi-LiT consistently outperforms current state-of-the-art (SOTA) models across multiple metrics, underscoring its strong practical potential.

