---
layout: default
title: meval: A Statistical Toolbox for Fine-Grained Model Performance Analysis
---

# meval: A Statistical Toolbox for Fine-Grained Model Performance Analysis
**arXiv**：[2512.17409v1](https://arxiv.org/abs/2512.17409) · [PDF](https://arxiv.org/pdf/2512.17409.pdf)  
**作者**：Dishantkumar Sutariya, Eike Petersen  

**一句话要点**：提出meval统计工具箱，用于医学影像中细粒度模型性能分析的统计严谨评估。

**关键词**：模型性能分析, 统计工具箱, 医学影像, 子组分析, 多重比较校正

## 3 点简述
- 核心问题：模型性能按患者和记录属性分层分析时，需处理样本大小、基础率差异及多重比较校正。
- 方法要点：提供统计工具，支持选择适当性能指标、计算不确定性并识别有趣子组。
- 实验或效果：在ISIC2020皮肤病变和MIMIC-CXR胸部X射线数据集上验证工具箱应用。

## 摘要（原文）

> Analyzing machine learning model performance stratified by patient and recording properties is becoming the accepted norm and often yields crucial insights about important model failure modes. Performing such analyses in a statistically rigorous manner is non-trivial, however. Appropriate performance metrics must be selected that allow for valid comparisons between groups of different sample sizes and base rates; metric uncertainty must be determined and multiple comparisons be corrected for, in order to assess whether any observed differences may be purely due to chance; and in the case of intersectional analyses, mechanisms must be implemented to find the most `interesting' subgroups within combinatorially many subgroup combinations. We here present a statistical toolbox that addresses these challenges and enables practitioners to easily yet rigorously assess their models for potential subgroup performance disparities. While broadly applicable, the toolbox is specifically designed for medical imaging applications. The analyses provided by the toolbox are illustrated in two case studies, one in skin lesion malignancy classification on the ISIC2020 dataset and one in chest X-ray-based disease classification on the MIMIC-CXR dataset.

