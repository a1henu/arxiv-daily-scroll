---
layout: default
title: Parametric and Generative Forecasts of Day-Ahead Market Curves for Storage Optimization
---

# Parametric and Generative Forecasts of Day-Ahead Market Curves for Storage Optimization
**arXiv**：[2601.20226v1](https://arxiv.org/abs/2601.20226) · [PDF](https://arxiv.org/pdf/2601.20226.pdf)  
**作者**：Julian Gutierrez, Redouane Silvente  

**一句话要点**：提出参数化和生成式模型以预测日前市场曲线并优化储能策略。

**关键词**：日前市场预测, 储能优化, 参数化建模, 生成式模型, 价格压缩效应

## 3 点简述
- 核心问题：预测EPEX SPOT日前市场的聚合供需曲线以优化储能操作。
- 方法要点：参数化模型用低维表示和切比雪夫多项式快速预测；生成式模型基于天气和燃料变量生成订单级合成场景。
- 实验或效果：模型支持储能策略优化，量化收益分布，并分析价格压缩效应。

## 摘要（原文）

> We present two machine learning frameworks for forecasting aggregated curves and optimizing storage in the EPEX SPOT day-ahead market. First, a fast parametric model forecasts hourly demand and supply curves in a low-dimensional and grid-robust representation, with minimum and maximum volumes combined with a Chebyshev polynomial for the elastic segment. The model enables daily use with low error and clear interpretability. Second, for a more comprehensive analysis, though less suited to daily operation, we employ generative models that learn the joint distribution of 24-hour order-level submissions given weather and fuel variables. These models generate synthetic daily scenarios of individual buy and sell orders, which, once aggregated, yield hourly supply and demand curves. Based on these forecasts, we optimize a price-making storage strategy, quantify revenue distributions, and highlight the price-compression effect with lower peaks, higher off-peak levels, and diminishing returns as capacity expands.

