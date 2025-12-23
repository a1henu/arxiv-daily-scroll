---
layout: default
title: LIMOncello: Revisited IKFoM on the SGal(3) Manifold for Fast LiDAR-Inertial Odometry
---

# LIMOncello: Revisited IKFoM on the SGal(3) Manifold for Fast LiDAR-Inertial Odometry
**arXiv**：[2512.19567v1](https://arxiv.org/abs/2512.19567) · [PDF](https://arxiv.org/pdf/2512.19567.pdf)  
**作者**：Carlos Pérez-Ruiz, Joan Solà  

**一句话要点**：提出LIMOncello，在SGal(3)流形上建模6-DoF运动，用于快速激光雷达-惯性里程计。

**关键词**：激光雷达-惯性里程计, SGal(3)流形, 迭代卡尔曼滤波, 增量八叉树映射, 实时定位, 开源实现

## 3 点简述
- 核心问题：在低可观测条件下，传统状态表示（如SO(3)×ℝ⁶）可能导致漂移和数值不稳定。
- 方法要点：使用SGal(3)流形提供一致且数值稳定的离散时间传播模型，结合迭代误差状态卡尔曼滤波后端。
- 实验或效果：在真实数据集上实现竞争性精度，提高几何稀疏环境下的鲁棒性，保持实时性能和稳定内存增长。

## 摘要（原文）

> This work introduces LIMOncello, a tightly coupled LiDAR-Inertial Odometry system that models 6-DoF motion on the $\mathrm{SGal}(3)$ manifold within an iterated error-state Kalman filter backend. Compared to state representations defined on $\mathrm{SO}(3)\times\mathbb{R}^6$, the use of $\mathrm{SGal}(3)$ provides a coherent and numerically stable discrete-time propagation model that helps limit drift in low-observability conditions.
>   LIMOncello also includes a lightweight incremental i-Octree mapping backend that enables faster updates and substantially lower memory usage than incremental kd-tree style map structures, without relying on locality-restricted search heuristics. Experiments on multiple real-world datasets show that LIMOncello achieves competitive accuracy while improving robustness in geometrically sparse environments. The system maintains real-time performance with stable memory growth and is released as an extensible open-source implementation at https://github.com/CPerezRuiz335/LIMOncello.

