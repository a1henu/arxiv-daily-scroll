---
layout: default
title: AtlasMorph: Learning conditional deformable templates for brain MRI
---

# AtlasMorph: Learning conditional deformable templates for brain MRI
**arXiv**：[2511.13609v1](https://arxiv.org/abs/2511.13609) · [PDF](https://arxiv.org/pdf/2511.13609.pdf)  
**作者**：Marianne Rakic, Andrew Hoopes, S. Mazdak Abulnaga, Mert R. Sabuncu, John V. Guttag, Adrian V. Dalca  

**一句话要点**：提出AtlasMorph框架，学习条件可变形模板以优化脑MRI分析

**关键词**：可变形模板, 脑MRI分析, 条件学习, 卷积配准网络, 图像配准

## 3 点简述
- 核心问题：脑MRI分析中模板构建昂贵，现有模板难以代表大变异人群。
- 方法要点：使用卷积配准网络学习基于年龄、性别等属性的条件模板。
- 实验或效果：在3D脑MRI数据集上验证，条件模板提升配准性能。

## 摘要（原文）

> Deformable templates, or atlases, are images that represent a prototypical anatomy for a population, and are often enhanced with probabilistic anatomical label maps. They are commonly used in medical image analysis for population studies and computational anatomy tasks such as registration and segmentation. Because developing a template is a computationally expensive process, relatively few templates are available. As a result, analysis is often conducted with sub-optimal templates that are not truly representative of the study population, especially when there are large variations within this population. We propose a machine learning framework that uses convolutional registration neural networks to efficiently learn a function that outputs templates conditioned on subject-specific attributes, such as age and sex. We also leverage segmentations, when available, to produce anatomical segmentation maps for the resulting templates. The learned network can also be used to register subject images to the templates. We demonstrate our method on a compilation of 3D brain MRI datasets, and show that it can learn high-quality templates that are representative of populations. We find that annotated conditional templates enable better registration than their unlabeled unconditional counterparts, and outperform other templates construction methods.

