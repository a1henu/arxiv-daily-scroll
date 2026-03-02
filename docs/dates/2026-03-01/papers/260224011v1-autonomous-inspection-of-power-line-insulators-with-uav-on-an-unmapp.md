---
layout: default
title: Autonomous Inspection of Power Line Insulators with UAV on an Unmapped Transmission Tower
---

# Autonomous Inspection of Power Line Insulators with UAV on an Unmapped Transmission Tower
**arXiv**：[2602.24011v1](https://arxiv.org/abs/2602.24011) · [PDF](https://arxiv.org/pdf/2602.24011.pdf)  
**作者**：Václav Riss, Vít Krátký, Robert Pěnička, Martin Saska  

**一句话要点**：提出基于相机-LiDAR融合的在线检测算法，实现无人机在未知输电塔上的自主绝缘子巡检。

**关键词**：无人机巡检, 传感器融合, 绝缘子检测, 在线定位, 输电塔维护

## 3 点简述
- 核心问题：无人机在无先验地图的输电塔上自主巡检绝缘子，需在线检测与定位。
- 方法要点：结合CNN检测绝缘子、LiDAR点云投影与DBSCAN/RANSAC/PCA定位算法。
- 实验或效果：仿真中单次飞行节省24%时间，真实实验定位误差约0.16米，方差显著降低。

## 摘要（原文）

> This paper introduces an online inspection algorithm that enables an autonomous UAV to fly around a transmission tower and obtain detailed inspection images without a prior map of the tower. Our algorithm relies on camera-LiDAR sensor fusion for online detection and localization of insulators. In particular, the algorithm is based on insulator detection using a convolutional neural network, projection of LiDAR points onto the image, and filtering them using the bounding boxes. The detection pipeline is coupled with several proposed insulator localization methods based on DBSCAN, RANSAC, and PCA algorithms. The performance of the proposed online inspection algorithm and camera-LiDAR sensor fusion pipeline is demonstrated through simulation and real-world flights. In simulation, we showed that our single-flight inspection strategy can save up to 24 % of total inspection time, compared to the two-flight strategy of scanning the tower and afterwards visiting the inspection waypoints in the optimal way. In a real-world experiment, the best performing proposed method achieves a mean horizontal and vertical localization error for the insulator of 0.16 +- 0.08 m and 0.16 +- 0.11 m, respectively. Compared to the most relevant approach, the proposed method achieves more than an order of magnitude lower variance in horizontal insulator localization error.

