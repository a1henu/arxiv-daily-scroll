---
layout: default
title: FACT-GS: Frequency-Aligned Complexity-Aware Texture Reparameterization for 2D Gaussian Splatting
---

# FACT-GS: Frequency-Aligned Complexity-Aware Texture Reparameterization for 2D Gaussian Splatting
**arXiv**：[2511.23292v1](https://arxiv.org/abs/2511.23292) · [PDF](https://arxiv.org/pdf/2511.23292.pdf)  
**作者**：Tianhao Xie, Linlian Jiang, Xinxin Zuo, Yang Wang, Tiberiu Popa  

**一句话要点**：提出FACT-GS框架，通过频率对齐的纹理重参数化解决高斯溅射中纹理采样效率低的问题。

**关键词**：高斯溅射, 纹理重参数化, 自适应采样, 实时渲染, 频率对齐

## 3 点简述
- 核心问题：传统高斯溅射使用均匀纹理采样，导致高频区域欠采样和平滑区域浪费容量，影响细节表现。
- 方法要点：基于自适应采样理论，引入可学习的频率感知分配策略，通过变形场的雅可比矩阵调制局部采样密度。
- 实验或效果：在相同参数预算下，恢复更锐利的高频细节，同时保持实时渲染性能。

## 摘要（原文）

> Realistic scene appearance modeling has advanced rapidly with Gaussian Splatting, which enables real-time, high-quality rendering. Recent advances introduced per-primitive textures that incorporate spatial color variations within each Gaussian, improving their expressiveness. However, texture-based Gaussians parameterize appearance with a uniform per-Gaussian sampling grid, allocating equal sampling density regardless of local visual complexity. This leads to inefficient texture space utilization, where high-frequency regions are under-sampled and smooth regions waste capacity, causing blurred appearance and loss of fine structural detail. We introduce FACT-GS, a Frequency-Aligned Complexity-aware Texture Gaussian Splatting framework that allocates texture sampling density according to local visual frequency. Grounded in adaptive sampling theory, FACT-GS reformulates texture parameterization as a differentiable sampling-density allocation problem, replacing the uniform textures with a learnable frequency-aware allocation strategy implemented via a deformation field whose Jacobian modulates local sampling density. Built on 2D Gaussian Splatting, FACT-GS performs non-uniform sampling on fixed-resolution texture grids, preserving real-time performance while recovering sharper high-frequency details under the same parameter budget.

