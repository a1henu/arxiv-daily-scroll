---
layout: default
title: Electricity Price Forecasting: Bridging Linear Models, Neural Networks and Online Learning
---

# Electricity Price Forecasting: Bridging Linear Models, Neural Networks and Online Learning
**arXiv**：[2601.02856v1](https://arxiv.org/abs/2601.02856) · [PDF](https://arxiv.org/pdf/2601.02856.pdf)  
**作者**：Btissame El Mahtout, Florian Ziel  

**一句话要点**：提出结合线性与非线性前馈神经结构的多元神经网络方法，用于电力价格预测。

**关键词**：电力价格预测, 神经网络, 在线学习, 预测组合, 多元特征, 计算效率

## 3 点简述
- 核心问题：电力价格预测在不确定市场中面临线性模型无法捕捉非线性关系、非线性模型计算成本高的挑战。
- 方法要点：集成在线学习和预测组合，结合风能、太阳能、需求模式、燃料和碳市场等多元特征。
- 实验或效果：在主要欧洲电力市场六年的研究中，显著降低计算成本并提升预测精度（RMSE和MAE减少12-18%）。

## 摘要（原文）

> Precise day-ahead forecasts for electricity prices are crucial to ensure efficient portfolio management, support strategic decision-making for power plant operations, enable efficient battery storage optimization, and facilitate demand response planning. However, developing an accurate prediction model is highly challenging in an uncertain and volatile market environment. For instance, although linear models generally exhibit competitive performance in predicting electricity prices with minimal computational requirements, they fail to capture relevant nonlinear relationships. Nonlinear models, on the other hand, can improve forecasting accuracy with a surge in computational costs. We propose a novel multivariate neural network approach that combines linear and nonlinear feed-forward neural structures. Unlike previous hybrid models, our approach integrates online learning and forecast combination for efficient training and accuracy improvement. It also incorporates all relevant characteristics, particularly the fundamental relationships arising from wind and solar generation, electricity demand patterns, related energy fuel and carbon markets, in addition to autoregressive dynamics and calendar effects. Compared to the current state-of-the-art benchmark models, the proposed forecasting method significantly reduces computational cost while delivering superior forecasting accuracy (12-13% RMSE and 15-18% MAE reductions). Our results are derived from a six-year forecasting study conducted on major European electricity markets.

