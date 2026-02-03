---
layout: default
title: An Optimization Method for Autoregressive Time Series Forecasting
---

# An Optimization Method for Autoregressive Time Series Forecasting
**arXiv**：[2602.02288v1](https://arxiv.org/abs/2602.02288) · [PDF](https://arxiv.org/pdf/2602.02288.pdf)  
**作者**：Zheng Li, Jerry Cheng, Huanying Gu  

**一句话要点**：提出一种自回归时间序列预测优化方法，通过强制预测误差随步长增加和灵活拼接短时预测来提升长时预测性能。

**关键词**：时间序列预测, 自回归模型, 优化方法, 长时预测, Transformer, 损失函数设计

## 3 点简述
- 当前时间序列预测模型依赖Transformer架构，通过扩大模型规模而非真正自回归展开实现长时预测，忽略了时间因果性。
- 新方法在损失函数中惩罚预测误差不随步长增加的情况，并允许模型拼接短时自回归预测以形成灵活长时预测。
- 实验表明，该方法在多个基准上达到新SOTA，MSE降低超10%，并使短时预测模型能可靠预测步长超7.5倍的长时序列。

## 摘要（原文）

> Current time-series forecasting models are primarily based on transformer-style neural networks. These models achieve long-term forecasting mainly by scaling up the model size rather than through genuinely autoregressive (AR) rollout. From the perspective of large language model training, the traditional training process for time-series forecasting models ignores temporal causality. In this paper, we propose a novel training method for time-series forecasting that enforces two key properties: (1) AR prediction errors should increase with the forecasting horizon. Any violation of this principle is considered random guessing and is explicitly penalized in the loss function, and (2) the method enables models to concatenate short-term AR predictions for forming flexible long-term forecasts. Empirical results demonstrate that our method establishes a new state-of-the-art across multiple benchmarks, achieving an MSE reduction of more than 10% compared to iTransformer and other recent strong baselines. Furthermore, it enables short-horizon forecasting models to perform reliable long-term predictions at horizons over 7.5 times longer. Code is available at https://github.com/LizhengMathAi/AROpt

