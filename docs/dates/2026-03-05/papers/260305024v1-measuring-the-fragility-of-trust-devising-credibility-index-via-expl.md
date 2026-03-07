---
layout: default
title: Measuring the Fragility of Trust: Devising Credibility Index via Explanation Stability (CIES) for Business Decision Support Systems
---

# Measuring the Fragility of Trust: Devising Credibility Index via Explanation Stability (CIES) for Business Decision Support Systems
**arXiv**：[2603.05024v1](https://arxiv.org/abs/2603.05024) · [PDF](https://arxiv.org/pdf/2603.05024.pdf)  
**作者**：Alin-Gabriel Vaduva, Simona-Vasilica Oprea, Adela Bara  

**一句话要点**：提出基于解释稳定性的可信度指数（CIES），量化商业决策支持系统中AI解释的稳健性。

**关键词**：可解释人工智能, 解释稳定性, 商业决策支持, 可信度指标, 数据扰动, 树模型分类

## 3 点简述
- 核心问题：XAI方法（如SHAP、LIME）的解释在真实数据扰动下的可信度缺乏量化指标。
- 方法要点：CIES使用基于排名的加权距离函数，衡量模型解释在商业噪声下的稳定性，突出关键特征变化的影响。
- 实验或效果：在三个数据集、四个树模型上验证，CIES优于基线指标，并提供解释可信度的敏感性分析。

## 摘要（原文）

> Explainable Artificial Intelligence (XAI) methods (SHAP, LIME) are increasingly adopted to interpret models in high-stakes businesses. However, the credibility of these explanations, their stability under realistic data perturbations, remains unquantified. This paper introduces the Credibility Index via Explanation Stability (CIES), a mathematically grounded metric that measures how robust a model's explanations are when subject to realistic business noise. CIES captures whether the reasons behind a prediction remain consistent, not just the prediction itself. The metric employs a rank-weighted distance function that penalizes instability in the most important features disproportionately, reflecting business semantics where changes in top decision drivers are more consequential than changes in marginal features. We evaluate CIES across three datasets (customer churn, credit risk, employee attrition), four tree-based classification models and two data balancing conditions. Results demonstrate that model complexity impacts explanation credibility, class imbalance treatment via SMOTE affects not only predictive performance but also explanation stability, and CIES provides statistically superior discriminative power compared to a uniform baseline metric (p < 0.01 in all 24 configurations). A sensitivity analysis across four noise levels confirms the robustness of the metric itself. These findings offer business practitioners a deployable "credibility warning system" for AI-driven decision support.

