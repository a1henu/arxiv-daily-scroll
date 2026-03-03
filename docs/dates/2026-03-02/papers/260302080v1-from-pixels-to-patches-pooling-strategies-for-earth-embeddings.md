---
layout: default
title: From Pixels to Patches: Pooling Strategies for Earth Embeddings
---

# From Pixels to Patches: Pooling Strategies for Earth Embeddings
**arXiv**：[2603.02080v1](https://arxiv.org/abs/2603.02080) · [PDF](https://arxiv.org/pdf/2603.02080.pdf)  
**作者**：Isaac Corley, Caleb Robinson, Inbal Becker-Reshef, Juan M. Lavista Ferres  

**一句话要点**：提出多种池化策略以提升地理空间基础模型从像素到补丁嵌入的泛化能力

**关键词**：地理空间基础模型, 像素嵌入聚合, 池化策略, 地理泛化, EuroSAT-Embed数据集, 统计池化

## 3 点简述
- 核心问题：像素级嵌入聚合为补丁表示时，默认均值池化丢弃变异性，导致空间偏移下精度下降超10%。
- 方法要点：评估11种无训练和2种参数化池化方法，推荐广义均值池化作为直接替代，统计池化在嵌入尺寸增加下表现最佳。
- 实验或效果：在EuroSAT-Embed数据集上，丰富池化方案将地理泛化差距相对减少达40%，空间分割精度提升达5%。

## 摘要（原文）

> As geospatial foundation models shift from patch-level to pixel-level embeddings, practitioners must aggregate thousands of pixel vectors into patch representations that preserve class-discriminative signal while matching downstream label resolution. The default choice, mean pooling, discards within-patch variability and can drop accuracy by more than 10% under spatial shift. To evaluate this effect, we introduce EuroSAT-Embed: 81,000 embedding GeoTIFFs derived from three foundation models: AlphaEarth, OlmoEarth, and Tessera. We benchmark 11 training-free and 2 parametric pooling methods under both random and geographically disjoint test splits. Our results show that richer pooling schemes reduce the geographic generalization gap by up to 40% relative to mean pooling and increases accuracy by up to 5% on spatial splits. We recommend Generalized Mean Pooling (GeM) as a drop-in replacement for mean pooling: it improves accuracy without increasing embedding dimensionality. For maximum accuracy, Stats pooling (concatenation of min/max/mean/std pooling) performs best at 4x the embedding size. We further find that pooling effectiveness varies across embedding sources and that higher-dimensional embeddings benefit most from distributional statistics.

