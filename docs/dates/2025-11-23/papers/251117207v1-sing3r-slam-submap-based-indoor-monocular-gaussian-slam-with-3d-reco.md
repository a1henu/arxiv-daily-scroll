---
layout: default
title: SING3R-SLAM: Submap-based Indoor Monocular Gaussian SLAM with 3D Reconstruction Priors
---

# SING3R-SLAM: Submap-based Indoor Monocular Gaussian SLAM with 3D Reconstruction Priors
**arXiv**：[2511.17207v1](https://arxiv.org/abs/2511.17207) · [PDF](https://arxiv.org/pdf/2511.17207.pdf)  
**作者**：Kunyi Li, Michael Niemeyer, Sen Wang, Stefano Gasperini, Nassir Navab, Federico Tombari  

**一句话要点**：提出SING3R-SLAM以解决单目SLAM中的漂移和冗余问题，实现高效3D重建。

**关键词**：单目SLAM, 3D重建, 高斯表示, 子图融合, 漂移校正, 新颖视图渲染

## 3 点简述
- 核心问题：单目SLAM中漂移和冗余点云限制效率和下游任务应用。
- 方法要点：结合局部一致子图与全局高斯表示，联合优化几何和相机位姿。
- 实验或效果：在真实数据集上实现SOTA跟踪、重建和渲染，跟踪精度提升超12%。

## 摘要（原文）

> Recent advances in dense 3D reconstruction enable the accurate capture of local geometry; however, integrating them into SLAM is challenging due to drift and redundant point maps, which limit efficiency and downstream tasks, such as novel view synthesis. To address these issues, we propose SING3R-SLAM, a globally consistent and compact Gaussian-based dense RGB SLAM framework. The key idea is to combine locally consistent 3D reconstructions with a unified global Gaussian representation that jointly refines scene geometry and camera poses, enabling efficient and versatile 3D mapping for multiple downstream applications. SING3R-SLAM first builds locally consistent submaps through our lightweight tracking and reconstruction module, and then progressively aligns and fuses them into a global Gaussian map that enforces cross-view geometric consistency. This global map, in turn, provides feedback to correct local drift and enhance the robustness of tracking. Extensive experiments demonstrate that SING3R-SLAM achieves state-of-the-art tracking, 3D reconstruction, and novel view rendering, resulting in over 12% improvement in tracking and producing finer, more detailed geometry, all while maintaining a compact and memory-efficient global representation on real-world datasets.

