---
layout: default
title: Monocular Endoscopic Tissue 3D Reconstruction with Multi-Level Geometry Regularization
---

# Monocular Endoscopic Tissue 3D Reconstruction with Multi-Level Geometry Regularization
**arXiv**：[2602.20718v1](https://arxiv.org/abs/2602.20718) · [PDF](https://arxiv.org/pdf/2602.20718.pdf)  
**作者**：Yangsen Chen, Hao Wang  

**一句话要点**：提出基于3D高斯泼溅的多级几何正则化方法，以解决单目内窥镜组织3D重建中表面平滑与实时渲染的挑战。

**关键词**：单目内窥镜重建, 3D高斯泼溅, 几何正则化, 实时渲染, 软组织变形

## 3 点简述
- 核心问题：现有方法在单目内窥镜组织重建中难以同时实现平滑表面和实时渲染。
- 方法要点：结合符号距离场构建网格约束高斯泼溅，并引入局部刚性和全局非刚性正则化指导变形。
- 实验或效果：定量和定性分析显示，该方法在纹理和几何上均获得高质量重建，并支持快速渲染。

## 摘要（原文）

> Reconstructing deformable endoscopic tissues is crucial for achieving robot-assisted surgery. However, 3D Gaussian Splatting-based approaches encounter challenges in achieving consistent tissue surface reconstruction, while existing NeRF-based methods lack real-time rendering capabilities. In pursuit of both smooth deformable surfaces and real-time rendering, we introduce a novel approach based on 3D Gaussian Splatting. Specifically, we introduce surface-aware reconstruction, initially employing a Sign Distance Field-based method to construct a mesh, subsequently utilizing this mesh to constrain the Gaussian Splatting reconstruction process. Furthermore, to ensure the generation of physically plausible deformations, we incorporate local rigidity and global non-rigidity restrictions to guide Gaussian deformation, tailored for the highly deformable nature of soft endoscopic tissue. Based on 3D Gaussian Splatting, our proposed method delivers a fast rendering process and smooth surface appearances. Quantitative and qualitative analysis against alternative methodologies shows that our approach achieves solid reconstruction quality in both textures and geometries.

