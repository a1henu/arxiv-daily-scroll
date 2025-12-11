---
layout: default
title: A Granular Framework for Construction Material Price Forecasting: Econometric and Machine-Learning Approaches
---

# A Granular Framework for Construction Material Price Forecasting: Econometric and Machine-Learning Approaches
**arXiv**：[2512.09360v1](https://arxiv.org/abs/2512.09360) · [PDF](https://arxiv.org/pdf/2512.09360.pdf)  
**作者**：Boge Lyu, Qianye Yin, Iris Denise Tommelein, Hanyang Liu, Karnamohit Ranka, Karthik Yeluripati, Junzhe Shi  

**一句话要点**：提出基于CSI MasterFormat的细粒度框架，结合计量与机器学习方法预测建筑材料价格，以提升成本估算可靠性。

**关键词**：建筑材料价格预测, 细粒度框架, 时间序列模型, LSTM, CSI MasterFormat, 成本估算

## 3 点简述
- 核心问题：建筑材料价格持续波动，对成本估算和项目交付构成显著风险，需细粒度预测方法。
- 方法要点：利用CSI MasterFormat作为数据结构，整合原材料价格等解释变量，评估LSTM、ARIMA等四种时间序列模型。
- 实验或效果：解释变量显著提升所有模型性能，LSTM表现最佳，RMSE低至1.390，MAPE为0.957，优于ARIMA达59%。

## 摘要（原文）

> The persistent volatility of construction material prices poses significant risks to cost estimation, budgeting, and project delivery, underscoring the urgent need for granular and scalable forecasting methods. This study develops a forecasting framework that leverages the Construction Specifications Institute (CSI) MasterFormat as the target data structure, enabling predictions at the six-digit section level and supporting detailed cost projections across a wide spectrum of building materials. To enhance predictive accuracy, the framework integrates explanatory variables such as raw material prices, commodity indexes, and macroeconomic indicators. Four time-series models, Long Short-Term Memory (LSTM), Autoregressive Integrated Moving Average (ARIMA), Vector Error Correction Model (VECM), and Chronos-Bolt, were evaluated under both baseline configurations (using CSI data only) and extended versions with explanatory variables. Results demonstrate that incorporating explanatory variables significantly improves predictive performance across all models. Among the tested approaches, the LSTM model consistently achieved the highest accuracy, with RMSE values as low as 1.390 and MAPE values of 0.957, representing improvements of up to 59\% over the traditional statistical time-series model, ARIMA. Validation across multiple CSI divisions confirmed the framework's scalability, while Division 06 (Wood, Plastics, and Composites) is presented in detail as a demonstration case. This research offers a robust methodology that enables owners and contractors to improve budgeting practices and achieve more reliable cost estimation at the Definitive level.

