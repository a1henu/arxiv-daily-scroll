---
layout: default
title: Gaussian Mesh Renderer for Lightweight Differentiable Rendering
---

# Gaussian Mesh Renderer for Lightweight Differentiable Rendering
**arXiv**：[2602.14493v1](https://arxiv.org/abs/2602.14493) · [PDF](https://arxiv.org/pdf/2602.14493.pdf)  
**作者**：Xinpeng Liu, Fumio Okura  

**一句话要点**：提出高斯网格渲染器以解决传统网格可微渲染器优化慢或内存占用大的问题。

**关键词**：可微渲染, 高斯泼溅, 网格优化, 表面重建, 梯度平滑

## 3 点简述
- 核心问题：传统基于网格的可微渲染器优化速度慢或内存占用大，影响表面重建效率。
- 方法要点：利用3D高斯泼溅的高效光栅化过程，将高斯基元与网格三角形紧密集成，实现平滑梯度流。
- 实验或效果：相比传统方法，实现更平滑梯度，支持小批量优化，提升内存效率，代码已开源。

## 摘要（原文）

> 3D Gaussian Splatting (3DGS) has enabled high-fidelity virtualization with fast rendering and optimization for novel view synthesis. On the other hand, triangle mesh models still remain a popular choice for surface reconstruction but suffer from slow or heavy optimization in traditional mesh-based differentiable renderers. To address this problem, we propose a new lightweight differentiable mesh renderer leveraging the efficient rasterization process of 3DGS, named Gaussian Mesh Renderer (GMR), which tightly integrates the Gaussian and mesh representations. Each Gaussian primitive is analytically derived from the corresponding mesh triangle, preserving structural fidelity and enabling the gradient flow. Compared to the traditional mesh renderers, our method achieves smoother gradients, which especially contributes to better optimization using smaller batch sizes with limited memory. Our implementation is available in the public GitHub repository at https://github.com/huntorochi/Gaussian-Mesh-Renderer.

