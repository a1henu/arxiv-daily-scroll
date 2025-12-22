---
layout: default
title: Imputation Uncertainty in Interpretable Machine Learning Methods
---

# Imputation Uncertainty in Interpretable Machine Learning Methods
**arXiv**：[2512.17689v1](https://arxiv.org/abs/2512.17689) · [PDF](https://arxiv.org/pdf/2512.17689.pdf)  
**作者**：Pegah Golchian, Marvin N. Wright  

**一句话要点**：比较不同插补方法对可解释机器学习置信区间覆盖概率的影响

**关键词**：缺失值插补, 可解释机器学习, 置信区间, 插补不确定性, 方差估计

## 3 点简述
- 核心问题：缺失值影响可解释机器学习方法，现有研究忽略插补不确定性对置信区间的影响
- 方法要点：比较单次插补和多重插补对排列特征重要性、部分依赖图和Shapley值的置信区间覆盖概率
- 实验或效果：单次插补低估方差，多重插补在多数情况下接近名义覆盖水平

## 摘要（原文）

> In real data, missing values occur frequently, which affects the interpretation with interpretable machine learning (IML) methods. Recent work considers bias and shows that model explanations may differ between imputation methods, while ignoring additional imputation uncertainty and its influence on variance and confidence intervals. We therefore compare the effects of different imputation methods on the confidence interval coverage probabilities of the IML methods permutation feature importance, partial dependence plots and Shapley values. We show that single imputation leads to underestimation of variance and that, in most cases, only multiple imputation is close to nominal coverage.

