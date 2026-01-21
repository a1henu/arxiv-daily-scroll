---
layout: default
title: Towards Effective Negation Modeling in Joint Audio-Text Models for Music
---

# Towards Effective Negation Modeling in Joint Audio-Text Models for Music
**arXiv**：[2601.13931v1](https://arxiv.org/abs/2601.13931) · [PDF](https://arxiv.org/pdf/2601.13931.pdf)  
**作者**：Yannis Vasilakis, Rachel Bittner, Johan Pauwels  

**一句话要点**：提出文本增强和对比损失方法，以改进联合音频-文本模型在音乐中的否定语义建模。

**关键词**：联合音频-文本模型, 否定语义建模, 对比学习, 音乐检索, 文本增强

## 3 点简述
- 核心问题：联合音频-文本模型在音乐检索中难以可靠处理否定语义，如区分有无音乐元素。
- 方法要点：通过文本增强引入否定，并设计基于差异的对比损失，在嵌入空间中显式分离原始和否定描述。
- 实验或效果：实验表明，该方法在提升否定处理能力的同时，基本保持了检索性能。

## 摘要（原文）

> Joint audio-text models are widely used for music retrieval, yet they struggle with semantic phenomena such as negation. Negation is fundamental for distinguishing the absence (or presence) of musical elements (e.g., "with vocals" vs. "without vocals"), but current systems fail to represent this reliably. In this work, we investigate and mitigate this limitation by training CLAP models from scratch on the Million Song Dataset with LP-MusicCaps-MSD captions. We introduce negation through text augmentation and a dissimilarity-based contrastive loss, designed to explicitly separate original and negated captions in the joint embedding space. To evaluate progress, we propose two protocols that frame negation modeling as retrieval and binary classification tasks. Experiments demonstrate that both methods, individually and combined, improve negation handling while largely preserving retrieval performance.

