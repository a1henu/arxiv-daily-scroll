---
layout: default
title: TreeLoc++: Robust 6-DoF LiDAR Localization in Forests with a Compact Digital Forest Inventory
---

# TreeLoc++: Robust 6-DoF LiDAR Localization in Forests with a Compact Digital Forest Inventory
**arXiv**：[2603.03695v1](https://arxiv.org/abs/2603.03695) · [PDF](https://arxiv.org/pdf/2603.03695.pdf)  
**作者**：Minwoo Jung, Dongjae Lee, Nived Chebrolu, Haedam Oh, Maurice Fallon, Ayoung Kim  

**一句话要点**：提出TreeLoc++框架，利用紧凑数字森林清单实现森林中鲁棒的6自由度LiDAR定位。

**关键词**：森林定位, 数字森林清单, 6自由度姿态估计, LiDAR定位, 紧凑地图表示

## 3 点简述
- 核心问题：现有森林定位方法依赖密集点云，存储和维护成本高，且数字森林清单在定位研究中被忽视。
- 方法要点：直接使用数字森林清单作为判别表示，通过距离直方图编码局部树布局，结合DBH过滤和优化提升姿态估计稳定性。
- 实验或效果：在27个序列上评估，实现厘米级精度，仅用250KB地图数据，优于依赖点云地图的基线方法。

## 摘要（原文）

> Reliable localization is essential for sustainable forest management, as it allows robots or sensor systems to revisit and monitor the status of individual trees over long periods. In modern forestry, this management is structured around Digital Forest Inventories (DFIs), which encode stems using compact geometric attributes rather than raw data. Despite their central role, DFIs have been overlooked in localization research, and most methods still rely on dense gigabyte-sized point clouds that are costly to store and maintain. To improve upon this, we propose TreeLoc++, a global localization framework that operates directly on DFIs as a discriminative representation, eliminating the need to use the raw point clouds. TreeLoc++ reduces false matches in structurally ambiguous forests and improves the reliability of full 6-DoF pose estimation. It augments coarse retrieval with a pairwise distance histogram that encodes local tree-layout context, subsequently refining candidates via DBH-based filtering and yaw-consistent inlier selection to further reduce mismatches. Furthermore, a constrained optimization leveraging tree geometry jointly estimates roll, pitch, and height, enhancing pose stability and enabling accurate localization without reliance on dense 3D point cloud data. Evaluations on 27 sequences recorded in forests across three datasets and four countries show that TreeLoc++ achieves precise localization with centimeter-level accuracy. We further demonstrate robustness to long-term change by localizing data recorded in 2025 against inventories built from 2023 data, spanning a two-year interval. The system represents 15 sessions spanning 7.98 km of trajectories using only 250KB of map data and outperforms both hand-crafted and learning-based baselines that rely on point cloud maps. This demonstrates the scalability of TreeLoc++ for long-term deployment.

