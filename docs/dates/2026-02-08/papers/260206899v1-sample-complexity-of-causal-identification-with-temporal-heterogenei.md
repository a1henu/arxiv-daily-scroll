---
layout: default
title: Sample Complexity of Causal Identification with Temporal Heterogeneity
---

# Sample Complexity of Causal Identification with Temporal Heterogeneity
**arXiv**：[2602.06899v1](https://arxiv.org/abs/2602.06899) · [PDF](https://arxiv.org/pdf/2602.06899.pdf)  
**作者**：Ameya Rathod, Sujay Belsare, Salvik Krishna Nautiyal, Dhruv Laad, Ponnurangam Kumaraguru  

**一句话要点**：整合时间序列动态与多环境异质性，分析因果图识别的样本复杂度与稳健性极限。

**关键词**：因果识别, 时间异质性, 样本复杂度, 重尾分布, 非平稳系统, 信息论界限

## 3 点简述
- 核心问题：从观测数据中唯一恢复因果图是病态问题，需利用结构或分布假设。
- 方法要点：结合时间异质性和环境异质性，推导统一可识别性条件，分析高斯与重尾噪声下的统计极限。
- 实验或效果：证明时间结构可弥补环境多样性不足，量化重尾分布下样本复杂度的显著偏离。

## 摘要（原文）

> Recovering a unique causal graph from observational data is an ill-posed problem because multiple generating mechanisms can lead to the same observational distribution. This problem becomes solvable only by exploiting specific structural or distributional assumptions. While recent work has separately utilized time-series dynamics or multi-environment heterogeneity to constrain this problem, we integrate both as complementary sources of heterogeneity. This integration yields unified necessary identifiability conditions and enables a rigorous analysis of the statistical limits of recovery under thin versus heavy-tailed noise. In particular, temporal structure is shown to effectively substitute for missing environmental diversity, possibly achieving identifiability even under insufficient heterogeneity. Extending this analysis to heavy-tailed (Student's t) distributions, we demonstrate that while geometric identifiability conditions remain invariant, the sample complexity diverges significantly from the Gaussian baseline. Explicit information-theoretic bounds quantify this cost of robustness, establishing the fundamental limits of covariance-based causal graph recovery methods in realistic non-stationary systems. This work shifts the focus from whether causal structure is identifiable to whether it is statistically recoverable in practice.

