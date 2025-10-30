---
layout: default
title: DRIP: Dynamic patch Reduction via Interpretable Pooling
---

# DRIP: Dynamic patch Reduction via Interpretable Pooling
**arXiv**：[2510.25067v1](https://arxiv.org/abs/2510.25067) · [PDF](https://arxiv.org/pdf/2510.25067.pdf)  
**作者**：Yusen Peng, Sachin Kumar  

**一句话要点**：提出DRIP方法以降低视觉语言模型预训练计算成本

**关键词**：视觉语言模型, 动态令牌合并, 计算效率优化, 对比预训练, 图像分类

## 3 点简述
- 核心问题：大规模视觉语言模型预训练计算成本高，阻碍从头训练。
- 方法要点：通过可解释池化动态合并视觉编码器深层令牌，适应输入图像。
- 实验效果：在ImageNet和CLIP预训练中显著减少GFLOP，保持性能。

## 摘要（原文）

> Recently, the advances in vision-language models, including contrastive
> pretraining and instruction tuning, have greatly pushed the frontier of
> multimodal AI. However, owing to the large-scale and hence expensive
> pretraining, the efficiency concern has discouraged researchers from attempting
> to pretrain a vision language model from scratch. In this work, we propose
> Dynamic patch Reduction via Interpretable Pooling (DRIP), which adapts to the
> input images and dynamically merges tokens in the deeper layers of a visual
> encoder. Our results on both ImageNet training from scratch and CLIP
> contrastive pretraining demonstrate a significant GFLOP reduction while
> maintaining comparable classification/zero-shot performance. To further
> validate our proposed method, we conduct continual pretraining on a large
> biology dataset, extending its impact into scientific domains.

