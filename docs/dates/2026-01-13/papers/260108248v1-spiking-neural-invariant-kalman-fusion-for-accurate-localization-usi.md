---
layout: default
title: Spiking Neural-Invariant Kalman Fusion for Accurate Localization Using Low-Cost IMUs
---

# Spiking Neural-Invariant Kalman Fusion for Accurate Localization Using Low-Cost IMUs
**arXiv**：[2601.08248v1](https://arxiv.org/abs/2601.08248) · [PDF](https://arxiv.org/pdf/2601.08248.pdf)  
**作者**：Yaohua Liu, Qiao Xu, Yemin Wang, Hui Yi Leong, Binkai Ou  

**一句话要点**：提出融合脉冲神经网络与不变扩展卡尔曼滤波的框架，以提升低成本IMU在移动机器人定位中的精度与鲁棒性。

**关键词**：脉冲神经网络, 不变扩展卡尔曼滤波, 低成本IMU, 移动机器人定位, 噪声自适应

## 3 点简述
- 核心问题：低成本IMU噪声复杂非线性，直接用于航位推算导致定位精度显著下降。
- 方法要点：设计脉冲神经网络从噪声IMU数据提取运动特征，动态调整不变扩展卡尔曼滤波的协方差噪声参数。
- 实验或效果：在KITTI数据集和真实移动机器人数据上验证，定位精度优于现有方法，对传感器噪声鲁棒性强。

## 摘要（原文）

> Low-cost inertial measurement units (IMUs) are widely utilized in mobile robot localization due to their affordability and ease of integration. However, their complex, nonlinear, and time-varying noise characteristics often lead to significant degradation in localization accuracy when applied directly for dead reckoning. To overcome this limitation, we propose a novel brain-inspired state estimation framework that combines a spiking neural network (SNN) with an invariant extended Kalman filter (InEKF). The SNN is designed to extract motion-related features from long sequences of IMU data affected by substantial random noise and is trained via a surrogate gradient descent algorithm to enable dynamic adaptation of the covariance noise parameter within the InEKF. By fusing the SNN output with raw IMU measurements, the proposed method enhances the robustness and accuracy of pose estimation. Extensive experiments conducted on the KITTI dataset and real-world data collected using a mobile robot equipped with a low-cost IMU demonstrate that the proposed approach outperforms state-of-the-art methods in localization accuracy and exhibits strong robustness to sensor noise, highlighting its potential for real-world mobile robot applications.

