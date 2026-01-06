---
layout: default
title: Mind the Gap: Continuous Magnification Sampling for Pathology Foundation Models
---

# Mind the Gap: Continuous Magnification Sampling for Pathology Foundation Models
**arXiv**：[2601.02198v1](https://arxiv.org/abs/2601.02198) · [PDF](https://arxiv.org/pdf/2601.02198.pdf)  
**作者**：Alexander Möllers, Julius Hense, Florian Schulz, Timo Milbich, Maximilian Alber, Lukas Ruff  

**一句话要点**：提出连续放大倍数采样方法以优化病理学基础模型在跨放大倍数下的性能

**关键词**：病理学基础模型, 放大倍数采样, 多源域适应, 连续采样, 性能优化, 组织病理学

## 3 点简述
- 核心问题：病理学基础模型在跨放大倍数下的性能差异及训练中放大倍数采样的影响未知
- 方法要点：建模放大倍数采样为多源域适应问题，引入连续采样消除覆盖间隙，推导优化采样分布
- 实验或效果：连续采样在中间放大倍数上提升达4个百分点，优化分布可进一步提高性能

## 摘要（原文）

> In histopathology, pathologists examine both tissue architecture at low magnification and fine-grained morphology at high magnification. Yet, the performance of pathology foundation models across magnifications and the effect of magnification sampling during training remain poorly understood. We model magnification sampling as a multi-source domain adaptation problem and develop a simple theoretical framework that reveals systematic trade-offs between sampling strategies. We show that the widely used discrete uniform sampling of magnifications (0.25, 0.5, 1.0, 2.0 mpp) leads to degradation at intermediate magnifications. We introduce continuous magnification sampling, which removes gaps in magnification coverage while preserving performance at standard scales. Further, we derive sampling distributions that optimize representation quality across magnification scales. To evaluate these strategies, we introduce two new benchmarks (TCGA-MS, BRACS-MS) with appropriate metrics. Our experiments show that continuous sampling substantially improves over discrete sampling at intermediate magnifications, with gains of up to 4 percentage points in balanced classification accuracy, and that optimized distributions can further improve performance. Finally, we evaluate current histopathology foundation models, finding that magnification is a primary driver of performance variation across models. Our work paves the way towards future pathology foundation models that perform reliably across magnifications.

