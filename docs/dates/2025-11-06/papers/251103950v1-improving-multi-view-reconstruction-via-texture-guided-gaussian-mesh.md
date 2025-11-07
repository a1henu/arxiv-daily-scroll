---
layout: default
title: Improving Multi-View Reconstruction via Texture-Guided Gaussian-Mesh Joint Optimization
---

# Improving Multi-View Reconstruction via Texture-Guided Gaussian-Mesh Joint Optimization
**arXiv**：[2511.03950v1](https://arxiv.org/abs/2511.03950) · [PDF](https://arxiv.org/pdf/2511.03950.pdf)  
**作者**：Zhejia Cai, Puhua Jiang, Shiwei Mao, Hongkun Cao, Ruqi Huang  

**一句话要点**：提出纹理引导的高斯-网格联合优化方法，以改进多视图重建，支持3D编辑任务。

**关键词**：多视图重建, 高斯-网格联合优化, 可微渲染, 几何正则化, 纹理引导, 3D编辑

## 3 点简述
- 核心问题：现有方法在几何精度与渲染真实感间权衡，解耦优化阻碍编辑。
- 方法要点：联合优化网格几何与顶点颜色，利用高斯引导可微渲染和正则化。
- 实验或效果：获得高质量重建，可应用于重光照和形状变形等下游任务。

## 摘要（原文）

> Reconstructing real-world objects from multi-view images is essential for
> applications in 3D editing, AR/VR, and digital content creation. Existing
> methods typically prioritize either geometric accuracy (Multi-View Stereo) or
> photorealistic rendering (Novel View Synthesis), often decoupling geometry and
> appearance optimization, which hinders downstream editing tasks. This paper
> advocates an unified treatment on geometry and appearance optimization for
> seamless Gaussian-mesh joint optimization. More specifically, we propose a
> novel framework that simultaneously optimizes mesh geometry (vertex positions
> and faces) and vertex colors via Gaussian-guided mesh differentiable rendering,
> leveraging photometric consistency from input images and geometric
> regularization from normal and depth maps. The obtained high-quality 3D
> reconstruction can be further exploit in down-stream editing tasks, such as
> relighting and shape deformation. The code will be publicly available upon
> acceptance.

