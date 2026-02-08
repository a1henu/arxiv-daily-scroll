---
layout: default
title: Geographically-aware Transformer-based Traffic Forecasting for Urban Motorway Digital Twins
---

# Geographically-aware Transformer-based Traffic Forecasting for Urban Motorway Digital Twins
**arXiv**：[2602.05983v1](https://arxiv.org/abs/2602.05983) · [PDF](https://arxiv.org/pdf/2602.05983.pdf)  
**作者**：Krešimir Kušić, Vinny Cahill, Ivana Dusparic  

**一句话要点**：提出地理感知Transformer交通预测模型以提升高速公路数字孪生中的交通预测精度

**关键词**：交通预测, 数字孪生, Transformer模型, 地理感知, 互信息, 高速公路管理

## 3 点简述
- 核心问题：高速公路交通预测因时空复杂性和非线性动态而困难，现有序列模型在精度和复杂度上需改进
- 方法要点：利用传感器间互信息引入地理感知，增强Transformer模型以捕捉空间关系，不增加模型复杂度
- 实验或效果：在日内瓦高速公路网络真实数据上验证，相比标准Transformer，地理感知提升了预测准确性

## 摘要（原文）

> The operational effectiveness of digital-twin technology in motorway traffic management depends on the availability of a continuous flow of high-resolution real-time traffic data. To function as a proactive decision-making support layer within traffic management, a digital twin must also incorporate predicted traffic conditions in addition to real-time observations. Due to the spatio-temporal complexity and the time-variant, non-linear nature of traffic dynamics, predicting motorway traffic remains a difficult problem. Sequence-based deep-learning models offer clear advantages over classical machine learning and statistical models in capturing long-range, temporal dependencies in time-series traffic data, yet limitations in forecasting accuracy and model complexity point to the need for further improvements. To improve motorway traffic forecasting, this paper introduces a Geographically-aware Transformer-based Traffic Forecasting GATTF model, which exploits the geographical relationships between distributed sensors using their mutual information (MI). The model has been evaluated using real-time data from the Geneva motorway network in Switzerland and results confirm that incorporating geographical awareness through MI enhances the accuracy of GATTF forecasting compared to a standard Transformer, without increasing model complexity.

