---
layout: default
title: ZACH-ViT: A Zero-Token Vision Transformer with ShuffleStrides Data Augmentation for Robust Lung Ultrasound Classification
---

# ZACH-ViT: A Zero-Token Vision Transformer with ShuffleStrides Data Augmentation for Robust Lung Ultrasound Classification
**arXiv**：[2510.17650v1](https://arxiv.org/abs/2510.17650) · [PDF](https://arxiv.org/pdf/2510.17650.pdf)  
**作者**：Athanasios Angelakis, Amne Mousa, Micah L. A. Heldeweg, Laurens A. Biesheuvel, Mark A. Haaksma, Jasper M. Smit, Pieter R. Tuinman, Paul W. G. Elbers  

**一句话要点**：提出ZACH-ViT与ShuffleStrides数据增强，用于鲁棒的肺部超声分类。

**关键词**：零标记视觉Transformer, 数据增强, 肺部超声分类, 排列不变性, 小数据医学成像

## 3 点简述
- 核心问题：肺部超声视频中区分心源性肺水肿与非心源性/正常肺的视觉变异性高，导致分类困难。
- 方法要点：ZACH-ViT移除位置嵌入和[CLS]标记，实现全排列不变性；SSDA增强泛化能力。
- 实验或效果：在380个视频上验证，ZACH-ViT取得最高ROC-AUC，训练更快，参数更少。

## 摘要（原文）

> Differentiating cardiogenic pulmonary oedema (CPE) from non-cardiogenic and
> structurally normal lungs in lung ultrasound (LUS) videos remains challenging
> due to the high visual variability of non-cardiogenic inflammatory patterns
> (NCIP/ARDS-like), interstitial lung disease, and healthy lungs. This
> heterogeneity complicates automated classification as overlapping B-lines and
> pleural artefacts are common. We introduce ZACH-ViT (Zero-token Adaptive
> Compact Hierarchical Vision Transformer), a 0.25 M-parameter Vision Transformer
> variant that removes both positional embeddings and the [CLS] token, making it
> fully permutation-invariant and suitable for unordered medical image data. To
> enhance generalization, we propose ShuffleStrides Data Augmentation (SSDA),
> which permutes probe-view sequences and frame orders while preserving
> anatomical validity. ZACH-ViT was evaluated on 380 LUS videos from 95
> critically ill patients against nine state-of-the-art baselines. Despite the
> heterogeneity of the non-cardiogenic group, ZACH-ViT achieved the highest
> validation and test ROC-AUC (0.80 and 0.79) with balanced sensitivity (0.60)
> and specificity (0.91), while all competing models collapsed to trivial
> classification. It trains 1.35x faster than Minimal ViT (0.62M parameters) with
> 2.5x fewer parameters, supporting real-time clinical deployment. These results
> show that aligning architectural design with data structure can outperform
> scale in small-data medical imaging.

