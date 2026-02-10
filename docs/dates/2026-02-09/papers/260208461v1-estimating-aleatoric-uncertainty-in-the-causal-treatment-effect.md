---
layout: default
title: Estimating Aleatoric Uncertainty in the Causal Treatment Effect
---

# Estimating Aleatoric Uncertainty in the Causal Treatment Effect
**arXiv**：[2602.08461v1](https://arxiv.org/abs/2602.08461) · [PDF](https://arxiv.org/pdf/2602.08461.pdf)  
**作者**：Liyuan Xu, Bijan Mazaheri  

**一句话要点**：提出VTE和CVTE作为因果治疗效应中固有随机不确定性的度量，并开发非参数核估计器。

**关键词**：因果推断, 治疗效应方差, 非参数估计, 随机不确定性, 核方法

## 3 点简述
- 核心问题：因果推断中个体治疗响应的变异性与不确定性研究不足。
- 方法要点：在温和假设下可识别VTE和CVTE，提出非参数核估计器并理论证明收敛。
- 实验或效果：在合成和半模拟数据集上验证方法优于或可比朴素基线。

## 摘要（原文）

> Previous work on causal inference has primarily focused on averages and conditional averages of treatment effects, with significantly less attention on variability and uncertainty in individual treatment responses. In this paper, we introduce the variance of the treatment effect (VTE) and conditional variance of treatment effect (CVTE) as the natural measure of aleatoric uncertainty inherent in treatment responses, and we demonstrate that these quantities are identifiable from observed data under mild assumptions, even in the presence of unobserved confounders. We further propose nonparametric kernel-based estimators for VTE and CVTE, and our theoretical analysis establishes their convergence. We also test the performance of our method through extensive empirical experiments on both synthetic and semi-simulated datasets, where it demonstrates superior or comparable performance to naive baselines.

