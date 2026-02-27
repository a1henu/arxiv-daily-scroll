---
layout: default
title: A Data-Driven Approach to Support Clinical Renal Replacement Therapy
---

# A Data-Driven Approach to Support Clinical Renal Replacement Therapy
**arXiv**：[2602.22902v1](https://arxiv.org/abs/2602.22902) · [PDF](https://arxiv.org/pdf/2602.22902.pdf)  
**作者**：Alice Balboni, Luis Escobar, Andrea Manno, Fabrizio Rossi, Maria Cristina Ruffa, Gianluca Villa, Giordano D'Aloisio, Antonio Consolo  

**一句话要点**：提出基于机器学习的可解释模型，预测危重患者连续肾脏替代治疗中的膜污染。

**关键词**：膜污染预测, 连续肾脏替代治疗, 机器学习, 可解释模型, 反事实分析, 表格数据

## 3 点简述
- 核心问题：预测危重患者CRRT中的膜污染，以指导临床干预。
- 方法要点：采用表格数据方法，结合ADASYN过采样和随机森林等模型，避免直接时序建模。
- 实验或效果：模型在10%再平衡率下达到77.6%敏感性和96.3%特异性，优于LSTM，并通过Shapley值进行反事实分析。

## 摘要（原文）

> This study investigates a data-driven machine learning approach to predict membrane fouling in critically ill patients undergoing Continuous Renal Replacement Therapy (CRRT). Using time-series data from an ICU, 16 clinically selected features were identified to train predictive models. To ensure interpretability and enable reliable counterfactual analysis, the researchers adopted a tabular data approach rather than modeling temporal dependencies directly. Given the imbalance between fouling and non-fouling cases, the ADASYN oversampling technique was applied to improve minority class representation. Random Forest, XGBoost, and LightGBM models were tested, achieving balanced performance with 77.6% sensitivity and 96.3% specificity at a 10% rebalancing rate. Results remained robust across different forecasting horizons. Notably, the tabular approach outperformed LSTM recurrent neural networks, suggesting that explicit temporal modeling was not necessary for strong predictive performance. Feature selection further reduced the model to five key variables, improving simplicity and interpretability with minimal loss of accuracy. A Shapley value-based counterfactual analysis was applied to the best-performing model, successfully identifying minimal input changes capable of reversing fouling predictions. Overall, the findings support the viability of interpretable machine learning models for predicting membrane fouling during CRRT. The integration of prediction and counterfactual analysis offers practical clinical value, potentially guiding therapeutic adjustments to reduce fouling risk and improve patient management.

