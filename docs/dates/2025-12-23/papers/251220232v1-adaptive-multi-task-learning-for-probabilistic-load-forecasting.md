---
layout: default
title: Adaptive Multi-task Learning for Probabilistic Load Forecasting
---

# Adaptive Multi-task Learning for Probabilistic Load Forecasting
**arXiv**：[2512.20232v1](https://arxiv.org/abs/2512.20232) · [PDF](https://arxiv.org/pdf/2512.20232.pdf)  
**作者**：Onintze Zaballa, Verónica Álvarez, Santiago Mazuelas  

**一句话要点**：提出自适应多任务学习方法以解决多实体概率负荷预测中的动态模式变化问题

**关键词**：概率负荷预测, 自适应多任务学习, 向量值隐马尔可夫模型, 动态模式适应, 不确定性评估

## 3 点简述
- 核心问题：多实体负荷预测面临不确定性、动态消费模式变化和实体间相关性挑战，现有方法多为离线学习，无法适应变化
- 方法要点：基于向量值隐马尔可夫模型，通过递归过程动态更新参数，实现自适应多任务学习和概率预测
- 实验或效果：在包含动态消费模式的数据集上评估，方法在预测性能和不确定性评估方面优于现有方法

## 摘要（原文）

> Simultaneous load forecasting across multiple entities (e.g., regions, buildings) is crucial for the efficient, reliable, and cost-effective operation of power systems. Accurate load forecasting is a challenging problem due to the inherent uncertainties in load demand, dynamic changes in consumption patterns, and correlations among entities. Multi-task learning has emerged as a powerful machine learning approach that enables the simultaneous learning across multiple related problems. However, its application to load forecasting remains underexplored and is limited to offline learning-based methods, which cannot capture changes in consumption patterns. This paper presents an adaptive multi-task learning method for probabilistic load forecasting. The proposed method can dynamically adapt to changes in consumption patterns and correlations among entities. In addition, the techniques presented provide reliable probabilistic predictions for loads of multiples entities and assess load uncertainties. Specifically, the method is based on vectorvalued hidden Markov models and uses a recursive process to update the model parameters and provide predictions with the most recent parameters. The performance of the proposed method is evaluated using datasets that contain the load demand of multiple entities and exhibit diverse and dynamic consumption patterns. The experimental results show that the presented techniques outperform existing methods both in terms of forecasting performance and uncertainty assessment.

