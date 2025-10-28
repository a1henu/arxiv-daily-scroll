---
layout: default
title: Quality-controlled registration of urban MLS point clouds reducing drift effects by adaptive fragmentation
---

# Quality-controlled registration of urban MLS point clouds reducing drift effects by adaptive fragmentation
**arXiv**：[2510.23416v1](https://arxiv.org/abs/2510.23416) · [PDF](https://arxiv.org/pdf/2510.23416.pdf)  
**作者**：Marco Antonio Ortiz Rincon, Yihui Yang, Christoph Holst  

**一句话要点**：提出自适应分块与PV-GICP方法以解决城市MLS点云配准中的漂移问题

**关键词**：点云配准, 移动激光扫描, 城市建模, 漂移校正, 迭代最近点

## 3 点简述
- 核心问题：城市移动激光扫描点云配准中漂移、密度不均和遮挡导致精度下降
- 方法要点：SSC预处理识别正交平面分块，PV-GICP在体素内选择性使用平面进行精细配准
- 实验效果：在慕尼黑数据集上实现亚0.01米平均精度，计算时间减少超50%

## 摘要（原文）

> This study presents a novel workflow designed to efficiently and accurately
> register large-scale mobile laser scanning (MLS) point clouds to a target model
> point cloud in urban street scenarios. This workflow specifically targets the
> complexities inherent in urban environments and adeptly addresses the
> challenges of integrating point clouds that vary in density, noise
> characteristics, and occlusion scenarios, which are common in bustling city
> centers. Two methodological advancements are introduced. First, the proposed
> Semi-sphere Check (SSC) preprocessing technique optimally fragments MLS
> trajectory data by identifying mutually orthogonal planar surfaces. This step
> reduces the impact of MLS drift on the accuracy of the entire point cloud
> registration, while ensuring sufficient geometric features within each fragment
> to avoid local minima. Second, we propose Planar Voxel-based Generalized
> Iterative Closest Point (PV-GICP), a fine registration method that selectively
> utilizes planar surfaces within voxel partitions. This pre-process strategy not
> only improves registration accuracy but also reduces computation time by more
> than 50% compared to conventional point-to-plane ICP methods. Experiments on
> real-world datasets from Munich's inner city demonstrate that our workflow
> achieves sub-0.01 m average registration accuracy while significantly
> shortening processing times. The results underscore the potential of the
> proposed methods to advance automated 3D urban modeling and updating, with
> direct applications in urban planning, infrastructure management, and dynamic
> city monitoring.

