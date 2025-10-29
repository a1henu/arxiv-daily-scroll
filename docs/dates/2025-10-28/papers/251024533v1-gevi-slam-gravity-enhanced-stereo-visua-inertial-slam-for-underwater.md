---
layout: default
title: GeVI-SLAM: Gravity-Enhanced Stereo Visua Inertial SLAM for Underwater Robots
---

# GeVI-SLAM: Gravity-Enhanced Stereo Visua Inertial SLAM for Underwater Robots
**arXiv**：[2510.24533v1](https://arxiv.org/abs/2510.24533) · [PDF](https://arxiv.org/pdf/2510.24533.pdf)  
**作者**：Yuan Shen, Yuze Hong, Guangyang Zeng, Tengfei Zhang, Pui Yi Chui, Ziyang Hong, Junfeng Wu  

**一句话要点**：提出GeVI-SLAM以解决水下机器人视觉惯性SLAM的精度和稳定性问题

**关键词**：水下机器人SLAM, 视觉惯性SLAM, 重力增强, 立体相机, PnP优化, IMU初始化

## 3 点简述
- 核心问题：水下机器人视觉退化和IMU运动激励不足导致SLAM精度低
- 方法要点：利用立体相机深度估计和重力初始化，减少自由度并优化姿态跟踪
- 实验或效果：在模拟和真实数据中，相比先进方法，精度和稳定性更高

## 摘要（原文）

> Accurate visual inertial simultaneous localization and mapping (VI SLAM) for
> underwater robots remains a significant challenge due to frequent visual
> degeneracy and insufficient inertial measurement unit (IMU) motion excitation.
> In this paper, we present GeVI-SLAM, a gravity-enhanced stereo VI SLAM system
> designed to address these issues. By leveraging the stereo camera's direct
> depth estimation ability, we eliminate the need to estimate scale during IMU
> initialization, enabling stable operation even under low acceleration dynamics.
> With precise gravity initialization, we decouple the pitch and roll from the
> pose estimation and solve a 4 degrees of freedom (DOF) Perspective-n-Point
> (PnP) problem for pose tracking. This allows the use of a minimal 3-point
> solver, which significantly reduces computational time to reject outliers
> within a Random Sample Consensus framework. We further propose a
> bias-eliminated 4-DOF PnP estimator with provable consistency, ensuring the
> relative pose converges to the true value as the feature number increases. To
> handle dynamic motion, we refine the full 6-DOF pose while jointly estimating
> the IMU covariance, enabling adaptive weighting of the gravity prior. Extensive
> experiments on simulated and real-world data demonstrate that GeVI-SLAM
> achieves higher accuracy and greater stability compared to state-of-the-art
> methods.

