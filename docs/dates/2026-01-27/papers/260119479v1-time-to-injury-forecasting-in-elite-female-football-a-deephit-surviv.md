---
layout: default
title: Time-to-Injury Forecasting in Elite Female Football: A DeepHit Survival Approach
---

# Time-to-Injury Forecasting in Elite Female Football: A DeepHit Survival Approach
**arXiv**：[2601.19479v1](https://arxiv.org/abs/2601.19479) · [PDF](https://arxiv.org/pdf/2601.19479.pdf)  
**作者**：Victoria Catterall, Cise Midoglu, Stephen Lynch  

**一句话要点**：提出基于DeepHit生存模型的足球运动员时间到伤预测方法，以提升损伤预测的准确性和可解释性。

**关键词**：时间到伤预测, DeepHit生存模型, 足球损伤分析, 纵向数据建模, 可解释性机器学习

## 3 点简述
- 核心问题：现有足球损伤预测方法依赖静态数据和二元结果，实用性受限。
- 方法要点：使用DeepHit神经网络处理纵向监测数据，提供个体化、时变风险估计。
- 实验或效果：在SoccerMon数据集上，DeepHit的C指数达0.762，优于基线模型，并通过SHAP增强可解释性。

## 摘要（原文）

> Injury occurrence in football poses significant challenges for athletes and teams, carrying personal, competitive, and financial consequences. While machine learning has been applied to injury prediction before, existing approaches often rely on static pre-season data and binary outcomes, limiting their real-world utility. This study investigates the feasibility of using a DeepHit neural network to forecast time-to-injury from longitudinal athlete monitoring data, while providing interpretable predictions. The analysis utilised the publicly available SoccerMon dataset, containing two seasons of training, match, and wellness records from elite female footballers. Data was pre-processed through cleaning, feature engineering, and the application of three imputation strategies. Baseline models (Random Forest, XGBoost, Logistic Regression) were optimised via grid search for benchmarking, while the DeepHit model, implemented with a multilayer perceptron backbone, was evaluated using chronological and leave-one-player-out (LOPO) validation. DeepHit achieved a concordance index of 0.762, outperforming baseline models and delivering individualised, time-varying risk estimates. Shapley Additive Explanations (SHAP) identified clinically relevant predictors consistent with established risk factors, enhancing interpretability. Overall, this study provides a novel proof of concept: survival modelling with DeepHit shows strong potential to advance injury forecasting in football, offering accurate, explainable, and actionable insights for injury prevention across competitive levels.

