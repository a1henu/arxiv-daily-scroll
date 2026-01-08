---
layout: default
title: Unsupervised Modular Adaptive Region Growing and RegionMix Classification for Wind Turbine Segmentation
---

# Unsupervised Modular Adaptive Region Growing and RegionMix Classification for Wind Turbine Segmentation
**arXiv**：[2601.04065v1](https://arxiv.org/abs/2601.04065) · [PDF](https://arxiv.org/pdf/2601.04065.pdf)  
**作者**：Raül Pérez-Gonzalo, Riccardo Magro, Andreas Espersen, Antonio Agudo  

**一句话要点**：提出无监督模块化自适应区域生长与RegionMix分类方法，以解决风力涡轮机叶片分割中的标注效率问题。

**关键词**：风力涡轮机分割, 无监督区域生长, 区域分类, 数据增强, 跨站点泛化

## 3 点简述
- 核心问题：风力涡轮机叶片分割依赖密集标注，标注成本高，可扩展性差。
- 方法要点：采用无监督模块化自适应区域生长生成图像区域，结合RegionMix增强策略提升分类鲁棒性。
- 实验或效果：在分割准确性和跨站点泛化方面达到先进水平，有效减少标注需求。

## 摘要（原文）

> Reliable operation of wind turbines requires frequent inspections, as even minor surface damages can degrade aerodynamic performance, reduce energy output, and accelerate blade wear. Central to automating these inspections is the accurate segmentation of turbine blades from visual data. This task is traditionally addressed through dense, pixel-wise deep learning models. However, such methods demand extensive annotated datasets, posing scalability challenges. In this work, we introduce an annotation-efficient segmentation approach that reframes the pixel-level task into a binary region classification problem. Image regions are generated using a fully unsupervised, interpretable Modular Adaptive Region Growing technique, guided by image-specific Adaptive Thresholding and enhanced by a Region Merging process that consolidates fragmented areas into coherent segments. To improve generalization and classification robustness, we introduce RegionMix, an augmentation strategy that synthesizes new training samples by combining distinct regions. Our framework demonstrates state-of-the-art segmentation accuracy and strong cross-site generalization by consistently segmenting turbine blades across distinct windfarms.

