---
layout: default
title: EGG-Fusion: Efficient 3D Reconstruction with Geometry-aware Gaussian Surfel on the Fly
---

# EGG-Fusion: Efficient 3D Reconstruction with Geometry-aware Gaussian Surfel on the Fly
**arXiv**：[2512.01296v1](https://arxiv.org/abs/2512.01296) · [PDF](https://arxiv.org/pdf/2512.01296.pdf)  
**作者**：Xiaokun Pan, Zhenzhe Li, Zhichao Ye, Hongjia Zhai, Guofeng Zhang  

**一句话要点**：提出EGG-Fusion系统，通过几何感知高斯面元与信息滤波融合，实现实时高精度三维重建。

**关键词**：实时三维重建, 可微分渲染, 高斯面元映射, 信息滤波融合, 几何感知优化, SLAM系统

## 3 点简述
- 核心问题：现有可微分渲染方法在实时计算和传感器噪声敏感性方面面临挑战，导致重建几何保真度下降。
- 方法要点：采用鲁棒稀疏到稠密相机跟踪和几何感知高斯面元映射模块，引入基于信息滤波的融合方法以显式处理传感器噪声。
- 实验或效果：在Replica和ScanNet++基准上实现0.6cm表面重建误差，比SOTA方法精度提升超20%，并保持24 FPS实时处理。

## 摘要（原文）

> Real-time 3D reconstruction is a fundamental task in computer graphics. Recently, differentiable-rendering-based SLAM system has demonstrated significant potential, enabling photorealistic scene rendering through learnable scene representations such as Neural Radiance Fields (NeRF) and 3D Gaussian Splatting (3DGS). Current differentiable rendering methods face dual challenges in real-time computation and sensor noise sensitivity, leading to degraded geometric fidelity in scene reconstruction and limited practicality. To address these challenges, we propose a novel real-time system EGG-Fusion, featuring robust sparse-to-dense camera tracking and a geometry-aware Gaussian surfel mapping module, introducing an information filter-based fusion method that explicitly accounts for sensor noise to achieve high-precision surface reconstruction. The proposed differentiable Gaussian surfel mapping effectively models multi-view consistent surfaces while enabling efficient parameter optimization. Extensive experimental results demonstrate that the proposed system achieves a surface reconstruction error of 0.6\textit{cm} on standardized benchmark datasets including Replica and ScanNet++, representing over 20\% improvement in accuracy compared to state-of-the-art (SOTA) GS-based methods. Notably, the system maintains real-time processing capabilities at 24 FPS, establishing it as one of the most accurate differentiable-rendering-based real-time reconstruction systems. Project Page: https://zju3dv.github.io/eggfusion/

