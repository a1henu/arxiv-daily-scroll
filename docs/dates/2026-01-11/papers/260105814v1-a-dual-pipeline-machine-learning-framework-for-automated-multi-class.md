---
layout: default
title: A Dual Pipeline Machine Learning Framework for Automated Multi Class Sleep Disorder Screening Using Hybrid Resampling and Ensemble Learning
---

# A Dual Pipeline Machine Learning Framework for Automated Multi Class Sleep Disorder Screening Using Hybrid Resampling and Ensemble Learning
**arXiv**：[2601.05814v1](https://arxiv.org/abs/2601.05814) · [PDF](https://arxiv.org/pdf/2601.05814.pdf)  
**作者**：Md Sultanul Islam Ovi, Muhsina Tarannum Munfa, Miftahul Alam Adib, Syed Sabbir Hasan  

**一句话要点**：提出双管道机器学习框架，用于基于混合重采样和集成学习的自动多类睡眠障碍筛查。

**关键词**：睡眠障碍筛查, 双管道框架, 混合重采样, 集成学习, 特征选择, 非侵入性风险分层

## 3 点简述
- 核心问题：临床睡眠研究资源密集，难以扩展至人群筛查，需准确分类失眠和睡眠呼吸暂停。
- 方法要点：采用统计管道和包装管道并行处理，结合混合SMOTETomek重采样处理类别不平衡。
- 实验或效果：Extra Trees和K近邻算法准确率达98.67%，推理延迟低于400毫秒，显著优于基线。

## 摘要（原文）

> Accurate classification of sleep disorders, particularly insomnia and sleep apnea, is important for reducing long term health risks and improving patient quality of life. However, clinical sleep studies are resource intensive and are difficult to scale for population level screening. This paper presents a Dual Pipeline Machine Learning Framework for multi class sleep disorder screening using the Sleep Health and Lifestyle dataset. The framework consists of two parallel processing streams: a statistical pipeline that targets linear separability using Mutual Information and Linear Discriminant Analysis, and a wrapper based pipeline that applies Boruta feature selection with an autoencoder for non linear representation learning. To address class imbalance, we use the hybrid SMOTETomek resampling strategy. In experiments, Extra Trees and K Nearest Neighbors achieved an accuracy of 98.67%, outperforming recent baselines on the same dataset. Statistical testing using the Wilcoxon Signed Rank Test indicates that the improvement over baseline configurations is significant, and inference latency remains below 400 milliseconds. These results suggest that the proposed dual pipeline design supports accurate and efficient automated screening for non invasive sleep disorder risk stratification.

