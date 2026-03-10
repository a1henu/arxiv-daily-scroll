---
layout: default
title: HDR-NSFF: High Dynamic Range Neural Scene Flow Fields
---

# HDR-NSFF: High Dynamic Range Neural Scene Flow Fields
**arXiv**：[2603.08313v1](https://arxiv.org/abs/2603.08313) · [PDF](https://arxiv.org/pdf/2603.08313.pdf)  
**作者**：Shin Dong-Yeon, Kim Jun-Seong, Kwon Byung-Ki, Tae-Hyun Oh  

**一句话要点**：提出HDR-NSFF以从交替曝光单目视频重建动态高动态范围辐射场

**关键词**：高动态范围, 神经辐射场, 4D高斯溅射, 场景流, 单目视频, 时空视图合成

## 3 点简述
- 核心问题：传统HDR方法基于2D像素对齐，在动态场景中易产生重影和时间不一致。
- 方法要点：采用4D时空建模，统一端到端管道建模HDR辐射、3D场景流、几何和色调映射。
- 实验或效果：在真实世界HDR-GoPro数据集上实现新颖时空视图合成的最先进性能。

## 摘要（原文）

> Radiance of real-world scenes typically spans a much wider dynamic range than what standard cameras can capture. While conventional HDR methods merge alternating-exposure frames, these approaches are inherently constrained to 2D pixel-level alignment, often leading to ghosting artifacts and temporal inconsistency in dynamic scenes. To address these limitations, we present HDR-NSFF, a paradigm shift from 2D-based merging to 4D spatio-temporal modeling. Our framework reconstructs dynamic HDR radiance fields from alternating-exposure monocular videos by representing the scene as a continuous function of space and time, and is compatible with both neural radiance field and 4D Gaussian Splatting (4DGS) based dynamic representations. This unified end-to-end pipeline explicitly models HDR radiance, 3D scene flow, geometry, and tone-mapping, ensuring physical plausibility and global coherence. We further enhance robustness by (i) extending semantic-based optical flow with DINO features to achieve exposure-invariant motion estimation, and (ii) incorporating a generative prior as a regularizer to compensate for limited observation in monocular captures and saturation-induced information loss. To evaluate HDR space-time view synthesis, we present the first real-world HDR-GoPro dataset specifically designed for dynamic HDR scenes. Experiments demonstrate that HDR-NSFF recovers fine radiance details and coherent dynamics even under challenging exposure variations, thereby achieving state-of-the-art performance in novel space-time view synthesis. Project page: https://shin-dong-yeon.github.io/HDR-NSFF/

