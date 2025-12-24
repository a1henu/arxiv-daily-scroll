---
layout: default
title: Explainable time-series forecasting with sampling-free SHAP for Transformers
---

# Explainable time-series forecasting with sampling-free SHAP for Transformers
**arXiv**：[2512.20514v1](https://arxiv.org/abs/2512.20514) · [PDF](https://arxiv.org/pdf/2512.20514.pdf)  
**作者**：Matthias Hertel, Sebastian Pütz, Ralf Mikut, Veit Hagenmeyer, Benjamin Schäfer  

**一句话要点**：提出SHAPformer，基于Transformer实现无采样SHAP解释的时间序列预测模型。

**关键词**：时间序列预测, 可解释AI, Transformer, SHAP, 注意力机制, 电力负荷分析

## 3 点简述
- 核心问题：时间序列预测中SHAP方法效率低且假设特征独立，影响解释准确性。
- 方法要点：利用Transformer注意力机制操作，基于特征子集进行预测，实现无采样快速解释。
- 实验或效果：在合成数据上提供真实解释，在真实电力负荷数据中预测性能竞争且揭示关键洞察。

## 摘要（原文）

> Time-series forecasts are essential for planning and decision-making in many domains. Explainability is key to building user trust and meeting transparency requirements. Shapley Additive Explanations (SHAP) is a popular explainable AI framework, but it lacks efficient implementations for time series and often assumes feature independence when sampling counterfactuals. We introduce SHAPformer, an accurate, fast and sampling-free explainable time-series forecasting model based on the Transformer architecture. It leverages attention manipulation to make predictions based on feature subsets. SHAPformer generates explanations in under one second, several orders of magnitude faster than the SHAP Permutation Explainer. On synthetic data with ground truth explanations, SHAPformer provides explanations that are true to the data. Applied to real-world electrical load data, it achieves competitive predictive performance and delivers meaningful local and global insights, such as identifying the past load as the key predictor and revealing a distinct model behavior during the Christmas period.

