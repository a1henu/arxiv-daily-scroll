---
layout: default
title: Security Risks in Machining Process Monitoring: Sequence-to-Sequence Learning for Reconstruction of CNC Axis Positions
---

# Security Risks in Machining Process Monitoring: Sequence-to-Sequence Learning for Reconstruction of CNC Axis Positions
**arXiv**：[2603.01702v1](https://arxiv.org/abs/2603.01702) · [PDF](https://arxiv.org/pdf/2603.01702.pdf)  
**作者**：Lukas Krupp, Rickmar Stahlschmidt, Norbert Wehn  

**一句话要点**：提出基于序列到序列学习的CNC轴位置重建方法，以解决加速度计监控数据的安全风险问题。

**关键词**：CNC位置重建, 序列到序列学习, 加速度计监控, 安全风险, 工业机器学习

## 3 点简述
- 核心问题：加速度计监控数据可能泄露CNC机床运动信息，构成安全威胁，传统信号处理方法因噪声和传感器非理想性难以重建位置。
- 方法要点：采用LSTM序列到序列模型，从工业铣削数据中学习并重建轴和刀具位置，克服非理想性影响。
- 实验或效果：相比双积分法，重建误差降低高达98%（简单运动）和85%（复杂序列），保留轨迹几何特征。

## 摘要（原文）

> Accelerometer-based process monitoring is widely deployed in modern machining systems. When mounted on moving machine components, such sensors implicitly capture kinematic information related to machine motion and tool trajectories. If this information can be reconstructed, condition monitoring data constitutes a severe security threat, particularly for retrofitted or weakly protected sensor systems. Classical signal processing approaches are infeasible for position reconstruction from broadband accelerometer signals due to sensor- and process-specific non-idealities, like noise or sensor placement effects. In this work, we demonstrate that sequence-to-sequence machine learning models can overcome these non-idealities and enable reconstruction of CNC axis and tool positions. Our approach employs LSTM-based sequence-to-sequence models and is evaluated on an industrial milling dataset. We show that learning-based models reduce the reconstruction error by up to 98% for low complexity motion profiles and by up to 85% for complex machining sequences compared to double integration. Furthermore, key geometric characteristics of tool trajectories and workpiece-related motion features are preserved. To the best of our knowledge, this is the first study demonstrating learning-based CNC position reconstruction from industrial condition monitoring accelerometer data.

