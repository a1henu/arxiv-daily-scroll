---
layout: default
title: Temporal Kolmogorov-Arnold Networks (T-KAN) for High-Frequency Limit Order Book Forecasting: Efficiency, Interpretability, and Alpha Decay
---

# Temporal Kolmogorov-Arnold Networks (T-KAN) for High-Frequency Limit Order Book Forecasting: Efficiency, Interpretability, and Alpha Decay
**arXiv**：[2601.02310v1](https://arxiv.org/abs/2601.02310) · [PDF](https://arxiv.org/pdf/2601.02310.pdf)  
**作者**：Ahmad Makinde  

**一句话要点**：提出T-KAN以解决高频限价订单簿预测中的Alpha衰减问题

**关键词**：高频交易预测, 限价订单簿分析, T-KAN网络, B样条激活, Alpha衰减, FPGA优化

## 3 点简述
- 核心问题：高频交易中限价订单簿数据噪声大、非线性强，传统模型如DeepLOB在时间跨度增加时预测能力下降。
- 方法要点：用可学习的B样条激活函数替代标准LSTM的固定线性权重，学习市场信号的形状而非仅幅度。
- 实验或效果：在k=100时间跨度上F1分数相对提升19.1%，交易成本下回报率优于DeepLOB，模型可解释性强且适合FPGA低延迟实现。

## 摘要（原文）

> High-Frequency trading (HFT) environments are characterised by large volumes of limit order book (LOB) data, which is notoriously noisy and non-linear. Alpha decay represents a significant challenge, with traditional models such as DeepLOB losing predictive power as the time horizon (k) increases. In this paper, using data from the FI-2010 dataset, we introduce Temporal Kolmogorov-Arnold Networks (T-KAN) to replace the fixed, linear weights of standard LSTMs with learnable B-spline activation functions. This allows the model to learn the 'shape' of market signals as opposed to just their magnitude. This resulted in a 19.1% relative improvement in the F1-score at the k = 100 horizon. The efficacy of T-KAN networks cannot be understated, producing a 132.48% return compared to the -82.76% DeepLOB drawdown under 1.0 bps transaction costs. In addition to this, the T-KAN model proves quite interpretable, with the 'dead-zones' being clearly visible in the splines. The T-KAN architecture is also uniquely optimized for low-latency FPGA implementation via High level Synthesis (HLS). The code for the experiments in this project can be found at https://github.com/AhmadMak/Temporal-Kolmogorov-Arnold-Networks-T-KAN-for-High-Frequency-Limit-Order-Book-Forecasting.

