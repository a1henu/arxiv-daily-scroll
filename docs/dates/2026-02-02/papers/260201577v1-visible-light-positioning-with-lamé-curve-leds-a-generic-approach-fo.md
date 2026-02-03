---
layout: default
title: Visible Light Positioning With Lamé Curve LEDs: A Generic Approach for Camera Pose Estimation
---

# Visible Light Positioning With Lamé Curve LEDs: A Generic Approach for Camera Pose Estimation
**arXiv**：[2602.01577v1](https://arxiv.org/abs/2602.01577) · [PDF](https://arxiv.org/pdf/2602.01577.pdf)  
**作者**：Wenxuan Pan, Yang Yang, Dong Wei, Zhiyu Zhu, Jintao Wang, Huan Wu, Yao Nie  

**一句话要点**：提出基于Lamé曲线LED的通用可见光定位算法，解决异构LED形状场景下的相机姿态估计问题。

**关键词**：可见光定位, 相机姿态估计, Lamé曲线, 非线性最小二乘, 免对应点PnP

## 3 点简述
- 核心问题：现有基于LED形状的可见光定位方法受限于单一几何形状，在异构LED形状场景中失效。
- 方法要点：利用Lamé曲线统一表示常见LED形状，通过非线性最小二乘和免对应点PnP算法实现相机姿态估计。
- 实验或效果：仿真和实验验证，位置误差降低超40%，平均定位精度小于4厘米。

## 摘要（原文）

> Camera-based visible light positioning (VLP) is a promising technique for accurate and low-cost indoor camera pose estimation (CPE). To reduce the number of required light-emitting diodes (LEDs), advanced methods commonly exploit LED shape features for positioning. Although interesting, they are typically restricted to a single LED geometry, leading to failure in heterogeneous LED-shape scenarios. To address this challenge, this paper investigates Lamé curves as a unified representation of common LED shapes and proposes a generic VLP algorithm using Lamé curve-shaped LEDs, termed LC-VLP. In the considered system, multiple ceiling-mounted Lamé curve-shaped LEDs periodically broadcast their curve parameters via visible light communication, which are captured by a camera-equipped receiver. Based on the received LED images and curve parameters, the receiver can estimate the camera pose using LC-VLP. Specifically, an LED database is constructed offline to store the curve parameters, while online positioning is formulated as a nonlinear least-squares problem and solved iteratively. To provide a reliable initialization, a correspondence-free perspective-\textit{n}-points (FreeP\textit{n}P) algorithm is further developed, enabling approximate CPE without any pre-calibrated reference points. The performance of LC-VLP is verified by both simulations and experiments. Simulations show that LC-VLP outperforms state-of-the-art methods in both circular- and rectangular-LED scenarios, achieving reductions of over 40% in position error and 25% in rotation error. Experiments further show that LC-VLP can achieve an average position accuracy of less than 4 cm.

