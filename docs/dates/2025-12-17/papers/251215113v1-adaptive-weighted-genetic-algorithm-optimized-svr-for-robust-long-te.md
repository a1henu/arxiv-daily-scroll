---
layout: default
title: Adaptive Weighted Genetic Algorithm-Optimized SVR for Robust Long-Term Forecasting of Global Stock Indices for investment decisions
---

# Adaptive Weighted Genetic Algorithm-Optimized SVR for Robust Long-Term Forecasting of Global Stock Indices for investment decisions
**arXiv**：[2512.15113v1](https://arxiv.org/abs/2512.15113) · [PDF](https://arxiv.org/pdf/2512.15113.pdf)  
**作者**：Mohit Beniwal  

**一句话要点**：提出改进遗传算法优化的支持向量回归模型，用于全球股指长期价格预测以支持投资决策。

**关键词**：长期预测, 遗传算法优化, 支持向量回归, 全球股指, 投资决策, 计算效率

## 3 点简述
- 核心问题：长期价格预测因不确定性高而具挑战性，但对投资者至关重要。
- 方法要点：使用改进遗传算法优化SVR超参数，结合全训练集和近期数据调整趋势。
- 实验或效果：在五个全球指数上测试，相比LSTM和OGA-SVR，MAPE分别降低19.87%和50.03%，执行时间更短。

## 摘要（原文）

> Long-term price forecasting remains a formidable challenge due to the inherent uncertainty over the long term, despite some success in short-term predictions. Nonetheless, accurate long-term forecasts are essential for high-net-worth individuals, institutional investors, and traders. The proposed improved genetic algorithm-optimized support vector regression (IGA-SVR) model is specifically designed for long-term price prediction of global indices. The performance of the IGA-SVR model is rigorously evaluated and compared against the state-of-the-art baseline models, the Long Short-Term Memory (LSTM), and the forward-validating genetic algorithm optimized support vector regression (OGA-SVR). Extensive testing was conducted on the five global indices, namely Nifty, Dow Jones Industrial Average (DJI), DAX Performance Index (DAX), Nikkei 225 (N225), and Shanghai Stock Exchange Composite Index (SSE) from 2021 to 2024 of daily price prediction up to a year. Overall, the proposed IGA-SVR model achieved a reduction in MAPE by 19.87% compared to LSTM and 50.03% compared to OGA-SVR, demonstrating its superior performance in long-term daily price forecasting of global indices. Further, the execution time for LSTM was approximately 20 times higher than that of IGA-SVR, highlighting the high accuracy and computational efficiency of the proposed model. The genetic algorithm selects the optimal hyperparameters of SVR by minimizing the arithmetic mean of the Mean Absolute Percentage Error (MAPE) calculated over the full training dataset and the most recent five years of training data. This purposefully designed training methodology adjusts for recent trends while retaining long-term trend information, thereby offering enhanced generalization compared to the LSTM and rolling-forward validation approach employed by OGA-SVR, which forgets long-term trends and suffers from recency bias.

