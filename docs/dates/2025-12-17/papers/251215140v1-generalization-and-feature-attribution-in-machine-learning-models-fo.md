---
layout: default
title: Generalization and Feature Attribution in Machine Learning Models for Crop Yield and Anomaly Prediction in Germany
---

# Generalization and Feature Attribution in Machine Learning Models for Crop Yield and Anomaly Prediction in Germany
**arXiv**：[2512.15140v1](https://arxiv.org/abs/2512.15140) · [PDF](https://arxiv.org/pdf/2512.15140.pdf)  
**作者**：Roland Baatz  

**一句话要点**：揭示机器学习模型在德国作物产量预测中泛化与特征归因的脆弱性

**关键词**：作物产量预测, 泛化性能, 特征归因, 时间验证, 机器学习模型, 农业数据科学

## 3 点简述
- 核心问题：模型在时间独立验证中泛化性能显著下降，但特征重要性仍看似可信
- 方法要点：系统比较集成树模型与深度学习模型在时空验证下的表现
- 实验或效果：发现后验可解释性方法在模型未泛化时可能误导解释

## 摘要（原文）

> This study examines the generalization performance and interpretability of machine learning (ML) models used for predicting crop yield and yield anomalies in Germany's NUTS-3 regions. Using a high-quality, long-term dataset, the study systematically compares the evaluation and temporal validation behavior of ensemble tree-based models (XGBoost, Random Forest) and deep learning approaches (LSTM, TCN).
>   While all models perform well on spatially split, conventional test sets, their performance degrades substantially on temporally independent validation years, revealing persistent limitations in generalization. Notably, models with strong test-set accuracy, but weak temporal validation performance can still produce seemingly credible SHAP feature importance values. This exposes a critical vulnerability in post hoc explainability methods: interpretability may appear reliable even when the underlying model fails to generalize.
>   These findings underscore the need for validation-aware interpretation of ML predictions in agricultural and environmental systems. Feature importance should not be accepted at face value unless models are explicitly shown to generalize to unseen temporal and spatial conditions. The study advocates for domain-aware validation, hybrid modeling strategies, and more rigorous scrutiny of explainability methods in data-driven agriculture. Ultimately, this work addresses a growing challenge in environmental data science: how can we evaluate generalization robustly enough to trust model explanations?

