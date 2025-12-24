---
layout: default
title: ScoreMatchingRiesz: Auto-DML with Infinitesimal Classification
---

# ScoreMatchingRiesz: Auto-DML with Infinitesimal Classification
**arXiv**：[2512.20523v1](https://arxiv.org/abs/2512.20523) · [PDF](https://arxiv.org/pdf/2512.20523.pdf)  
**作者**：Masahiro Kato  

**一句话要点**：提出基于分数匹配的Riesz表示器估计方法，以缓解因果推断中的过拟合问题。

**关键词**：Riesz表示器估计, 分数匹配, 因果推断, 密度比估计, 去偏机器学习

## 3 点简述
- 核心问题：直接密度比估计在因果推断中易过拟合，影响Riesz表示器估计的准确性。
- 方法要点：扩展分数匹配技术至Riesz表示器估计，通过建模密度比为多个中间密度比乘积来缓解过拟合。
- 实验或效果：未知，但方法理论上能提供√n一致且高效的估计器，并连接边际效应与平均政策效应。

## 摘要（原文）

> This study proposes Riesz representer estimation methods based on score matching. The Riesz representer is a key component in debiased machine learning for constructing $\sqrt{n}$-consistent and efficient estimators in causal inference and structural parameter estimation. To estimate the Riesz representer, direct approaches have garnered attention, such as Riesz regression and the covariate balancing propensity score. These approaches can also be interpreted as variants of direct density ratio estimation (DRE) in several applications such as average treatment effect estimation. In DRE, it is well known that flexible models can easily overfit the observed data due to the estimand and the form of the loss function. To address this issue, recent work has proposed modeling the density ratio as a product of multiple intermediate density ratios and estimating it using score-matching techniques, which are often used in the diffusion model literature. We extend score-matching-based DRE methods to Riesz representer estimation. Our proposed method not only mitigates overfitting but also provides insights for causal inference by bridging marginal effects and average policy effects through time score functions.

