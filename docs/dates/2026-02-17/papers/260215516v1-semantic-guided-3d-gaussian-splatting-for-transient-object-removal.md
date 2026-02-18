---
layout: default
title: Semantic-Guided 3D Gaussian Splatting for Transient Object Removal
---

# Semantic-Guided 3D Gaussian Splatting for Transient Object Removal
**arXiv**：[2602.15516v1](https://arxiv.org/abs/2602.15516) · [PDF](https://arxiv.org/pdf/2602.15516.pdf)  
**作者**：Aditi Prabakaran, Priyesh Shukla  

**一句话要点**：提出语义引导的3D高斯泼溅方法，以解决多视角捕获中瞬态物体导致的鬼影问题。

**关键词**：3D高斯泼溅, 瞬态物体移除, 语义引导, 视觉语言模型, 实时渲染, 重建质量

## 3 点简述
- 核心问题：多视角捕获中的瞬态物体在3D高斯泼溅重建中引起鬼影伪影，现有方法内存成本高或易受视差模糊影响。
- 方法要点：利用视觉语言模型进行语义过滤，通过CLIP相似度分数对高斯泼溅进行类别感知的瞬态物体移除，包括不透明度正则化和定期剪枝。
- 实验或效果：在RobustNeRF基准测试中，相比原始3D高斯泼溅，在四个序列上重建质量一致提升，同时保持低内存开销和实时渲染性能。

## 摘要（原文）

> Transient objects in casual multi-view captures cause ghosting artifacts in 3D Gaussian Splatting (3DGS) reconstruction. Existing solutions relied on scene decomposition at significant memory cost or on motion-based heuristics that were vulnerable to parallax ambiguity. A semantic filtering framework was proposed for category-aware transient removal using vision-language models. CLIP similarity scores between rendered views and distractor text prompts were accumulated per-Gaussian across training iterations. Gaussians exceeding a calibrated threshold underwent opacity regularization and periodic pruning. Unlike motion-based approaches, semantic classification resolved parallax ambiguity by identifying object categories independently of motion patterns. Experiments on the RobustNeRF benchmark demonstrated consistent improvement in reconstruction quality over vanilla 3DGS across four sequences, while maintaining minimal memory overhead and real-time rendering performance. Threshold calibration and comparisons with baselines validated semantic guidance as a practical strategy for transient removal in scenarios with predictable distractor categories.

