---
layout: default
title: Orientation-Free Neural Network-Based Bias Estimation for Low-Cost Stationary Accelerometers
---

# Orientation-Free Neural Network-Based Bias Estimation for Low-Cost Stationary Accelerometers
**arXiv**：[2511.13071v1](https://arxiv.org/abs/2511.13071) · [PDF](https://arxiv.org/pdf/2511.13071.pdf)  
**作者**：Michal Levin, Itzik Klein  

**一句话要点**：提出基于神经网络的校准方法以解决低成本加速度计在静止条件下的偏差估计问题

**关键词**：加速度计校准, 神经网络方法, 偏差估计, 静止条件, 低成本传感器

## 3 点简述
- 核心问题：低成本加速度计偏差误差影响性能，传统校准需传感器水平或复杂定向过程
- 方法要点：使用无模型学习方法估计偏差，无需传感器定向或旋转
- 实验或效果：在13.39小时数据集上验证，误差比传统方法降低超52%

## 摘要（原文）

> Low-cost micro-electromechanical accelerometers are widely used in navigation, robotics, and consumer devices for motion sensing and position estimation. However, their performance is often degraded by bias errors. To eliminate deterministic bias terms a calibration procedure is applied under stationary conditions. It requires accelerom- eter leveling or complex orientation-dependent calibration procedures. To overcome those requirements, in this paper we present a model-free learning-based calibration method that estimates accelerometer bias under stationary conditions, without requiring knowledge of the sensor orientation and without the need to rotate the sensors. The proposed approach provides a fast, practical, and scalable solution suitable for rapid field deployment. Experimental validation on a 13.39-hour dataset collected from six accelerometers shows that the proposed method consistently achieves error levels more than 52% lower than traditional techniques. On a broader scale, this work contributes to the advancement of accurate calibration methods in orientation-free scenarios. As a consequence, it improves the reliability of low-cost inertial sensors in diverse scientific and industrial applications and eliminates the need for leveled calibration.

