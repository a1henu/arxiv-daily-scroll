---
layout: default
title: When Data Quality Issues Collide: A Large-Scale Empirical Study of Co-Occurring Data Quality Issues in Software Defect Prediction
---

# When Data Quality Issues Collide: A Large-Scale Empirical Study of Co-Occurring Data Quality Issues in Software Defect Prediction
**arXiv**：[2512.17460v1](https://arxiv.org/abs/2512.17460) · [PDF](https://arxiv.org/pdf/2512.17460.pdf)  
**作者**：Emmanuel Charleson Dapaah, Jens Grabowski  

**一句话要点**：首次大规模实证分析软件缺陷预测中五种数据质量问题共现的影响与阈值

**关键词**：软件缺陷预测, 数据质量问题, 共现分析, 可解释提升机, 阈值识别, 模型性能评估

## 3 点简述
- 核心问题：软件缺陷预测模型受数据质量问题制约，现有研究孤立分析，忽略问题共现与交互。
- 方法要点：使用可解释提升机和分层交互分析，在默认超参数下量化374个数据集和五种分类器的直接与条件效应。
- 实验或效果：发现共现普遍，识别有害阈值（如类别重叠0.20），揭示反直觉模式（如离群值在低无关特征时提升性能）。

## 摘要（原文）

> Software Defect Prediction (SDP) models are central to proactive software quality assurance, yet their effectiveness is often constrained by the quality of available datasets. Prior research has typically examined single issues such as class imbalance or feature irrelevance in isolation, overlooking that real-world data problems frequently co-occur and interact. This study presents, to our knowledge, the first large-scale empirical analysis in SDP that simultaneously examines five co-occurring data quality issues (class imbalance, class overlap, irrelevant features, attribute noise, and outliers) across 374 datasets and five classifiers. We employ Explainable Boosting Machines together with stratified interaction analysis to quantify both direct and conditional effects under default hyperparameter settings, reflecting practical baseline usage.
>   Our results show that co-occurrence is nearly universal: even the least frequent issue (attribute noise) appears alongside others in more than 93% of datasets. Irrelevant features and imbalance are nearly ubiquitous, while class overlap is the most consistently harmful issue. We identify stable tipping points around 0.20 for class overlap, 0.65-0.70 for imbalance, and 0.94 for irrelevance, beyond which most models begin to degrade. We also uncover counterintuitive patterns, such as outliers improving performance when irrelevant features are low, underscoring the importance of context-aware evaluation. Finally, we expose a performance-robustness trade-off: no single learner dominates under all conditions.
>   By jointly analyzing prevalence, co-occurrence, thresholds, and conditional effects, our study directly addresses a persistent gap in SDP research. Hence, moving beyond isolated analyses to provide a holistic, data-aware understanding of how quality issues shape model performance in real-world settings.

