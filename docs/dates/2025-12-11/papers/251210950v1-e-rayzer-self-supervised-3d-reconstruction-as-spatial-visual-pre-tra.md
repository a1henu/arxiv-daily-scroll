---
layout: default
title: E-RayZer: Self-supervised 3D Reconstruction as Spatial Visual Pre-training
---

# E-RayZer: Self-supervised 3D Reconstruction as Spatial Visual Pre-training
**arXiv**：[2512.10950v1](https://arxiv.org/abs/2512.10950) · [PDF](https://arxiv.org/pdf/2512.10950.pdf)  
**作者**：Qitao Zhao, Hao Tan, Qianqian Wang, Sai Bi, Kai Zhang, Kalyan Sunkavalli, Shubham Tulsiani, Hanwen Jiang  

**一句话要点**：提出E-RayZer，通过显式几何的自监督三维重建实现三维感知视觉预训练。

**关键词**：三维重建, 自监督学习, 视觉预训练, 多视图图像, 几何表示, 课程学习

## 3 点简述
- 核心问题：自监督预训练在三维感知表示学习上未充分探索，现有方法如RayZer依赖隐式视图合成。
- 方法要点：直接在三维空间进行自监督重建，引入细粒度学习课程以优化收敛和可扩展性。
- 实验或效果：在姿态估计上显著优于RayZer，下游任务中超越DINOv3等领先模型。

## 摘要（原文）

> Self-supervised pre-training has revolutionized foundation models for languages, individual 2D images and videos, but remains largely unexplored for learning 3D-aware representations from multi-view images. In this paper, we present E-RayZer, a self-supervised large 3D Vision model that learns truly 3D-aware representations directly from unlabeled images. Unlike prior self-supervised methods such as RayZer that infer 3D indirectly through latent-space view synthesis, E-RayZer operates directly in 3D space, performing self-supervised 3D reconstruction with Explicit geometry. This formulation eliminates shortcut solutions and yields representations that are geometrically grounded. To ensure convergence and scalability, we introduce a novel fine-grained learning curriculum that organizes training from easy to hard samples and harmonizes heterogeneous data sources in an entirely unsupervised manner. Experiments demonstrate that E-RayZer significantly outperforms RayZer on pose estimation, matches or sometimes surpasses fully supervised reconstruction models such as VGGT. Furthermore, its learned representations outperform leading visual pre-training models (e.g., DINOv3, CroCo v2, VideoMAE V2, and RayZer) when transferring to 3D downstream tasks, establishing E-RayZer as a new paradigm for 3D-aware visual pre-training.

