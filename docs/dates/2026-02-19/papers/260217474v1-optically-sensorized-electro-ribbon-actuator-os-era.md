---
layout: default
title: Optically Sensorized Electro-Ribbon Actuator (OS-ERA)
---

# Optically Sensorized Electro-Ribbon Actuator (OS-ERA)
**arXiv**：[2602.17474v1](https://arxiv.org/abs/2602.17474) · [PDF](https://arxiv.org/pdf/2602.17474.pdf)  
**作者**：Carolina Gay, Petr Trunin, Diana Cafiso, Yuejun Xu, Majid Taghavi, Lucia Beccai  

**一句话要点**：提出光学传感电带致动器以解决电带致动器传感精度不足的问题，实现高保真弯曲状态分类。

**关键词**：电带致动器, 光学传感, 软波导传感器, 弯曲状态分类, 闭环控制, 电压速度不变性

## 3 点简述
- 电带致动器传感依赖电容传感器，精度有限，阻碍精确控制。
- 设计并嵌入两个软光学波导传感器，分析运动中的复杂曲率，训练分类器映射信号区分八种弯曲状态。
- 验证模型显示信号轨迹保持形状，分类准确，具有电压和速度不变性，支持闭环控制。

## 摘要（原文）

> Electro-Ribbon Actuators (ERAs) are lightweight flexural actuators that exhibit ultrahigh displacement and fast movement. However, their embedded sensing relies on capacitive sensors with limited precision, which hinders accurate control. We introduce OS-ERA, an optically sensorized ERA that yields reliable proprioceptive information, and we focus on the design and integration of a sensing solution without affecting actuation. To analyse the complex curvature of an ERA in motion, we design and embed two soft optical waveguide sensors. A classifier is trained to map the sensing signals in order to distinguish eight bending states. We validate our model on six held-out trials and compare it against signals' trajectories learned from training runs. Across all tests, the sensing output signals follow the training manifold, and the predicted sequence mirrors real performance and confirms repeatability. Despite deliberate train-test mismatches in actuation speed, the signal trajectories preserve their shape, and classification remains consistently accurate, demonstrating practical voltage- and speed-invariance. As a result, OS-ERA classifies bending states with high fidelity; it is fast and repeatable, solving a longstanding bottleneck of the ERA, enabling steps toward closed-loop control.

