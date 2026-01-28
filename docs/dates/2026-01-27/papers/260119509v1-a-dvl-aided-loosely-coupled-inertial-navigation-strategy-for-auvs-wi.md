---
layout: default
title: A DVL Aided Loosely Coupled Inertial Navigation Strategy for AUVs with Attitude Error Modeling and Variance Propagation
---

# A DVL Aided Loosely Coupled Inertial Navigation Strategy for AUVs with Attitude Error Modeling and Variance Propagation
**arXiv**：[2601.19509v1](https://arxiv.org/abs/2601.19509) · [PDF](https://arxiv.org/pdf/2601.19509.pdf)  
**作者**：Jin Huang, Zichen Liu, Haoda Li, Zhikun Wang, Ying Chen  

**一句话要点**：提出姿态误差建模与方差传播的DVL辅助松耦合惯性导航策略，以解决AUV长期导航中姿态误差累积导致的性能下降问题。

**关键词**：水下导航, 惯性导航系统, 多普勒速度计, 姿态误差建模, 方差传播, 自主水下航行器

## 3 点简述
- 核心问题：传统SINS/DVL松耦合架构中，姿态估计误差累积导致速度投影偏差，影响长期导航精度。
- 方法要点：引入姿态误差感知的DVL速度变换模型和基于协方差矩阵的方差传播方法，补偿投影偏差并实现统计一致的噪声建模。
- 实验或效果：仿真与现场实验显示，联合应用改进后，3D位置RMSE提升78.3%，最大分量位置误差减少71.8%，有效抑制长期误差发散。

## 摘要（原文）

> In underwater navigation systems, strap-down inertial navigation system/Doppler velocity log (SINS/DVL)-based loosely coupled architectures are widely adopted. Conventional approaches project DVL velocities from the body coordinate system to the navigation coordinate system using SINS-derived attitude; however, accumulated attitude estimation errors introduce biases into velocity projection and degrade navigation performance during long-term operation. To address this issue, two complementary improvements are introduced. First, a vehicle attitude error-aware DVL velocity transformation model is formulated by incorporating attitude error terms into the observation equation to reduce projection-induced velocity bias. Second, a covariance matrix-based variance propagation method is developed to transform DVL measurement uncertainty across coordinate systems, introducing an expectation-based attitude error compensation term to achieve statistically consistent noise modeling. Simulation and field experiment results demonstrate that both improvements individually enhance navigation accuracy and confirm that accumulated attitude errors affect both projected velocity measurements and their associated uncertainty. When jointly applied, long-term error divergence is effectively suppressed. Field experimental results show that the proposed approach achieves a 78.3% improvement in 3D position RMSE and a 71.8% reduction in the maximum component-wise position error compared with the baseline IMU+DVL method, providing a robust solution for improving long-term SINS/DVL navigation performance.

