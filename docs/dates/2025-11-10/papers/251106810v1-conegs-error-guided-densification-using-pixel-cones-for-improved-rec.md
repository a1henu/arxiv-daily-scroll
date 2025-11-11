---
layout: default
title: ConeGS: Error-Guided Densification Using Pixel Cones for Improved Reconstruction with Fewer Primitives
---

# ConeGS: Error-Guided Densification Using Pixel Cones for Improved Reconstruction with Fewer Primitives
**arXiv**：[2511.06810v1](https://arxiv.org/abs/2511.06810) · [PDF](https://arxiv.org/pdf/2511.06810.pdf)  
**作者**：Bartłomiej Baranowski, Stefano Esposito, Patricia Gschoßmann, Anpei Chen, Andreas Geiger  

**一句话要点**：提出ConeGS以改进3D高斯溅射重建，使用像素锥引导致密化减少基元数量

**关键词**：3D高斯溅射, 致密化方法, 图像空间引导, 基元优化, 新视角合成

## 3 点简述
- 核心问题：3D高斯溅射基元分布不佳，依赖克隆致密化导致基元过多且覆盖不足
- 方法要点：基于图像空间误差引导，沿像素锥插入新高斯，结合不透明度惩罚和预算控制
- 实验或效果：在严格基元约束下显著提升重建质量和渲染性能，实验验证一致改进

## 摘要（原文）

> 3D Gaussian Splatting (3DGS) achieves state-of-the-art image quality and
> real-time performance in novel view synthesis but often suffers from a
> suboptimal spatial distribution of primitives. This issue stems from
> cloning-based densification, which propagates Gaussians along existing
> geometry, limiting exploration and requiring many primitives to adequately
> cover the scene. We present ConeGS, an image-space-informed densification
> framework that is independent of existing scene geometry state. ConeGS first
> creates a fast Instant Neural Graphics Primitives (iNGP) reconstruction as a
> geometric proxy to estimate per-pixel depth. During the subsequent 3DGS
> optimization, it identifies high-error pixels and inserts new Gaussians along
> the corresponding viewing cones at the predicted depth values, initializing
> their size according to the cone diameter. A pre-activation opacity penalty
> rapidly removes redundant Gaussians, while a primitive budgeting strategy
> controls the total number of primitives, either by a fixed budget or by
> adapting to scene complexity, ensuring high reconstruction quality. Experiments
> show that ConeGS consistently enhances reconstruction quality and rendering
> performance across Gaussian budgets, with especially strong gains under tight
> primitive constraints where efficient placement is crucial.

