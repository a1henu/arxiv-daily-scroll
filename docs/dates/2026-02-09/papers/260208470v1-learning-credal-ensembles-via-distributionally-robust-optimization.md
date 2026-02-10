---
layout: default
title: Learning Credal Ensembles via Distributionally Robust Optimization
---

# Learning Credal Ensembles via Distributionally Robust Optimization
**arXiv**：[2602.08470v1](https://arxiv.org/abs/2602.08470) · [PDF](https://arxiv.org/pdf/2602.08470.pdf)  
**作者**：Kaizheng Wang, Ghifari Adam Faza, Fabio Cuzzolin, Siu Lun Chau, David Moens, Hans Hallez  

**一句话要点**：提出CreDRO方法，通过分布鲁棒优化学习可信集合，以捕捉训练与测试数据间分布偏移引起的认知不确定性。

**关键词**：可信预测器, 认知不确定性, 分布鲁棒优化, 集合学习, 分布偏移, 选择性分类

## 3 点简述
- 核心问题：现有可信预测器主要基于训练随机性定义认知不确定性，忽略更深层分布偏移的影响。
- 方法要点：定义认知不确定性为模型在训练与测试数据非独立同分布假设下的分歧，利用分布鲁棒优化学习集合。
- 实验或效果：在多个基准测试中，CreDRO在分布外检测和医疗选择性分类任务上优于现有可信方法。

## 摘要（原文）

> Credal predictors are models that are aware of epistemic uncertainty and produce a convex set of probabilistic predictions. They offer a principled way to quantify predictive epistemic uncertainty (EU) and have been shown to improve model robustness in various settings. However, most state-of-the-art methods mainly define EU as disagreement caused by random training initializations, which mostly reflects sensitivity to optimization randomness rather than uncertainty from deeper sources. To address this, we define EU as disagreement among models trained with varying relaxations of the i.i.d. assumption between training and test data. Based on this idea, we propose CreDRO, which learns an ensemble of plausible models through distributionally robust optimization. As a result, CreDRO captures EU not only from training randomness but also from meaningful disagreement due to potential distribution shifts between training and test data. Empirical results show that CreDRO consistently outperforms existing credal methods on tasks such as out-of-distribution detection across multiple benchmarks and selective classification in medical applications.

