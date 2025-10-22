---
layout: default
title: PLANA3R: Zero-shot Metric Planar 3D Reconstruction via Feed-Forward Planar Splatting
---

# PLANA3R: Zero-shot Metric Planar 3D Reconstruction via Feed-Forward Planar Splatting
**arXiv**：[2510.18714v1](https://arxiv.org/abs/2510.18714) · [PDF](https://arxiv.org/pdf/2510.18714.pdf)  
**作者**：Changkun Liu, Bin Tan, Zeran Ke, Shangzhan Zhang, Jiachen Liu, Ming Qian, Nan Xue, Yujun Shen, Tristan Braud  

**一句话要点**：提出PLANA3R框架，从无位姿双视图图像实现度量平面3D重建。

**关键词**：度量3D重建, 平面基元, 无位姿图像, Vision Transformers, 平面溅射, 室内场景

## 3 点简述
- 核心问题：从无位姿双视图图像进行度量3D重建，利用室内场景的几何规律。
- 方法要点：使用Vision Transformers提取稀疏平面基元，通过平面溅射监督几何学习。
- 实验效果：在多个室内数据集验证，泛化能力强，支持3D表面重建和深度估计。

## 摘要（原文）

> This paper addresses metric 3D reconstruction of indoor scenes by exploiting
> their inherent geometric regularities with compact representations. Using
> planar 3D primitives - a well-suited representation for man-made environments -
> we introduce PLANA3R, a pose-free framework for metric Planar 3D Reconstruction
> from unposed two-view images. Our approach employs Vision Transformers to
> extract a set of sparse planar primitives, estimate relative camera poses, and
> supervise geometry learning via planar splatting, where gradients are
> propagated through high-resolution rendered depth and normal maps of
> primitives. Unlike prior feedforward methods that require 3D plane annotations
> during training, PLANA3R learns planar 3D structures without explicit plane
> supervision, enabling scalable training on large-scale stereo datasets using
> only depth and normal annotations. We validate PLANA3R on multiple indoor-scene
> datasets with metric supervision and demonstrate strong generalization to
> out-of-domain indoor environments across diverse tasks under metric evaluation
> protocols, including 3D surface reconstruction, depth estimation, and relative
> pose estimation. Furthermore, by formulating with planar 3D representation, our
> method emerges with the ability for accurate plane segmentation. The project
> page is available at https://lck666666.github.io/plana3r

