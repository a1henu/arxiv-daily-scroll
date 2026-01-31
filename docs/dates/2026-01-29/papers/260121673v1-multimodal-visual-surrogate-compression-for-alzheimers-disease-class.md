---
layout: default
title: Multimodal Visual Surrogate Compression for Alzheimer's Disease Classification
---

# Multimodal Visual Surrogate Compression for Alzheimer's Disease Classification
**arXiv**：[2601.21673v1](https://arxiv.org/abs/2601.21673) · [PDF](https://arxiv.org/pdf/2601.21673.pdf)  
**作者**：Dexuan Ding, Ciyuan Peng, Endrowednes Kuantama, Jingcai Guo, Jia Wu, Jian Yang, Amin Beheshti, Ming-Hsuan Yang, Yuankai Qi  

**一句话要点**：提出多模态视觉代理压缩方法，用于阿尔茨海默病分类，以解决高维sMRI图像处理中的计算成本、跨切片关系丢失和特征提取能力有限问题。

**关键词**：阿尔茨海默病分类, 多模态视觉代理压缩, 结构MRI处理, 2D基础模型对齐, 跨切片上下文捕获

## 3 点简述
- 核心问题：现有sMRI表示学习方法存在高计算成本、跨切片关系丢失和特征提取能力有限的问题。
- 方法要点：通过体积上下文编码器和自适应切片融合模块，将3D sMRI压缩为2D视觉代理，与冻结的2D基础模型对齐以提取强大表示。
- 实验或效果：在三个大规模阿尔茨海默病基准测试中，MVSC在二元和多类分类任务上表现优于最先进方法。

## 摘要（原文）

> High-dimensional structural MRI (sMRI) images are widely used for Alzheimer's Disease (AD) diagnosis. Most existing methods for sMRI representation learning rely on 3D architectures (e.g., 3D CNNs), slice-wise feature extraction with late aggregation, or apply training-free feature extractions using 2D foundation models (e.g., DINO). However, these three paradigms suffer from high computational cost, loss of cross-slice relations, and limited ability to extract discriminative features, respectively. To address these challenges, we propose Multimodal Visual Surrogate Compression (MVSC). It learns to compress and adapt large 3D sMRI volumes into compact 2D features, termed as visual surrogates, which are better aligned with frozen 2D foundation models to extract powerful representations for final AD classification. MVSC has two key components: a Volume Context Encoder that captures global cross-slice context under textual guidance, and an Adaptive Slice Fusion module that aggregates slice-level information in a text-enhanced, patch-wise manner. Extensive experiments on three large-scale Alzheimer's disease benchmarks demonstrate our MVSC performs favourably on both binary and multi-class classification tasks compared against state-of-the-art methods.

