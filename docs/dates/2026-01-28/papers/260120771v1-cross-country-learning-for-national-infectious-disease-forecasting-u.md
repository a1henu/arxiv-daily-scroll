---
layout: default
title: Cross-Country Learning for National Infectious Disease Forecasting Using European Data
---

# Cross-Country Learning for National Infectious Disease Forecasting Using European Data
**arXiv**：[2601.20771v1](https://arxiv.org/abs/2601.20771) · [PDF](https://arxiv.org/pdf/2601.20771.pdf)  
**作者**：Zacharias Komodromos, Kleanthis Malialis, Artemis Kontou, Panayiotis Kolios  

**一句话要点**：提出跨国学习框架，利用欧洲数据增强塞浦路斯COVID-19病例预测性能

**关键词**：传染病预测, 跨国学习, 时间序列分析, 数据增强, COVID-19, 机器学习模型

## 3 点简述
- 核心问题：单国历史数据有限，限制机器学习模型在传染病预测中的表现。
- 方法要点：通过整合多国时间序列数据，训练单一模型以利用共享流行病动态。
- 实验或效果：在塞浦路斯案例中，跨国数据能一致提升多步预测性能。

## 摘要（原文）

> Accurate forecasting of infectious disease incidence is critical for public health planning and timely intervention. While most data-driven forecasting approaches rely primarily on historical data from a single country, such data are often limited in length and variability, restricting the performance of machine learning (ML) models. In this work, we investigate a cross-country learning approach for infectious disease forecasting, in which a single model is trained on time series data from multiple countries and evaluated on a country of interest. This setting enables the model to exploit shared epidemic dynamics across countries and to benefit from an enlarged training set. We examine this approach through a case study on COVID-19 case forecasting in Cyprus, using surveillance data from European countries. We evaluate multiple ML models and analyse the impact of the lookback window length and cross-country `data augmentation' on multi-step forecasting performance. Our results show that incorporating data from other countries can lead to consistent improvements over models trained solely on national data. Although the empirical focus is on Cyprus and COVID-19, the proposed framework and findings are applicable to infectious disease forecasting more broadly, particularly in settings with limited national historical data.

