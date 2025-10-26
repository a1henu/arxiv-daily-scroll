---
layout: default
title: Degradation-Aware Cooperative Multi-Modal GNSS-Denied Localization Leveraging LiDAR-Based Robot Detections
---

# Degradation-Aware Cooperative Multi-Modal GNSS-Denied Localization Leveraging LiDAR-Based Robot Detections
**arXiv**：[2510.20480v1](https://arxiv.org/abs/2510.20480) · [PDF](https://arxiv.org/pdf/2510.20480.pdf)  
**作者**：Václav Pritzl, Xianjia Yu, Tomi Westerlund, Petr Štěpán, Martin Saska  

**一句话要点**：提出自适应多模态多机器人协同定位方法，以应对GNSS缺失环境中的传感器退化问题。

**关键词**：多机器人协同定位, 多模态传感器融合, 因子图优化, 传感器退化处理, GNSS缺失环境

## 3 点简述
- 核心问题：多机器人系统中异步多模态数据融合困难，传感器退化影响定位精度。
- 方法要点：使用因子图融合VIO、LIO和机器人间检测，自适应加权以应对退化。
- 实验或效果：在真实UGV和UAV数据上验证，显著提升退化条件下的定位精度。

## 摘要（原文）

> Accurate long-term localization using onboard sensors is crucial for robots
> operating in Global Navigation Satellite System (GNSS)-denied environments.
> While complementary sensors mitigate individual degradations, carrying all the
> available sensor types on a single robot significantly increases the size,
> weight, and power demands. Distributing sensors across multiple robots enhances
> the deployability but introduces challenges in fusing asynchronous, multi-modal
> data from independently moving platforms. We propose a novel adaptive
> multi-modal multi-robot cooperative localization approach using a factor-graph
> formulation to fuse asynchronous Visual-Inertial Odometry (VIO), LiDAR-Inertial
> Odometry (LIO), and 3D inter-robot detections from distinct robots in a
> loosely-coupled fashion. The approach adapts to changing conditions, leveraging
> reliable data to assist robots affected by sensory degradations. A novel
> interpolation-based factor enables fusion of the unsynchronized measurements.
> LIO degradations are evaluated based on the approximate scan-matching Hessian.
> A novel approach of weighting odometry data proportionally to the Wasserstein
> distance between the consecutive VIO outputs is proposed. A theoretical
> analysis is provided, investigating the cooperative localization problem under
> various conditions, mainly in the presence of sensory degradations. The
> proposed method has been extensively evaluated on real-world data gathered with
> heterogeneous teams of an Unmanned Ground Vehicle (UGV) and Unmanned Aerial
> Vehicles (UAVs), showing that the approach provides significant improvements in
> localization accuracy in the presence of various sensory degradations.

