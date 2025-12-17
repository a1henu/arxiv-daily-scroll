---
layout: default
title: Spherical Voronoi: Directional Appearance as a Differentiable Partition of the Sphere
---

# Spherical Voronoi: Directional Appearance as a Differentiable Partition of the Sphere
**arXiv**：[2512.14180v1](https://arxiv.org/abs/2512.14180) · [PDF](https://arxiv.org/pdf/2512.14180.pdf)  
**作者**：Francesco Di Sario, Daniel Rebain, Dor Verbin, Marco Grangetto, Andrea Tagliasacchi  

**一句话要点**：提出球面Voronoi作为3D高斯泼溅中外观建模的统一框架，以解决球谐函数在捕捉高光和反射方面的局限性。

**关键词**：3D高斯泼溅, 外观建模, 球面Voronoi, 反射探针, 新视角合成, 可微分渲染

## 3 点简述
- 核心问题：球谐函数在3D高斯泼溅中难以处理高频信号和镜面反射，导致渲染不真实。
- 方法要点：使用球面Voronoi将方向域划分为可学习区域，提供平滑边界参数化，简化优化并支持反射探针。
- 实验或效果：在合成和真实数据集上实现先进结果，证明SV在显式3D表示中提供高效通用的外观建模方案。

## 摘要（原文）

> Radiance field methods (e.g. 3D Gaussian Splatting) have emerged as a powerful paradigm for novel view synthesis, yet their appearance modeling often relies on Spherical Harmonics (SH), which impose fundamental limitations. SH struggle with high-frequency signals, exhibit Gibbs ringing artifacts, and fail to capture specular reflections - a key component of realistic rendering. Although alternatives like spherical Gaussians offer improvements, they add significant optimization complexity. We propose Spherical Voronoi (SV) as a unified framework for appearance representation in 3D Gaussian Splatting. SV partitions the directional domain into learnable regions with smooth boundaries, providing an intuitive and stable parameterization for view-dependent effects. For diffuse appearance, SV achieves competitive results while keeping optimization simpler than existing alternatives. For reflections - where SH fail - we leverage SV as learnable reflection probes, taking reflected directions as input following principles from classical graphics. This formulation attains state-of-the-art results on synthetic and real-world datasets, demonstrating that SV offers a principled, efficient, and general solution for appearance modeling in explicit 3D representations.

