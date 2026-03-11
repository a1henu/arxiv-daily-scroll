---
layout: default
title: VarSplat: Uncertainty-aware 3D Gaussian Splatting for Robust RGB-D SLAM
---

# VarSplat: Uncertainty-aware 3D Gaussian Splatting for Robust RGB-D SLAM
**arXiv**：[2603.09673v1](https://arxiv.org/abs/2603.09673) · [PDF](https://arxiv.org/pdf/2603.09673.pdf)  
**作者**：Anh Thuan Tran, Jana Kosecka  

**一句话要点**：提出VarSplat，一种不确定性感知的3D高斯泼溅SLAM系统，以提升RGB-D SLAM在低纹理等场景的鲁棒性。

**关键词**：3D高斯泼溅, 不确定性建模, RGB-D SLAM, 可微分渲染, 鲁棒性优化

## 3 点简述
- 现有3DGS-SLAM方法隐含处理测量可靠性，导致姿态估计和全局对齐在低纹理区域易漂移。
- VarSplat显式学习每个泼溅的外观方差，通过总方差定律和alpha合成渲染可微分像素级不确定性图。
- 实验在合成和真实数据集上显示，VarSplat提升了鲁棒性，在跟踪、建图和视图合成方面具有竞争力或更优。

## 摘要（原文）

> Simultaneous Localization and Mapping (SLAM) with 3D Gaussian Splatting (3DGS) enables fast, differentiable rendering and high-fidelity reconstruction across diverse real-world scenes. However, existing 3DGS-SLAM approaches handle measurement reliability implicitly, making pose estimation and global alignment susceptible to drift in low-texture regions, transparent surfaces, or areas with complex reflectance properties. To this end, we introduce VarSplat, an uncertainty-aware 3DGS-SLAM system that explicitly learns per-splat appearance variance. By using the law of total variance with alpha compositing, we then render differentiable per-pixel uncertainty map via efficient, single-pass rasterization. This map guides tracking, submap registration, and loop detection toward focusing on reliable regions and contributes to more stable optimization. Experimental results on Replica (synthetic) and TUM-RGBD, ScanNet, and ScanNet++ (real-world) show that VarSplat improves robustness and achieves competitive or superior tracking, mapping, and novel view synthesis rendering compared to existing studies for dense RGB-D SLAM.

