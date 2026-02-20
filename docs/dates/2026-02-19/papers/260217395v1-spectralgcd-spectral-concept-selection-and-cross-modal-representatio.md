---
layout: default
title: SpectralGCD: Spectral Concept Selection and Cross-modal Representation Learning for Generalized Category Discovery
---

# SpectralGCD: Spectral Concept Selection and Cross-modal Representation Learning for Generalized Category Discovery
**arXiv**：[2602.17395v1](https://arxiv.org/abs/2602.17395) · [PDF](https://arxiv.org/pdf/2602.17395.pdf)  
**作者**：Lorenzo Caselli, Marco Mistretta, Simone Magistri, Andrew D. Bagdanov  

**一句话要点**：提出SpectralGCD，通过谱概念选择和跨模态表示学习解决广义类别发现中的过拟合与计算成本问题。

**关键词**：广义类别发现, 跨模态表示学习, 谱概念选择, 知识蒸馏, 计算效率优化

## 3 点简述
- 核心问题：广义类别发现中仅依赖图像特征易过拟合旧类，现有多模态方法独立处理模态且计算成本高。
- 方法要点：使用CLIP跨模态相似度作为统一表示，通过谱过滤自动选择相关概念，结合前向和反向知识蒸馏保持语义质量。
- 实验或效果：在六个基准测试中达到或超越最先进方法精度，计算成本显著降低。

## 摘要（原文）

> Generalized Category Discovery (GCD) aims to identify novel categories in unlabeled data while leveraging a small labeled subset of known classes. Training a parametric classifier solely on image features often leads to overfitting to old classes, and recent multimodal approaches improve performance by incorporating textual information. However, they treat modalities independently and incur high computational cost. We propose SpectralGCD, an efficient and effective multimodal approach to GCD that uses CLIP cross-modal image-concept similarities as a unified cross-modal representation. Each image is expressed as a mixture over semantic concepts from a large task-agnostic dictionary, which anchors learning to explicit semantics and reduces reliance on spurious visual cues. To maintain the semantic quality of representations learned by an efficient student, we introduce Spectral Filtering which exploits a cross-modal covariance matrix over the softmaxed similarities measured by a strong teacher model to automatically retain only relevant concepts from the dictionary. Forward and reverse knowledge distillation from the same teacher ensures that the cross-modal representations of the student remain both semantically sufficient and well-aligned. Across six benchmarks, SpectralGCD delivers accuracy comparable to or significantly superior to state-of-the-art methods at a fraction of the computational cost. The code is publicly available at: https://github.com/miccunifi/SpectralGCD.

