---
layout: default
title: Prototype-Driven Adaptation for Few-Shot Object Detection
---

# Prototype-Driven Adaptation for Few-Shot Object Detection
**arXiv**：[2510.25318v1](https://arxiv.org/abs/2510.25318) · [PDF](https://arxiv.org/pdf/2510.25318.pdf)  
**作者**：Yushen Huang, Zhiming Wang  

**一句话要点**：提出原型驱动对齐方法以解决少样本目标检测中的基类偏差和校准不稳定问题

**关键词**：少样本目标检测, 原型学习, 度量学习, 类别适应, 目标检测基准

## 3 点简述
- 核心问题：少样本目标检测存在基类偏差和校准不稳定，仅少量新类样本可用
- 方法要点：引入轻量级原型驱动对齐头，提供原型匹配作为线性分类器的补充
- 实验或效果：在VOC和GFSOD基准上，新类性能提升，基类影响小，计算开销可忽略

## 摘要（原文）

> Few-shot object detection (FSOD) often suffers from base-class bias and
> unstable calibration when only a few novel samples are available. We propose
> Prototype-Driven Alignment (PDA), a lightweight, plug-in metric head for DeFRCN
> that provides a prototype-based "second opinion" complementary to the linear
> classifier. PDA maintains support-only prototypes in a learnable
> identity-initialized projection space and optionally applies
> prototype-conditioned RoI alignment to reduce geometric mismatch. During
> fine-tuning, prototypes can be adapted via exponential moving average(EMA)
> updates on labeled foreground RoIs-without introducing class-specific
> parameters-and are frozen at inference to ensure strict protocol compliance.
> PDA employs a best-of-K matching scheme to capture intra-class multi-modality
> and temperature-scaled fusion to combine metric similarities with detector
> logits. Experiments on VOC FSOD and GFSOD benchmarks show that PDA consistently
> improves novel-class performance with minimal impact on base classes and
> negligible computational overhead.

