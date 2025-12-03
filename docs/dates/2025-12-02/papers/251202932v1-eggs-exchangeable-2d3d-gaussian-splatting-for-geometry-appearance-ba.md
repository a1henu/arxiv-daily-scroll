---
layout: default
title: EGGS: Exchangeable 2D/3D Gaussian Splatting for Geometry-Appearance Balanced Novel View Synthesis
---

# EGGS: Exchangeable 2D/3D Gaussian Splatting for Geometry-Appearance Balanced Novel View Synthesis
**arXiv**：[2512.02932v1](https://arxiv.org/abs/2512.02932) · [PDF](https://arxiv.org/pdf/2512.02932.pdf)  
**作者**：Yancheng Zhang, Guangyu Sun, Chen Chen  

**一句话要点**：提出可交换2D/3D高斯泼溅以平衡几何与外观的新视图合成方法

**关键词**：新视图合成, 高斯泼溅, 几何外观平衡, 混合表示, 实时渲染, CUDA加速

## 3 点简述
- 核心问题：3D高斯泼溅外观保真但几何不一致，2D高斯泼溅几何一致但纹理细节不足
- 方法要点：集成2D和3D高斯，通过混合渲染、自适应类型交换和频率解耦优化实现平衡
- 实验或效果：在渲染质量、几何精度和效率上优于现有方法，支持高效训练和推理

## 摘要（原文）

> Novel view synthesis (NVS) is crucial in computer vision and graphics, with wide applications in AR, VR, and autonomous driving. While 3D Gaussian Splatting (3DGS) enables real-time rendering with high appearance fidelity, it suffers from multi-view inconsistencies, limiting geometric accuracy. In contrast, 2D Gaussian Splatting (2DGS) enforces multi-view consistency but compromises texture details. To address these limitations, we propose Exchangeable Gaussian Splatting (EGGS), a hybrid representation that integrates 2D and 3D Gaussians to balance appearance and geometry. To achieve this, we introduce Hybrid Gaussian Rasterization for unified rendering, Adaptive Type Exchange for dynamic adaptation between 2D and 3D Gaussians, and Frequency-Decoupled Optimization that effectively exploits the strengths of each type of Gaussian representation. Our CUDA-accelerated implementation ensures efficient training and inference. Extensive experiments demonstrate that EGGS outperforms existing methods in rendering quality, geometric accuracy, and efficiency, providing a practical solution for high-quality NVS.

