---
layout: default
title: UrbanAI 2025 Challenge: Linear vs Transformer Models for Long-Horizon Exogenous Temperature Forecasting
---

# UrbanAI 2025 Challenge: Linear vs Transformer Models for Long-Horizon Exogenous Temperature Forecasting
**arXiv**：[2512.10866v1](https://arxiv.org/abs/2512.10866) · [PDF](https://arxiv.org/pdf/2512.10866.pdf)  
**作者**：Ruslan Gokhman  

**一句话要点**：在线性模型与Transformer模型对比中，DLinear在长时程外生温度预测中表现最佳。

**关键词**：时间序列预测, 外生预测, 线性模型, Transformer模型, 温度预测, 长时程预测

## 3 点简述
- 研究长时程外生温度预测，仅使用室内温度历史数据进行单变量预测。
- 对比线性模型（Linear、NLinear、DLinear）与Transformer家族模型（Transformer、Informer、Autoformer）。
- 实验显示线性模型普遍优于Transformer模型，DLinear在所有数据分割中准确率最高。

## 摘要（原文）

> We study long-horizon exogenous-only temperature forecasting - a challenging univariate setting where only the past values of the indoor temperature are used for prediction - using linear and Transformer-family models. We evaluate Linear, NLinear, DLinear, Transformer, Informer, and Autoformer under standardized train, validation, and test splits. Results show that linear baselines (Linear, NLinear, DLinear) consistently outperform more complex Transformer-family architectures, with DLinear achieving the best overall accuracy across all splits. These findings highlight that carefully designed linear models remain strong baselines for time series forecasting in challenging exogenous-only settings.

