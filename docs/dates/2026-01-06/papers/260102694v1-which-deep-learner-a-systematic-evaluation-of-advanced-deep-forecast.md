---
layout: default
title: Which Deep Learner? A Systematic Evaluation of Advanced Deep Forecasting Models Accuracy and Efficiency for Network Traffic Prediction
---

# Which Deep Learner? A Systematic Evaluation of Advanced Deep Forecasting Models Accuracy and Efficiency for Network Traffic Prediction
**arXiv**：[2601.02694v1](https://arxiv.org/abs/2601.02694) · [PDF](https://arxiv.org/pdf/2601.02694.pdf)  
**作者**：Eilaf MA Babai, Aalaa MA Babai, Koji Okamura  

**一句话要点**：系统评估十二种先进深度学习模型在多种网络流量预测场景下的准确性与效率

**关键词**：网络流量预测, 深度学习模型评估, 时间序列预测, Transformer架构, 资源效率分析

## 3 点简述
- 核心问题：网络流量预测因环境与时间尺度多变，需识别有效模型部署选择与建模方向。
- 方法要点：比较基于Transformer与传统DL的十二种模型，评估性能、鲁棒性、数据效率和资源效率。
- 实验或效果：在四个真实数据集上测试，揭示性能区间、效率阈值及平衡准确性与效率的架构。

## 摘要（原文）

> Network traffic prediction is essential for automating modern network management. It is a difficult time series forecasting (TSF) problem that has been addressed by Deep Learning (DL) models due to their ability to capture complex patterns. Advances in forecasting, from sophisticated transformer architectures to simple linear models, have improved performance across diverse prediction tasks. However, given the variability of network traffic across network environments and traffic series timescales, it is essential to identify effective deployment choices and modeling directions for network traffic prediction. This study systematically identify and evaluates twelve advanced TSF models -including transformer-based and traditional DL approaches, each with unique advantages for network traffic prediction- against three statistical baselines on four real traffic datasets, across multiple time scales and horizons, assessing performance, robustness to anomalies, data gaps, external factors, data efficiency, and resource efficiency in terms of time, memory, and energy. Results highlight performance regimes, efficiency thresholds, and promising architectures that balance accuracy and efficiency, demonstrating robustness to traffic challenges and suggesting new directions beyond traditional RNNs.

