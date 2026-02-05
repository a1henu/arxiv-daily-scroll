---
layout: default
title: Turning mechanistic models into forecasters by using machine learning
---

# Turning mechanistic models into forecasters by using machine learning
**arXiv**：[2602.04114v1](https://arxiv.org/abs/2602.04114) · [PDF](https://arxiv.org/pdf/2602.04114.pdf)  
**作者**：Amit K. Chakraborty, Hao Wang, Pouria Ramazi  

**一句话要点**：提出时变参数数据驱动方程发现框架，以提升复杂动态系统建模与预测性能

**关键词**：数据驱动方程发现, 时变参数建模, 动态系统预测, 机器学习集成, 时间序列分析

## 3 点简述
- 核心问题：传统数据驱动方法假设参数恒定，难以捕捉动态系统的时间演化特性
- 方法要点：允许参数随时间变化，从数据中学习时变参数并推断含常量和时变参数的系统方程
- 实验或效果：在多个数据集上验证，建模误差低于3%，预测误差低于6%，优于CNN-LSTM和GBM

## 摘要（原文）

> The equations of complex dynamical systems may not be identified by expert knowledge, especially if the underlying mechanisms are unknown. Data-driven discovery methods address this challenge by inferring governing equations from time-series data using a library of functions constructed from the measured variables. However, these methods typically assume time-invariant coefficients, which limits their ability to capture evolving system dynamics. To overcome this limitation, we allow some of the parameters to vary over time, learn their temporal evolution directly from data, and infer a system of equations that incorporates both constant and time-varying parameters. We then transform this framework into a forecasting model by predicting the time-varying parameters and substituting these predictions into the learned equations. The model is validated using datasets for Susceptible-Infected-Recovered, Consumer--Resource, greenhouse gas concentration, and Cyanobacteria cell count. By dynamically adapting to temporal shifts, our proposed model achieved a mean absolute error below 3\% for learning a time series and below 6\% for forecasting up to a month ahead. We additionally compare forecasting performance against CNN-LSTM and Gradient Boosting Machine (GBM), and show that our model outperforms these methods across most datasets. Our findings demonstrate that integrating time-varying parameters into data-driven discovery of differential equations improves both modeling accuracy and forecasting performance.

