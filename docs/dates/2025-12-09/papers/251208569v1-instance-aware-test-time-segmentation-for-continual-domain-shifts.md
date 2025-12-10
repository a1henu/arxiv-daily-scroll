---
layout: default
title: Instance-Aware Test-Time Segmentation for Continual Domain Shifts
---

# Instance-Aware Test-Time Segmentation for Continual Domain Shifts
**arXiv**：[2512.08569v1](https://arxiv.org/abs/2512.08569) · [PDF](https://arxiv.org/pdf/2512.08569.pdf)  
**作者**：Seunghwan Lee, Inyoung Jung, Hojoon Lee, Eunil Park, Sungeun Hong  

**一句话要点**：提出实例感知测试时分割方法，以解决持续域偏移下语义分割的伪标签可靠性问题。

**关键词**：持续测试时适应, 语义分割, 域偏移, 伪标签调整, 实例感知学习, 动态平衡

## 3 点简述
- 核心问题：现有持续测试时适应方法依赖固定阈值，无法处理不同类别和实例的难度差异，导致语义分割中错误累积。
- 方法要点：自适应调整伪标签以反映每张图像的置信度分布，并动态平衡受域偏移影响最大的类别的学习。
- 实验或效果：在八个持续测试时适应和测试时适应场景中，包括合成到真实和长期偏移，方法一致优于现有技术。

## 摘要（原文）

> Continual Test-Time Adaptation (CTTA) enables pre-trained models to adapt to continuously evolving domains. Existing methods have improved robustness but typically rely on fixed or batch-level thresholds, which cannot account for varying difficulty across classes and instances. This limitation is especially problematic in semantic segmentation, where each image requires dense, multi-class predictions. We propose an approach that adaptively adjusts pseudo labels to reflect the confidence distribution within each image and dynamically balances learning toward classes most affected by domain shifts. This fine-grained, class- and instance-aware adaptation produces more reliable supervision and mitigates error accumulation throughout continual adaptation. Extensive experiments across eight CTTA and TTA scenarios, including synthetic-to-real and long-term shifts, show that our method consistently outperforms state-of-the-art techniques, setting a new standard for semantic segmentation under evolving conditions.

