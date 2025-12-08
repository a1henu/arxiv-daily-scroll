---
layout: default
title: How Ensemble Learning Balances Accuracy and Overfitting: A Bias-Variance Perspective on Tabular Data
---

# How Ensemble Learning Balances Accuracy and Overfitting: A Bias-Variance Perspective on Tabular Data
**arXiv**：[2512.05469v1](https://arxiv.org/abs/2512.05469) · [PDF](https://arxiv.org/pdf/2512.05469.pdf)  
**作者**：Zubair Ahmed Mohammad  

**一句话要点**：通过偏差-方差视角分析集成学习在表格数据上如何平衡准确性与过拟合

**关键词**：集成学习, 偏差-方差权衡, 表格数据分类, 泛化性能, 模型选择

## 3 点简述
- 研究集成模型在表格分类任务中平衡高准确性与小泛化差距的机制
- 采用重复分层交叉验证和统计检验比较线性模型、单决策树及九种集成方法
- 结果显示集成方法通过平均或受控提升减少方差，在非线性数据上提升测试准确率5-7点，泛化差距低于3%

## 摘要（原文）

> Ensemble models often achieve higher accuracy than single learners, but their ability to maintain small generalization gaps is not always well understood. This study examines how ensembles balance accuracy and overfitting across four tabular classification tasks: Breast Cancer, Heart Disease, Pima Diabetes, and Credit Card Fraud. Using repeated stratified cross validation with statistical significance testing, we compare linear models, a single decision tree, and nine ensemble methods. The results show that ensembles can reach high accuracy without large gaps by reducing variance through averaging or controlled boosting. On nearly linear and clean data, linear models already generalize well and ensembles offer little additional benefit. On datasets with meaningful nonlinear structure, tree based ensembles increase test accuracy by 5 to 7 points while keeping gaps below 3 percent. On noisy or highly imbalanced datasets, ensembles remain competitive but require regularization to avoid fitting noise or majority class patterns. We also compute simple dataset complexity indicators, such as linearity score, Fisher ratio, and noise estimate, which explain when ensembles are likely to control variance effectively. Overall, the study provides a clear view of how and when ensembles maintain high accuracy while keeping overfitting low, offering practical guidance for model selection in real world tabular applications.

