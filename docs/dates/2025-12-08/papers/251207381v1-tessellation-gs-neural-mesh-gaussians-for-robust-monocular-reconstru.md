---
layout: default
title: Tessellation GS: Neural Mesh Gaussians for Robust Monocular Reconstruction of Dynamic Objects
---

# Tessellation GS: Neural Mesh Gaussians for Robust Monocular Reconstruction of Dynamic Objects
**arXiv**：[2512.07381v1](https://arxiv.org/abs/2512.07381) · [PDF](https://arxiv.org/pdf/2512.07381.pdf)  
**作者**：Shuohan Tao, Boyao Zhou, Hanzhang Tu, Yuwang Wang, Yebin Liu  

**一句话要点**：提出Tessellation GS，基于网格面约束2D高斯以从单相机稳健重建动态物体

**关键词**：动态场景重建, 高斯溅射, 单相机重建, 网格约束, 自适应细分

## 3 点简述
- 核心问题：3D高斯溅射在稀疏视图和动态场景中因各向异性导致过拟合和泛化差
- 方法要点：将2D高斯锚定在网格面上，通过自适应面细分和神经特征推断属性
- 实验或效果：在单静态相机下，外观和网格重建任务中LPIPS降低29.1%，Chamfer距离减少49.2%

## 摘要（原文）

> 3D Gaussian Splatting (GS) enables highly photorealistic scene reconstruction from posed image sequences but struggles with viewpoint extrapolation due to its anisotropic nature, leading to overfitting and poor generalization, particularly in sparse-view and dynamic scene reconstruction. We propose Tessellation GS, a structured 2D GS approach anchored on mesh faces, to reconstruct dynamic scenes from a single continuously moving or static camera. Our method constrains 2D Gaussians to localized regions and infers their attributes via hierarchical neural features on mesh faces. Gaussian subdivision is guided by an adaptive face subdivision strategy driven by a detail-aware loss function. Additionally, we leverage priors from a reconstruction foundation model to initialize Gaussian deformations, enabling robust reconstruction of general dynamic objects from a single static camera, previously extremely challenging for optimization-based methods. Our method outperforms previous SOTA method, reducing LPIPS by 29.1% and Chamfer distance by 49.2% on appearance and mesh reconstruction tasks.

