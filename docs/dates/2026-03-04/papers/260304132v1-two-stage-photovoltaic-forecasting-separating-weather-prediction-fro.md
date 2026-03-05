---
layout: default
title: Two-Stage Photovoltaic Forecasting: Separating Weather Prediction from Plant-Characteristics
---

# Two-Stage Photovoltaic Forecasting: Separating Weather Prediction from Plant-Characteristics
**arXiv**：[2603.04132v1](https://arxiv.org/abs/2603.04132) · [PDF](https://arxiv.org/pdf/2603.04132.pdf)  
**作者**：Philipp Danner, Hermann de Meer  

**一句话要点**：提出两阶段光伏预测方法，分离天气预测与电站特性建模以提升预测精度

**关键词**：光伏预测, 两阶段建模, 天气预测误差, 电站特性, 误差分布拟合, 神经网络集成

## 3 点简述
- 核心问题：光伏预测误差分布细节缺失，且未分析天气预测误差来源。
- 方法要点：分解为天气预测模型和电站特性模型，使用卫星观测作为中间层。
- 实验或效果：使用天气预测时误差增加，广义双曲分布和t分布能拟合误差。

## 摘要（原文）

> Several energy management applications rely on accurate photovoltaic generation forecasts. Common metrics like mean absolute error or root-mean-square error, omit error-distribution details needed for stochastic optimization. In addition, several approaches use weather forecasts as inputs without analyzing the source of the prediction error. To overcome this gap, we decompose forecasting into a weather forecast model for environmental parameters such as solar irradiance and temperature and a plant characteristic model that captures site-specific parameters like panel orientation, temperature influence, or regular shading. Satellite-based weather observation serves as an intermediate layer. We analyze the error distribution of the high-resolution rapid-refresh numerical weather prediction model that covers the United States as a black-box model for weather forecasting and train an ensemble of neural networks on historical power output data for the plant characteristic model. Results show mean absolute error increases by 11% and 68% for two selected photovoltaic systems when using weather forecasts instead of satellite-based ground-truth weather observations as a perfect forecast. The generalized hyperbolic and Student's t distributions adequately fit the forecast errors across lead times.

