---
layout: default
title: SSR-GS: Separating Specular Reflection in Gaussian Splatting for Glossy Surface Reconstruction
---

# SSR-GS: Separating Specular Reflection in Gaussian Splatting for Glossy Surface Reconstruction
**arXiv**：[2603.05152v1](https://arxiv.org/abs/2603.05152) · [PDF](https://arxiv.org/pdf/2603.05152.pdf)  
**作者**：Ningjing Fan, Yiqun Wang  

**一句话要点**：提出SSR-GS框架以解决复杂光照下光泽表面重建的挑战

**关键词**：光泽表面重建, 镜面反射建模, 3D高斯溅射, 视觉几何先验, 复杂光照场景

## 3 点简述
- 核心问题：3D高斯溅射在强镜面反射和多表面互反射场景中难以准确重建光泽表面
- 方法要点：引入预过滤Mip-Cubemap建模直接镜面反射，IndiASG模块捕获间接镜面反射，设计视觉几何先验优化损失
- 实验或效果：在合成和真实数据集上验证，实现光泽表面重建的先进性能

## 摘要（原文）

> In recent years, 3D Gaussian splatting (3DGS) has achieved remarkable progress in novel view synthesis. However, accurately reconstructing glossy surfaces under complex illumination remains challenging, particularly in scenes with strong specular reflections and multi-surface interreflections. To address this issue, we propose SSR-GS, a specular reflection modeling framework for glossy surface reconstruction. Specifically, we introduce a prefiltered Mip-Cubemap to model direct specular reflections efficiently, and propose an IndiASG module to capture indirect specular reflections.
>   Furthermore, we design Visual Geometry Priors (VGP) that couple a reflection-aware visual prior via a reflection score (RS) to downweight the photometric loss contribution of reflection-dominated regions, with geometry priors derived from VGGT, including progressively decayed depth supervision and transformed normal constraints. Extensive experiments on both synthetic and real-world datasets demonstrate that SSR-GS achieves state-of-the-art performance in glossy surface reconstruction.

