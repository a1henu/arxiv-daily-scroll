---
layout: default
title: PLANING: A Loosely Coupled Triangle-Gaussian Framework for Streaming 3D Reconstruction
---

# PLANING: A Loosely Coupled Triangle-Gaussian Framework for Streaming 3D Reconstruction
**arXiv**：[2601.22046v1](https://arxiv.org/abs/2601.22046) · [PDF](https://arxiv.org/pdf/2601.22046.pdf)  
**作者**：Changjian Jiang, Kerui Ren, Xudong Li, Kaiwen Song, Linning Xu, Tao Lu, Junting Dong, Yu Zhang, Bo Dai, Mulin Yu  

**一句话要点**：提出PLANING框架，通过松散耦合三角形与高斯表示实现高效流式3D重建，兼顾几何精度与渲染质量。

**关键词**：流式3D重建, 混合表示, 几何解耦, 在线优化, 单目图像序列, 计算效率

## 3 点简述
- 核心问题：现有单目图像序列流式重建方法难以同时实现高质量渲染与准确几何。
- 方法要点：采用松散耦合的显式几何基元与神经高斯混合表示，解耦几何与外观建模。
- 实验或效果：在ScanNetV2上重建速度提升5倍以上，几何精度提升18.52%，渲染质量超越ARTDECO。

## 摘要（原文）

> Streaming reconstruction from monocular image sequences remains challenging, as existing methods typically favor either high-quality rendering or accurate geometry, but rarely both. We present PLANING, an efficient on-the-fly reconstruction framework built on a hybrid representation that loosely couples explicit geometric primitives with neural Gaussians, enabling geometry and appearance to be modeled in a decoupled manner. This decoupling supports an online initialization and optimization strategy that separates geometry and appearance updates, yielding stable streaming reconstruction with substantially reduced structural redundancy. PLANING improves dense mesh Chamfer-L2 by 18.52% over PGSR, surpasses ARTDECO by 1.31 dB PSNR, and reconstructs ScanNetV2 scenes in under 100 seconds, over 5x faster than 2D Gaussian Splatting, while matching the quality of offline per-scene optimization. Beyond reconstruction quality, the structural clarity and computational efficiency of \modelname~make it well suited for a broad range of downstream applications, such as enabling large-scale scene modeling and simulation-ready environments for embodied AI. Project page: https://city-super.github.io/PLANING/ .

