---
layout: default
title: Predictive Inorganic Synthesis based on Machine Learning using Small Data sets: a case study of size-controlled Cu Nanoparticles
---

# Predictive Inorganic Synthesis based on Machine Learning using Small Data sets: a case study of size-controlled Cu Nanoparticles
**arXiv**：[2512.16545v1](https://arxiv.org/abs/2512.16545) · [PDF](https://arxiv.org/pdf/2512.16545.pdf)  
**作者**：Brent Motmans, Digvijay Ghogare, Thijs G. I. van Wijk, An Hardy, Danny E. P. Vanpoucke  

**一句话要点**：提出基于小数据集的机器学习方法，预测微波辅助多元醇合成中铜纳米颗粒的尺寸控制。

**关键词**：机器学习, 无机合成预测, 小数据集, 铜纳米颗粒, 尺寸控制, 集成回归

## 3 点简述
- 核心问题：铜纳米颗粒合成对参数敏感，实验优化耗时且数据稀缺，难以实现可重复的尺寸控制。
- 方法要点：使用拉丁超立方采样高效覆盖参数空间，基于AMADEUS框架构建集成回归模型预测颗粒尺寸。
- 实验或效果：在25个合成的小数据集上，模型预测准确度（R²=0.74）优于传统统计方法（R²=0.60）。

## 摘要（原文）

> Copper nanoparticles (Cu NPs) have a broad applicability, yet their synthesis is sensitive to subtle changes in reaction parameters. This sensitivity, combined with the time- and resource-intensive nature of experimental optimization, poses a major challenge in achieving reproducible and size-controlled synthesis. While Machine Learning (ML) shows promise in materials research, its application is often limited by scarcity of large high-quality experimental data sets. This study explores ML to predict the size of Cu NPs from microwave-assisted polyol synthesis using a small data set of 25 in-house performed syntheses. Latin Hypercube Sampling is used to efficiently cover the parameter space while creating the experimental data set. Ensemble regression models, built with the AMADEUS framework, successfully predict particle sizes with high accuracy ($R^2 = 0.74$), outperforming classical statistical approaches ($R^2 = 0.60$). Overall, this study highlights that, for lab-scale synthesis optimization, high-quality small datasets combined with classical, interpretable ML models outperform traditional statistical methods and are fully sufficient for quantitative synthesis prediction. This approach provides a sustainable and experimentally realistic pathway toward data-driven inorganic synthesis design.

