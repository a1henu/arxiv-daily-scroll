---
layout: default
title: Fast Mining and Dynamic Time-to-Event Prediction over Multi-sensor Data Streams
---

# Fast Mining and Dynamic Time-to-Event Prediction over Multi-sensor Data Streams
**arXiv**：[2601.04741v1](https://arxiv.org/abs/2601.04741) · [PDF](https://arxiv.org/pdf/2601.04741.pdf)  
**作者**：Kota Nakamura, Koki Kawabata, Yasuko Matsubara, Yasushi Sakurai  

**一句话要点**：提出TimeCast动态预测框架，用于实时预测多传感器数据流中的机器故障时间

**关键词**：动态时间预测, 多传感器数据流, 在线学习, 机器故障预测, 实时分析

## 3 点简述
- 核心问题：如何基于实时多传感器数据流连续预测机器故障发生时间
- 方法要点：动态识别时间演化模式阶段，为每个阶段学习独立模型以适应变化
- 实验或效果：在真实数据集上，TimeCast比现有方法预测更准，计算时间大幅减少

## 摘要（原文）

> Given real-time sensor data streams obtained from machines, how can we continuously predict when a machine failure will occur? This work aims to continuously forecast the timing of future events by analyzing multi-sensor data streams. A key characteristic of real-world data streams is their dynamic nature, where the underlying patterns evolve over time. To address this, we present TimeCast, a dynamic prediction framework designed to adapt to these changes and provide accurate, real-time predictions of future event time. Our proposed method has the following properties: (a) Dynamic: it identifies the distinct time-evolving patterns (i.e., stages) and learns individual models for each, enabling us to make adaptive predictions based on pattern shifts. (b) Practical: it finds meaningful stages that capture time-varying interdependencies between multiple sensors and improve prediction performance; (c) Scalable: our algorithm scales linearly with the input size and enables online model updates on data streams. Extensive experiments on real datasets demonstrate that TimeCast provides higher prediction accuracy than state-of-the-art methods while finding dynamic changes in data streams with a great reduction in computational time.

