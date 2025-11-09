---
layout: default
title: Unveiling Deep Semantic Uncertainty Perception for Language-Anchored Multi-modal Vision-Brain Alignment
---

# Unveiling Deep Semantic Uncertainty Perception for Language-Anchored Multi-modal Vision-Brain Alignment
**arXiv**：[2511.04078v1](https://arxiv.org/abs/2511.04078) · [PDF](https://arxiv.org/pdf/2511.04078.pdf)  
**作者**：Zehui Feng, Chenqi Zhang, Mingru Wang, Minuo Wei, Shiwei Cheng, Cuntai Guan, Ting Han  

**一句话要点**：提出Bratrix框架，通过语言锚定多模态对齐解决视觉-脑信号语义解码挑战

**关键词**：多模态对齐, 脑信号解码, 语义不确定性, 语言锚定, 视觉-脑接口, EEG检索

## 3 点简述
- 核心问题：视觉信号与脑信号对齐受限于语义缺失和噪声，影响解码鲁棒性。
- 方法要点：使用语言锚定语义矩阵和不确定性感知模块，实现视觉-语言-脑共享空间对齐。
- 实验或效果：在EEG、MEG、fMRI基准上提升检索、重建和描述性能，EEG检索任务提升14.3%。

## 摘要（原文）

> Unveiling visual semantics from neural signals such as EEG, MEG, and fMRI
> remains a fundamental challenge due to subject variability and the entangled
> nature of visual features. Existing approaches primarily align neural activity
> directly with visual embeddings, but visual-only representations often fail to
> capture latent semantic dimensions, limiting interpretability and deep
> robustness. To address these limitations, we propose Bratrix, the first
> end-to-end framework to achieve multimodal Language-Anchored Vision-Brain
> alignment. Bratrix decouples visual stimuli into hierarchical visual and
> linguistic semantic components, and projects both visual and brain
> representations into a shared latent space, enabling the formation of aligned
> visual-language and brain-language embeddings. To emulate human-like perceptual
> reliability and handle noisy neural signals, Bratrix incorporates a novel
> uncertainty perception module that applies uncertainty-aware weighting during
> alignment. By leveraging learnable language-anchored semantic matrices to
> enhance cross-modal correlations and employing a two-stage training strategy of
> single-modality pretraining followed by multimodal fine-tuning, Bratrix-M
> improves alignment precision. Extensive experiments on EEG, MEG, and fMRI
> benchmarks demonstrate that Bratrix improves retrieval, reconstruction, and
> captioning performance compared to state-of-the-art methods, specifically
> surpassing 14.3% in 200-way EEG retrieval task. Code and model are available.

