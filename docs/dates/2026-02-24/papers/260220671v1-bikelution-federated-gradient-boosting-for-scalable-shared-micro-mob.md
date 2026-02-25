---
layout: default
title: Bikelution: Federated Gradient-Boosting for Scalable Shared Micro-Mobility Demand Forecasting
---

# Bikelution: Federated Gradient-Boosting for Scalable Shared Micro-Mobility Demand Forecasting
**arXiv**：[2602.20671v1](https://arxiv.org/abs/2602.20671) · [PDF](https://arxiv.org/pdf/2602.20671.pdf)  
**作者**：Antonios Tziorvas, Andreas Tritsarolis, Yannis Theodoridis  

**一句话要点**：提出Bikelution，基于联邦梯度提升树，用于可扩展的无桩共享单车需求预测。

**关键词**：联邦学习, 梯度提升树, 需求预测, 共享单车, 隐私保护, 时空数据

## 3 点简述
- 核心问题：无桩共享单车需求预测受外部因素影响，传统时间序列模型不足，集中式机器学习存在隐私和带宽问题。
- 方法要点：采用联邦学习框架，结合梯度提升树，保护数据隐私，支持中期（最多六小时）需求预测。
- 实验或效果：在三个真实数据集上验证，性能与集中式变体相当，优于现有方法，展示隐私保护预测的可行性。

## 摘要（原文）

> The rapid growth of dockless bike-sharing systems has generated massive spatio-temporal datasets useful for fleet allocation, congestion reduction, and sustainable mobility. Bike demand, however, depends on several external factors, making traditional time-series models insufficient. Centralized Machine Learning (CML) yields high-accuracy forecasts but raises privacy and bandwidth issues when data are distributed across edge devices. To overcome these limitations, we propose Bikelution, an efficient Federated Learning (FL) solution based on gradient-boosted trees that preserves privacy while delivering accurate mid-term demand forecasts up to six hours ahead. Experiments on three real-world BSS datasets show that Bikelution is comparable to its CML-based variant and outperforms the current state-of-the-art. The results highlight the feasibility of privacy-aware demand forecasting and outline the trade-offs between FL and CML approaches.

