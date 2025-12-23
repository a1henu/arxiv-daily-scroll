---
layout: default
title: From Black-Box Tuning to Guided Optimization via Hyperparameters Interaction Analysis
---

# From Black-Box Tuning to Guided Optimization via Hyperparameters Interaction Analysis
**arXiv**：[2512.19246v1](https://arxiv.org/abs/2512.19246) · [PDF](https://arxiv.org/pdf/2512.19246.pdf)  
**作者**：Moncef Garouani, Ayah Barhrhouj  

**一句话要点**：提出MetaSHAP方法，通过元学习和SHAP分析提供可解释的超参数调优指导

**关键词**：超参数调优, 可解释AI, 元学习, SHAP分析, 贝叶斯优化

## 3 点简述
- 超参数调优计算成本高，需理解其重要性和交互作用
- MetaSHAP利用历史配置学习代理模型，基于SHAP分析超参数交互
- 在164个分类数据集和14个分类器上验证，提供可靠重要性排名和性能指导

## 摘要（原文）

> Hyperparameters tuning is a fundamental, yet computationally expensive, step in optimizing machine learning models. Beyond optimization, understanding the relative importance and interaction of hyperparameters is critical to efficient model development. In this paper, we introduce MetaSHAP, a scalable semi-automated eXplainable AI (XAI) method, that uses meta-learning and Shapley values analysis to provide actionable and dataset-aware tuning insights. MetaSHAP operates over a vast benchmark of over 09 millions evaluated machine learning pipelines, allowing it to produce interpretable importance scores and actionable tuning insights that reveal how much each hyperparameter matters, how it interacts with others and in which value ranges its influence is concentrated. For a given algorithm and dataset, MetaSHAP learns a surrogate performance model from historical configurations, computes hyperparameters interactions using SHAP-based analysis, and derives interpretable tuning ranges from the most influential hyperparameters. This allows practitioners not only to prioritize which hyperparameters to tune, but also to understand their directionality and interactions. We empirically validate MetaSHAP on a diverse benchmark of 164 classification datasets and 14 classifiers, demonstrating that it produces reliable importance rankings and competitive performance when used to guide Bayesian optimization.

