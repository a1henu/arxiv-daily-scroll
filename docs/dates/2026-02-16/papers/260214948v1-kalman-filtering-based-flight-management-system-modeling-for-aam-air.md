---
layout: default
title: Kalman Filtering Based Flight Management System Modeling for AAM Aircraft
---

# Kalman Filtering Based Flight Management System Modeling for AAM Aircraft
**arXiv**：[2602.14948v1](https://arxiv.org/abs/2602.14948) · [PDF](https://arxiv.org/pdf/2602.14948.pdf)  
**作者**：Balram Kandoria, Aryaman Singh Samyal  

**一句话要点**：提出基于卡尔曼滤波的AAM飞行管理系统建模方法，以解决飞行计划验证中的不确定性传播问题。

**关键词**：卡尔曼滤波, 高级空中机动性, 飞行管理系统, 不确定性传播, ADS-B数据, 飞行计划验证

## 3 点简述
- 核心问题：AAM飞行计划验证需处理时空不确定性，现有方法依赖保守线性模型，缺乏自适应能力。
- 方法要点：使用sigmoid混合测量噪声协方差建模FMS架构，基于航点进度动态调整测量信任度，实现自然校正行为。
- 实验或效果：基于真实ADS-B数据验证，训练集调参后在验证集上达到76%的到达时间预测准确率。

## 摘要（原文）

> Advanced Aerial Mobility (AAM) operations require strategic flight planning services that predict both spatial and temporal uncertainties to safely validate flight plans against hazards such as weather cells, restricted airspaces, and CNS disruption areas. Current uncertainty estimation methods for AAM vehicles rely on conservative linear models due to limited real-world performance data. This paper presents a novel Kalman Filter-based uncertainty propagation method that models AAM Flight Management System (FMS) architectures through sigmoid-blended measurement noise covariance. Unlike existing approaches with fixed uncertainty thresholds, our method continuously adapts the filter's measurement trust based on progress toward waypoints, enabling FMS correction behavior to emerge naturally. The approach scales proportionally with control inputs and is tunable to match specific aircraft characteristics or route conditions. We validate the method using real ADS-B data from general aviation aircraft divided into training and verification sets. Uncertainty propagation parameters were tuned on the training set, achieving 76% accuracy in predicting arrival times when compared against the verification dataset, demonstrating the method's effectiveness for strategic flight plan validation in AAM operations.

