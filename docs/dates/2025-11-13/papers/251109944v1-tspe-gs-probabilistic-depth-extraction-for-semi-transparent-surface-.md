---
layout: default
title: TSPE-GS: Probabilistic Depth Extraction for Semi-Transparent Surface Reconstruction via 3D Gaussian Splatting
---

# TSPE-GS: Probabilistic Depth Extraction for Semi-Transparent Surface Reconstruction via 3D Gaussian Splatting
**arXiv**：[2511.09944v1](https://arxiv.org/abs/2511.09944) · [PDF](https://arxiv.org/pdf/2511.09944.pdf)  
**作者**：Zhiyuan Xu, Nan Min, Yuhang Guo, Tong Wei  

**一句话要点**：提出TSPE-GS以解决半透明表面重建中的深度模糊问题

**关键词**：半透明表面重建, 3D高斯泼溅, 概率深度提取, 多模态分布, 深度模糊解决

## 3 点简述
- 核心问题：3D高斯泼溅假设像素单深度，无法重建多表面可见的半透明场景。
- 方法要点：均匀采样透射率，建模像素级多模态不透明度和深度分布。
- 实验效果：在公开和自收集数据集上显著提升半透明几何重建，保持不透明场景性能。

## 摘要（原文）

> 3D Gaussian Splatting offers a strong speed-quality trade-off but struggles to reconstruct semi-transparent surfaces because most methods assume a single depth per pixel, which fails when multiple surfaces are visible. We propose TSPE-GS (Transparent Surface Probabilistic Extraction for Gaussian Splatting), which uniformly samples transmittance to model a pixel-wise multi-modal distribution of opacity and depth, replacing the prior single-peak assumption and resolving cross-surface depth ambiguity. By progressively fusing truncated signed distance functions, TSPE-GS reconstructs external and internal surfaces separately within a unified framework. The method generalizes to other Gaussian-based reconstruction pipelines without extra training overhead. Extensive experiments on public and self-collected semi-transparent and opaque datasets show TSPE-GS significantly improves semi-transparent geometry reconstruction while maintaining performance on opaque scenes.

