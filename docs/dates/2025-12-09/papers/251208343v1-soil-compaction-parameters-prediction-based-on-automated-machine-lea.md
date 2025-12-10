---
layout: default
title: Soil Compaction Parameters Prediction Based on Automated Machine Learning Approach
---

# Soil Compaction Parameters Prediction Based on Automated Machine Learning Approach
**arXiv**：[2512.08343v1](https://arxiv.org/abs/2512.08343) · [PDF](https://arxiv.org/pdf/2512.08343.pdf)  
**作者**：Caner Erden, Alparslan Serhat Demir, Abdullah Hulusi Kokcam, Talas Fikret Kurnaz, Ugur Dagdeviren  

**一句话要点**：提出基于AutoML的方法预测土壤压实参数，以提升建筑工程中的预测准确性与泛化能力。

**关键词**：土壤压实参数预测, 自动化机器学习, XGBoost算法, 建筑工程应用, 异质数据集

## 3 点简述
- 核心问题：传统土壤压实参数预测方法劳动密集且准确性有限，机器学习模型在异质数据集上泛化能力不足。
- 方法要点：采用自动化机器学习（AutoML）自动选择算法和优化超参数，以XGBoost为最佳算法。
- 实验或效果：在独立数据集上，XGBoost对最大干密度和最优含水率的预测R²值分别达80.4%和89.1%。

## 摘要（原文）

> Soil compaction is critical in construction engineering to ensure the stability of structures like road embankments and earth dams. Traditional methods for determining optimum moisture content (OMC) and maximum dry density (MDD) involve labor-intensive laboratory experiments, and empirical regression models have limited applicability and accuracy across diverse soil types. In recent years, artificial intelligence (AI) and machine learning (ML) techniques have emerged as alternatives for predicting these compaction parameters. However, ML models often struggle with prediction accuracy and generalizability, particularly with heterogeneous datasets representing various soil types. This study proposes an automated machine learning (AutoML) approach to predict OMC and MDD. AutoML automates algorithm selection and hyperparameter optimization, potentially improving accuracy and scalability. Through extensive experimentation, the study found that the Extreme Gradient Boosting (XGBoost) algorithm provided the best performance, achieving R-squared values of 80.4% for MDD and 89.1% for OMC on a separate dataset. These results demonstrate the effectiveness of AutoML in predicting compaction parameters across different soil types. The study also highlights the importance of heterogeneous datasets in improving the generalization and performance of ML models. Ultimately, this research contributes to more efficient and reliable construction practices by enhancing the prediction of soil compaction parameters.

