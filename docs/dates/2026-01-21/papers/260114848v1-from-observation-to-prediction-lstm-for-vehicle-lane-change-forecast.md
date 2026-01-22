---
layout: default
title: From Observation to Prediction: LSTM for Vehicle Lane Change Forecasting on Highway On/Off-Ramps
---

# From Observation to Prediction: LSTM for Vehicle Lane Change Forecasting on Highway On/Off-Ramps
**arXiv**：[2601.14848v1](https://arxiv.org/abs/2601.14848) · [PDF](https://arxiv.org/pdf/2601.14848.pdf)  
**作者**：Mohamed Abouras, Catherine M. Elias  

**一句话要点**：提出多层LSTM架构，用于预测高速公路匝道区域车辆换道行为，提升道路安全。

**关键词**：车辆行为预测, LSTM模型, 高速公路匝道, 无人机数据集, 预测准确性

## 3 点简述
- 核心问题：高速公路匝道区域车辆行为预测，因交互变化大而研究不足。
- 方法要点：利用ExiD无人机数据集，训练多层LSTM模型，测试不同预测时间范围。
- 实验或效果：在4秒预测范围内，匝道区域准确率约76%，一般高速公路场景达94%。

## 摘要（原文）

> On and off-ramps are understudied road sections even though they introduce a higher level of variation in highway interactions. Predicting vehicles' behavior in these areas can decrease the impact of uncertainty and increase road safety. In this paper, the difference between this Area of Interest (AoI) and a straight highway section is studied. Multi-layered LSTM architecture to train the AoI model with ExiD drone dataset is utilized. In the process, different prediction horizons and different models' workflow are tested. The results show great promise on horizons up to 4 seconds with prediction accuracy starting from about 76% for the AoI and 94% for the general highway scenarios on the maximum horizon.

