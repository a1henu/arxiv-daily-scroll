---
layout: default
title: SAMRI: Segment Anything Model for MRI
---

# SAMRI: Segment Anything Model for MRI
**arXiv**：[2510.26635v1](https://arxiv.org/abs/2510.26635) · [PDF](https://arxiv.org/pdf/2510.26635.pdf)  
**作者**：Zhao Wang, Wei Dai, Thuy Thanh Dao, Steffen Bollmann, Hongfu Sun, Craig Engstrom, Shekhar S. Chandra  

**一句话要点**：提出SAMRI以解决MRI分割中的泛化问题，通过微调SAM适应MRI模态。

**关键词**：医学图像分割, Segment Anything Model, MRI适应, 微调策略, 泛化性能

## 3 点简述
- 核心问题：MRI分割因对比度、强度不均和协议差异导致CNN方法泛化差。
- 方法要点：采用两阶段策略微调SAM的掩码解码器，大幅减少训练时间和参数。
- 实验或效果：在百万MR切片上验证，平均Dice达0.87，泛化能力强。

## 摘要（原文）

> Accurate magnetic resonance imaging (MRI) segmentation is crucial for
> clinical decision-making, but remains labor-intensive when performed manually.
> Convolutional neural network (CNN)-based methods can be accurate and efficient,
> but often generalize poorly to MRI's variable contrast, intensity
> inhomogeneity, and protocols. Although the transformer-based Segment Anything
> Model (SAM) has demonstrated remarkable generalizability in natural images,
> existing adaptations often treat MRI as another imaging modality, overlooking
> these modality-specific challenges. We present SAMRI, an MRI-specialized SAM
> trained and validated on 1.1 million labeled MR slices spanning whole-body
> organs and pathologies. We demonstrate that SAM can be effectively adapted to
> MRI by simply fine-tuning its mask decoder using a two-stage strategy, reducing
> training time by 94% and trainable parameters by 96% versus full-model
> retraining. Across diverse MRI segmentation tasks, SAMRI achieves a mean Dice
> of 0.87, delivering state-of-the-art accuracy across anatomical regions and
> robust generalization on unseen structures, particularly small and clinically
> important structures.

