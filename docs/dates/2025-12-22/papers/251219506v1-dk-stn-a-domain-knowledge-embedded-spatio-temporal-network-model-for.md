---
layout: default
title: DK-STN: A Domain Knowledge Embedded Spatio-Temporal Network Model for MJO Forecast
---

# DK-STN: A Domain Knowledge Embedded Spatio-Temporal Network Model for MJO Forecast
**arXiv**：[2512.19506v1](https://arxiv.org/abs/2512.19506) · [PDF](https://arxiv.org/pdf/2512.19506.pdf)  
**作者**：Hongliang Li, Nong Zhang, Zhewen Xu, Xiang Li, Changzheng Liu, Chongbo Zhao, Jie Wu  

**一句话要点**：提出DK-STN模型，通过嵌入领域知识提升MJO预测的准确性与稳定性。

**关键词**：MJO预测, 时空网络, 领域知识嵌入, 气候数据建模, 神经网络优化

## 3 点简述
- 核心问题：传统数值天气预报方法资源消耗大且不稳定，现有神经网络方法预测精度不足。
- 方法要点：构建时空网络，嵌入领域知识增强与处理，结合数值天气预报与神经网络优势。
- 实验或效果：使用ERA5数据，输入7天数据可快速预测28天，误差仅2-3天，精度与ECMWF相当但效率更高。

## 摘要（原文）

> Understanding and predicting the Madden-Julian Oscillation (MJO) is fundamental for precipitation forecasting and disaster prevention. To date, long-term and accurate MJO prediction has remained a challenge for researchers. Conventional MJO prediction methods using Numerical Weather Prediction (NWP) are resource-intensive, time-consuming, and highly unstable (most NWP methods are sensitive to seasons, with better MJO forecast results in winter). While existing Artificial Neural Network (ANN) methods save resources and speed forecasting, their accuracy never reaches the 28 days predicted by the state-of-the-art NWP method, i.e., the operational forecasts from ECMWF, since neural networks cannot handle climate data effectively. In this paper, we present a Domain Knowledge Embedded Spatio-Temporal Network (DK-STN), a stable neural network model for accurate and efficient MJO forecasting. It combines the benefits of NWP and ANN methods and successfully improves the forecast accuracy of ANN methods while maintaining a high level of efficiency and stability. We begin with a spatial-temporal network (STN) and embed domain knowledge in it using two key methods: (i) applying a domain knowledge enhancement method and (ii) integrating a domain knowledge processing method into network training. We evaluated DK-STN with the 5th generation of ECMWF reanalysis (ERA5) data and compared it with ECMWF. Given 7 days of climate data as input, DK-STN can generate reliable forecasts for the following 28 days in 1-2 seconds, with an error of only 2-3 days in different seasons. DK-STN significantly exceeds ECMWF in that its forecast accuracy is equivalent to ECMWF's, while its efficiency and stability are significantly superior.

