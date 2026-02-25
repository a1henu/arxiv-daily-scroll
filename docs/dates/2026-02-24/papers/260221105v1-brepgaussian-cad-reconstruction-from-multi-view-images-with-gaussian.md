---
layout: default
title: BrepGaussian: CAD reconstruction from Multi-View Images with Gaussian Splatting
---

# BrepGaussian: CAD reconstruction from Multi-View Images with Gaussian Splatting
**arXiv**：[2602.21105v1](https://arxiv.org/abs/2602.21105) · [PDF](https://arxiv.org/pdf/2602.21105.pdf)  
**作者**：Jiaxing Yu, Dongyang Ren, Hangyu Xu, Zhouyuxiao Yang, Yuanqi Li, Jie Guo, Zhengkang Zhou, Yanwen Guo  

**一句话要点**：提出BrepGaussian框架，从多视角图像重建CAD边界表示，基于高斯溅射渲染器与两阶段学习。

**关键词**：CAD重建, 边界表示, 高斯溅射, 多视角图像, 几何学习, 特征细化

## 3 点简述
- 核心问题：从非结构化数据恢复CAD边界表示（B-rep）具有挑战性，现有方法依赖密集点云且泛化能力有限。
- 方法要点：采用高斯溅射渲染器学习特征，通过两阶段框架先捕获几何与边缘，再细化面片特征以实现干净几何与一致实例表示。
- 实验或效果：广泛实验显示优于现有方法，代码与数据集将在接受后发布。

## 摘要（原文）

> The boundary representation (B-rep) models a 3D solid as its explicit boundaries: trimmed corners, edges, and faces. Recovering B-rep representation from unstructured data is a challenging and valuable task of computer vision and graphics. Recent advances in deep learning have greatly improved the recovery of 3D shape geometry, but still depend on dense and clean point clouds and struggle to generalize to novel shapes. We propose B-rep Gaussian Splatting (BrepGaussian), a novel framework that learns 3D parametric representations from 2D images. We employ a Gaussian Splatting renderer with learnable features, followed by a specific fitting strategy. To disentangle geometry reconstruction and feature learning, we introduce a two-stage learning framework that first captures geometry and edges and then refines patch features to achieve clean geometry and coherent instance representations. Extensive experiments demonstrate the superior performance of our approach to state-of-the-art methods. We will release our code and datasets upon acceptance.

