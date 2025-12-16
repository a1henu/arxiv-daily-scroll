---
layout: default
title: Pancakes: Consistent Multi-Protocol Image Segmentation Across Biomedical Domains
---

# Pancakes: Consistent Multi-Protocol Image Segmentation Across Biomedical Domains
**arXiv**：[2512.13534v1](https://arxiv.org/abs/2512.13534) · [PDF](https://arxiv.org/pdf/2512.13534.pdf)  
**作者**：Marianne Rakic, Siyu Gai, Etienne Chollet, John V. Guttag, Adrian V. Dalca  

**一句话要点**：提出Pancakes框架以解决生物医学图像多协议分割的一致性问题

**关键词**：生物医学图像分割, 多协议分割, 语义一致性, 基础模型, 自动分割

## 3 点简述
- 核心问题：现有模型通常仅支持单一分割协议或需手动指定，缺乏自动多协议分割能力
- 方法要点：引入新问题表述，自动生成多标签分割图，确保跨图像语义一致性
- 实验或效果：在七个未见数据集上显著优于现有基础模型，产生语义连贯的分割结果

## 摘要（原文）

> A single biomedical image can be meaningfully segmented in multiple ways, depending on the desired application. For instance, a brain MRI can be segmented according to tissue types, vascular territories, broad anatomical regions, fine-grained anatomy, or pathology, etc. Existing automatic segmentation models typically either (1) support only a single protocol, the one they were trained on, or (2) require labor-intensive manual prompting to specify the desired segmentation. We introduce Pancakes, a framework that, given a new image from a previously unseen domain, automatically generates multi-label segmentation maps for multiple plausible protocols, while maintaining semantic consistency across related images. Pancakes introduces a new problem formulation that is not currently attainable by existing foundation models. In a series of experiments on seven held-out datasets, we demonstrate that our model can significantly outperform existing foundation models in producing several plausible whole-image segmentations, that are semantically coherent across images.

