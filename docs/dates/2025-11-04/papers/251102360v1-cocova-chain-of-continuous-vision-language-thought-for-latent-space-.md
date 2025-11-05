---
layout: default
title: CoCoVa: Chain of Continuous Vision-Language Thought for Latent Space Reasoning
---

# CoCoVa: Chain of Continuous Vision-Language Thought for Latent Space Reasoning
**arXiv**：[2511.02360v1](https://arxiv.org/abs/2511.02360) · [PDF](https://arxiv.org/pdf/2511.02360.pdf)  
**作者**：Jizheng Ma, Xiaofei Zhou, Yanlong Song, Han Yan  

**一句话要点**：提出CoCoVa框架，通过连续潜空间推理解决视觉语言模型离散化瓶颈问题

**关键词**：视觉语言模型, 连续推理, 潜空间优化, 多任务学习, 跨模态融合, 注意力机制

## 3 点简述
- 核心问题：视觉语言模型受限于离散语言空间，无法充分表达视觉感知的丰富性。
- 方法要点：引入LQ-Former迭代优化潜思维向量，结合对比学习和扩散重建进行多任务训练。
- 实验或效果：在1.5B骨干模型上超越或媲美更大模型，潜空间捕获可解释推理模式。

## 摘要（原文）

> In human cognition, there exist numerous thought processes that are tacit and
> beyond verbal expression, enabling us to understand and interact with the world
> in multiple ways. However, contemporary Vision-Language Models (VLMs) remain
> constrained to reasoning within the discrete and rigid space of linguistic
> tokens, thereby bottlenecking the rich, high-dimensional nature of visual
> perception. To bridge this gap, we propose CoCoVa (Chain of Continuous
> Vision-Language Thought), a novel framework for vision-language model that
> leverages continuous cross-modal reasoning for diverse vision-language tasks.
> The core of CoCoVa is an iterative reasoning cycle, where a novel Latent
> Q-Former (LQ-Former) acts as a dynamic reasoning engine, iteratively refining a
> chain of latent thought vectors through cross-modal fusion. To focus this
> process, a token selection mechanism dynamically identifies salient visual
> regions, mimicking attentional focus. To ensure these latent thoughts remain
> grounded, we train the model with a multi-task objective that combines
> contrastive learning and diffusion-based reconstruction, enforcing alignment
> between latent representations and both visual and textual modalities.
> Evaluations show CoCoVa improves accuracy and token efficiency over strong
> baselines. With a 1.5B backbone, it competes with or surpasses larger 7B-9B
> models on almost all benchmarks. When scaled to 7B LLM backbones, it remains
> competitive with state-of-the-art models. Qualitative analysis validates that
> learned latent space captures interpretable and structured reasoning patterns,
> highlighting the potential of CoCoVa to bridge the representational gap between
> discrete language processing and the continuous nature of visual understanding.

