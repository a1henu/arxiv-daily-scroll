---
layout: default
title: AMO-HEAD: Adaptive MARG-Only Heading Estimation for UAVs under Magnetic Disturbances
---

# AMO-HEAD: Adaptive MARG-Only Heading Estimation for UAVs under Magnetic Disturbances
**arXiv**：[2510.10979v1](https://arxiv.org/abs/2510.10979) · [PDF](https://arxiv.org/pdf/2510.10979.pdf)  
**作者**：Qizhi Guo, Siyuan Yang, Junning Lyu, Jianjun Sun, Defu Lin, Shaoming He  

**一句话要点**：提出自适应MARG航向估计方法，解决无人机在磁干扰环境下的航向精度问题

**关键词**：航向估计, 扩展卡尔曼滤波, 磁干扰补偿, 无人机导航, 自适应算法

## 3 点简述
- 室内环境磁干扰严重，导致无人机航向估计精度下降
- 基于EKF框架，集成陀螺仪、加速度计和磁力计数据，自适应补偿噪声和磁干扰
- 真实环境实验验证，在磁干扰条件下提供精确航向估计

## 摘要（原文）

> Accurate and robust heading estimation is crucial for unmanned aerial
> vehicles (UAVs) when conducting indoor inspection tasks. However, the cluttered
> nature of indoor environments often introduces severe magnetic disturbances,
> which can significantly degrade heading accuracy. To address this challenge,
> this paper presents an Adaptive MARG-Only Heading (AMO-HEAD) estimation
> approach for UAVs operating in magnetically disturbed environments. AMO-HEAD is
> a lightweight and computationally efficient Extended Kalman Filter (EKF)
> framework that leverages inertial and magnetic sensors to achieve reliable
> heading estimation. In the proposed approach, gyroscope angular rate
> measurements are integrated to propagate the quaternion state, which is
> subsequently corrected using accelerometer and magnetometer data. The corrected
> quaternion is then used to compute the UAV's heading. An adaptive process noise
> covariance method is introduced to model and compensate for gyroscope
> measurement noise, bias drift, and discretization errors arising from the Euler
> method integration. To mitigate the effects of external magnetic disturbances,
> a scaling factor is applied based on real-time magnetic deviation detection. A
> theoretical observability analysis of the proposed AMO-HEAD is performed using
> the Lie derivative. Extensive experiments were conducted in real world indoor
> environments with customized UAV platforms. The results demonstrate the
> effectiveness of the proposed algorithm in providing precise heading estimation
> under magnetically disturbed conditions.

