---
layout: default
title: DiffBMP: Differentiable Rendering with Bitmap Primitives
---

# DiffBMP: Differentiable Rendering with Bitmap Primitives
**arXiv**：[2602.22625v1](https://arxiv.org/abs/2602.22625) · [PDF](https://arxiv.org/pdf/2602.22625.pdf)  
**作者**：Seongmin Hong, Junghun James Kim, Daehyeop Kim, Insoo Chung, Se Young Chun  

**一句话要点**：提出DiffBMP以解决传统可微渲染器局限于矢量图形的问题，支持位图图像的高效优化。

**关键词**：可微渲染, 位图图像, 并行计算, CUDA实现, 优化技术, 创意工作流

## 3 点简述
- 核心问题：传统可微渲染器主要处理矢量图形，但现实世界图像多为位图，缺乏高效可微渲染方案。
- 方法要点：采用高度并行化渲染管线，包括自定义CUDA实现计算梯度，支持高斯模糊软光栅化等技术。
- 实验或效果：在消费级GPU上，可在1分钟内优化数千位图基元的位置、旋转、缩放、颜色和透明度。

## 摘要（原文）

> We introduce DiffBMP, a scalable and efficient differentiable rendering engine for a collection of bitmap images. Our work addresses a limitation that traditional differentiable renderers are constrained to vector graphics, given that most images in the world are bitmaps. Our core contribution is a highly parallelized rendering pipeline, featuring a custom CUDA implementation for calculating gradients. This system can, for example, optimize the position, rotation, scale, color, and opacity of thousands of bitmap primitives all in under 1 min using a consumer GPU. We employ and validate several techniques to facilitate the optimization: soft rasterization via Gaussian blur, structure-aware initialization, noisy canvas, and specialized losses/heuristics for videos or spatially constrained images. We demonstrate DiffBMP is not just an isolated tool, but a practical one designed to integrate into creative workflows. It supports exporting compositions to a native, layered file format, and the entire framework is publicly accessible via an easy-to-hack Python package.

