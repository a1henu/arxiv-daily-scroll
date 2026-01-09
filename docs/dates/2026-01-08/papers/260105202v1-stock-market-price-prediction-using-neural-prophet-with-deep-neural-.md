---
layout: default
title: Stock Market Price Prediction using Neural Prophet with Deep Neural Network
---

# Stock Market Price Prediction using Neural Prophet with Deep Neural Network
**arXiv**：[2601.05202v1](https://arxiv.org/abs/2601.05202) · [PDF](https://arxiv.org/pdf/2601.05202.pdf)  
**作者**：Navin Chhibber, Suneel Khemka, Navneet Kumar Tyagi, Rohit Tewari, Bireswar Banerjee, Piyush Ranjan  

**一句话要点**：提出NP-DNN模型以解决股票价格预测中概率范围预测不足的问题

**关键词**：股票价格预测, 深度神经网络, 多层感知机, Neural Prophet, 时间序列预测

## 3 点简述
- 核心问题：现有统计方法难以有效预测未来股票价格的概率范围
- 方法要点：结合Neural Prophet与多层感知机，通过Z-score归一化和缺失值填补预处理数据
- 实验或效果：模型准确率达99.21%，优于基于融合大语言模型的方法

## 摘要（原文）

> Stock market price prediction is a significant interdisciplinary research domain that depends at the intersection of finance, statistics, and economics. Forecasting Accurately predicting stock prices has always been a focal point for various researchers. However, existing statistical approaches for time-series prediction often fail to effectively forecast the probability range of future stock prices. Hence, to solve this problem, the Neural Prophet with a Deep Neural Network (NP-DNN) is proposed to predict stock market prices. The preprocessing technique used in this research is Z-score normalization, which normalizes stock price data by removing scale differences, making patterns easier to detect. Missing value imputation fills gaps in historical data, enhancing the models use of complete information for more accurate predictions. The Multi-Layer Perceptron (MLP) learns complex nonlinear relationships among stock market prices and extracts hidden patterns from the input data, thereby creating meaningful feature representations for better prediction accuracy. The proposed NP-DNN model achieved an accuracy of 99.21% compared with other approaches using the Fused Large Language Model. Keywords: deep neural network, forecasting stock prices, multi-layer perceptron, neural prophet, stock market price prediction.

