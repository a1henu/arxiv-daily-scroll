---
layout: default
title: NativeTok: Native Visual Tokenization for Improved Image Generation
---

# NativeTok: Native Visual Tokenization for Improved Image Generation
**arXiv**：[2601.22837v1](https://arxiv.org/abs/2601.22837) · [PDF](https://arxiv.org/pdf/2601.22837.pdf)  
**作者**：Bin Wu, Mengqi Huang, Weinan Jia, Zhendong Mao  

**一句话要点**：提出NativeTok框架，通过原生视觉分词改进基于VQ的图像生成

**关键词**：图像生成, 视觉分词, 因果依赖, Transformer模型, 分层训练

## 3 点简述
- 核心问题：现有VQ图像生成中分词与生成阶段不匹配，导致依赖关系弱和偏差
- 方法要点：引入原生视觉分词，使用MIT和MoCET嵌入因果依赖，并设计分层训练策略
- 实验或效果：广泛实验验证NativeTok在高效重建和提升生成一致性方面的有效性

## 摘要（原文）

> VQ-based image generation typically follows a two-stage pipeline: a tokenizer encodes images into discrete tokens, and a generative model learns their dependencies for reconstruction. However, improved tokenization in the first stage does not necessarily enhance the second-stage generation, as existing methods fail to constrain token dependencies. This mismatch forces the generative model to learn from unordered distributions, leading to bias and weak coherence. To address this, we propose native visual tokenization, which enforces causal dependencies during tokenization. Building on this idea, we introduce NativeTok, a framework that achieves efficient reconstruction while embedding relational constraints within token sequences. NativeTok consists of: (1) a Meta Image Transformer (MIT) for latent image modeling, and (2) a Mixture of Causal Expert Transformer (MoCET), where each lightweight expert block generates a single token conditioned on prior tokens and latent features. We further design a Hierarchical Native Training strategy that updates only new expert blocks, ensuring training efficiency. Extensive experiments demonstrate the effectiveness of NativeTok.

