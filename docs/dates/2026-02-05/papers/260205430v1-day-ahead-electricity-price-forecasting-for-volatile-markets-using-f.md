---
layout: default
title: Day-Ahead Electricity Price Forecasting for Volatile Markets Using Foundation Models with Regularization Strategy
---

# Day-Ahead Electricity Price Forecasting for Volatile Markets Using Foundation Models with Regularization Strategy
**arXiv**：[2602.05430v1](https://arxiv.org/abs/2602.05430) · [PDF](https://arxiv.org/pdf/2602.05430.pdf)  
**作者**：Kritchanat Ponyuenyong, Pengyu Tu, Jia Wei Tan, Wei Soon Cheong, Jamie Ng Suat Ling, Lianlian Jiang  

**一句话要点**：提出尖峰正则化策略，评估时间序列基础模型在波动电力市场中的日前电价预测性能。

**关键词**：电价预测, 时间序列基础模型, 尖峰正则化, 波动市场, 深度学习, 外生变量

## 3 点简述
- 核心问题：电力市场波动性和非线性使电价预测困难，传统模型难以捕捉复杂依赖。
- 方法要点：引入尖峰正则化策略，评估多种时间序列基础模型，整合外生因素如天气和日历变量。
- 实验或效果：在新加坡波动市场数据上，时间序列基础模型优于传统方法，MAPE提升最高达37.4%。

## 摘要（原文）

> Electricity price forecasting (EPF) is essential for energy markets stakeholders (e.g. grid operators, energy traders, policymakers) but remains challenging due to the inherent volatility and nonlinearity of price signals. Traditional statistical and deep learning (DL) models often struggle to capture complex temporal dependencies and integrate heterogeneous data effectively. While time series foundation models (TSFMs) have shown strong performance in general time series forecasting tasks, such as traffic forecasting and weather forecasting. However, their effectiveness in day-ahead EPF, particularly in volatile markets, remains underexplored. This paper presents a spike regularization strategy and evaluates a wide range of TSFMs, including Tiny Time Mixers (TTMs), MOIRAI, MOMENT, and TimesFM, against traditional statistical and DL models such as Autoregressive Integrated Moving Average (ARIMA), Long-short Term Memory (LSTM), and Convolutional Neural Network - LSTM (CNN-LSTM) using half-hourly wholesale market data with volatile trends in Singapore. Exogenous factors (e.g. weather and calendar variables) are also incorporated into models where applicable. Results demonstrate that TSFMs consistently outperform traditional approaches, achieving up to 37.4% improvement in MAPE across various evaluation settings. The findings offer practical guidance for improving forecast accuracy and decision-making in volatile electricity markets.

