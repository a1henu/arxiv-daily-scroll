---
layout: default
title: Integrating Meteorological and Operational Data: A Novel Approach to Understanding Railway Delays in Finland
---

# Integrating Meteorological and Operational Data: A Novel Approach to Understanding Railway Delays in Finland
**arXiv**：[2601.16592v1](https://arxiv.org/abs/2601.16592) · [PDF](https://arxiv.org/pdf/2601.16592.pdf)  
**作者**：Vinicius Pozzobon Borin, Jean Michel de Souza Sant'Ana, Usama Raheel, Nurul Huda Mahmood  

**一句话要点**：提出首个公开的芬兰铁路运营与气象数据集成数据集，用于分析铁路延误

**关键词**：铁路延误预测, 气象数据集成, 时空数据分析, 机器学习应用, 芬兰铁路网络

## 3 点简述
- 核心问题：铁路延误受复杂因素影响，现有数据集缺乏气象与运营数据的整合，尤其在北欧地区。
- 方法要点：集成芬兰铁路运营数据与209个气象站观测，通过时空对齐和特征工程处理，涵盖28个特征和约3850万条观测。
- 实验或效果：使用XGBoost回归预测站点延误，平均绝对误差为2.73分钟，验证数据集在机器学习应用中的实用性。

## 摘要（原文）

> Train delays result from complex interactions between operational, technical, and environmental factors. While weather impacts railway reliability, particularly in Nordic regions, existing datasets rarely integrate meteorological information with operational train data. This study presents the first publicly available dataset combining Finnish railway operations with synchronized meteorological observations from 2018-2024. The dataset integrates operational metrics from Finland Digitraffic Railway Traffic Service with weather measurements from 209 environmental monitoring stations, using spatial-temporal alignment via Haversine distance. It encompasses 28 engineered features across operational variables and meteorological measurements, covering approximately 38.5 million observations from Finland's 5,915-kilometer rail network. Preprocessing includes strategic missing data handling through spatial fallback algorithms, cyclical encoding of temporal features, and robust scaling of weather data to address sensor outliers. Analysis reveals distinct seasonal patterns, with winter months exhibiting delay rates exceeding 25\% and geographic clustering of high-delay corridors in central and northern Finland. Furthermore, the work demonstrates applications of the data set in analysing the reliability of railway traffic in Finland. A baseline experiment using XGBoost regression achieved a Mean Absolute Error of 2.73 minutes for predicting station-specific delays, demonstrating the dataset's utility for machine learning applications. The dataset enables diverse applications, including train delay prediction, weather impact assessment, and infrastructure vulnerability mapping, providing researchers with a flexible resource for machine learning applications in railway operations research.

