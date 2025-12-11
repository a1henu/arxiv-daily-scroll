---
layout: default
title: Cauchy-Schwarz Fairness Regularizer
---

# Cauchy-Schwarz Fairness Regularizer
**arXiv**：[2512.09467v1](https://arxiv.org/abs/2512.09467) · [PDF](https://arxiv.org/pdf/2512.09467.pdf)  
**作者**：Yezi Liu, Hanning Chen, Wenjun Huang, Yang Ni, Mohsen Imani  

**一句话要点**：提出柯西-施瓦茨公平正则器以提升机器学习中的群体公平性

**关键词**：群体公平, 正则化方法, 柯西-施瓦茨散度, 机器学习公平性, 敏感属性处理

## 3 点简述
- 现有公平正则器基于异构距离度量，导致行为难以解释且性能不一致
- 基于柯西-施瓦茨散度设计正则器，具有紧致泛化界和尺度鲁棒性
- 在多个基准数据集上实验，改善公平指标并保持准确度，实现更稳定的效用-公平权衡

## 摘要（原文）

> Group fairness in machine learning is often enforced by adding a regularizer that reduces the dependence between model predictions and sensitive attributes. However, existing regularizers are built on heterogeneous distance measures and design choices, which makes their behavior hard to reason about and their performance inconsistent across tasks. This raises a basic question: what properties make a good fairness regularizer? We address this question by first organizing existing in-process methods into three families: (i) matching prediction statistics across sensitive groups, (ii) aligning latent representations, and (iii) directly minimizing dependence between predictions and sensitive attributes. Through this lens, we identify desirable properties of the underlying distance measure, including tight generalization bounds, robustness to scale differences, and the ability to handle arbitrary prediction distributions. Motivated by these properties, we propose a Cauchy-Schwarz (CS) fairness regularizer that penalizes the empirical CS divergence between prediction distributions conditioned on sensitive groups. Under a Gaussian comparison, we show that CS divergence yields a tighter bound than Kullback-Leibler divergence, Maximum Mean Discrepancy, and the mean disparity used in Demographic Parity, and we discuss how these advantages translate to a distribution-free, kernel-based estimator that naturally extends to multiple sensitive attributes. Extensive experiments on four tabular benchmarks and one image dataset demonstrate that the proposed CS regularizer consistently improves Demographic Parity and Equal Opportunity metrics while maintaining competitive accuracy, and achieves a more stable utility-fairness trade-off across hyperparameter settings compared to prior regularizers.

