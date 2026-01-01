---
layout: default
title: A Scalable Framework for logP Prediction: From Terabyte-Scale Data Integration to Interpretable Ensemble Modeling
---

# A Scalable Framework for logP Prediction: From Terabyte-Scale Data Integration to Interpretable Ensemble Modeling
**arXiv**：[2512.24643v1](https://arxiv.org/abs/2512.24643) · [PDF](https://arxiv.org/pdf/2512.24643.pdf)  
**作者**：Malikussaid, Septian Caesar Floresko, Ade Romadhony, Isman Kurniawan, Warih Maharani, Hilal Hudan Nuha  

**一句话要点**：提出可扩展框架用于logP预测，通过数据集成和分层建模提升性能

**关键词**：logP预测, 数据集成, 树基集成模型, 分层建模, SHAP分析, 2D描述符

## 3 点简述
- 核心问题：从三大化学数据库整合426850个生物活性化合物，解决logP预测的数据集成挑战
- 方法要点：采用字节偏移索引架构，处理时间从超100天降至3.2小时，并评估线性与树基集成模型
- 实验或效果：分层建模策略在测试集上实现R平方0.767，RMSE 0.731，优于传统方法

## 摘要（原文）

> This study presents a large-scale predictive modeling framework for logP prediction using 426850 bioactive compounds rigorously curated from the intersection of three authoritative chemical databases: PubChem, ChEMBL, and eMolecules. We developed a novel computational infrastructure to address the data integration challenge, reducing processing time from a projected over 100 days to 3.2 hours through byte-offset indexing architecture, a 740-fold improvement. Our comprehensive analysis revealed critical insights into the multivariate nature of lipophilicity: while molecular weight exhibited weak bivariate correlation with logP, SHAP analysis on ensemble models identified it as the single most important predictor globally. We systematically evaluated multiple modeling approaches, discovering that linear models suffered from inherent heteroskedasticity that classical remediation strategies, including weighted least squares and Box-Cox transformation, failed to address. Tree-based ensemble methods, including Random Forest and XGBoost, proved inherently robust to this violation, achieving an R-squared of 0.765 and RMSE of 0.731 logP units on the test set. Furthermore, a stratified modeling strategy, employing specialized models for drug-like molecules (91 percent of dataset) and extreme cases (nine percent), achieved optimal performance: an RMSE of 0.838 for the drug-like subset and an R-squared of 0.767 for extreme molecules, the highest of all evaluated approaches. These findings provide actionable guidance for molecular design, establish robust baselines for lipophilicity prediction using only 2D descriptors, and demonstrate that well-curated, descriptor-based ensemble models remain competitive with state-of-the-art graph neural network architectures.

