---
layout: default
title: Bounded-Abstention Multi-horizon Time-series Forecasting
---

# Bounded-Abstention Multi-horizon Time-series Forecasting
**arXiv**：[2602.04714v1](https://arxiv.org/abs/2602.04714) · [PDF](https://arxiv.org/pdf/2602.04714.pdf)  
**作者**：Luca Stradiotti, Laurens Devos, Anna Monreale, Jesse Davis, Andrea Pugnana  

**一句话要点**：提出有界弃权多步时间序列预测方法，以解决现有弃权策略在多步预测中的不适用问题。

**关键词**：多步时间序列预测, 弃权学习, 结构化预测, 最优策略, 算法实现

## 3 点简述
- 核心问题：多步时间序列预测中，现有弃权策略忽略预测的结构性和相关性，导致不适用。
- 方法要点：形式化多步预测弃权学习问题，提出三种自然弃权概念，并推导最优策略及实现算法。
- 实验或效果：在24个数据集上评估，算法显著优于现有基线方法。

## 摘要（原文）

> Multi-horizon time-series forecasting involves simultaneously making predictions for a consecutive sequence of subsequent time steps. This task arises in many application domains, such as healthcare and finance, where mispredictions can have a high cost and reduce trust. The learning with abstention framework tackles these problems by allowing a model to abstain from offering a prediction when it is at an elevated risk of making a misprediction. Unfortunately, existing abstention strategies are ill-suited for the multi-horizon setting: they target problems where a model offers a single prediction for each instance. Hence, they ignore the structured and correlated nature of the predictions offered by a multi-horizon forecaster. We formalize the problem of learning with abstention for multi-horizon forecasting setting and show that its structured nature admits a richer set of abstention problems. Concretely, we propose three natural notions of how a model could abstain for multi-horizon forecasting. We theoretically analyze each problem to derive the optimal abstention strategy and propose an algorithm that implements it. Extensive evaluation on 24 datasets shows that our proposed algorithms significantly outperforms existing baselines.

