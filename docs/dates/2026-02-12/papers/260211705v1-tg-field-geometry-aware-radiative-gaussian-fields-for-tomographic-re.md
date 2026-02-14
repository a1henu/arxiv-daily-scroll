---
layout: default
title: TG-Field: Geometry-Aware Radiative Gaussian Fields for Tomographic Reconstruction
---

# TG-Field: Geometry-Aware Radiative Gaussian Fields for Tomographic Reconstruction
**arXiv**：[2602.11705v1](https://arxiv.org/abs/2602.11705) · [PDF](https://arxiv.org/pdf/2602.11705.pdf)  
**作者**：Yuxiang Zhong, Jun Wei, Chaoqi Chen, Senyou An, Hui Huang  

**一句话要点**：提出TG-Field以解决稀疏投影和动态运动下的CT重建伪影问题

**关键词**：CT重建, 3D高斯溅射, 动态重建, 稀疏投影, 几何感知, 时空注意力

## 3 点简述
- 核心问题：现有3DGS方法在稀疏投影和动态运动中产生严重伪影
- 方法要点：结合几何感知高斯变形、多分辨率哈希编码和时空注意力机制
- 实验或效果：在合成和真实数据集上优于现有方法，实现高精度重建

## 摘要（原文）

> 3D Gaussian Splatting (3DGS) has revolutionized 3D scene representation with superior efficiency and quality. While recent adaptations for computed tomography (CT) show promise, they struggle with severe artifacts under highly sparse-view projections and dynamic motions. To address these challenges, we propose Tomographic Geometry Field (TG-Field), a geometry-aware Gaussian deformation framework tailored for both static and dynamic CT reconstruction. A multi-resolution hash encoder is employed to capture local spatial priors, regularizing primitive parameters under ultra-sparse settings. We further extend the framework to dynamic reconstruction by introducing time-conditioned representations and a spatiotemporal attention block to adaptively aggregate features, thereby resolving spatiotemporal ambiguities and enforcing temporal coherence. In addition, a motion-flow network models fine-grained respiratory motion to track local anatomical deformations. Extensive experiments on synthetic and real-world datasets demonstrate that TG-Field consistently outperforms existing methods, achieving state-of-the-art reconstruction accuracy under highly sparse-view conditions.

