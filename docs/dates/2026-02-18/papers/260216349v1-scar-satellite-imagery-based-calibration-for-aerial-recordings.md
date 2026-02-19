---
layout: default
title: SCAR: Satellite Imagery-Based Calibration for Aerial Recordings
---

# SCAR: Satellite Imagery-Based Calibration for Aerial Recordings
**arXiv**：[2602.16349v1](https://arxiv.org/abs/2602.16349) · [PDF](https://arxiv.org/pdf/2602.16349.pdf)  
**作者**：Henry Hölzemann, Michael Schleiss  

**一句话要点**：提出SCAR方法，利用卫星图像实现空中视觉惯性系统的长期自动校准优化。

**关键词**：视觉惯性校准, 卫星图像对齐, 长期空中操作, 自动参数估计, 地理空间数据利用

## 3 点简述
- 核心问题：空中视觉惯性系统在野外部署中校准参数易退化，传统方法依赖专用校准操作或人工地面控制点。
- 方法要点：通过将空中图像与公开正射影像和海拔模型生成的2D-3D对应关系对齐，估计内外参数。
- 实验或效果：在两年六个大规模空中任务中评估，SCAR显著降低重投影误差，提升定位精度，优于现有基线。

## 摘要（原文）

> We introduce SCAR, a method for long-term auto-calibration refinement of aerial visual-inertial systems that exploits georeferenced satellite imagery as a persistent global reference. SCAR estimates both intrinsic and extrinsic parameters by aligning aerial images with 2D--3D correspondences derived from publicly available orthophotos and elevation models. In contrast to existing approaches that rely on dedicated calibration maneuvers or manually surveyed ground control points, our method leverages external geospatial data to detect and correct calibration degradation under field deployment conditions. We evaluate our approach on six large-scale aerial campaigns conducted over two years under diverse seasonal and environmental conditions. Across all sequences, SCAR consistently outperforms established baselines (Kalibr, COLMAP, VINS-Mono), reducing median reprojection error by a large margin, and translating these calibration gains into substantially lower visual localization rotation errors and higher pose accuracy. These results demonstrate that SCAR provides accurate, robust, and reproducible calibration over long-term aerial operations without the need for manual intervention.

