---
layout: default
title: DAMM-LOAM: Degeneracy Aware Multi-Metric LiDAR Odometry and Mapping
---

# DAMM-LOAM: Degeneracy Aware Multi-Metric LiDAR Odometry and Mapping
**arXiv**：[2510.13287v1](https://arxiv.org/abs/2510.13287) · [PDF](https://arxiv.org/pdf/2510.13287.pdf)  
**作者**：Nishant Chandna, Akshat Kaushal  

**一句话要点**：提出DAMM-LOAM以解决LiDAR SLAM在稀疏特征和重复结构环境中的位姿估计退化问题

**关键词**：LiDAR SLAM, 点云分类, 退化感知ICP, 闭环检测, 室内导航, 位姿估计

## 3 点简述
- 核心问题：LiDAR SLAM在稀疏特征、重复几何结构和高频运动场景中位姿估计易退化
- 方法要点：通过点云分类和退化感知加权ICP算法提升对应点准确性和位姿估计精度
- 实验或效果：在室内长走廊等环境中显著提高里程计精度，并实现鲁棒闭环检测

## 摘要（原文）

> LiDAR Simultaneous Localization and Mapping (SLAM) systems are essential for
> enabling precise navigation and environmental reconstruction across various
> applications. Although current point-to-plane ICP algorithms perform effec-
> tively in structured, feature-rich environments, they struggle in scenarios
> with sparse features, repetitive geometric structures, and high-frequency
> motion. This leads to degeneracy in 6- DOF pose estimation. Most
> state-of-the-art algorithms address these challenges by incorporating
> additional sensing modalities, but LiDAR-only solutions continue to face
> limitations under such conditions. To address these issues, we propose a novel
> Degeneracy-Aware Multi-Metric LiDAR Odometry and Map- ping (DAMM-LOAM) module.
> Our system improves mapping accuracy through point cloud classification based
> on surface normals and neighborhood analysis. Points are classified into
> ground, walls, roof, edges, and non-planar points, enabling accurate
> correspondences. A Degeneracy-based weighted least squares-based ICP algorithm
> is then applied for accurate odom- etry estimation. Additionally, a Scan
> Context based back-end is implemented to support robust loop closures.
> DAMM-LOAM demonstrates significant improvements in odometry accuracy,
> especially in indoor environments such as long corridors

