---
layout: default
title: A2VISR: An Active and Adaptive Ground-Aerial Localization System Using Visual Inertial and Single-Range Fusion
---

# A2VISR: An Active and Adaptive Ground-Aerial Localization System Using Visual Inertial and Single-Range Fusion
**arXiv**：[2512.16367v1](https://arxiv.org/abs/2512.16367) · [PDF](https://arxiv.org/pdf/2512.16367.pdf)  
**作者**：Sijia Chen, Wei Dong  

**一句话要点**：提出A2VISR系统，通过主动自适应视觉惯性单距融合增强杂乱环境中飞行机器人定位鲁棒性

**关键词**：地面-空中协作定位, 主动视觉系统, 多传感器融合, 自适应估计, 视觉惯性里程计, 单距测距

## 3 点简述
- 核心问题：传统固定相机定位方法在视觉退化时距离受限且易捕获失败，影响飞行机器人定位。
- 方法要点：集成主动视觉、单距测距、惯性里程计和光流，采用降维估计器和自适应置信度评估算法融合多源测量。
- 实验或效果：在烟雾、光照变化等条件下，平均定位误差约0.09米，保持对捕获丢失和传感器故障的鲁棒性。

## 摘要（原文）

> It's a practical approach using the ground-aerial collaborative system to enhance the localization robustness of flying robots in cluttered environments, especially when visual sensors degrade. Conventional approaches estimate the flying robot's position using fixed cameras observing pre-attached markers, which could be constrained by limited distance and susceptible to capture failure. To address this issue, we improve the ground-aerial localization framework in a more comprehensive manner, which integrates active vision, single-ranging, inertial odometry, and optical flow. First, the designed active vision subsystem mounted on the ground vehicle can be dynamically rotated to detect and track infrared markers on the aerial robot, improving the field of view and the target recognition with a single camera. Meanwhile, the incorporation of single-ranging extends the feasible distance and enhances re-capture capability under visual degradation. During estimation, a dimension-reduced estimator fuses multi-source measurements based on polynomial approximation with an extended sliding window, balancing computational efficiency and redundancy. Considering different sensor fidelities, an adaptive sliding confidence evaluation algorithm is implemented to assess measurement quality and dynamically adjust the weighting parameters based on moving variance. Finally, extensive experiments under conditions such as smoke interference, illumination variation, obstacle occlusion, prolonged visual loss, and extended operating range demonstrate that the proposed approach achieves robust online localization, with an average root mean square error of approximately 0.09 m, while maintaining resilience to capture loss and sensor failures.

