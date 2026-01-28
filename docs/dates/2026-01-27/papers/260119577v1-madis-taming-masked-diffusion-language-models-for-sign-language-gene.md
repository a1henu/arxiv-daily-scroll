---
layout: default
title: MaDiS: Taming Masked Diffusion Language Models for Sign Language Generation
---

# MaDiS: Taming Masked Diffusion Language Models for Sign Language Generation
**arXiv**：[2601.19577v1](https://arxiv.org/abs/2601.19577) · [PDF](https://arxiv.org/pdf/2601.19577.pdf)  
**作者**：Ronglai Zuo, Rolandos Alexandros Potamias, Qi Sun, Evangelos Ververas, Jiankang Deng, Stefanos Zafeiriou  

**一句话要点**：提出MaDiS，一种基于掩码扩散的语言模型，用于手语生成，以解决自回归模型单向依赖和推理慢的问题。

**关键词**：手语生成, 掩码扩散模型, 跨模态预训练, 并行推理, 三层次学习, 解掩码策略

## 3 点简述
- 核心问题：自回归语言模型在手语生成中存在单向上下文建模和逐令牌推理慢的局限性。
- 方法要点：采用掩码扩散模型捕获双向依赖并支持并行多令牌生成，引入三层次跨模态预训练和新型解掩码策略加速收敛。
- 实验或效果：在多个数据集上实现优越性能，包括降低DTW误差和引入新指标，推理延迟减少近30%。

## 摘要（原文）

> Sign language generation (SLG) aims to translate written texts into expressive sign motions, bridging communication barriers for the Deaf and Hard-of-Hearing communities. Recent studies formulate SLG within the language modeling framework using autoregressive language models, which suffer from unidirectional context modeling and slow token-by-token inference. To address these limitations, we present MaDiS, a masked-diffusion-based language model for SLG that captures bidirectional dependencies and supports efficient parallel multi-token generation. We further introduce a tri-level cross-modal pretraining scheme that jointly learns from token-, latent-, and 3D physical-space objectives, leading to richer and more grounded sign representations. To accelerate model convergence in the fine-tuning stage, we design a novel unmasking strategy with temporal checkpoints, reducing the combinatorial complexity of unmasking orders by over $10^{41}$ times. In addition, a mixture-of-parts embedding layer is developed to effectively fuse information stored in different part-wise sign tokens through learnable gates and well-optimized codebooks. Extensive experiments on CSL-Daily, Phoenix-2014T, and How2Sign demonstrate that MaDiS achieves superior performance across multiple metrics, including DTW error and two newly introduced metrics, SiBLEU and SiCLIP, while reducing inference latency by nearly 30%. Code and models will be released on our project page.

