---
layout: default
title: PLESS: Pseudo-Label Enhancement with Spreading Scribbles for Weakly Supervised Segmentation
---

# PLESS: Pseudo-Label Enhancement with Spreading Scribbles for Weakly Supervised Segmentation
**arXiv**：[2602.11628v1](https://arxiv.org/abs/2602.11628) · [PDF](https://arxiv.org/pdf/2602.11628.pdf)  
**作者**：Yeva Gabrielyan, Varduhi Yeghiazaryan, Irina Voiculescu  

**一句话要点**：提出PLESS伪标签增强策略，通过层次化区域传播涂鸦信息，提升弱监督分割的可靠性和空间一致性。

**关键词**：弱监督分割, 涂鸦标注, 伪标签增强, 医学图像分割, 空间一致性

## 3 点简述
- 核心问题：涂鸦标注在弱监督分割中存在噪声和不完整监督，伪标签质量限制性能。
- 方法要点：基于图像层次化分区，在语义一致区域内传播涂鸦信息以优化伪标签，框架模型无关。
- 实验或效果：在两个心脏MRI数据集上测试四种涂鸦监督算法，均显示分割精度一致提升。

## 摘要（原文）

> Weakly supervised learning with scribble annotations uses sparse user-drawn strokes to indicate segmentation labels on a small subset of pixels. This annotation reduces the cost of dense pixel-wise labeling, but suffers inherently from noisy and incomplete supervision. Recent scribble-based approaches in medical image segmentation address this limitation using pseudo-label-based training; however, the quality of the pseudo-labels remains a key performance limit. We propose PLESS, a generic pseudo-label enhancement strategy which improves reliability and spatial consistency. It builds on a hierarchical partitioning of the image into a hierarchy of spatially coherent regions. PLESS propagates scribble information to refine pseudo-labels within semantically coherent regions. The framework is model-agnostic and easily integrates into existing pseudo-label methods. Experiments on two public cardiac MRI datasets (ACDC and MSCMRseg) across four scribble-supervised algorithms show consistent improvements in segmentation accuracy. Code will be made available on GitHub upon acceptance.

