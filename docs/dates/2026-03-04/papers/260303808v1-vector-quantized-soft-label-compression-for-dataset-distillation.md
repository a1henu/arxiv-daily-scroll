---
layout: default
title: Vector-Quantized Soft Label Compression for Dataset Distillation
---

# Vector-Quantized Soft Label Compression for Dataset Distillation
**arXiv**：[2603.03808v1](https://arxiv.org/abs/2603.03808) · [PDF](https://arxiv.org/pdf/2603.03808.pdf)  
**作者**：Ali Abbasi, Ashkan Shahbazi, Hamed Pirsiavash, Soheil Kolouri  

**一句话要点**：提出向量量化软标签压缩方法以解决数据集蒸馏中软标签存储开销大的问题。

**关键词**：数据集蒸馏, 软标签压缩, 向量量化, 存储优化, 图像分类, 语言模型蒸馏

## 3 点简述
- 核心问题：数据集蒸馏中软标签存储成本高，尤其在多类场景如ImageNet-1K。
- 方法要点：使用向量量化自编码器压缩软标签，实现高压缩比。
- 实验或效果：在ImageNet-1K上达到30-40倍额外压缩，性能保留超90%。

## 摘要（原文）

> Dataset distillation is an emerging technique for reducing the computational and storage costs of training machine learning models by synthesizing a small, informative subset of data that captures the essential characteristics of a much larger dataset. Recent methods pair synthetic samples and their augmentations with soft labels from a teacher model, enabling student models to generalize effectively despite the small size of the distilled dataset. While soft labels are critical for effective distillation, the storage and communication overhead they incur, especially when accounting for augmentations, is often overlooked. In practice, each distilled sample is associated with multiple soft labels, making them the dominant contributor to storage costs, particularly in large-class settings such as ImageNet-1K. In this paper, we present a rigorous analysis of bit requirements across dataset distillation frameworks, quantifying the storage demands of both distilled samples and their soft labels. To address the overhead, we introduce a vector-quantized autoencoder (VQAE) for compressing soft labels, achieving substantial compression while preserving the effectiveness of the distilled data. We validate our method on both vision and language distillation benchmarks. On ImageNet-1K, our proposed VQAE achieves 30--40x additional compression over RDED, LPLD, SRE2L, and CDA baselines while retaining over $90\%$ of their original performance.

