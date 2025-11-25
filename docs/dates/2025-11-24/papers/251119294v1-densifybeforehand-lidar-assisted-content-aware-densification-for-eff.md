---
layout: default
title: DensifyBeforehand: LiDAR-assisted Content-aware Densification for Efficient and Quality 3D Gaussian Splatting
---

# DensifyBeforehand: LiDAR-assisted Content-aware Densification for Efficient and Quality 3D Gaussian Splatting
**arXiv**：[2511.19294v1](https://arxiv.org/abs/2511.19294) · [PDF](https://arxiv.org/pdf/2511.19294.pdf)  
**作者**：Phurtivilai Patt, Leyang Huang, Yinqiang Zhang, Yang Lei  

**一句话要点**：提出LiDAR辅助内容感知预稠密化方法，以提升3D高斯泼溅的效率与质量

**关键词**：3D高斯泼溅, LiDAR辅助, 内容感知稠密化, ROI感知采样, 计算效率优化

## 3 点简述
- 核心问题：现有3D高斯泼溅依赖自适应密度控制，易产生漂浮伪影和资源浪费
- 方法要点：结合稀疏LiDAR和单目深度估计，采用ROI感知采样预稠密化场景
- 实验或效果：在四个新数据集上验证，降低资源消耗和训练时间，保持视觉质量

## 摘要（原文）

> This paper addresses the limitations of existing 3D Gaussian Splatting (3DGS) methods, particularly their reliance on adaptive density control, which can lead to floating artifacts and inefficient resource usage. We propose a novel densify beforehand approach that enhances the initialization of 3D scenes by combining sparse LiDAR data with monocular depth estimation from corresponding RGB images. Our ROI-aware sampling scheme prioritizes semantically and geometrically important regions, yielding a dense point cloud that improves visual fidelity and computational efficiency. This densify beforehand approach bypasses the adaptive density control that may introduce redundant Gaussians in the original pipeline, allowing the optimization to focus on the other attributes of 3D Gaussian primitives, reducing overlap while enhancing visual quality. Our method achieves comparable results to state-of-the-art techniques while significantly lowering resource consumption and training time. We validate our approach through extensive comparisons and ablation studies on four newly collected datasets, showcasing its effectiveness in preserving regions of interest in complex scenes.

