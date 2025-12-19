---
layout: default
title: SDFoam: Signed-Distance Foam for explicit surface reconstruction
---

# SDFoam: Signed-Distance Foam for explicit surface reconstruction
**arXiv**：[2512.16706v1](https://arxiv.org/abs/2512.16706) · [PDF](https://arxiv.org/pdf/2512.16706.pdf)  
**作者**：Antonella Rech, Nicola Conci, Nicola Garau  

**一句话要点**：提出SDFoam，结合显式Voronoi图和隐式符号距离场以改进表面重建精度

**关键词**：表面重建, 符号距离场, Voronoi图, 光线追踪, 隐式-显式混合模型, 网格优化

## 3 点简述
- 核心问题：现有方法如NeRF和3DGS在精确网格重建方面仍存在不足，导致表面模糊和拓扑错误
- 方法要点：通过联合学习显式Voronoi图和隐式SDF，利用光线追踪优化和Eikonal正则化，使Voronoi单元面与零水平集对齐
- 实验或效果：在多种场景中，SDFoam显著提升网格重建准确性（Chamfer距离），保持外观质量（PSNR、SSIM），且训练速度与RadiantFoam相当

## 摘要（原文）

> Neural radiance fields (NeRF) have driven impressive progress in view synthesis by using ray-traced volumetric rendering. Splatting-based methods such as 3D Gaussian Splatting (3DGS) provide faster rendering by rasterizing 3D primitives. RadiantFoam (RF) brought ray tracing back, achieving throughput comparable to Gaussian Splatting by organizing radiance with an explicit Voronoi Diagram (VD). Yet, all the mentioned methods still struggle with precise mesh reconstruction. We address this gap by jointly learning an explicit VD with an implicit Signed Distance Field (SDF). The scene is optimized via ray tracing and regularized by an Eikonal objective. The SDF introduces metric-consistent isosurfaces, which, in turn, bias near-surface Voronoi cell faces to align with the zero level set. The resulting model produces crisper, view-consistent surfaces with fewer floaters and improved topology, while preserving photometric quality and maintaining training speed on par with RadiantFoam. Across diverse scenes, our hybrid implicit-explicit formulation, which we name SDFoam, substantially improves mesh reconstruction accuracy (Chamfer distance) with comparable appearance (PSNR, SSIM), without sacrificing efficiency.

