---
layout: default
title: Event-Only Drone Trajectory Forecasting with RPM-Modulated Kalman Filtering
---

# Event-Only Drone Trajectory Forecasting with RPM-Modulated Kalman Filtering
**arXiv**：[2603.01997v1](https://arxiv.org/abs/2603.01997) · [PDF](https://arxiv.org/pdf/2603.01997.pdf)  
**作者**：Hari Prasanth S. M., Pejman Habibiroudkenar, Eerik Alamikkotervo, Dimitrios Bouzoulas, Risto Ojala  

**一句话要点**：提出基于RPM调制卡尔曼滤波的事件相机无人机轨迹预测方法，利用螺旋桨运动线索提升精度。

**关键词**：事件相机, 无人机轨迹预测, 卡尔曼滤波, 螺旋桨转速, 短中期预测, 无训练数据

## 3 点简述
- 核心问题：事件相机在无人机轨迹预测中应用有限，需提升短中期预测精度。
- 方法要点：从原始事件数据提取螺旋桨转速，融入RPM感知卡尔曼滤波框架进行轨迹预测。
- 实验或效果：在FRED数据集上，优于学习方法和基础卡尔曼滤波，平均和最终距离误差更低。

## 摘要（原文）

> Event cameras provide high-temporal-resolution visual sensing that is well suited for observing fast-moving aerial objects; however, their use for drone trajectory prediction remains limited. This work introduces an event-only drone forecasting method that exploits propeller-induced motion cues. Propeller rotational speed are extracted directly from raw event data and fused within an RPM-aware Kalman filtering framework. Evaluations on the FRED dataset show that the proposed method outperforms learning-based approaches and vanilla kalman filter in terms of average distance error and final distance error at 0.4s and 0.8s forecasting horizons. The results demonstrate robust and accurate short- and medium-horizon trajectory forecasting without reliance on RGB imagery or training data.

