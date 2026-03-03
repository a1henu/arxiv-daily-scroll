---
layout: default
title: D-GVIO: A Buffer-Driven and Efficient Decentralized GNSS-Visual-Inertial State Estimator for Multi-Agent Systems
---

# D-GVIO: A Buffer-Driven and Efficient Decentralized GNSS-Visual-Inertial State Estimator for Multi-Agent Systems
**arXiv**：[2603.01404v1](https://arxiv.org/abs/2603.01404) · [PDF](https://arxiv.org/pdf/2603.01404.pdf)  
**作者**：Yarong Luo, Wentao Lu, Chi Guo  

**一句话要点**：提出D-GVIO框架以解决多智能体系统中实时、鲁棒和高效的状态估计问题

**关键词**：多智能体系统, 分布式状态估计, GNSS-视觉-惯性里程计, 缓冲策略, 左不变扩展卡尔曼滤波, 鲁棒定位

## 3 点简述
- 核心问题：资源受限平台上的实时协同定位在鲁棒性和计算效率方面面临挑战
- 方法要点：采用协方差分割、缓冲策略和左不变扩展卡尔曼滤波实现高效分布式状态估计
- 实验或效果：通过缓冲驱动策略减少计算和通信负担，增强GNSS挑战环境下的鲁棒性

## 摘要（原文）

> Cooperative localization is essential for swarm applications like collaborative exploration and search-and-rescue missions. However, maintaining real-time capability, robustness, and computational efficiency on resource-constrained platforms presents significant challenges. To address these challenges, we propose D-GVIO, a buffer-driven and fully decentralized GNSS-Visual-Inertial Odometry (GVIO) framework that leverages a novel buffering strategy to support efficient and robust distributed state estimation. The proposed framework is characterized by four core mechanisms. Firstly, through covariance segmentation, covariance intersection and buffering strategy, we modularize propagation and update steps in distributed state estimation, significantly reducing computational and communication burdens. Secondly, the left-invariant extended Kalman filter (L-IEKF) is adopted for information fusion, which exhibits superior state estimation performance over the traditional extended Kalman filter (EKF) since its state transition matrix is independent of the system state. Thirdly, a buffer-based re-propagation strategy is employed to handle delayed measurements efficiently and accurately by leveraging the L-IEKF, eliminating the need for costly re-computation. Finally, an adaptive buffer-driven outlier detection method is proposed to dynamically cull GNSS outliers, enhancing robustness in GNSS-challenged environments.

