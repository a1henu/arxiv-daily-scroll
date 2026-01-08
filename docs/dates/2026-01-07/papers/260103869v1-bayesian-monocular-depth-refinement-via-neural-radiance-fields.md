---
layout: default
title: Bayesian Monocular Depth Refinement via Neural Radiance Fields
---

# Bayesian Monocular Depth Refinement via Neural Radiance Fields
**arXiv**：[2601.03869v1](https://arxiv.org/abs/2601.03869) · [PDF](https://arxiv.org/pdf/2601.03869.pdf)  
**作者**：Arun Muthukkumar  

**一句话要点**：提出MDENeRF框架，通过贝叶斯融合单目深度与NeRF深度以提升室内场景几何细节

**关键词**：单目深度估计, 神经辐射场, 贝叶斯融合, 深度细化, 室内场景, 不确定性估计

## 3 点简述
- 单目深度估计常产生平滑深度图，缺乏精细几何细节，影响场景理解准确性。
- MDENeRF结合单目深度全局结构、NeRF深度细节及不确定性，通过贝叶斯融合迭代优化。
- 在SUN RGB-D数据集上实验显示，该方法在关键指标上优于现有方法。

## 摘要（原文）

> Monocular depth estimation has applications in many fields, such as autonomous navigation and extended reality, making it an essential computer vision task. However, current methods often produce smooth depth maps that lack the fine geometric detail needed for accurate scene understanding. We propose MDENeRF, an iterative framework that refines monocular depth estimates using depth information from Neural Radiance Fields (NeRFs). MDENeRF consists of three components: (1) an initial monocular estimate for global structure, (2) a NeRF trained on perturbed viewpoints, with per-pixel uncertainty, and (3) Bayesian fusion of the noisy monocular and NeRF depths. We derive NeRF uncertainty from the volume rendering process to iteratively inject high-frequency fine details. Meanwhile, our monocular prior maintains global structure. We demonstrate superior performance on key metrics and experiments using indoor scenes from the SUN RGB-D dataset.

