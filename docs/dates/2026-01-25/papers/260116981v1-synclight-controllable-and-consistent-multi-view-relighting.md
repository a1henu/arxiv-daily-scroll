---
layout: default
title: SyncLight: Controllable and Consistent Multi-View Relighting
---

# SyncLight: Controllable and Consistent Multi-View Relighting
**arXiv**：[2601.16981v1](https://arxiv.org/abs/2601.16981) · [PDF](https://arxiv.org/pdf/2601.16981.pdf)  
**作者**：David Serrano-Lozano, Anand Bhattad, Luis Herranz, Jean-François Lalonde, Javier Vazquez-Corral  

**一句话要点**：提出SyncLight以解决多视角未标定场景中一致参数化重光照问题

**关键词**：多视角重光照, 扩散变换器, 潜在桥匹配, 零样本泛化, 混合数据集

## 3 点简述
- 核心问题：现有生成方法在多视角重光照中难以保持严格光照一致性，影响多相机广播等应用。
- 方法要点：基于多视角扩散变换器，通过潜在桥匹配训练，实现单次推理对多视角图像集的高保真重光照。
- 实验或效果：使用混合数据集训练，零样本泛化至任意视角，无需相机姿态信息，支持实际重光照工作流。

## 摘要（原文）

> We present SyncLight, the first method to enable consistent, parametric relighting across multiple uncalibrated views of a static scene. While single-view relighting has advanced significantly, existing generative approaches struggle to maintain the rigorous lighting consistency essential for multi-camera broadcasts, stereoscopic cinema, and virtual production. SyncLight addresses this by enabling precise control over light intensity and color across a multi-view capture of a scene, conditioned on a single reference edit. Our method leverages a multi-view diffusion transformer trained using a latent bridge matching formulation, achieving high-fidelity relighting of the entire image set in a single inference step. To facilitate training, we introduce a large-scale hybrid dataset comprising diverse synthetic environments -- curated from existing sources and newly designed scenes -- alongside high-fidelity, real-world multi-view captures under calibrated illumination. Surprisingly, though trained only on image pairs, SyncLight generalizes zero-shot to an arbitrary number of viewpoints, effectively propagating lighting changes across all views, without requiring camera pose information. SyncLight enables practical relighting workflows for multi-view capture systems.

