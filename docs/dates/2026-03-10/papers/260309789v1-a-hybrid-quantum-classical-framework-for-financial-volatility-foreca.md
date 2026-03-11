---
layout: default
title: A Hybrid Quantum-Classical Framework for Financial Volatility Forecasting Based on Quantum Circuit Born Machines
---

# A Hybrid Quantum-Classical Framework for Financial Volatility Forecasting Based on Quantum Circuit Born Machines
**arXiv**：[2603.09789v1](https://arxiv.org/abs/2603.09789) · [PDF](https://arxiv.org/pdf/2603.09789.pdf)  
**作者**：Yixiong Chen  

**一句话要点**：提出混合量子-经典框架，结合LSTM与量子电路Born机以提升金融市场波动率预测精度。

**关键词**：混合量子-经典计算, 金融波动率预测, 长短期记忆网络, 量子电路Born机, 高频时间序列

## 3 点简述
- 核心问题：传统方法难以处理金融时间序列的非线性和非平稳特性，影响波动率预测准确性。
- 方法要点：设计混合模型，LSTM提取历史数据动态特征，量子电路Born机作为可学习先验模块提供高质量先验分布。
- 实验或效果：在上证综指和沪深300指数高频数据上测试，混合模型在MSE、RMSE和QLIKE损失等指标上优于纯经典LSTM基线。

## 摘要（原文）

> Accurate forecasting of financial market volatility is crucial for risk management, option pricing, and portfolio optimization. Traditional econometric models and classical machine learning methods face challenges in handling the inherent non-linear and non-stationary characteristics of financial time series. In recent years, the rapid development of quantum computing has provided a new paradigm for solving complex optimization and sampling problems. This paper proposes a novel hybrid quantum-classical computing framework aimed at combining the powerful representation capabilities of classical neural networks with the unique advantages of quantum models. For the specific task of financial market volatility forecasting, we designed and implemented a hybrid model based on this framework, which combines a Long Short-Term Memory (LSTM) network with a Quantum Circuit Born Machine (QCBM). The LSTM is responsible for extracting complex dynamic features from historical time series data, while the QCBM serves as a learnable prior module, providing the model with a high-quality prior distribution to guide the forecasting process. We evaluated the model on two real financial datasets consisting of 5-minute high-frequency data from the Shanghai Stock Exchange (SSE) Composite Index and CSI 300 Index. Experimental results show that, compared to a purely classical LSTM baseline model, our hybrid quantum-classical model demonstrates significant advantages across multiple key metrics, including Mean Squared Error (MSE), Root Mean Squared Error (RMSE), and QLIKE loss, proving the great potential of quantum computing in enhancing the capabilities of financial forecasting models. More broadly, the proposed hybrid framework offers a flexible architecture that may be adapted to other machine learning tasks involving high-dimensional, complex, or non-linear data distributions.

