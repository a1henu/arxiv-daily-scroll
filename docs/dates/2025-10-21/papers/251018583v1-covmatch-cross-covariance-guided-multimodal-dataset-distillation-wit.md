---
layout: default
title: CovMatch: Cross-Covariance Guided Multimodal Dataset Distillation with Trainable Text Encoder
---

# CovMatch: Cross-Covariance Guided Multimodal Dataset Distillation with Trainable Text Encoder
**arXiv**：[2510.18583v1](https://arxiv.org/abs/2510.18583) · [PDF](https://arxiv.org/pdf/2510.18583.pdf)  
**作者**：Yongmin Lee, Hye Won Chung  

**一句话要点**：提出CovMatch以解决多模态数据集蒸馏中的跨模态对齐和可扩展性问题

**关键词**：多模态数据集蒸馏, 跨模态对齐, 跨协方差指导, 联合编码器优化, 检索准确率提升

## 3 点简述
- 核心问题：多模态对比学习数据集蒸馏面临跨模态对齐困难和计算成本高的问题
- 方法要点：通过跨协方差对齐和模态内特征正则化，联合优化图像和文本编码器
- 实验或效果：在Flickr30K和COCO上，使用500合成对实现检索准确率最高提升6.8%

## 摘要（原文）

> Multimodal dataset distillation aims to synthesize a small set of image-text
> pairs that enables efficient training of large-scale vision-language models.
> While dataset distillation has shown promise in unimodal tasks, extending it to
> multimodal contrastive learning presents key challenges: learning cross-modal
> alignment and managing the high computational cost of large encoders. Prior
> approaches address scalability by freezing the text encoder and update only the
> image encoder and text projection layer. However, we find this severely limits
> semantic alignment and becomes a bottleneck for performance scaling. We propose
> CovMatch, a scalable dataset distillation framework that aligns the
> cross-covariance of real and synthetic features while regularizing feature
> distributions within each modality. Unlike prior approaches, CovMatch enables
> joint optimization of both encoders, leading to stronger cross-modal alignment
> and improved performance. Evaluated on Flickr30K and COCO, CovMatch outperforms
> state-of-the-art multimodal distillation methods and achieves up to 6.8%
> absolute gains in retrieval accuracy using only 500 synthetic pairs.

