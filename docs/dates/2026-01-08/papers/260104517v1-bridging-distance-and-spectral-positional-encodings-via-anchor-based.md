---
layout: default
title: Bridging Distance and Spectral Positional Encodings via Anchor-Based Diffusion Geometry Approximation
---

# Bridging Distance and Spectral Positional Encodings via Anchor-Based Diffusion Geometry Approximation
**arXiv**：[2601.04517v1](https://arxiv.org/abs/2601.04517) · [PDF](https://arxiv.org/pdf/2601.04517.pdf)  
**作者**：Zimo Yan, Zheng Xie, Runfan Duan, Chang Liu, Wumei Du  

**一句话要点**：提出基于锚点的扩散几何近似方法，以桥接距离与谱位置编码，提升分子图学习性能。

**关键词**：分子图学习, 位置编码, 扩散几何, 锚点距离, 谱编码, 图神经网络

## 3 点简述
- 核心问题：距离编码与谱编码在分子图学习中的关系不明确，影响位置信号的有效利用。
- 方法要点：通过锚点距离和谱位置，推导显式三角测量映射，近似扩散几何，提供理论保证。
- 实验或效果：在DrugBank分子图上，距离编码方案恢复扩散几何，两种编码均显著优于无编码基线。

## 摘要（原文）

> Molecular graph learning benefits from positional signals that capture both local neighborhoods and global topology. Two widely used families are spectral encodings derived from Laplacian or diffusion operators and anchor-based distance encodings built from shortest-path information, yet their precise relationship is poorly understood. We interpret distance encodings as a low-rank surrogate of diffusion geometry and derive an explicit trilateration map that reconstructs truncated diffusion coordinates from transformed anchor distances and anchor spectral positions, with pointwise and Frobenius-gap guarantees on random regular graphs. On DrugBank molecular graphs using a shared GNP-based DDI prediction backbone, a distance-driven Nyström scheme closely recovers diffusion geometry, and both Laplacian and distance encodings substantially outperform a no-encoding baseline.

