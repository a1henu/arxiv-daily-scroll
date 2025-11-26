---
layout: default
title: MFM-point: Multi-scale Flow Matching for Point Cloud Generation
---

# MFM-point: Multi-scale Flow Matching for Point Cloud Generation
**arXiv**：[2511.20041v1](https://arxiv.org/abs/2511.20041) · [PDF](https://arxiv.org/pdf/2511.20041.pdf)  
**作者**：Petr Molodyk, Jaemoo Choi, David W. Romero, Ming-Yu Liu, Yongxin Chen  

**一句话要点**：提出多尺度流匹配框架以提升点云生成的可扩展性和性能

**关键词**：点云生成, 流匹配, 多尺度生成, 几何结构保持, 粗到细生成

## 3 点简述
- 点基方法直接生成点云，但性能常低于基于表示的方法
- 采用粗到细生成范式，引入结构化下采样和上采样策略
- 实验显示在点基方法中表现最佳，挑战基于表示的方法

## 摘要（原文）

> In recent years, point cloud generation has gained significant attention in 3D generative modeling. Among existing approaches, point-based methods directly generate point clouds without relying on other representations such as latent features, meshes, or voxels. These methods offer low training cost and algorithmic simplicity, but often underperform compared to representation-based approaches. In this paper, we propose MFM-Point, a multi-scale Flow Matching framework for point cloud generation that substantially improves the scalability and performance of point-based methods while preserving their simplicity and efficiency. Our multi-scale generation algorithm adopts a coarse-to-fine generation paradigm, enhancing generation quality and scalability without incurring additional training or inference overhead. A key challenge in developing such a multi-scale framework lies in preserving the geometric structure of unordered point clouds while ensuring smooth and consistent distributional transitions across resolutions. To address this, we introduce a structured downsampling and upsampling strategy that preserves geometry and maintains alignment between coarse and fine resolutions. Our experimental results demonstrate that MFM-Point achieves best-in-class performance among point-based methods and challenges the best representation-based methods. In particular, MFM-point demonstrates strong results in multi-category and high-resolution generation tasks.

