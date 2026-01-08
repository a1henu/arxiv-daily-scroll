---
layout: default
title: Stage-specific cancer survival prediction enriched by explainable machine learning
---

# Stage-specific cancer survival prediction enriched by explainable machine learning
**arXiv**：[2601.03977v1](https://arxiv.org/abs/2601.03977) · [PDF](https://arxiv.org/pdf/2601.03977.pdf)  
**作者**：Parisa Poorhasani, Bogdan Iancu  

**一句话要点**：提出可解释机器学习模型以预测癌症分期特异性生存率，基于SEER数据集

**关键词**：癌症生存预测, 可解释机器学习, 分期特异性模型, SHAP, LIME, SEER数据集

## 3 点简述
- 传统生存预测模型常混合所有癌症分期训练，可能高估性能并忽略分期差异。
- 使用SHAP和LIME等可解释技术揭示特征与癌症分期间的交互作用，增强模型透明度。
- 在结直肠癌、胃癌和肝癌中验证模型，识别不同分期和类型中影响生存的关键变量。

## 摘要（原文）

> Despite the fact that cancer survivability rates vary greatly between stages, traditional survival prediction models have frequently been trained and assessed using examples from all combined phases of the disease. This method may result in an overestimation of performance and ignore the stage-specific variations. Using the SEER dataset, we created and verified explainable machine learning (ML) models to predict stage-specific cancer survivability in colorectal, stomach, and liver cancers. ML-based cancer survival analysis has been a long-standing topic in the literature; however, studies involving the explainability and transparency of ML survivability models are limited. Our use of explainability techniques, including SHapley Additive exPlanations (SHAP) and Local Interpretable Model-agnostic Explanations (LIME), enabled us to illustrate significant feature-cancer stage interactions that would have remained hidden in traditional black-box models. We identified how certain demographic and clinical variables influenced survival differently across cancer stages and types. These insights provide not only transparency but also clinical relevance, supporting personalized treatment planning. By focusing on stage-specific models, this study provides new insights into the most important factors at each stage of cancer, offering transparency and potential clinical relevance to support personalized treatment planning.

