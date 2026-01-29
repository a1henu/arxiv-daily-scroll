---
layout: default
title: Conditional PED-ANOVA: Hyperparameter Importance in Hierarchical & Dynamic Search Spaces
---

# Conditional PED-ANOVA: Hyperparameter Importance in Hierarchical & Dynamic Search Spaces
**arXiv**：[2601.20800v1](https://arxiv.org/abs/2601.20800) · [PDF](https://arxiv.org/pdf/2601.20800.pdf)  
**作者**：Kaito Baba, Yoshihiko Ozaki, Shuhei Watanabe  

**一句话要点**：提出条件PED-ANOVA以估计条件搜索空间中的超参数重要性

**关键词**：超参数重要性, 条件搜索空间, PED-ANOVA, 机器学习优化, 超参数调优

## 3 点简述
- 核心问题：现有超参数重要性估计方法无法处理条件搜索空间，导致误导性结果。
- 方法要点：引入条件超参数重要性，推导闭式估计器，准确反映条件激活和域变化。
- 实验或效果：实验显示，条件PED-ANOVA在条件设置中提供有意义的重要性估计，优于现有方法。

## 摘要（原文）

> We propose conditional PED-ANOVA (condPED-ANOVA), a principled framework for estimating hyperparameter importance (HPI) in conditional search spaces, where the presence or domain of a hyperparameter can depend on other hyperparameters. Although the original PED-ANOVA provides a fast and efficient way to estimate HPI within the top-performing regions of the search space, it assumes a fixed, unconditional search space and therefore cannot properly handle conditional hyperparameters. To address this, we introduce a conditional HPI for top-performing regions and derive a closed-form estimator that accurately reflects conditional activation and domain changes. Experiments show that naive adaptations of existing HPI estimators yield misleading or uninterpretable importance estimates in conditional settings, whereas condPED-ANOVA consistently provides meaningful importances that reflect the underlying conditional structure.

