---
layout: default
title: Predicting Healthcare System Visitation Flow by Integrating Hospital Attributes and Population Socioeconomics with Human Mobility Data
---

# Predicting Healthcare System Visitation Flow by Integrating Hospital Attributes and Population Socioeconomics with Human Mobility Data
**arXiv**：[2601.15977v1](https://arxiv.org/abs/2601.15977) · [PDF](https://arxiv.org/pdf/2601.15977.pdf)  
**作者**：Binbin Lin, Lei Zou, Hao Tian, Heng Cai, Yifan Yang, Bing Zhou  

**一句话要点**：整合医院属性、人口社会经济与移动数据预测医疗访问流量

**关键词**：医疗访问预测, 移动数据分析, 深度引力模型, 异构图神经网络, SHAP分析

## 3 点简述
- 研究医疗访问模式受医院属性、人口社会经济和空间因素综合影响的问题
- 采用梯度提升、多层感知机、深度引力模型和异构图神经网络等五种模型进行流量预测
- 实验显示深度引力模型表现最佳，SHAP和PDP分析揭示不同因素对访问模式的影响

## 摘要（原文）

> Healthcare visitation patterns are influenced by a complex interplay of hospital attributes, population socioeconomics, and spatial factors. However, existing research often adopts a fragmented approach, examining these determinants in isolation. This study addresses this gap by integrating hospital capacities, occupancy rates, reputation, and popularity with population SES and spatial mobility patterns to predict visitation flows and analyze influencing factors. Utilizing four years of SafeGraph mobility data and user experience data from Google Maps Reviews, five flow prediction models, Naive Regression, Gradient Boosting, Multilayer Perceptrons (MLPs), Deep Gravity, and Heterogeneous Graph Neural Networks (HGNN),were trained and applied to simulate visitation flows in Houston, Texas, U.S. The Shapley additive explanation (SHAP) analysis and the Partial Dependence Plot (PDP) method were employed to examine the combined impacts of different factors on visitation patterns. The findings reveal that Deep Gravity outperformed other models. Hospital capacities, ICU occupancy rates, ratings, and popularity significantly influence visitation patterns, with their effects varying across different travel distances. Short-distance visits are primarily driven by convenience, whereas long-distance visits are influenced by hospital ratings. White-majority areas exhibited lower sensitivity to hospital ratings for short-distance visits, while Asian populations and those with higher education levels prioritized hospital rating in their visitation decisions. SES further influence these patterns, as areas with higher proportions of Hispanic, Black, under-18, and over-65 populations tend to have more frequent hospital visits, potentially reflecting greater healthcare needs or limited access to alternative medical services.

