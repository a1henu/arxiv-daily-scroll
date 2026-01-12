---
layout: default
title: GeoSurDepth: Spatial Geometry-Consistent Self-Supervised Depth Estimation for Surround-View Cameras
---

# GeoSurDepth: Spatial Geometry-Consistent Self-Supervised Depth Estimation for Surround-View Cameras
**arXiv**：[2601.05839v1](https://arxiv.org/abs/2601.05839) · [PDF](https://arxiv.org/pdf/2601.05839.pdf)  
**作者**：Weimin Liu, Wenjun Wang, Joshua H. Meng  

**一句话要点**：提出GeoSurDepth框架，利用几何一致性实现环视摄像头的自监督深度估计

**关键词**：自监督深度估计, 环视摄像头, 几何一致性, 视图合成, 自动驾驶, 3D场景理解

## 3 点简述
- 核心问题：现有方法多关注光度约束，未充分利用单目和环视中的几何结构。
- 方法要点：利用基础模型作为几何先验，保持空间3D法线一致性，并引入新视图合成管道。
- 实验或效果：在DDAD和nuScenes数据集上达到先进性能，验证几何一致性的有效性。

## 摘要（原文）

> Accurate surround-view depth estimation provides a competitive alternative to laser-based sensors and is essential for 3D scene understanding in autonomous driving. While prior studies have proposed various approaches that primarily focus on enforcing cross-view constraints at the photometric level, few explicitly exploit the rich geometric structure inherent in both monocular and surround-view setting. In this work, we propose GeoSurDepth, a framework that leverages geometry consistency as the primary cue for surround-view depth estimation. Concretely, we utilize foundation models as a pseudo geometry prior and feature representation enhancement tool to guide the network to maintain surface normal consistency in spatial 3D space and regularize object- and texture-consistent depth estimation in 2D. In addition, we introduce a novel view synthesis pipeline where 2D-3D lifting is achieved with dense depth reconstructed via spatial warping, encouraging additional photometric supervision across temporal, spatial, and spatial-temporal contexts, and compensating for the limitations of single-view image reconstruction. Finally, a newly-proposed adaptive joint motion learning strategy enables the network to adaptively emphasize informative spatial geometry cues for improved motion reasoning. Extensive experiments on DDAD and nuScenes demonstrate that GeoSurDepth achieves state-of-the-art performance, validating the effectiveness of our approach. Our framework highlights the importance of exploiting geometry coherence and consistency for robust self-supervised multi-view depth estimation.

