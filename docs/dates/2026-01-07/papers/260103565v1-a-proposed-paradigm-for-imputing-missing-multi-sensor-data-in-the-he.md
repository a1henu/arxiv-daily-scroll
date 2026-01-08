---
layout: default
title: A Proposed Paradigm for Imputing Missing Multi-Sensor Data in the Healthcare Domain
---

# A Proposed Paradigm for Imputing Missing Multi-Sensor Data in the Healthcare Domain
**arXiv**：[2601.03565v1](https://arxiv.org/abs/2601.03565) · [PDF](https://arxiv.org/pdf/2601.03565.pdf)  
**作者**：Vaibhav Gupta, Florian Grensing, Beyza Cinar, Maria Maleshkova  

**一句话要点**：提出针对医疗多传感器数据缺失的定制化插补范式，以提升低血糖预测效果。

**关键词**：医疗数据插补, 多传感器时间序列, 低血糖预测, 机器学习应用, 深度学习应用, 特征定制化

## 3 点简述
- 核心问题：多传感器数据因噪声和频繁缺失值阻碍低血糖预测，需处理异质时间模式。
- 方法要点：分析现有插补技术，基于特征特性和缺失时长定制机器学习与深度学习方法。
- 实验或效果：通过系统范式评估插补策略，强调特征时间动态和多技术组合的重要性。

## 摘要（原文）

> Chronic diseases such as diabetes pose significant management challenges, particularly due to the risk of complications like hypoglycemia, which require timely detection and intervention. Continuous health monitoring through wearable sensors offers a promising solution for early prediction of glycemic events. However, effective use of multisensor data is hindered by issues such as signal noise and frequent missing values. This study examines the limitations of existing datasets and emphasizes the temporal characteristics of key features relevant to hypoglycemia prediction. A comprehensive analysis of imputation techniques is conducted, focusing on those employed in state-of-the-art studies. Furthermore, imputation methods derived from machine learning and deep learning applications in other healthcare contexts are evaluated for their potential to address longer gaps in time-series data. Based on this analysis, a systematic paradigm is proposed, wherein imputation strategies are tailored to the nature of specific features and the duration of missing intervals. The review concludes by emphasizing the importance of investigating the temporal dynamics of individual features and the implementation of multiple, feature-specific imputation techniques to effectively address heterogeneous temporal patterns inherent in the data.

