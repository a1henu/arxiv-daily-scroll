---
layout: default
title: SwiftNDC: Fast Neural Depth Correction for High-Fidelity 3D Reconstruction
---

# SwiftNDC: Fast Neural Depth Correction for High-Fidelity 3D Reconstruction
**arXiv**：[2602.22565v1](https://arxiv.org/abs/2602.22565) · [PDF](https://arxiv.org/pdf/2602.22565.pdf)  
**作者**：Kang Han, Wei Xiang, Lu Yu, Mathew Wyatt, Gaowen Liu, Ramana Rao Kompella  

**一句话要点**：提出SwiftNDC框架，通过神经深度校正实现高效高保真3D重建

**关键词**：神经深度校正, 3D重建, 几何初始化, 3D高斯溅射, 新视角合成

## 3 点简述
- 问题：现有深度引导3D重建方法存在尺度漂移、多视角不一致和需大量优化的问题。
- 方法：构建神经深度校正场生成跨视角一致深度图，经反投影和滤波获得密集点云作为几何初始化。
- 效果：在五个数据集上验证，加速3D高斯溅射重建，提升网格质量和新视角合成渲染保真度。

## 摘要（原文）

> Depth-guided 3D reconstruction has gained popularity as a fast alternative to optimization-heavy approaches, yet existing methods still suffer from scale drift, multi-view inconsistencies, and the need for substantial refinement to achieve high-fidelity geometry. Here, we propose SwiftNDC, a fast and general framework built around a Neural Depth Correction field that produces cross-view consistent depth maps. From these refined depths, we generate a dense point cloud through back-projection and robust reprojection-error filtering, obtaining a clean and uniformly distributed geometric initialization for downstream reconstruction. This reliable dense geometry substantially accelerates 3D Gaussian Splatting (3DGS) for mesh reconstruction, enabling high-quality surfaces with significantly fewer optimization iterations. For novel-view synthesis, SwiftNDC can also improve 3DGS rendering quality, highlighting the benefits of strong geometric initialization. We conduct a comprehensive study across five datasets, including two for mesh reconstruction, as well as three for novel-view synthesis. SwiftNDC consistently reduces running time for accurate mesh reconstruction and boosts rendering fidelity for view synthesis, demonstrating the effectiveness of combining neural depth refinement with robust geometric initialization for high-fidelity and efficient 3D reconstruction.

