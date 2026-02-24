---
layout: default
title: Multivariate time-series forecasting of ASTRI-Horn monitoring data: A Normal Behavior Model
---

# Multivariate time-series forecasting of ASTRI-Horn monitoring data: A Normal Behavior Model
**arXiv**：[2602.19984v1](https://arxiv.org/abs/2602.19984) · [PDF](https://arxiv.org/pdf/2602.19984.pdf)  
**作者**：Federico Incardona, Alessandro Costa, Farida Farsian, Francesco Franchina, Giuseppe Leto, Emilio Mastriani, Kevin Munari, Giovanni Pareschi, Salvatore Scuderi, Sebastiano Spinello, Gino Tosti  

**一句话要点**：提出基于MLP的正常行为模型，用于ASTRI-Horn望远镜监测数据的多变量时间序列预测，支持异常检测。

**关键词**：时间序列预测, 正常行为模型, 多层感知机, 异常检测, 望远镜监测, 多变量分析

## 3 点简述
- 核心问题：预测ASTRI-Horn望远镜在正常操作下的15个物理变量监测时间序列，以支持早期异常检测。
- 方法要点：使用数据预处理、滑动窗口技术和多层感知机进行多变量预测，并与LSTM网络进行性能对比。
- 实验或效果：MLP模型在最佳配置下测试集MSE为0.019±0.003，NMAD为0.032±0.009，预测长达6.5小时性能稳定，收敛快于LSTM。

## 摘要（原文）

> This study presents a Normal Behavior Model (NBM) developed to forecast monitoring time-series data from the ASTRI-Horn Cherenkov telescope under normal operating conditions. The analysis focused on 15 physical variables acquired by the Telescope Control Unit between September 2022 and July 2024, representing sensor measurements from the Azimuth and Elevation motors. After data cleaning, resampling, feature selection, and correlation analysis, the dataset was segmented into fixed-length intervals, in which the first I samples represented the input sequence provided to the model, while the forecast length, T, indicated the number of future time steps to be predicted. A sliding-window technique was then applied to increase the number of intervals. A Multi-Layer Perceptron (MLP) was trained to perform multivariate forecasting across all features simultaneously. Model performance was evaluated using the Mean Squared Error (MSE) and the Normalized Median Absolute Deviation (NMAD), and it was also benchmarked against a Long Short-Term Memory (LSTM) network. The MLP model demonstrated consistent results across different features and I-T configurations, and matched the performance of the LSTM while converging faster. It achieved an MSE of 0.019+/-0.003 and an NMAD of 0.032+/-0.009 on the test set under its best configuration (4 hidden layers, 720 units per layer, and I-T lengths of 300 samples each, corresponding to 5 hours at 1-minute resolution). Extending the forecast horizon up to 6.5 hours-the maximum allowed by this configuration-did not degrade performance, confirming the model's effectiveness in providing reliable hour-scale predictions. The proposed NBM provides a powerful tool for enabling early anomaly detection in online ASTRI-Horn monitoring time series, offering a basis for the future development of a prognostics and health management system that supports predictive maintenance.

