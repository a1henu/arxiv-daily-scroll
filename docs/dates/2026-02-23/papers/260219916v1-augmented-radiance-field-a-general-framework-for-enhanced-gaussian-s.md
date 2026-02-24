---
layout: default
title: Augmented Radiance Field: A General Framework for Enhanced Gaussian Splatting
---

# Augmented Radiance Field: A General Framework for Enhanced Gaussian Splatting
**arXiv**：[2602.19916v1](https://arxiv.org/abs/2602.19916) · [PDF](https://arxiv.org/pdf/2602.19916.pdf)  
**作者**：Yixin Yang, Bojian Wu, Yang Zhou, Hui Huang  

**一句话要点**：提出增强高斯核以解决3D高斯泼溅中漫反射与镜面反射分离的挑战

**关键词**：3D高斯泼溅, 辐射场重建, 镜面反射建模, 实时渲染, 误差驱动补偿, 参数效率

## 3 点简述
- 核心问题：3D高斯泼溅依赖球谐函数编码颜色，难以准确分离漫反射和镜面反射，影响复杂反射的表示。
- 方法要点：引入增强高斯核，通过视点依赖的不透明度显式建模镜面效果，并采用误差驱动补偿策略提升渲染质量。
- 实验或效果：在渲染性能上超越先进NeRF方法，同时实现更高的参数效率，适用于现有3D高斯泼溅场景的增强。

## 摘要（原文）

> Due to the real-time rendering performance, 3D Gaussian Splatting (3DGS) has emerged as the leading method for radiance field reconstruction. However, its reliance on spherical harmonics for color encoding inherently limits its ability to separate diffuse and specular components, making it challenging to accurately represent complex reflections. To address this, we propose a novel enhanced Gaussian kernel that explicitly models specular effects through view-dependent opacity. Meanwhile, we introduce an error-driven compensation strategy to improve rendering quality in existing 3DGS scenes. Our method begins with 2D Gaussian initialization and then adaptively inserts and optimizes enhanced Gaussian kernels, ultimately producing an augmented radiance field. Experiments demonstrate that our method not only surpasses state-of-the-art NeRF methods in rendering performance but also achieves greater parameter efficiency. Project page at: https://xiaoxinyyx.github.io/augs.

