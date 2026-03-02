---
layout: default
title: Interpretable Multimodal Gesture Recognition for Drone and Mobile Robot Teleoperation via Log-Likelihood Ratio Fusion
---

# Interpretable Multimodal Gesture Recognition for Drone and Mobile Robot Teleoperation via Log-Likelihood Ratio Fusion
**arXiv**：[2602.23694v1](https://arxiv.org/abs/2602.23694) · [PDF](https://arxiv.org/pdf/2602.23694.pdf)  
**作者**：Seungyeol Baek, Jaspreet Singh, Lala Shakti Swarup Ray, Hymalai Bello, Paul Lukowicz, Sungho Suh  

**一句话要点**：提出基于对数似然比融合的多模态手势识别框架，用于无人机和移动机器人遥操作，提升鲁棒性与可解释性。

**关键词**：多模态手势识别, 对数似然比融合, 无人机遥操作, 移动机器人控制, 传感器融合, 可解释性分析

## 3 点简述
- 核心问题：视觉手势识别在遮挡、光照变化和杂乱背景下性能下降，限制实际应用。
- 方法要点：融合手腕Apple Watch的惯性数据与定制手套的电容传感信号，采用对数似然比进行后期融合。
- 实验或效果：性能媲美先进视觉基线，显著降低计算成本、模型大小和训练时间，适合实时控制。

## 摘要（原文）

> Human operators are still frequently exposed to hazardous environments such as disaster zones and industrial facilities, where intuitive and reliable teleoperation of mobile robots and Unmanned Aerial Vehicles (UAVs) is essential. In this context, hands-free teleoperation enhances operator mobility and situational awareness, thereby improving safety in hazardous environments. While vision-based gesture recognition has been explored as one method for hands-free teleoperation, its performance often deteriorates under occlusions, lighting variations, and cluttered backgrounds, limiting its applicability in real-world operations. To overcome these limitations, we propose a multimodal gesture recognition framework that integrates inertial data (accelerometer, gyroscope, and orientation) from Apple Watches on both wrists with capacitive sensing signals from custom gloves. We design a late fusion strategy based on the log-likelihood ratio (LLR), which not only enhances recognition performance but also provides interpretability by quantifying modality-specific contributions. To support this research, we introduce a new dataset of 20 distinct gestures inspired by aircraft marshalling signals, comprising synchronized RGB video, IMU, and capacitive sensor data. Experimental results demonstrate that our framework achieves performance comparable to a state-of-the-art vision-based baseline while significantly reducing computational cost, model size, and training time, making it well suited for real-time robot control. We therefore underscore the potential of sensor-based multimodal fusion as a robust and interpretable solution for gesture-driven mobile robot and drone teleoperation.

