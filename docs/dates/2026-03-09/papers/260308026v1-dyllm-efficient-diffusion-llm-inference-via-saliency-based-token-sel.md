---
layout: default
title: DyLLM: Efficient Diffusion LLM Inference via Saliency-based Token Selection and Partial Attention
---

# DyLLM: Efficient Diffusion LLM Inference via Saliency-based Token Selection and Partial Attention
**arXiv**：[2603.08026v1](https://arxiv.org/abs/2603.08026) · [PDF](https://arxiv.org/pdf/2603.08026.pdf)  
**作者**：Younjoo Lee, Junghoo Lee, Seungkyun Dan, Jaiyoung Park, Jung Ho Ahn  

**一句话要点**：提出DyLLM框架，通过基于显著性的令牌选择与部分注意力，加速掩码扩散语言模型的推理效率。

**关键词**：扩散语言模型, 推理加速, 令牌选择, 部分注意力, 时序稀疏性, 高效解码

## 3 点简述
- 核心问题：掩码扩散语言模型推理时迭代去噪过程计算开销大，因每步需处理整个序列。
- 方法要点：利用令牌表示的时序稀疏性，基于注意力上下文余弦相似度识别显著令牌，仅重新计算其前馈与注意力操作。
- 实验或效果：在推理与代码生成基准测试中，实现高达9.6倍吞吐量提升，同时基本保持LLaDA和Dream等模型的基线准确率。

## 摘要（原文）

> Masked Diffusion Language Models (MDLMs) enable parallel token decoding, providing a promising alternative to the sequential nature of autoregressive generation. However, their iterative denoising process remains computationally expensive because it repeatedly processes the entire sequence at every step. We observe that across these diffusion steps, most token representations remain stable; only a small subset, which we term salient tokens, contributes meaningfully to the next update. Leveraging this temporal sparsity, we present DyLLM, a training-free inference framework that accelerates decoding by selectively computing only these salient tokens. DyLLM identifies saliency by measuring the cosine similarity of attention contexts between adjacent denoising steps. It recomputes feed-forward and attention operations only for salient tokens while reusing cached activations for the remainder. Across diverse reasoning and code-generation benchmarks, DyLLM achieves up to 9.6x higher throughput while largely preserving the baseline accuracy of state-of-the-art models like LLaDA and Dream.

