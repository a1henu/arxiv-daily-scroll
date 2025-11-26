---
layout: default
title: Multivariate Forecasting of Bitcoin Volatility with Gradient Boosting: Deterministic, Probabilistic, and Feature Importance Perspectives
---

# Multivariate Forecasting of Bitcoin Volatility with Gradient Boosting: Deterministic, Probabilistic, and Feature Importance Perspectives
**arXiv**：[2511.20105v1](https://arxiv.org/abs/2511.20105) · [PDF](https://arxiv.org/pdf/2511.20105.pdf)  
**作者**：Grzegorz Dudek, Mateusz Kasprzyk, Paweł Pełka  

**一句话要点**：应用LGBM模型进行比特币波动率确定性及概率性预测，并分析特征重要性。

**关键词**：比特币波动率预测, 梯度提升机, 概率性预测, 特征重要性分析, 机器学习模型

## 3 点简述
- 核心问题：预测比特币实现波动率，处理非线性高方差特性。
- 方法要点：使用LGBM模型，结合69个预测因子，包括市场和宏观指标。
- 实验或效果：模型优于基线，识别交易量和滞后波动率等关键驱动因素。

## 摘要（原文）

> This study investigates the application of the Light Gradient Boosting Machine (LGBM) model for both deterministic and probabilistic forecasting of Bitcoin realized volatility. Utilizing a comprehensive set of 69 predictors -- encompassing market, behavioral, and macroeconomic indicators -- we evaluate the performance of LGBM-based models and compare them with both econometric and machine learning baselines. For probabilistic forecasting, we explore two quantile-based approaches: direct quantile regression using the pinball loss function, and a residual simulation method that transforms point forecasts into predictive distributions. To identify the main drivers of volatility, we employ gain-based and permutation feature importance techniques, consistently highlighting the significance of trading volume, lagged volatility measures, investor attention, and market capitalization. The results demonstrate that LGBM models effectively capture the nonlinear and high-variance characteristics of cryptocurrency markets while providing interpretable insights into the underlying volatility dynamics.

