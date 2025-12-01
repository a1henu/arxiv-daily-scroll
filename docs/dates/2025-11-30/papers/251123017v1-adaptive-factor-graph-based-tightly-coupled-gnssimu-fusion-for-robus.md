---
layout: default
title: Adaptive Factor Graph-Based Tightly Coupled GNSS/IMU Fusion for Robust Positionin
---

# Adaptive Factor Graph-Based Tightly Coupled GNSS/IMU Fusion for Robust Positionin
**arXiv**：[2511.23017v1](https://arxiv.org/abs/2511.23017) · [PDF](https://arxiv.org/pdf/2511.23017.pdf)  
**作者**：Elham Ahmadi, Alireza Olama, Petri Välisuo, Heidi Kuusniemi  

**一句话要点**：提出自适应因子图紧耦合GNSS/IMU融合框架，以增强城市峡谷等GNSS挑战环境中的定位鲁棒性。

**关键词**：GNSS/IMU融合, 因子图优化, 鲁棒定位, Barron损失函数, 城市导航

## 3 点简述
- 核心问题：GNSS挑战环境中，紧耦合GNSS/IMU融合易受非高斯噪声和异常值影响，定位可靠性不足。
- 方法要点：基于因子图框架，直接集成GNSS伪距测量与IMU预积分因子，并引入Barron损失函数自适应加权不可靠GNSS测量。
- 实验或效果：在UrbanNav数据集上评估，相比标准FGO定位误差减少达41%，在EKF基线上改进更显著。

## 摘要（原文）

> Reliable positioning in GNSS-challenged environments remains a critical challenge for navigation systems. Tightly coupled GNSS/IMU fusion improves robustness but remains vulnerable to non-Gaussian noise and outliers. We present a robust and adaptive factor graph-based fusion framework that directly integrates GNSS pseudorange measurements with IMU preintegration factors and incorporates the Barron loss, a general robust loss function that unifies several m-estimators through a single tunable parameter. By adaptively down weighting unreliable GNSS measurements, our approach improves resilience positioning. The method is implemented in an extended GTSAM framework and evaluated on the UrbanNav dataset. The proposed solution reduces positioning errors by up to 41% relative to standard FGO, and achieves even larger improvements over extended Kalman filter (EKF) baselines in urban canyon environments. These results highlight the benefits of Barron loss in enhancing the resilience of GNSS/IMU-based navigation in urban and signal-compromised environments.

