---
layout: default
title: Reformulating AI-based Multi-Object Relative State Estimation for Aleatoric Uncertainty-based Outlier Rejection of Partial Measurements
---

# Reformulating AI-based Multi-Object Relative State Estimation for Aleatoric Uncertainty-based Outlier Rejection of Partial Measurements
**arXiv**：[2602.02006v1](https://arxiv.org/abs/2602.02006) · [PDF](https://arxiv.org/pdf/2602.02006.pdf)  
**作者**：Thomas Jantos, Giulio Delama, Stephan Weiss, Jan Steinbrener  

**一句话要点**：提出基于AI的多目标相对状态估计新方法，通过重构测量方程和利用随机不确定性改进EKF性能。

**关键词**：多目标相对状态估计, 扩展卡尔曼滤波器, 随机不确定性, 异常值拒绝, 深度学习, 移动机器人定位

## 3 点简述
- 核心问题：AI测量在EKF融合中需量化不确定性和异常值拒绝能力。
- 方法要点：重构测量方程以解耦位置和旋转测量，支持部分测量拒绝。
- 实验或效果：用DNN预测的随机不确定性替换固定协方差矩阵，提升状态估计器性能与一致性。

## 摘要（原文）

> Precise localization with respect to a set of objects of interest enables mobile robots to perform various tasks. With the rise of edge devices capable of deploying deep neural networks (DNNs) for real-time inference, it stands to reason to use artificial intelligence (AI) for the extraction of object-specific, semantic information from raw image data, such as the object class and the relative six degrees of freedom (6-DoF) pose. However, fusing such AI-based measurements in an Extended Kalman Filter (EKF) requires quantifying the DNNs' uncertainty and outlier rejection capabilities.
>   This paper presents the benefits of reformulating the measurement equation in AI-based, object-relative state estimation. By deriving an EKF using the direct object-relative pose measurement, we can decouple the position and rotation measurements, thus limiting the influence of erroneous rotation measurements and allowing partial measurement rejection. Furthermore, we investigate the performance and consistency improvements for state estimators provided by replacing the fixed measurement covariance matrix of the 6-DoF object-relative pose measurements with the predicted aleatoric uncertainty of the DNN.

