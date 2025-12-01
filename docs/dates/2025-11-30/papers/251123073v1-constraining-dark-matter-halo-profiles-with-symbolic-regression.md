---
layout: default
title: Constraining dark matter halo profiles with symbolic regression
---

# Constraining dark matter halo profiles with symbolic regression
**arXiv**：[2511.23073v1](https://arxiv.org/abs/2511.23073) · [PDF](https://arxiv.org/pdf/2511.23073.pdf)  
**作者**：Alicia Martín, Tariq Yasin, Deaglan J. Bartlett, Harry Desmond, Pedro G. Ferreira  

**一句话要点**：提出符号回归方法以直接约束暗物质晕密度剖面，减少对模拟的依赖。

**关键词**：暗物质晕密度剖面, 符号回归, 弱透镜观测, 模型选择, 数据驱动约束

## 3 点简述
- 核心问题：传统暗物质晕密度剖面模型（如NFW）依赖模拟，受暗物质物理和重子建模不确定性影响。
- 方法要点：使用穷举符号回归（ESR）从观测数据中搜索最佳平衡精度与简洁性的解析表达式。
- 实验或效果：在模拟弱透镜数据上测试，低误差时恢复NFW剖面，高误差时更简单函数被优选。

## 摘要（原文）

> Dark matter haloes are typically characterised by radial density profiles with fixed forms motivated by simulations (e.g. NFW). However, simulation predictions depend on uncertain dark matter physics and baryonic modelling. Here, we present a method to constrain halo density profiles directly from observations using Exhaustive Symbolic Regression (ESR), a technique that searches the space of analytic expressions for the function that best balances accuracy and simplicity for a given dataset. We test the approach on mock weak lensing excess surface density (ESD) data of synthetic clusters with NFW profiles. Motivated by real data, we assign each ESD data point a constant fractional uncertainty and vary this uncertainty and the number of clusters to probe how data precision and sample size affect model selection. For fractional errors around 5%, ESR recovers the NFW profile even from samples as small as 20 clusters. At higher uncertainties representative of current surveys, simpler functions are favoured over NFW, though it remains competitive. This preference arises because weak lensing errors are smallest in the outskirts, causing the fits to be dominated by the outer profile. ESR therefore provides a robust, simulation-independent framework both for testing mass models and determining which features of a halo's density profile are genuinely constrained by the data.

