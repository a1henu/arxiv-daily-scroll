---
layout: default
title: GVSynergy-Det: Synergistic Gaussian-Voxel Representations for Multi-View 3D Object Detection
---

# GVSynergy-Det: Synergistic Gaussian-Voxel Representations for Multi-View 3D Object Detection
**arXiv**：[2512.23176v1](https://arxiv.org/abs/2512.23176) · [PDF](https://arxiv.org/pdf/2512.23176.pdf)  
**作者**：Yi Zhang, Yi Wang, Lei Yao, Lap-Pui Chau  

**一句话要点**：提出GVSynergy-Det框架，通过高斯-体素协同表示提升无深度监督的多视图3D目标检测精度

**关键词**：多视图3D目标检测, 高斯-体素协同表示, 无深度监督, 几何特征增强, 室内场景理解

## 3 点简述
- 核心问题：图像基3D检测面临高精度需密集3D监督与无监督下几何提取不准确的挑战。
- 方法要点：结合连续高斯表示和离散体素表示，通过可学习集成机制协同增强几何特征。
- 实验或效果：在ScanNetV2和ARKitScenes数据集上实现最先进性能，无需深度或密集3D几何监督。

## 摘要（原文）

> Image-based 3D object detection aims to identify and localize objects in 3D space using only RGB images, eliminating the need for expensive depth sensors required by point cloud-based methods. Existing image-based approaches face two critical challenges: methods achieving high accuracy typically require dense 3D supervision, while those operating without such supervision struggle to extract accurate geometry from images alone. In this paper, we present GVSynergy-Det, a novel framework that enhances 3D detection through synergistic Gaussian-Voxel representation learning. Our key insight is that continuous Gaussian and discrete voxel representations capture complementary geometric information: Gaussians excel at modeling fine-grained surface details while voxels provide structured spatial context. We introduce a dual-representation architecture that: 1) adapts generalizable Gaussian Splatting to extract complementary geometric features for detection tasks, and 2) develops a cross-representation enhancement mechanism that enriches voxel features with geometric details from Gaussian fields. Unlike previous methods that either rely on time-consuming per-scene optimization or utilize Gaussian representations solely for depth regularization, our synergistic strategy directly leverages features from both representations through learnable integration, enabling more accurate object localization. Extensive experiments demonstrate that GVSynergy-Det achieves state-of-the-art results on challenging indoor benchmarks, significantly outperforming existing methods on both ScanNetV2 and ARKitScenes datasets, all without requiring any depth or dense 3D geometry supervision (e.g., point clouds or TSDF).

