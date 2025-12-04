---
layout: default
title: Conditional updates of neural network weights for increased out of training performance
---

# Conditional updates of neural network weights for increased out of training performance
**arXiv**：[2512.03653v1](https://arxiv.org/abs/2512.03653) · [PDF](https://arxiv.org/pdf/2512.03653.pdf)  
**作者**：Jan Saynisch-Wagner, Saran Rajendran Sari  

**一句话要点**：提出条件性权重更新方法以增强神经网络在训练数据与应用数据不相似时的性能

**关键词**：条件性权重更新, 分布外泛化, 权重外推, 气候科学应用, 神经网络适应

## 3 点简述
- 核心问题：训练数据与应用数据不相似（如分布外问题、模式或体制偏移）导致神经网络性能下降
- 方法要点：通过重训练子集获取权重异常，建立预测器与异常的回归关系，并外推权重至应用数据
- 实验或效果：在气候科学三个用例中成功实现时间、空间和跨域外推

## 摘要（原文）

> This study proposes a method to enhance neural network performance when training data and application data are not very similar, e.g., out of distribution problems, as well as pattern and regime shifts. The method consists of three main steps: 1) Retrain the neural network towards reasonable subsets of the training data set and note down the resulting weight anomalies. 2) Choose reasonable predictors and derive a regression between the predictors and the weight anomalies. 3) Extrapolate the weights, and thereby the neural network, to the application data. We show and discuss this method in three use cases from the climate sciences, which include successful temporal, spatial and cross-domain extrapolations of neural networks.

