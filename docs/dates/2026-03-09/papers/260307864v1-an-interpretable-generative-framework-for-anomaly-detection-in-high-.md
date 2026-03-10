---
layout: default
title: An Interpretable Generative Framework for Anomaly Detection in High-Dimensional Financial Time Series
---

# An Interpretable Generative Framework for Anomaly Detection in High-Dimensional Financial Time Series
**arXiv**：[2603.07864v1](https://arxiv.org/abs/2603.07864) · [PDF](https://arxiv.org/pdf/2603.07864.pdf)  
**作者**：Waldyn G Martinez  

**一句话要点**：提出ReGEN-TAD可解释生成框架，用于高维金融时序异常检测

**关键词**：异常检测, 金融时序分析, 生成模型, 可解释性, 卷积-Transformer架构

## 3 点简述
- 核心问题：高维金融时序因复杂时序依赖和时变截面结构，异常检测困难
- 方法要点：结合联合预测与重构，集成预测不一致、重构退化等互补信号
- 实验或效果：在合成和金融面板数据上验证，提升对结构化偏差的鲁棒性

## 摘要（原文）

> Detecting structural instability and anomalies in high-dimensional financial time series is challenging due to complex temporal dependence and evolving cross-sectional structure. We propose ReGEN-TAD, an interpretable generative framework that integrates modern machine learning with econometric diagnostics for anomaly detection. The model combines joint forecasting and reconstruction within a refined convolutional--transformer architecture and aggregates complementary signals capturing predictive inconsistency, reconstruction degradation, latent distortion, and volatility shifts. Robust calibration yields a unified anomaly score without labeled data. Experiments on synthetic and financial panels demonstrate improved robustness to structured deviations while enabling economically coherent factor-level attribution.

