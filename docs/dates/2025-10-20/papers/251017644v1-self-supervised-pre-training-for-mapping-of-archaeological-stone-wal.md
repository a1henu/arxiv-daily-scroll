---
layout: default
title: Self-supervised Pre-training for Mapping of Archaeological Stone Wall in Historic Landscapes Using High-Resolution DEM Derivatives
---

# Self-supervised Pre-training for Mapping of Archaeological Stone Wall in Historic Landscapes Using High-Resolution DEM Derivatives
**arXiv**：[2510.17644v1](https://arxiv.org/abs/2510.17644) · [PDF](https://arxiv.org/pdf/2510.17644.pdf)  
**作者**：Zexian Huang, Mashnoon Islam, Brian Armstrong, Kourosh Khoshelham, Martin Tomko  

**一句话要点**：提出DINO-CV自监督预训练框架，用于高分辨率DEM衍生物中考古石墙的自动映射。

**关键词**：自监督学习, DEM衍生物分割, 知识蒸馏, 考古石墙映射, 高分辨率LiDAR

## 3 点简述
- 核心问题：植被遮挡和标注数据稀缺阻碍干石墙的自动映射。
- 方法要点：基于知识蒸馏的自监督跨视图预训练，学习DEM衍生物的视觉和几何不变表示。
- 实验或效果：在Budj Bim测试中，mIoU达68.6%，仅用10%标注数据时保持63.8%。

## 摘要（原文）

> Dry-stone walls hold significant heritage and environmental value. Mapping
> these structures is essential for ecosystem preservation and wildfire
> management in Australia. Yet, many walls remain unidentified due to their
> inaccessibility and the high cost of manual mapping. Deep learning-based
> segmentation offers a scalable solution, but two major challenges persist: (1)
> visual occlusion of low-lying walls by dense vegetation, and (2) limited
> labeled data for supervised training. We propose DINO-CV, a segmentation
> framework for automatic mapping of low-lying dry-stone walls using
> high-resolution Airborne LiDAR-derived digital elevation models (DEMs). DEMs
> overcome visual occlusion by capturing terrain structures hidden beneath
> vegetation, enabling analysis of structural rather than spectral cues. DINO-CV
> introduces a self-supervised cross-view pre-training strategy based on
> knowledge distillation to mitigate data scarcity. It learns invariant visual
> and geometric representations across multiple DEM derivatives, supporting
> various vision backbones including ResNet, Wide ResNet, and Vision
> Transformers. Applied to the UNESCO World Heritage cultural landscape of Budj
> Bim, Victoria, the method identifies one of Australia's densest collections of
> colonial dry-stone walls beyond Indigenous heritage contexts. DINO-CV achieves
> a mean Intersection over Union (mIoU) of 68.6% on test areas and maintains
> 63.8% mIoU when fine-tuned with only 10% labeled data. These results
> demonstrate the potential of self-supervised learning on high-resolution DEM
> derivatives for automated dry-stone wall mapping in vegetated and heritage-rich
> environments with scarce annotations.

