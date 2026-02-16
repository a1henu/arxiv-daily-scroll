---
layout: default
title: Probabilistic Wind Power Forecasting with Tree-Based Machine Learning and Weather Ensembles
---

# Probabilistic Wind Power Forecasting with Tree-Based Machine Learning and Weather Ensembles
**arXiv**：[2602.13010v1](https://arxiv.org/abs/2602.13010) · [PDF](https://arxiv.org/pdf/2602.13010.pdf)  
**作者**：Max Bruninx, Diederik van Binsbergen, Timothy Verstraeten, Ann Nowé, Jan Helsen  

**一句话要点**：提出基于梯度提升树和天气集合的概率性风电功率预测方法，以提升电网集成可再生能源的准确性。

**关键词**：风电功率预测, 概率预测, 梯度提升树, 天气集合, 条件扩散模型, 可再生能源集成

## 3 点简述
- 核心问题：风电功率预测对电网集成可再生能源至关重要，需提高预测精度和概率性估计。
- 方法要点：使用梯度提升树结合天气集合，比较三种概率预测方法：保形分位数回归、自然梯度提升和条件扩散模型。
- 实验或效果：在比利时海上风电场数据上验证，机器学习方法相比传统工程方法提升平均绝对误差达53%和33%，条件扩散模型表现最佳。

## 摘要（原文）

> Accurate production forecasts are essential to continue facilitating the integration of renewable energy sources into the power grid. This paper illustrates how to obtain probabilistic day-ahead forecasts of wind power generation via gradient boosting trees using an ensemble of weather forecasts. To this end, we perform a comparative analysis across three state-of-the-art probabilistic prediction methods-conformalised quantile regression, natural gradient boosting and conditional diffusion models-all of which can be combined with tree-based machine learning. The methods are validated using four years of data for all wind farms present within the Belgian offshore zone. Additionally, the point forecasts are benchmarked against deterministic engineering methods, using either the power curve or an advanced approach incorporating a calibrated analytical wake model. The experimental results show that the machine learning methods improve the mean absolute error by up to 53% and 33% compared to the power curve and the calibrated wake model. Considering the three probabilistic prediction methods, the conditional diffusion model is found to yield the best overall probabilistic and point estimate of wind power generation. Moreover, the findings suggest that the use of an ensemble of weather forecasts can improve point forecast accuracy by up to 23%.

