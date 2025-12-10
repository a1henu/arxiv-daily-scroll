---
layout: default
title: RLCNet: An end-to-end deep learning framework for simultaneous online calibration of LiDAR, RADAR, and Camera
---

# RLCNet: An end-to-end deep learning framework for simultaneous online calibration of LiDAR, RADAR, and Camera
**arXiv**：[2512.08262v1](https://arxiv.org/abs/2512.08262) · [PDF](https://arxiv.org/pdf/2512.08262.pdf)  
**作者**：Hafeez Husain Cholakkal, Stefano Arrigoni, Francesco Braghin  

**一句话要点**：提出RLCNet端到端深度学习框架，用于自动驾驶中LiDAR、RADAR和相机的同步在线校准。

**关键词**：多模态传感器校准, 在线校准, 深度学习框架, 自动驾驶感知, 端到端训练, 鲁棒性优化

## 3 点简述
- 核心问题：动态环境下传感器外参校准因机械振动和漂移而困难，影响自动驾驶感知可靠性。
- 方法要点：设计端到端可训练框架，结合加权移动平均和异常值剔除，实现实时在线校准和参数动态调整。
- 实验或效果：在真实数据集验证，展示优于现有方法的精度和鲁棒性，支持实际部署。

## 摘要（原文）

> Accurate extrinsic calibration of LiDAR, RADAR, and camera sensors is essential for reliable perception in autonomous vehicles. Still, it remains challenging due to factors such as mechanical vibrations and cumulative sensor drift in dynamic environments. This paper presents RLCNet, a novel end-to-end trainable deep learning framework for the simultaneous online calibration of these multimodal sensors. Validated on real-world datasets, RLCNet is designed for practical deployment and demonstrates robust performance under diverse conditions. To support real-time operation, an online calibration framework is introduced that incorporates a weighted moving average and outlier rejection, enabling dynamic adjustment of calibration parameters with reduced prediction noise and improved resilience to drift. An ablation study highlights the significance of architectural choices, while comparisons with existing methods demonstrate the superior accuracy and robustness of the proposed approach.

