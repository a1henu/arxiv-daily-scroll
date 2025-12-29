---
layout: default
title: Direction Finding with Sparse Arrays Based on Variable Window Size Spatial Smoothing
---

# Direction Finding with Sparse Arrays Based on Variable Window Size Spatial Smoothing
**arXiv**：[2512.22024v1](https://arxiv.org/abs/2512.22024) · [PDF](https://arxiv.org/pdf/2512.22024.pdf)  
**作者**：Wesley S. Leite, Rodrigo C. de Lamare, Yuriy Zakharov, Wei Liu, Martin Haardt  

**一句话要点**：提出可变窗口空间平滑框架以增强稀疏阵列的到达方向估计性能

**关键词**：稀疏阵列, 到达方向估计, 空间平滑, 可变窗口, 共阵列MUSIC

## 3 点简述
- 核心问题：稀疏线性阵列在到达方向估计中面临信号与噪声子空间分离不足的挑战
- 方法要点：通过压缩平滑孔径，用未扰动低秩项替换扰动秩一外积，提升子空间分离度
- 实验或效果：仿真显示相对于固定窗口方法，性能显著提升且复杂度降低

## 摘要（原文）

> In this work, we introduce a variable window size (VWS) spatial smoothing framework that enhances coarray-based direction of arrival (DOA) estimation for sparse linear arrays. By compressing the smoothing aperture, the proposed VWS Coarray MUSIC (VWS-CA-MUSIC) and VWS Coarray root-MUSIC (VWS-CA-rMUSIC) algorithms replace part of the perturbed rank-one outer products in the smoothed coarray data with unperturbed low-rank additional terms, increasing the separation between signal and noise subspaces, while preserving the signal subspace span. We also derive the bounds that guarantees identifiability, by limiting the values that can be assumed by the compression parameter. Simulations with sparse geometries reveal significant performance improvements and complexity savings relative to the fixed-window coarray MUSIC method.

