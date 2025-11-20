---
layout: default
title: Complex-Valued 2D Gaussian Representation for Computer-Generated Holography
---

# Complex-Valued 2D Gaussian Representation for Computer-Generated Holography
**arXiv**：[2511.15022v1](https://arxiv.org/abs/2511.15022) · [PDF](https://arxiv.org/pdf/2511.15022.pdf)  
**作者**：Yicheng Zhan, Xiangjun Gao, Long Quan, Kaan Akşit  

**一句话要点**：提出基于复值2D高斯基元的全息图表示法，以降低参数空间和内存使用。

**关键词**：计算机生成全息术, 复值高斯表示, 可微渲染, 参数优化, 内存效率

## 3 点简述
- 核心问题：传统全息图存储像素信息导致高参数空间和内存开销。
- 方法要点：使用结构化复值2D高斯基元替换像素存储，并开发可微光栅器。
- 实验效果：降低VRAM使用达2.5倍，优化速度提升50%，重建质量更高。

## 摘要（原文）

> We propose a new hologram representation based on structured complex-valued 2D Gaussian primitives, which replaces per-pixel information storage and reduces the parameter search space by up to 10:1. To enable end-to-end training, we develop a differentiable rasterizer for our representation, integrated with a GPU-optimized light propagation kernel in free space. Our extensive experiments show that our method achieves up to 2.5x lower VRAM usage and 50% faster optimization while producing higher-fidelity reconstructions than existing methods. We further introduce a conversion procedure that adapts our representation to practical hologram formats, including smooth and random phase-only holograms. Our experiments show that this procedure can effectively suppress noise artifacts observed in previous methods. By reducing the hologram parameter search space, our representation enables a more scalable hologram estimation in the next-generation computer-generated holography systems.

