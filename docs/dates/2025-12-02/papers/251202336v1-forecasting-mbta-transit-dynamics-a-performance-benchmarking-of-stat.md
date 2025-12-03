---
layout: default
title: Forecasting MBTA Transit Dynamics: A Performance Benchmarking of Statistical and Machine Learning Models
---

# Forecasting MBTA Transit Dynamics: A Performance Benchmarking of Statistical and Machine Learning Models
**arXiv**：[2512.02336v1](https://arxiv.org/abs/2512.02336) · [PDF](https://arxiv.org/pdf/2512.02336.pdf)  
**作者**：Sai Siddharth Nalamalpu, Kaining Yuan, Aiden Zhou, Eugene Pinsky  

**一句话要点**：比较统计与机器学习模型，预测MBTA地铁使用和延误，发现时序特征优于天气数据。

**关键词**：公共交通预测, 机器学习模型, 特征重要性, 点过程模型, RMSE评估

## 3 点简述
- 核心问题：预测MBTA地铁次日使用量和系统延误数，以提升效率和乘客满意度。
- 方法要点：评估10-11种模型，包括自激点过程模型，分析特征如星期、季节和天气的影响。
- 实验或效果：通过RMSE测试，发现星期或季节数据比天气数据更有效，天气数据可能导致过拟合。

## 摘要（原文）

> The Massachusetts Bay Transportation Authority (MBTA) is the main public transit provider in Boston, operating multiple means of transport, including trains, subways, and buses. However, the system often faces delays and fluctuations in ridership volume, which negatively affect efficiency and passenger satisfaction. To further understand this phenomenon, this paper compares the performance of existing and unique methods to determine the best approach in predicting gated station entries in the subway system (a proxy for subway usage) and the number of delays in the overall MBTA system. To do so, this research considers factors that tend to affect public transportation, such as day of week, season, pressure, wind speed, average temperature, and precipitation. This paper evaluates the performance of 10 statistical and machine learning models on predicting next-day subway usage. On predicting delay count, the number of models is extended to 11 per day by introducing a self-exciting point process model, representing a unique application of a point-process framework for MBTA delay modeling. This research involves experimenting with the selective inclusion of features to determine feature importance, testing model accuracy via Root Mean Squared Error (RMSE). Remarkably, it is found that providing either day of week or season data has a more substantial benefit to predictive accuracy compared to weather data; in fact, providing weather data generally worsens performance, suggesting a tendency of models to overfit.

