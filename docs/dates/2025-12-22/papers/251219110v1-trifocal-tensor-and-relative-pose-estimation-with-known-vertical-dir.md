---
layout: default
title: Trifocal Tensor and Relative Pose Estimation with Known Vertical Direction
---

# Trifocal Tensor and Relative Pose Estimation with Known Vertical Direction
**arXiv**：[2512.19110v1](https://arxiv.org/abs/2512.19110) · [PDF](https://arxiv.org/pdf/2512.19110.pdf)  
**作者**：Tao Li, Zhenbao Yu, Banglei Guan, Jianli Han, Weimin Lv, Friedrich Fraundorfer  

**一句话要点**：提出基于已知垂直方向的相对位姿估计方法，减少点对应需求以提高效率。

**关键词**：相对位姿估计, 三焦张量, 垂直方向约束, 最小解, 视觉里程计, RANSAC

## 3 点简述
- 核心问题：在已知相机垂直方向时，估计多视图间的相对位姿，减少未知参数。
- 方法要点：提供线性闭式解（需四点对应）和最小解（需三点对应），利用Gröbner基求解器。
- 实验或效果：在合成数据和KITTI真实场景测试中，位姿估计精度优于其他方法，适用于RANSAC框架。

## 摘要（原文）

> This work presents two novel solvers for estimating the relative poses among views with known vertical directions. The vertical directions of camera views can be easily obtained using inertial measurement units (IMUs) which have been widely used in autonomous vehicles, mobile phones, and unmanned aerial vehicles (UAVs). Given the known vertical directions, our lgorithms only need to solve for two rotation angles and two translation vectors. In this paper, a linear closed-form solution has been described, requiring only four point correspondences in three views. We also propose a minimal solution with three point correspondences using the latest Gröbner basis solver. Since the proposed methods require fewer point correspondences, they can be efficiently applied within the RANSAC framework for outliers removal and pose estimation in visual odometry. The proposed method has been tested on both synthetic data and real-world scenes from KITTI. The experimental results show that the accuracy of the estimated poses is superior to other alternative methods.

