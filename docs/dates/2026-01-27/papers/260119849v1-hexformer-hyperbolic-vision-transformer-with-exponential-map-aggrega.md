---
layout: default
title: HexFormer: Hyperbolic Vision Transformer with Exponential Map Aggregation
---

# HexFormer: Hyperbolic Vision Transformer with Exponential Map Aggregation
**arXiv**：[2601.19849v1](https://arxiv.org/abs/2601.19849) · [PDF](https://arxiv.org/pdf/2601.19849.pdf)  
**作者**：Haya Alyoussef, Ahmad Bdeir, Diego Coello de Portugal Mecke, Tom Hanika, Niels Landwehr, Lars Schmidt-Thieme  

**一句话要点**：提出HexFormer，一种基于指数映射聚合的双曲视觉Transformer，用于图像分类以建模层次结构。

**关键词**：双曲几何, 视觉Transformer, 指数映射聚合, 图像分类, 梯度稳定性, 注意力机制

## 3 点简述
- 核心问题：图像等数据中的层次和关系结构在欧几里得几何中难以建模，双曲几何提供更自然框架。
- 方法要点：引入指数映射聚合的注意力机制，设计双曲ViT和混合变体，提升表示准确性和稳定性。
- 实验或效果：在多个数据集上优于欧几里得基线和先前双曲ViT，混合变体表现最佳，梯度更稳定且训练更鲁棒。

## 摘要（原文）

> Data across modalities such as images, text, and graphs often contains hierarchical and relational structures, which are challenging to model within Euclidean geometry. Hyperbolic geometry provides a natural framework for representing such structures. Building on this property, this work introduces HexFormer, a hyperbolic vision transformer for image classification that incorporates exponential map aggregation within its attention mechanism. Two designs are explored: a hyperbolic ViT (HexFormer) and a hybrid variant (HexFormer-Hybrid) that combines a hyperbolic encoder with an Euclidean linear classification head. HexFormer incorporates a novel attention mechanism based on exponential map aggregation, which yields more accurate and stable aggregated representations than standard centroid based averaging, showing that simpler approaches retain competitive merit. Experiments across multiple datasets demonstrate consistent performance improvements over Euclidean baselines and prior hyperbolic ViTs, with the hybrid variant achieving the strongest overall results. Additionally, this study provides an analysis of gradient stability in hyperbolic transformers. The results reveal that hyperbolic models exhibit more stable gradients and reduced sensitivity to warmup strategies compared to Euclidean architectures, highlighting their robustness and efficiency in training. Overall, these findings indicate that hyperbolic geometry can enhance vision transformer architectures by improving gradient stability and accuracy. In addition, relatively simple mechanisms such as exponential map aggregation can provide strong practical benefits.

