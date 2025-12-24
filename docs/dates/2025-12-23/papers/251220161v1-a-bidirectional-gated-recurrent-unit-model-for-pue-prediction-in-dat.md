---
layout: default
title: A Bidirectional Gated Recurrent Unit Model for PUE Prediction in Data Centers
---

# A Bidirectional Gated Recurrent Unit Model for PUE Prediction in Data Centers
**arXiv**：[2512.20161v1](https://arxiv.org/abs/2512.20161) · [PDF](https://arxiv.org/pdf/2512.20161.pdf)  
**作者**：Dhivya Dharshini Kannan, Anupam Trivedi, Dipti Srinivasan  

**一句话要点**：提出基于双向门控循环单元的模型以预测数据中心能效指标PUE。

**关键词**：数据中心能效, PUE预测, 双向门控循环单元, 特征选择, 神经网络模型, 能源管理

## 3 点简述
- 核心问题：数据中心能耗高，需优化能效管理，PUE是关键指标。
- 方法要点：使用BiGRU模型预测PUE，通过RFECV算法选择特征并优化超参数。
- 实验或效果：在新加坡数据中心模拟数据集上比较BiGRU与GRU，评估指标包括MSE、MAE和R平方。

## 摘要（原文）

> Data centers account for significant global energy consumption and a carbon footprint. The recent increasing demand for edge computing and AI advancements drives the growth of data center storage capacity. Energy efficiency is a cost-effective way to combat climate change, cut energy costs, improve business competitiveness, and promote IT and environmental sustainability. Thus, optimizing data center energy management is the most important factor in the sustainability of the world. Power Usage Effectiveness (PUE) is used to represent the operational efficiency of the data center. Predicting PUE using Neural Networks provides an understanding of the effect of each feature on energy consumption, thus enabling targeted modifications of those key features to improve energy efficiency. In this paper, we have developed Bidirectional Gated Recurrent Unit (BiGRU) based PUE prediction model and compared the model performance with GRU. The data set comprises 52,560 samples with 117 features using EnergyPlus, simulating a DC in Singapore. Sets of the most relevant features are selected using the Recursive Feature Elimination with Cross-Validation (RFECV) algorithm for different parameter settings. These feature sets are used to find the optimal hyperparameter configuration and train the BiGRU model. The performance of the optimized BiGRU-based PUE prediction model is then compared with that of GRU using mean squared error (MSE), mean absolute error (MAE), and R-squared metrics.

