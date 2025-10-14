---
layout: default
title: VA-GS: Enhancing the Geometric Representation of Gaussian Splatting via View Alignment
---

# VA-GS: Enhancing the Geometric Representation of Gaussian Splatting via View Alignment
**arXiv**：[2510.11473v1](https://arxiv.org/abs/2510.11473) · [PDF](https://arxiv.org/pdf/2510.11473.pdf)  
**作者**：Qing Li, Huifang Feng, Xun Gong, Yu-Shen Liu  

**一句话要点**：提出VA-GS方法，通过视图对齐增强3D高斯泼溅的几何表示，以改进表面重建和新视角合成。

**关键词**：3D高斯泼溅, 表面重建, 新视角合成, 视图对齐, 几何表示, 多视图一致性

## 3 点简述
- 核心问题：3D高斯泼溅在图像渲染损失下几何不准确且多视图对齐不一致。
- 方法要点：引入边缘感知渲染损失、可见性感知光度对齐损失和法向约束。
- 实验或效果：在标准基准测试中实现表面重建和新视角合成的最先进性能。

## 摘要（原文）

> 3D Gaussian Splatting has recently emerged as an efficient solution for
> high-quality and real-time novel view synthesis. However, its capability for
> accurate surface reconstruction remains underexplored. Due to the discrete and
> unstructured nature of Gaussians, supervision based solely on image rendering
> loss often leads to inaccurate geometry and inconsistent multi-view alignment.
> In this work, we propose a novel method that enhances the geometric
> representation of 3D Gaussians through view alignment (VA). Specifically, we
> incorporate edge-aware image cues into the rendering loss to improve surface
> boundary delineation. To enforce geometric consistency across views, we
> introduce a visibility-aware photometric alignment loss that models occlusions
> and encourages accurate spatial relationships among Gaussians. To further
> mitigate ambiguities caused by lighting variations, we incorporate normal-based
> constraints to refine the spatial orientation of Gaussians and improve local
> surface estimation. Additionally, we leverage deep image feature embeddings to
> enforce cross-view consistency, enhancing the robustness of the learned
> geometry under varying viewpoints and illumination. Extensive experiments on
> standard benchmarks demonstrate that our method achieves state-of-the-art
> performance in both surface reconstruction and novel view synthesis. The source
> code is available at https://github.com/LeoQLi/VA-GS.

