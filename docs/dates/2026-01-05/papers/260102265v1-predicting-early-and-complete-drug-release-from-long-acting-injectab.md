---
layout: default
title: Predicting Early and Complete Drug Release from Long-Acting Injectables Using Explainable Machine Learning
---

# Predicting Early and Complete Drug Release from Long-Acting Injectables Using Explainable Machine Learning
**arXiv**：[2601.02265v1](https://arxiv.org/abs/2601.02265) · [PDF](https://arxiv.org/pdf/2601.02265.pdf)  
**作者**：Karla N. Robles, Manar D. Samad  

**一句话要点**：提出可解释机器学习方法以优化长效注射剂药物释放预测

**关键词**：长效注射剂, 药物释放预测, 可解释机器学习, Shapley解释, 数据转换, 聚合物基药物递送

## 3 点简述
- 核心问题：传统方法难以解析长效注射剂复杂物化性质对药物释放的影响
- 方法要点：采用数据转换和可解释ML框架，预测早期和完全释放曲线
- 实验或效果：在72小时释放预测中相关性>0.65，释放类型分类F1分数达0.87

## 摘要（原文）

> Polymer-based long-acting injectables (LAIs) have transformed the treatment of chronic diseases by enabling controlled drug delivery, thus reducing dosing frequency and extending therapeutic duration. Achieving controlled drug release from LAIs requires extensive optimization of the complex underlying physicochemical properties. Machine learning (ML) can accelerate LAI development by modeling the complex relationships between LAI properties and drug release. However, recent ML studies have provided limited information on key properties that modulate drug release, due to the lack of custom modeling and analysis tailored to LAI data. This paper presents a novel data transformation and explainable ML approach to synthesize actionable information from 321 LAI formulations by predicting early drug release at 24, 48, and 72 hours, classification of release profile types, and prediction of complete release profiles. These three experiments investigate the contribution and control of LAI material characteristics in early and complete drug release profiles. A strong correlation (>0.65) is observed between the true and predicted drug release in 72 hours, while a 0.87 F1-score is obtained in classifying release profile types. A time-independent ML framework predicts delayed biphasic and triphasic curves with better performance than current time-dependent approaches. Shapley additive explanations reveal the relative influence of material characteristics during early and for complete release which fill several gaps in previous in-vitro and ML-based studies. The novel approach and findings can provide a quantitative strategy and recommendations for scientists to optimize the drug-release dynamics of LAI. The source code for the model implementation is publicly available.

