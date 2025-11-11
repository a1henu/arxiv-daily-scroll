---
layout: default
title: NeuroBridge: Bio-Inspired Self-Supervised EEG-to-Image Decoding via Cognitive Priors and Bidirectional Semantic Alignment
---

# NeuroBridge: Bio-Inspired Self-Supervised EEG-to-Image Decoding via Cognitive Priors and Bidirectional Semantic Alignment
**arXiv**：[2511.06836v1](https://arxiv.org/abs/2511.06836) · [PDF](https://arxiv.org/pdf/2511.06836.pdf)  
**作者**：Wenjiang Zhang, Sifeng Wang, Yuwei Su, Xinyu Li, Chen Zhang, Suyu Zhong  

**一句话要点**：提出NeuroBridge自监督架构，通过认知先验和双向语义对齐解决脑电到图像解码的语义不匹配问题。

**关键词**：脑电到图像解码, 自监督学习, 跨模态对齐, 认知先验, 零样本检索

## 3 点简述
- 核心问题：脑电与图像数据稀缺且语义不匹配，限制视觉神经解码性能。
- 方法要点：结合认知先验增强和共享语义投影器，实现双向跨模态对齐。
- 实验效果：在200路零样本检索任务中，准确率显著提升，优于现有方法。

## 摘要（原文）

> Visual neural decoding seeks to reconstruct or infer perceived visual stimuli
> from brain activity patterns, providing critical insights into human cognition
> and enabling transformative applications in brain-computer interfaces and
> artificial intelligence. Current approaches, however, remain constrained by the
> scarcity of high-quality stimulus-brain response pairs and the inherent
> semantic mismatch between neural representations and visual content. Inspired
> by perceptual variability and co-adaptive strategy of the biological systems,
> we propose a novel self-supervised architecture, named NeuroBridge, which
> integrates Cognitive Prior Augmentation (CPA) with Shared Semantic Projector
> (SSP) to promote effective cross-modality alignment. Specifically, CPA
> simulates perceptual variability by applying asymmetric, modality-specific
> transformations to both EEG signals and images, enhancing semantic diversity.
> Unlike previous approaches, SSP establishes a bidirectional alignment process
> through a co-adaptive strategy, which mutually aligns features from two
> modalities into a shared semantic space for effective cross-modal learning.
> NeuroBridge surpasses previous state-of-the-art methods under both
> intra-subject and inter-subject settings. In the intra-subject scenario, it
> achieves the improvements of 12.3% in top-1 accuracy and 10.2% in top-5
> accuracy, reaching 63.2% and 89.9% respectively on a 200-way zero-shot
> retrieval task. Extensive experiments demonstrate the effectiveness,
> robustness, and scalability of the proposed framework for neural visual
> decoding.

