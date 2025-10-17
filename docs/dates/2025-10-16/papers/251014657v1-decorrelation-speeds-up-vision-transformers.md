---
layout: default
title: Decorrelation Speeds Up Vision Transformers
---

# Decorrelation Speeds Up Vision Transformers
**arXiv**：[2510.14657v1](https://arxiv.org/abs/2510.14657) · [PDF](https://arxiv.org/pdf/2510.14657.pdf)  
**作者**：Kieran Carrigg, Rob van Gastel, Melda Yeghaian, Sander Dalm, Faysal Boughorbel, Marcel van Gerven  

**一句话要点**：提出去相关反向传播以加速视觉变换器预训练，降低计算成本。

**关键词**：视觉变换器, 去相关反向传播, 掩码自编码器, 预训练加速, 图像分割, 能效优化

## 3 点简述
- MAE预训练ViT在低标签场景性能强，但计算成本高，工业应用受限。
- 集成DBP到MAE预训练，减少层间输入相关性，加速收敛且保持稳定。
- 实验显示预训练时间减少21.1%，碳排放降低21.4%，分割mIoU提升1.1点。

## 摘要（原文）

> Masked Autoencoder (MAE) pre-training of vision transformers (ViTs) yields
> strong performance in low-label regimes but comes with substantial
> computational costs, making it impractical in time- and resource-constrained
> industrial settings. We address this by integrating Decorrelated
> Backpropagation (DBP) into MAE pre-training, an optimization method that
> iteratively reduces input correlations at each layer to accelerate convergence.
> Applied selectively to the encoder, DBP achieves faster pre-training without
> loss of stability. On ImageNet-1K pre-training with ADE20K fine-tuning, DBP-MAE
> reduces wall-clock time to baseline performance by 21.1%, lowers carbon
> emissions by 21.4% and improves segmentation mIoU by 1.1 points. We observe
> similar gains when pre-training and fine-tuning on proprietary industrial data,
> confirming the method's applicability in real-world scenarios. These results
> demonstrate that DBP can reduce training time and energy use while improving
> downstream performance for large-scale ViT pre-training.

