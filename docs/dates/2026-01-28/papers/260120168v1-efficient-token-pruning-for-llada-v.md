---
layout: default
title: Efficient Token Pruning for LLaDA-V
---

# Efficient Token Pruning for LLaDA-V
**arXiv**：[2601.20168v1](https://arxiv.org/abs/2601.20168) · [PDF](https://arxiv.org/pdf/2601.20168.pdf)  
**作者**：Zhewen Wan, Tianchen Song, Chen Lin, Zhiyong Zhao, Xianpeng Lang  

**一句话要点**：提出结构化令牌剪枝策略以提升LLaDA-V的计算效率

**关键词**：令牌剪枝, 扩散模型, 多模态模型, 计算效率, 注意力分析

## 3 点简述
- LLaDA-V等扩散式大模型因双向注意力和迭代去噪导致计算开销大
- 通过注意力分析发现跨模态信息聚合在中后层，提出针对中后层的令牌剪枝
- 实验显示最佳配置减少65%计算成本，保持95%任务性能

## 摘要（原文）

> Diffusion-based large multimodal models, such as LLaDA-V, have demonstrated impressive capabilities in vision-language understanding and generation. However, their bidirectional attention mechanism and diffusion-style iterative denoising paradigm introduce significant computational overhead, as visual tokens are repeatedly processed across all layers and denoising steps. In this work, we conduct an in-depth attention analysis and reveal that, unlike autoregressive decoders, LLaDA-V aggregates cross-modal information predominantly in middle-to-late layers, leading to delayed semantic alignment. Motivated by this observation, we propose a structured token pruning strategy inspired by FastV, selectively removing a proportion of visual tokens at designated layers to reduce FLOPs while preserving critical semantic information. To the best of our knowledge, this is the first work to investigate structured token pruning in diffusion-based large multimodal models. Unlike FastV, which focuses on shallow-layer pruning, our method targets the middle-to-late layers of the first denoising step to align with LLaDA-V's delayed attention aggregation to maintain output quality, and the first-step pruning strategy reduces the computation across all subsequent steps. Our framework provides an empirical basis for efficient LLaDA-V inference and highlights the potential of vision-aware pruning in diffusion-based multimodal models. Across multiple benchmarks, our best configuration reduces computational cost by up to 65% while preserving an average of 95% task performance.

