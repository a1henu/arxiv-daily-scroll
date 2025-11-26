---
layout: default
title: iMontage: Unified, Versatile, Highly Dynamic Many-to-many Image Generation
---

# iMontage: Unified, Versatile, Highly Dynamic Many-to-many Image Generation
**arXiv**：[2511.20635v1](https://arxiv.org/abs/2511.20635) · [PDF](https://arxiv.org/pdf/2511.20635.pdf)  
**作者**：Zhoujie Fu, Xianfang Zeng, Jinghong Lan, Xinyao Liao, Cheng Chen, Junyi Chen, Jiacheng Wei, Wei Cheng, Shiyu Liu, Yunuo Chen, Gang Yu, Guosheng Lin  

**一句话要点**：提出iMontage框架，将视频模型重用于多对多图像生成，实现高动态范围与自然过渡。

**关键词**：多对多图像生成, 视频模型适应, 动态范围扩展, 上下文一致性, 图像编辑统一框架

## 3 点简述
- 核心问题：视频模型动态受限，难以生成高多样性图像集。
- 方法要点：采用最小侵入式适应策略，结合数据整理与训练范式。
- 实验或效果：在多项任务中保持上下文一致性，生成超常规动态场景。

## 摘要（原文）

> Pre-trained video models learn powerful priors for generating high-quality, temporally coherent content. While these models excel at temporal coherence, their dynamics are often constrained by the continuous nature of their training data. We hypothesize that by injecting the rich and unconstrained content diversity from image data into this coherent temporal framework, we can generate image sets that feature both natural transitions and a far more expansive dynamic range. To this end, we introduce iMontage, a unified framework designed to repurpose a powerful video model into an all-in-one image generator. The framework consumes and produces variable-length image sets, unifying a wide array of image generation and editing tasks. To achieve this, we propose an elegant and minimally invasive adaptation strategy, complemented by a tailored data curation process and training paradigm. This approach allows the model to acquire broad image manipulation capabilities without corrupting its invaluable original motion priors. iMontage excels across several mainstream many-in-many-out tasks, not only maintaining strong cross-image contextual consistency but also generating scenes with extraordinary dynamics that surpass conventional scopes. Find our homepage at: https://kr1sjfu.github.io/iMontage-web/.

