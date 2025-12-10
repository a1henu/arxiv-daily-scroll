---
layout: default
title: Long-Sequence LSTM Modeling for NBA Game Outcome Prediction Using a Novel Multi-Season Dataset
---

# Long-Sequence LSTM Modeling for NBA Game Outcome Prediction Using a Novel Multi-Season Dataset
**arXiv**：[2512.08591v1](https://arxiv.org/abs/2512.08591) · [PDF](https://arxiv.org/pdf/2512.08591.pdf)  
**作者**：Charles Rios, Longzhen Han, Almas Baimagambetov, Nikolaos Polatidis  

**一句话要点**：提出长序列LSTM模型，利用多赛季数据集预测NBA比赛结果，以应对概念漂移和时序依赖问题。

**关键词**：长序列建模, LSTM, NBA比赛预测, 多赛季数据集, 时序依赖, 深度学习

## 3 点简述
- 核心问题：现有NBA比赛预测模型存在概念漂移、时序上下文有限和跨赛季不稳定性。
- 方法要点：构建覆盖2004-05至2024-25赛季的新数据集，并设计LSTM模型，序列长度达9,840场比赛以捕获长期趋势。
- 实验或效果：LSTM在准确率、精确度和AUC-ROC上均优于传统ML和DL基线，最高准确率达72.35%。

## 摘要（原文）

> Predicting the outcomes of professional basketball games, particularly in the National Basketball Association (NBA), has become increasingly important for coaching strategy, fan engagement, and sports betting. However, many existing prediction models struggle with concept drift, limited temporal context, and instability across seasons. To advance forecasting in this domain, we introduce a newly constructed longitudinal NBA dataset covering the 2004-05 to 2024-25 seasons and present a deep learning framework designed to model long-term performance trends. Our primary contribution is a Long Short-Term Memory (LSTM) architecture that leverages an extended sequence length of 9,840 games equivalent to eight full NBA seasons to capture evolving team dynamics and season-over-season dependencies. We compare this model against several traditional Machine Learning (ML) and Deep Learning (DL) baselines, including Logistic Regression, Random Forest, Multi-Layer Perceptron (MLP), and Convolutional Neural Network (CNN). The LSTM achieves the best performance across all metrics, with 72.35 accuracy, 73.15 precision and 76.13 AUC-ROC. These results demonstrate the importance of long-sequence temporal modeling in basketball outcome prediction and highlight the value of our new multi-season dataset for developing robust, generalizable NBA forecasting systems.

