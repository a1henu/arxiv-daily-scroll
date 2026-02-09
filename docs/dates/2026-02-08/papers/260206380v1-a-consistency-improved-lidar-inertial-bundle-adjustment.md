---
layout: default
title: A Consistency-Improved LiDAR-Inertial Bundle Adjustment
---

# A Consistency-Improved LiDAR-Inertial Bundle Adjustment
**arXiv**：[2602.06380v1](https://arxiv.org/abs/2602.06380) · [PDF](https://arxiv.org/pdf/2602.06380.pdf)  
**作者**：Xinran Li, Shuaikang Zheng, Pengcheng Zheng, Xinyang Wang, Jiacheng Li, Zhitian Li, Xudong Zou  

**一句话要点**：提出一致性改进的激光雷达-惯性束调整方法，以解决特征参数化与协方差估计不一致问题。

**关键词**：激光雷达-惯性SLAM, 束调整, 一致性估计, 特征参数化, 立体投影表示

## 3 点简述
- 核心问题：基于特征的SLAM系统存在特征参数化与估计协方差不一致，影响定位精度。
- 方法要点：采用立体投影表示参数化平面和边缘特征，结合MAP和FEJ实现一致性估计。
- 实验或效果：应用于激光雷达-惯性里程计，未知具体性能提升。

## 摘要（原文）

> Simultaneous Localization and Mapping (SLAM) using 3D LiDAR has emerged as a cornerstone for autonomous navigation in robotics. While feature-based SLAM systems have achieved impressive results by leveraging edge and planar structures, they often suffer from the inconsistent estimator associated with feature parameterization and estimated covariance. In this work, we present a consistency-improved LiDAR-inertial bundle adjustment (BA) with tailored parameterization and estimator. First, we propose a stereographic-projection representation parameterizing the planar and edge features, and conduct a comprehensive observability analysis to support its integrability with consistent estimator. Second, we implement a LiDAR-inertial BA with Maximum a Posteriori (MAP) formulation and First-Estimate Jacobians (FEJ) to preserve the accurate estimated covariance and observability properties of the system. Last, we apply our proposed BA method to a LiDAR-inertial odometry.

