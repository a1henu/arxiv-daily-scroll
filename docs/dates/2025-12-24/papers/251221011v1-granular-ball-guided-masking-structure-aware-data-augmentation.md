---
layout: default
title: Granular-ball Guided Masking: Structure-aware Data Augmentation
---

# Granular-ball Guided Masking: Structure-aware Data Augmentation
**arXiv**：[2512.21011v1](https://arxiv.org/abs/2512.21011) · [PDF](https://arxiv.org/pdf/2512.21011.pdf)  
**作者**：Shuyin Xia, Fan Chen, Dawei Dai, Meng Yang, Junwei Han, Xinbo Gao, Guoyin Wang  

**一句话要点**：提出粒度球引导掩码以增强结构感知的数据增强，提升模型鲁棒性。

**关键词**：数据增强, 结构感知, 粒度球计算, 掩码策略, 计算机视觉, 模型鲁棒性

## 3 点简述
- 核心问题：现有掩码数据增强缺乏结构感知，可能丢弃关键语义信息。
- 方法要点：基于粒度球计算，通过粗到细分层掩码自适应保留语义丰富区域。
- 实验或效果：在多个基准测试中提升分类准确率和掩码图像重建效果。

## 摘要（原文）

> Deep learning models have achieved remarkable success in computer vision, but they still rely heavily on large-scale labeled data and tend to overfit when data are limited or distributions shift. Data augmentation, particularly mask-based information dropping, can enhance robustness by forcing models to explore complementary cues; however, existing approaches often lack structural awareness and may discard essential semantics. We propose Granular-ball Guided Masking (GBGM), a structure-aware augmentation strategy guided by Granular-ball Computing (GBC). GBGM adaptively preserves semantically rich, structurally important regions while suppressing redundant areas through a coarse-to-fine hierarchical masking process, producing augmentations that are both representative and discriminative. Extensive experiments on multiple benchmarks demonstrate consistent improvements in classification accuracy and masked image reconstruction, confirming the effectiveness and broad applicability of the proposed method. Simple and model-agnostic, it integrates seamlessly into CNNs and Vision Transformers and provides a new paradigm for structure-aware data augmentation.

